class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 바이너리 리스트(0..1)
        # 한 개 제거해야함
        # 최장 서브 배열의 길이를 반환
        # 최장 서브 배열은 오직 1개의 결과 배열을 가져야함
        # 서브 배열이 없으면 0 반환
        
        # 0이 없는 경우 있는 경우
        zero_cnt=[]
        given_len=len(nums)
        for i in range(given_len):
            num=nums[i]
            if num==0:
                zero_cnt.append(i)
        
        if not zero_cnt:
            return given_len-1
        result=[]
        max_len=0
        for zero_idx in zero_cnt:
            cnt=0
            # print("zero idx ",zero_idx)
            for i in range(given_len):
                # print(f"i : {i} cnt : {cnt}")
                if i==zero_idx:
                    continue
                if nums[i]==1:
                    cnt+=1
                else:
                    cnt=0
                if max_len<cnt:
                    max_len=cnt
            
            
        return max_len
    
    
#     zero idx  0
# i : 0 cnt : 0
# i : 1 cnt : 0
# i : 2 cnt : 1
# i : 3 cnt : 2
# i : 4 cnt : 3
# i : 5 cnt : 0
# i : 6 cnt : 1
# i : 7 cnt : 2
# i : 8 cnt : 0
# zero idx  4
# i : 0 cnt : 0
# i : 1 cnt : 0
# i : 2 cnt : 1
# i : 3 cnt : 2
# i : 4 cnt : 3
# i : 5 cnt : 3
# i : 6 cnt : 4
# i : 7 cnt : 5
# i : 8 cnt : 0
# zero idx  7
# i : 0 cnt : 0
# i : 1 cnt : 0
# i : 2 cnt : 1
# i : 3 cnt : 2
# i : 4 cnt : 3
# i : 5 cnt : 0
# i : 6 cnt : 1
# i : 7 cnt : 2
# i : 8 cnt : 2
