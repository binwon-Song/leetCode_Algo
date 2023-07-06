class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 양수의 정수 배열이 주어짐
        # target 또한 양수임
        # 최소 길이 서브 배열을 반환해야함 (배열의 합이 target과 같거나 높아야함 )
        # 아무런 서브 배열이 없으면 0 반환
        n = len(nums)
        max_value = max(nums)

        if max_value >= target:
            return 1

        left = 0
        right = 0
        curr_sum = 0
        min_len = float('inf')

        while right < n:
            curr_sum += nums[right]

            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != float('inf') else 0