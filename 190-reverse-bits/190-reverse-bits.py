class Solution:
    def reverseBits(self, n: int) -> int:
        # convert int to binary string
        data = bin(n)
        # 0b000........ we are only selecting our string after 2nd index
        data = data[2:]
         # zfill is used to add zeros at the begining of the string until it reaches the length as specidifed
        data = data.zfill(32)
        # slicing technique to reverse the string
        data = data[::-1]
        # integer conversion with base 2
        return int(data, 2)