from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Return the k most frequent elements in nums

        Args:
            nums: non-empty integer arrays
            k: number of most frequent elemets, where 1 <= k < len(unique nums)

        Return:
            k most frequent elements in a list

        Trick: use heapify to get top k instead of sorting

        Bucket Sort: O(n)
        Heap: O(n + k log m)
        Sort: O(n + m log m)
        where n is len(nums), m is # of unique numbers, k is requested

        Time Complexity: O(n) 
        Space Complexity: O(n)
        """
        # Use hashmap to calculate freqeuncy of each elements
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # TRICK: BUCKET SORT
        # freq table[f] = [n], f is frequency, n is element
        freq = [[] for _ in range(len(nums)+1)] 
        for (n, c) in count.items():
            freq[c-1].append(n)

        # get top k
        res, i = [], len(nums)-1
        while i >= 0 and len(res) < k:
            res += freq[i]
            i -= 1
        return res

        # HEAP: heap to get top k
        # heap = [(-freq, n) for (n, freq) in count.items()]
        # heapq.heapify(heap)
        # res = [heapq.heappop(heap)[1] for _ in range(k)]
        # return res

        # SORT: Sort the hashmap O(m) where m is number number of unique elements in nums max 95
        # lambda i : i sort by key, lambda i : count[i] sort by values, lambda i : lenth[i] sort by length
        # sorted_count = sorted(count, key = lambda i: count[i], reverse=True)
        # return sorted_count[:k]