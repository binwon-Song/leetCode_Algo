from heapq import heappush, heappop
class Solution:
    # def heap_sort(heap,size):
    #     result=[]
    #     for i in range(size):
    #             result.append(heappop(heap)[1:])
    #     return result

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], 
    k: int) -> List[List[int]]:
        #num1 and num2 is ascending array
        # (u,v) is first array element and one element of second array
        result=[]
        heap=[]
        visited=set()
        len_num1=len(nums1)
        len_num2=len(nums2)

        # all sequence
        # for i in nums1:
        #         for j in nums2:
        #             heappush(heap,[i+j,i,j])
        heappush(heap,[nums1[0]+nums2[0],0,0])        
        visited.add((0,0))
        
        while k and heap:
            # if len_num1*len_num2<=k: # all possible way
            #     for i in range(len_num1*len_num2):
            #         result.append(heappop(heap)[1:])
            #     return result
            # else: # k pair
            #     for i in range(k):
            #         result.append(heappop(heap)[1:])
            _,num1_idx,num2_idx=heappop(heap)
            result.append([nums1[num1_idx],nums2[num2_idx]])
            if num1_idx+1<len_num1 and (num1_idx+1,num2_idx) not in visited:
                heappush(heap,[nums1[num1_idx+1]+nums2[num2_idx],num1_idx+1,num2_idx])
                visited.add((num1_idx+1,num2_idx))
            if num2_idx+1<len_num2 and (num1_idx,num2_idx+1) not in visited:
                heappush(heap,[nums1[num1_idx]+nums2[num2_idx+1],num1_idx,num2_idx+1])
                visited.add((num1_idx,num2_idx+1))
            
            k-=1
        return result