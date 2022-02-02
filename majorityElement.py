class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = dict()

        for n in nums:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1
        for key, value in hm.items():
            if (value >= (len(nums) / 2)):
                return key

        return -1

# Python implementation for the above approach

# Function to find majority element
def findMajority(arr, n):
	candidate = -1
	votes = 0
	
	# Finding majority candidate
	for i in range (n):
		if (votes == 0):
			candidate = arr[i]
			votes = 1
		else:
			if (arr[i] == candidate):
				votes += 1
			else:
				votes -= 1
	count = 0
	
	# Checking if majority candidate occurs more than n/2
	# times
	for i in range (n):
		if (arr[i] == candidate):
			count += 1
			
	if (count > n // 2):
		return candidate
	else:
		return -1

# Driver Code

arr = [ 2, 2, 2, 1, 1, 1, 1]
n = len(arr)
majority = findMajority(arr, n)
print(" The majority element is :" ,majority)
	
# This code is contributed by shivanisinghss2110
