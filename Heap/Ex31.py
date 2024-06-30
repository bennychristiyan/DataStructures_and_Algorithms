"""Write a function named stream_max that takes as its input a list of integers (nums). The function should return a list of the same length, 
where each element in the output list is the maximum number seen so far in the input list.
More specifically, for each index i in the input list, the element at the same index in the output list should be the maximum value among the 
elements at indices 0 through i in the input list.
Use the provided MaxHeap class to solve this problem. You should not need to modify the MaxHeap class to complete this task.

Function Signature: def stream_max(nums):

Examples:
If the input list is [1, 3, 2, 5, 4], the function should return [1, 3, 3, 5, 5].

Explanation:
    At index 0, the maximum number seen so far is 1.
    At index 1, the maximum number seen so far is 3.
    At index 2, the maximum number seen so far is still 3.
    At index 3, the maximum number seen so far is 5.
    At index 4, the maximum number seen so far is still 5.

So, the output list is [1, 3, 3, 5, 5].
Similarly, if the input list is [7, 2, 4, 6, 1], the function should return [7, 7, 7, 7, 7].

Explanation:
    At each index, the maximum number seen so far is 7.

So, the output list is [7, 7, 7, 7, 7].

Constraints:
You may assume that the input list does not contain any null or undefined elements"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
                       
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
        


def stream_max(nums):
    a = MaxHeap()
    result = []
    for i in nums:
        a.insert(i)
        result.append(a.heap[0])
    return result
    



test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i+1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')


#Output
"""

    Test 1
    Input: []
    Expected Output: []
    Actual Output: []
    Status: Passed
    Test 2
    Input: [1]
    Expected Output: [1]
    Actual Output: [1]
    Status: Passed
    Test 3
    Input: [1, 2, 3, 4, 5]
    Expected Output: [1, 2, 3, 4, 5]
    Actual Output: [1, 2, 3, 4, 5]
    Status: Passed
    Test 4
    Input: [1, 2, 2, 1, 3, 3, 3, 2, 2]
    Expected Output: [1, 2, 2, 2, 3, 3, 3, 3, 3]
    Actual Output: [1, 2, 2, 2, 3, 3, 3, 3, 3]
    Status: Passed
    Test 5
    Input: [-1, -2, -3, -4, -5]
    Expected Output: [-1, -1, -1, -1, -1]
    Actual Output: [-1, -1, -1, -1, -1]
    Status: Passed

"""

