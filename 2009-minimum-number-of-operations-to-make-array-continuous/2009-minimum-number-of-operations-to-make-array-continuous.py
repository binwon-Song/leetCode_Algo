class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        
        for i in range(len(new_nums)): # sort한 배열 돎
            left = new_nums[i] # 배열 인덱스 start 설정
            right = left + n - 1 # right는 정해져 있음
            j = bisect_right(new_nums, right) # 이진 탐색으로 끝 지점을 찾음
            count = j - i  # 끝 지점보다 밖에 있는 값들을 카운트함
            ans = min(ans, n - count)  # len-count는 최소 연산 횟수임

        return ans