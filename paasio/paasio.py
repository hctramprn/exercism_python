import io

# MeteredFile: Implement using a subclassing model

class MeteredFile(io.BufferedReader):
    """A custom file class that provides metering capabilities for read and write operations."""

    def __init__(self, *args, **kwargs):
        # Initialize the MeteredFile instance by calling the superclass constructor
        super().__init__(*args, **kwargs)
        # Initialize metering attributes
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0
        # Flag to indicate if the context manager has been entered
        self._context_manager_entered = False

    def __enter__(self):
        # When entering the context manager, set the flag to True
        self._context_manager_entered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # When exiting the context manager, set the flag to False and call the superclass's __exit__ method
        self._context_manager_entered = False
        return super().__exit__(exc_type, exc_val, exc_tb)

    def read(self, size=-1):
        # Read data from the file using the superclass's read method
        data = super().read(size)
        # Update metering attributes if the context manager has been entered
        if self._context_manager_entered:
            self._read_bytes += len(data)
            self._read_ops += 1
        return data

    def write(self, b):
        # Write data to the file using the superclass's write method
        written_bytes = super().write(b)
        # Update metering attributes if the context manager has been entered
        if self._context_manager_entered:
            self._write_bytes += written_bytes
            self._write_ops += 1
        return written_bytes

    def __iter__(self):
        # Allow the file object to be an iterable and return itself
        return self

    def __next__(self):
        # Read the next line from the file using the superclass's readline method
        data = super().readline()
        # Update metering attributes for the read operation
        self._read_bytes += len(data)
        self._read_ops += 1
        # Raise StopIteration if there is no data to read
        if data:
            return data
        else:
            raise StopIteration

    @property
    def read_bytes(self):
        # Property to get the total number of bytes read
        return self._read_bytes

    @property
    def read_ops(self):
        # Property to get the total number of read operations
        return self._read_ops

    @property
    def write_bytes(self):
        # Property to get the total number of bytes written
        return self._write_bytes

    @property
    def write_ops(self):
        # Property to get the total number of write operations
        return self._write_ops


# MeteredSocket: Implement using a delegation model

class MeteredSocket:
    """A custom socket class that provides metering capabilities for recv and send operations."""

    def __init__(self, socket):
        # Store the provided socket object
        self._socket = socket
        # Initialize metering attributes
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self):
        # Context manager entry point, return the instance itself
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Pass any exceptions to the original socket's __exit__ method
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        # Receive data from the socket using the original socket's recv method
        data = self._socket.recv(bufsize, flags)
        # Update metering attributes for the receive operation
        self._recv_bytes += len(data)
        self._recv_ops += 1
        return data

    @property
    def recv_bytes(self):
        # Property to get the total number of bytes received
        return self._recv_bytes

    @property
    def recv_ops(self):
        # Property to get the total number of receive operations
        return self._recv_ops

    def send(self, data, flags=0):
        # Send data over the socket using the original socket's send method
        sent_bytes = self._socket.send(data, flags)
        # Update metering attributes for the send operation
        self._send_bytes += sent_bytes
        self._send_ops += 1
        return sent_bytes

    @property
    def send_bytes(self):
        # Property to get the total number of bytes sent
        return self._send_bytes

    @property
    def send_ops(self):
        # Property to get the total number of send operations
        return self._send_ops
