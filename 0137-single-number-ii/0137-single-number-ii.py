class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 모든 요소는 3번 등장 1개 제외
        # 제외된 1개는 정확히 1번 등장함
        # 제외된 1개를 찾아야함
        # 선형시간, 일정한 추가 공간 사용
        dict=defaultdict(int)
        for i in nums:
            dict[i]+=1
        for key,value in dict.items():
            if value==1:
                return key
        