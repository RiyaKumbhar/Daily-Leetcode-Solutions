class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # a dictionary to store how many times each number appears
        freq = [[] for i in range(len(nums) + 1)] # a list where: index = frequency; value at index = list of numbers with that frequency

        for n in nums: #Loop through each number and count how many times it appears
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = [] #Prepare list to store the answer
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res