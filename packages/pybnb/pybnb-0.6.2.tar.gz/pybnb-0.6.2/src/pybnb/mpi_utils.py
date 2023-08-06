"""
Various utility function for MPI.

Copyright by Gabriel A. Hackebeil (gabe.hackebeil@gmail.com).
"""

import array

# avoids generating a deprecation warning in python 3.7
def _array_to_string(out):
    """converts an array of bytes to a string"""
    if hasattr(out, 'tobytes'):
        # array.tobytes was added in python 3.2
        return out.tobytes().decode("utf8")
    else:
        return out.tostring().decode("utf8")

class Message(object):
    """A helper class for probing for and receiving
    messages. A single instance of this class is meant to be
    reused.

    Parameters
    ----------
    comm : :class:`mpi4py.MPI.Comm`
        The MPI communicator to use.
    """
    __slots__ = ("status","data","comm")
    def __init__(self, comm):
        import mpi4py.MPI
        self.comm = comm
        self.status = mpi4py.MPI.Status()
        self.data = None
    def probe(self, **kwds):
        """Perform a blocking test for a message"""
        self.comm.Probe(status=self.status)
        self.data = None
    def recv(self, datatype=None, data=None):
        """Complete the receive for the most recent message
        probe and return the data as a numeric array or a
        string, depending on the datatype keyword.

        Parameters
        ----------
        datatype : {``mpi4py.MPI.DOUBLE``, ``mpi4py.MPI.CHAR``}, optional
            An MPI datatype used to interpret the received
            data. If None, ``mpi4py.MPI.DOUBLE`` will be
            used. (default: None)
        data : array.array or None, optional
            An existing data array to store data into. If
            None, one will be created. (default: None)
        """
        assert not self.status.Get_error()
        if datatype is None:
            count = self.status.Get_count()
        else:
            count = self.status.Get_count(datatype=datatype)
        if count == 0:
            recv_nothing(self.comm,
                         self.status)
        else:
            self.data = recv_data(self.comm,
                                  self.status,
                                  datatype=datatype,
                                  out=data)
    @property
    def tag(self): return self.status.Get_tag()
    @property
    def source(self): return self.status.Get_source()

def recv_nothing(comm, status):
    """A helper function for receiving an empty
    message. This function is not thread safe.

    Parameters
    ----------
    comm : :class:`mpi4py.MPI.Comm`
        An MPI communicator.
    status : :class:`mpi4py.MPI.Status`
        An MPI status object that has been populated with
        information about the message to be received via a
        probe. If None, a new status object will be created
        and an empty message will be expected from any
        source with any tag. (default: None)

    Returns
    -------
    status : :class:`mpi4py.MPI.Status`
        If the original status argument was not None, it
        will be returned after being updated by the
        receive. Otherwise, the status object that was
        created will be returned.
    """
    import mpi4py.MPI
    if recv_nothing._nothing is None:
        recv_nothing._nothing = [array.array("B",[]),
                                 mpi4py.MPI.CHAR]
    assert not status.Get_error()
    assert status.Get_count(mpi4py.MPI.CHAR) == 0
    comm.Recv(recv_nothing._nothing,
              source=status.Get_source(),
              tag=status.Get_tag(),
              status=status)
    assert not status.Get_error()
    assert status.Get_count(mpi4py.MPI.CHAR) == 0
    return status
recv_nothing._nothing = None

def send_nothing(comm, dest, tag=0):
    """A helper function for sending an empty message
    with a given tag. This function is not thread safe.

    Parameters
    ----------
    comm : :class:`mpi4py.MPI.Comm`
        An MPI communicator.
    dest : int
        The process rank to send the message to.
    tag : int, optional
        A valid MPI tag to use for the message. (default: 0)
    """
    import mpi4py.MPI
    if send_nothing._nothing is None:
        send_nothing._nothing = [array.array("B",[]),
                                 mpi4py.MPI.CHAR]
    comm.Send(send_nothing._nothing,
         dest,
         tag=tag)
send_nothing._nothing = None

def recv_data(comm, status, datatype, out=None):
    """A helper function for receiving numeric or string
    data sent using the lower-level buffer-based mpi4py
    routines.

    Parameters
    ----------
    comm : :class:`mpi4py.MPI.Comm`
        An MPI communicator.
    status : :class:`mpi4py.MPI.Status`
        An MPI status object that has been populated with
        information about the message to be received via a
        probe.
    datatype : :class:`mpi4py.MPI.Datatype`
        An MPI datatype used to interpret the received
        data. If the datatype is :obj:`mpi4py.MPI.CHAR`,
        the received data will be converted to a string.
    out : buffer-like object, optional
        A buffer-like object that is compatible with the datatype
        argument and can be passed to comm.Recv. Can only be left
        as None when the datatype is :obj:`mpi4py.MPI.CHAR`.

    Returns
    -------
    string or user-provided data buffer
    """
    import mpi4py.MPI
    assert not status.Get_error()
    size = status.Get_count(datatype)
    if datatype == mpi4py.MPI.CHAR:
        assert out is None
        out = array.array("B",b"\0")*size
    assert (out is not None) and \
        (len(out) >= size)
    comm.Recv([out,datatype],
              source=status.Get_source(),
              tag=status.Get_tag(),
              status=status)
    assert not status.Get_error()
    if datatype == mpi4py.MPI.CHAR:
        out = _array_to_string(out)
    return out
