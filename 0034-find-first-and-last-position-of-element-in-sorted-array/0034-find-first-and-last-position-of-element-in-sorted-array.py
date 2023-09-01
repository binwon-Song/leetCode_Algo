class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 비 내림차순 -> 오름차순
        # 타겟 값의 시작, 끝 지점을 찾아라
        # 타겟 값이 존재하지 않으면 [-1,-1] 반환
        
        # solution 1 : two pointer
        # solution 2 : bi-search
        
        start=0
        end=len(nums)-1
        ans=[-1,-1]
        while start<=end:
            mid=(start+end)//2
            print(mid,start,end)
            if nums[mid]==target:
                ans[0]=ans[1]=mid
                i=0
                while mid-i>=0 and nums[mid-i]==target: 
                    i+=1
                ans[0]=mid-i+1
                
                i=0
                while mid+i<len(nums) and nums[mid+i]==target: 
                    i+=1
                ans[1]=mid+i-1
                
                return ans
            if nums[mid]<=target:  # target is right
                print("target is right side")
                start=mid+1
            if nums[mid]>target: # target is left
                print("target is left side")
                end=mid-1
                
        return ans