class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = []
        for word, freq in count.items():
            heap.append((-freq, word))
        
        heapq.heapify(heap)

        res = []

        for _ in range(k):
            freq, word = heapq.heappop(heap)
            res.append(word)

        return res
        