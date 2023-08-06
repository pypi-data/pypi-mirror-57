##############################################################################
# H5Traj: An HDF5-backed variant of MDTraj.
#
# Author: Charlie Laughton
#
# Much of the code here is adapted from that in MDTraj:
#
# Authors: Robert McGibbon
# Contributors: Kyle A. Beauchamp, TJ Lane, Joshua Adelman, Lee-Ping Wang, Jason Swails
##############################################################################
import mdtraj as mdt
from mdtraj.utils import ensure_type, cast_indices
from mdtraj.geometry import distance
from mdtraj import _rmsd
from copy import deepcopy
import h5py
import os
import tempfile
import numpy as np

# supported extensions for constructing topologies
_TOPOLOGY_EXTS = ['.pdb', '.pdb.gz', '.h5','.lh5', '.prmtop', '.parm7', '.prm7',
                  '.psf', '.mol2', '.hoomdxml', '.gro', '.arc', '.hdf5', '.gsd']

def _get_extension(filename):
    (base, extension) = os.path.splitext(filename)
    if extension == '.gz':
        extension2 = os.path.splitext(base)[1]
        return extension2 + extension
    return extension


class Trajectory(mdt.Trajectory):
    
    def _string_summary_basic(self):
        """Basic summary of traj in string form."""
        unitcell_str = 'and unitcells' if self._have_unitcell else 'without unitcells'
        value = "h5t.Trajectory with %d frames, %d atoms, %d residues, %s" % (
                    self.n_frames, self.n_atoms, self.n_residues, unitcell_str)
        return value
    
    @property
    def _xyz(self):
        """Cartesian coordinates of each atom in each simulation frame
        Returns
        -------
        xyz : np.ndarray, shape=(n_frames, n_atoms, 3)
            A three dimensional numpy array, with the cartesian coordinates
            of each atoms in each frame.
        """
        return np.array(self._h5xyz)

    @_xyz.setter
    def _xyz(self, value):
        "Set the cartesian coordinates of each atom in each simulation frame"
        if hasattr(self, '_h5xyz'):
            self._h5xyz.resize(value.shape)
            self._h5xyz[:len(value)] = value
        else:
            self.h5file = h5py.File(tempfile.NamedTemporaryFile().name, 'w')
            shape = list(value.shape)
            shape[0] = None
            self._h5xyz = self.h5file.create_dataset('xyz', data=value, maxshape=shape)
        self._rmsd_traces = None
        
    def append(self, other, check_topology=True, discard_overlapping_frames=False):
        """Append data from other trajectories together along the time/frame axis.
        
        Parameters
        ----------
        other : Trajectory or list of Trajectory
            One or more trajectories to join with this one. These trajectories
            are *appended* to the end of this trajectory.
        check_topology : bool
            Ensure that the topology of `self` and `other` are identical before
            joining them. If false, the resulting trajectory will have the
            topology of `self`.
        discard_overlapping_frames : bool, optional
            If True, compare coordinates at trajectory edges to discard overlapping
            frames.  Default: False.
        
        """

        if isinstance(other, (Trajectory, mdt.Trajectory)):
            other = [other]
        if isinstance(other, list):
            if not all(isinstance(o, (Trajectory, mdt.Trajectory)) for o in other):
                raise TypeError('You can only join Trajectory instances')
            if not all(self.n_atoms == o.n_atoms for o in other):
                raise  ValueError('Number of atoms in self (%d) is not equal '
                          'to number of atoms in other' % (self.n_atoms))
            if check_topology and not all(self.topology == o.topology for o in other):
                raise ValueError('The topologies of the Trajectories are not the same')
            if not all(self._have_unitcell == o._have_unitcell for o in other):
                raise ValueError('Mixing trajectories with and without unitcell')
        else:
            raise TypeError('`other` must be a list of Trajectory or mdt.Trajectory. You supplied {}'.format(type(other)))


        # list containing all of the trajs to merge, including self
        trajectories = [self] + other
        if discard_overlapping_frames:
            for i in range(len(trajectories)-1):
                # last frame of trajectory i
                x0 = trajectories[i].xyz[-1]
                # first frame of trajectory i+1
                x1 = trajectories[i + 1].xyz[0]

                # check that all atoms are within 2e-3 nm
                # (this is kind of arbitrary)
                if np.all(np.abs(x1 - x0) < 2e-3):
                    trajectories[i] = trajectories[i][:-1]

        xyz_new = np.concatenate([t.xyz for t in trajectories[1:]])
        time = np.concatenate([t.time for t in trajectories])
        angles = lengths = None
        if self._have_unitcell:
            angles = np.concatenate([t.unitcell_angles for t in trajectories])
            lengths = np.concatenate([t.unitcell_lengths for t in trajectories])

        l_old = self.n_frames
        l_new = l_old + len(xyz_new)
        self._h5xyz.resize(l_new, axis=0)
        self._h5xyz[l_old:l_new] = xyz_new
        self.time = time
        self.unitcell_angles = angles
        self.unitcell_lengths = lengths

    
    def superpose(self, reference, frame=0, atom_indices=None,
                  ref_atom_indices=None, chunk=1000, parallel=True):
        """Superpose each conformation in this trajectory upon a reference
        Parameters
        ----------
        reference : Trajectory
            Align self to a particular frame in `reference`
        frame : int
            The index of the conformation in `reference` to align to.
        atom_indices : array_like, or None
            The indices of the atoms to superpose. If not
            supplied, all atoms will be used.
        ref_atom_indices : array_like, or None
            Use these atoms on the reference structure. If not supplied,
            the same atom indices will be used for this trajectory and the
            reference one.
        chunk : int
            The chunk size for the superposition process, to limit memory burden.
        parallel : bool
            Use OpenMP to run the superposition in parallel over multiple cores
        Returns
        -------
        self
        """

        if atom_indices is None:
            atom_indices = slice(None)

        if ref_atom_indices is None:
            ref_atom_indices = atom_indices

        if not isinstance(ref_atom_indices, slice) and (
            len(ref_atom_indices) != len(atom_indices)):
            raise ValueError("Number of atoms must be consistent!")

        ref_align_xyz = np.array(reference.xyz[frame, ref_atom_indices, :],
                                 copy=True, order='c').reshape(1, -1, 3)
        ref_offset = ref_align_xyz[0].astype('float64').mean(0)
        ref_align_xyz[0] -= ref_offset


        n_frames = self.xyz.shape[0]
        if chunk == 0:
            chunk = n_frames
        chunk_start = 0
        while chunk_start < n_frames:
            chunk_end = min(chunk_start + chunk, n_frames)
            self_align_xyz = np.asarray(self._h5xyz[chunk_start:chunk_end, atom_indices, :], order='c')
            self_displace_xyz = np.asarray(self._h5xyz[chunk_start:chunk_end], order='c')
        

            offset = np.mean(self_align_xyz, axis=1, dtype=np.float64).reshape(n_frames, 1, 3)
            self_align_xyz -= offset
            if self_align_xyz.ctypes.data != self_displace_xyz.ctypes.data:
                # when atom_indices is None, these two arrays alias the same memory
                # so we only need to do the centering once
                self_displace_xyz -= offset

        
            self_g = np.einsum('ijk,ijk->i', self_align_xyz, self_align_xyz)
            ref_g = np.einsum('ijk,ijk->i', ref_align_xyz , ref_align_xyz)

            _rmsd.superpose_atom_major(
                ref_align_xyz, self_align_xyz, ref_g, self_g, self_displace_xyz,
                0, parallel=parallel)

            self_displace_xyz += ref_offset
            self._h5xyz[chunk_start:chunk_end] = self_displace_xyz
            chunk_start = chunk_end
        return self

    def join(self, other, check_topology=True, discard_overlapping_frames=False):
        """Join two trajectories together along the time/frame axis.
        This method joins trajectories along the time axis, giving a new trajectory
        of length equal to the sum of the lengths of `self` and `other`.
        It can also be called by using `self + other`
        Parameters
        ----------
        other : Trajectory or list of Trajectory
            One or more trajectories to join with this one. These trajectories
            are *appended* to the end of this trajectory.
        check_topology : bool
            Ensure that the topology of `self` and `other` are identical before
            joining them. If false, the resulting trajectory will have the
            topology of `self`.
        discard_overlapping_frames : bool, optional
            If True, compare coordinates at trajectory edges to discard overlapping
            frames.  Default: False.
        See Also
        --------
        stack : join two trajectories along the atom axis
        """
        

        if isinstance(other, Trajectory):
            other = [other]
        if isinstance(other, list):
            if not all(isinstance(o, Trajectory) for o in other):
                raise TypeError('You can only join Trajectory instances')
            if not all(self.n_atoms == o.n_atoms for o in other):
                raise  ValueError('Number of atoms in self (%d) is not equal '
                          'to number of atoms in other' % (self.n_atoms))
            if check_topology and not all(self.topology == o.topology for o in other):
                raise ValueError('The topologies of the Trajectories are not the same')
            if not all(self._have_unitcell == o._have_unitcell for o in other):
                raise ValueError('Mixing trajectories with and without unitcell')
        else:
            raise TypeError('`other` must be a list of Trajectory. You supplied %d' % type(other))


        # list containing all of the trajs to merge, including self
        trajectories = [self] + other
        if discard_overlapping_frames:
            for i in range(len(trajectories)-1):
                # last frame of trajectory i
                x0 = trajectories[i].xyz[-1]
                # first frame of trajectory i+1
                x1 = trajectories[i + 1].xyz[0]

                # check that all atoms are within 2e-3 nm
                # (this is kind of arbitrary)
                if np.all(np.abs(x1 - x0) < 2e-3):
                    trajectories[i] = trajectories[i][:-1]

        new_traj = self.__class__(self.xyz, deepcopy(self._topology), time=self.time,
            unitcell_lengths=self.unitcell_lengths, unitcell_angles=self.unitcell_angles)
        for t in trajectories[1:]:
            new_traj.append(t)
        return new_traj

    def atom_slice(self, atom_indices, inplace=False):
        """Create a new trajectory from a subset of atoms
        Parameters
        ----------
        atom_indices : array-like, dtype=int, shape=(n_atoms)
            List of indices of atoms to retain in the new trajectory.
        inplace : bool, default=False
            If ``True``, the operation is done inplace, modifying ``self``.
            Otherwise, a copy is returned with the sliced atoms, and
            ``self`` is not modified.
        Returns
        -------
        traj : h5.Trajectory
            The return value is either ``self``, or the new trajectory,
            depending on the value of ``inplace``.
        See Also
        --------
        stack : stack multiple trajectories along the atom axis
        """
        xyz = np.array(self.xyz[:, atom_indices], order='C')
        topology = None
        if self._topology is not None:
            topology = self._topology.subset(atom_indices)

        if inplace:
            if self._topology is not None:
                self._topology = topology
            self._xyz = xyz

            return self

        unitcell_lengths = unitcell_angles = None
        if self._have_unitcell:
            unitcell_lengths = self._unitcell_lengths.copy()
            unitcell_angles = self._unitcell_angles.copy()
        time = self._time.copy()

        return Trajectory(xyz=xyz, topology=topology, time=time,
                          unitcell_lengths=unitcell_lengths,
                          unitcell_angles=unitcell_angles)

    def center_coordinates(self, mass_weighted=False):
        """Center each trajectory frame at the origin (0,0,0).
        This method acts inplace on the trajectory.  The centering can
        be either uniformly weighted (mass_weighted=False) or weighted by
        the mass of each atom (mass_weighted=True).
        Parameters
        ----------
        mass_weighted : bool, optional (default = False)
            If True, weight atoms by mass when removing COM.
        Returns
        -------
        self
        """
        chunk = 100
        n_frames = self.n_frames
        chunk_start = 0
        traces = []
        while chunk_start < n_frames:
            chunk_end = min(chunk_start + chunk, n_frames)
            t = mdt.Trajectory(self.xyz[chunk_start:chunk_end], self.top)
            if mass_weighted and self.top is not None:
                t.xyz -= distance.compute_center_of_mass(t)[:, np.newaxis, :]
            else:
                t._rmsd_traces = _rmsd._center_inplace_atom_major(t._xyz)
            self._h5xyz[chunk_start:chunk_end] = t.xyz
            traces.append(t._rmsd_traces)
            chunk_start = chunk_end
        #self._rmsd_traces = np.concatenate(traces)
        return self

def load(filename_or_filenames, top=None, **kwargs):
    """Load a trajectory from one or more files on disk.
    This function dispatches to one of the specialized trajectory loaders based
    on the extension on the filename. Because different trajectory formats save
    different information on disk, the specific keyword argument options supported
    depend on the specific loaded.
    Parameters
    ----------
    filename_or_filenames : {str, list of strings}
        Filename or list of filenames containing trajectory files.
    discard_overlapping_frames : bool, default=False
        Look for overlapping frames between the last frame of one filename and
        the first frame of a subsequent filename and discard them
    chunk : int, default = 100
        Number of frames to load in each chunk that is then appended to the underpinning
        temporary hdf5 file, thus limiting the memory burden. If zero, each file is
        loaded as one chunk.
    Other Parameters
    ----------------
    top : {str, Trajectory, Topology}
        Most trajectory formats do not contain topology information. Pass in
        either the path to a RCSB PDB file, a trajectory, or a topology to
        supply this information. This option is not required for the .h5, .lh5,
        and .pdb formats, which already contain topology information.
    stride : int, default=None
        Only read every stride-th frame
    atom_indices : array_like, optional
        If not none, then read only a subset of the atoms coordinates from the
        file. This may be slightly slower than the standard read because it
        requires an extra copy, but will save memory.
    Returns
    -------
    trajectory : h5t.Trajectory
        The resulting trajectory, as an h5t.Trajectory object.
    """
    if isinstance(filename_or_filenames, str):
        filenames = [filename_or_filenames]
    else:
        filenames = filename_or_filenames
    traj = None
    kwargs.pop('discard_overlapping_frames', None)
    for f in filenames:
        if os.path.splitext(f)[1] in ['.pdb', '.gro']:
            chunk = mdt.load(f, **kwargs)
            if traj is None:
                traj = Trajectory(chunk.xyz, chunk.topology, time=chunk.time, 
                                  unitcell_lengths=chunk.unitcell_lengths,
                                  unitcell_angles=chunk.unitcell_angles)
            else:
                traj.append(chunk)
        else:    
            for chunk in iterload(f, top=top, **kwargs):
                if traj is None:
                    traj = Trajectory(chunk.xyz, chunk.topology, 
                                      time=chunk.time, 
                                      unitcell_lengths=chunk.unitcell_lengths,
                                      unitcell_angles=chunk.unitcell_angles)
                else:
                    traj.append(chunk)
    return traj

def iterload(filename, chunk=100, **kwargs):
    """An iterator over a trajectory from one or more files on disk, in fragments
    This may be more memory efficient than loading an entire trajectory at
    once
    Parameters
    ----------
    filename : str
        Path to the trajectory file on disk
    chunk : int
        Number of frames to load at once from disk per iteration.  If 0, load all.
    Other Parameters
    ----------------
    top : {str, Trajectory, Topology}
        Most trajectory formats do not contain topology information. Pass in
        either the path to a RCSB PDB file, a trajectory, or a topology to
        supply this information. This option is not required for the .h5, .lh5,
        and .pdb formats, which already contain topology information.
    stride : int, default=None
        Only read every stride-th frame.
    atom_indices : array_like, optional
        If not none, then read only a subset of the atoms coordinates from the
        file. This may be slightly slower than the standard read because it
        requires an extra copy, but will save memory.
    skip : int, default=0
        Skip first n frames.
    See Also
    --------
    load, load_frame
    Examples
    --------
    >>> import mdtraj as md
    >>> for chunk in md.iterload('output.xtc', top='topology.pdb')
    ...    print chunk
    <mdtraj.Trajectory with 100 frames, 423 atoms at 0x110740a90>
    <mdtraj.Trajectory with 100 frames, 423 atoms at 0x110740a90>
    <mdtraj.Trajectory with 100 frames, 423 atoms at 0x110740a90>
    <mdtraj.Trajectory with 100 frames, 423 atoms at 0x110740a90>
    <mdtraj.Trajectory with 100 frames, 423 atoms at 0x110740a90>
    """
    stride = kwargs.pop('stride', 1)
    atom_indices = cast_indices(kwargs.pop('atom_indices', None))
    top = kwargs.pop('top', None)
    skip = kwargs.pop('skip', 0)

    extension = _get_extension(filename)
    if extension not in _TOPOLOGY_EXTS:
        topology = mdt.load_topology(top)

    if chunk == 0:
        # If chunk was 0 then we want to avoid filetype-specific code
        # in case of undefined behavior in various file parsers.
        # TODO: this will first apply stride, then skip!
        if extension not in _TOPOLOGY_EXTS:
            kwargs['top'] = top
        yield mdt.load(filename, **kwargs)[skip:]
    elif extension in ('.pdb', '.pdb.gz'):
        # the PDBTrajectortFile class doesn't follow the standard API. Fixing it
        # to support iterload could be worthwhile, but requires a deep refactor.
        t = mdt.load(filename, stride=stride, atom_indices=atom_indices)
        for i in range(0, len(t), chunk):
            yield t[i:i+chunk]
    elif extension in ('.gsd'):
        i = 0
        while True:
            traj = mdt.load(filename, stride=stride, atom_indices=atom_indices,
                    start=i, n_frames=chunk)
            if len(traj) ==0 :
                return
            i += chunk
            yield traj
    else:
        with (lambda x: mdt.open(x, n_atoms=topology.n_atoms)
              if extension in ('.crd', '.mdcrd')
              else mdt.open(filename))(filename) as f:
            if skip > 0:
                f.seek(skip)
            while True:
                if extension not in _TOPOLOGY_EXTS:
                    traj = f.read_as_traj(topology, n_frames=chunk*stride, stride=stride, atom_indices=atom_indices, **kwargs)
                else:
                    traj = f.read_as_traj(n_frames=chunk*stride, stride=stride, atom_indices=atom_indices, **kwargs)

                if len(traj) == 0:
                    return

                yield traj
