class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,h,curr=0,len(nums)-1,0
        while(curr<=h):
            if nums[curr]==0:
                nums[l],nums[curr]=nums[curr],nums[l]
                l+=1
                curr+=1
            elif nums[curr]==1:
                curr+=1
            elif nums[curr]==2:
                nums[h],nums[curr]=nums[curr],nums[h]
                h-=1    