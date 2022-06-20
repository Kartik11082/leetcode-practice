class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
#         if len(nums) == 0:
#             return None
#         left, right = 0, len(nums) - 1
#         mid = left + (right - left) // 2
        
#         node = TreeNode(nums[mid])
#         node.left = self.sortedArrayToBST(nums[:mid])
#         node.left = self.sortedArrayToBST(nums[mid:])
        
        # return node
        
        def constructTree(nums, left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])

            node.left = constructTree(nums, left, mid - 1)
            node.right = constructTree(nums, mid + 1, right)        

            return node
        
        if len(nums) == 0:
            return null
        left, right = 0, len(nums) - 1
        return constructTree(nums, left, right)
