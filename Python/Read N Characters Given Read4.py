"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read_bytes = 0
        
        while True:
            buffer = [""] * 4
            cur = read4(buffer)
            cur_length = min(cur, n - read_bytes)
            
            for i in xrange(cur_length):
                buf[read_bytes + i] = buffer[i]
            read_bytes += cur_length
            
            if cur is not 4 or read_bytes is n: break
        return read_bytes
