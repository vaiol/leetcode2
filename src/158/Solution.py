# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = [None] * 4
        self.buf4_len = 0
        self.buf4_i = 0
        self.buf_i = 0

    def file_read(self) -> int:
        self.buf4_len = read4(self.buf4)
        self.buf4_i = 0
        return self.buf4_len

    def buf4_read(self, buf: List[str], n: int) -> int:
        while self.buf4_len > 0 and n > 0:
            buf[self.buf_i] = self.buf4[self.buf4_i]
            self.buf4_len -= 1
            n -= 1
            self.buf_i += 1
            self.buf4_i += 1
        return n

    def read(self, buf: List[str], n: int) -> int:
        self.buf_i = 0
        tmp_n = n
        n = self.buf4_read(buf, n)
        while n > 0:
            read = self.file_read()
            n = self.buf4_read(buf, n)
            if read < 4:
                return tmp_n - n
        return tmp_n
        
        
            
        
