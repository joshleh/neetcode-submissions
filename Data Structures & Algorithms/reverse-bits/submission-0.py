class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for bit in range(0, 32):
            # shift result left by 1 (make room)
            result <<= 1

            # take rightmost bit from n
            rightmost = n & 1

            # add that bit into result (copy current bit from n)
            result |= rightmost

            # shift n right by 1 (move to next bit)
            n >>= 1

        return result