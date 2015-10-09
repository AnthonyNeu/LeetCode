"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
"""


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buffer_size = 0
        self.buffer_offset = 0 
        self.buffer = [""] * 4
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read_bytes = 0
        eof = False
        while read_bytes < n and not eof:
            if self.buffer_size is 0:
                cur = read4(self.buffer)
            else:
                cur = self.buffer_size
            if self.buffer_size is 0 and cur < 4:
                eof = True

            cur_length = min(cur, n - read_bytes)
            for i in xrange(cur_length):
                buf[read_bytes + i] = self.buffer[self.buffer_offset + i]
            
            read_bytes += cur_length
            self.buffer_offset = (self.buffer_offset + cur_length) % 4
            self.buffer_size = cur - cur_length
        return read_bytes
