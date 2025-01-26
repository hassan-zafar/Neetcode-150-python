from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # If k equals the number of elements in nums, return nums directly
        if k == len(nums):
            return nums

        # Count the frequency of each number
        count = Counter(nums)

        # Use a heap (min-heap by default in Python)
        # The heap will store elements based on their frequency
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))  # Push (frequency, number) onto the heap
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the element with the smallest frequency

        # Extract the elements from the heap, which are the top k frequent elements
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # If k equals the number of elements in nums, return nums directly
        if k == len(nums):
            return nums

        # Count the frequency of each number
        count = Counter(nums)

        # Use a heap (min-heap by default in Python)
        # The heap will store elements based on their frequency
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))  # Push (frequency, number) onto the heap
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the element with the smallest frequency

        # Extract the elements from the heap, which are the top k frequent elements
        return [num for _, num in heap]
