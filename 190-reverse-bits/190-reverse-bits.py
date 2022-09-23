class Solution:
    def reverseBits(self, n: int) -> int:
        # convert int to binary string and remove '0b'
        data = bin(n)[2:]
         # zfill is used to add zeros at the begining of the string until it reaches the length as specified
        data = data.zfill(32)
        # slicing technique to reverse the string
        data = data[::-1]
        # integer conversion with base 2
        return int(data, 2)