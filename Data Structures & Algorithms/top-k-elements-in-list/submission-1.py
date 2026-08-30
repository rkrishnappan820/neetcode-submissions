class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = defaultdict(int)
        output = []
        for num in nums:
            nums_freq[num] += 1
        
        sorted_nums_freq = dict(sorted(nums_freq.items(), key=lambda x : x[1], reverse=True))
        print(sorted_nums_freq)
        for sorted_num in sorted_nums_freq:
            if k > 0:
               output.append(sorted_num) 
               k -= 1
        return output