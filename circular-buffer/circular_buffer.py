class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None for _ in range(capacity)]
        self.capacity = capacity
        self.size = 0
        self.read_pointer = 0
        self.write_pointer = 0

    def write(self, data):
        # if buffer is full, raise an exception
        if self.size > 0:
            if self.capacity == self.size or self.read_pointer == self.write_pointer:
                raise BufferFullException("Circular buffer is full")

        # writes the new value
        self.buffer[self.write_pointer] = data

        # sets new size and pointer position
        self.size += 1
        self.write_pointer = (self.write_pointer + 1) % self.capacity

    def read(self):
        # checks if the buffer is empty
        if self.size == 0:
            raise BufferEmptyException("Circular buffer is empty")

        # gets the value at the pointer position
        value = self.buffer[self.read_pointer]

        # sets new size and pointer position
        self.size -= 1
        self.read_pointer = (self.read_pointer + 1) % self.capacity

        # returns the value at the original pointer position
        return value

    def overwrite(self, data):
        # if there is space left, function acts like write()
        if self.size < self.capacity:
            self.write(data)

        # else overwrite the oldest item and advances both pointers
        else:
            self.buffer[self.write_pointer] = data
            self.write_pointer = (self.write_pointer + 1) % self.capacity
            self.read_pointer = (self.read_pointer + 1) % self.capacity

    def clear(self):
        # resets init values
        self.buffer = [None for _ in range(self.capacity)]
        self.capacity = self.capacity
        self.size = 0
        self.read_pointer = 0
        self.write_pointer = 0
