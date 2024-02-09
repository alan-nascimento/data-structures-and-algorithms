from collections import OrderedDict
from typing import Any


class LRU_Cache:
    def __init__(self, capacity: int) -> None:
        self.cache: OrderedDict[Any, Any] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: Any) -> Any:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: Any, value: Any) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Test Case 1: Basic test case
cache = LRU_Cache(2)
cache.set(1, 1)
cache.set(2, 2)
assert cache.get(1) == 1
assert cache.get(2) == 2

# Test Case 2: Test case with null value
cache = LRU_Cache(2)
cache.set(1, None)
assert cache.get(1) == None

# Test Case 3: Test case with empty cache
cache = LRU_Cache(0)
cache.set(1, 1)
assert cache.get(1) == -1  # Expected output: -1 (cache size is 0)

# Test Case 4: Test case with large capacity
cache = LRU_Cache(1000000)
for i in range(1000000):
    cache.set(i, i)
assert cache.get(999999) == 999999  # Expected output: 999999 (most recently used)

# Test Case 5: Test case exceeding capacity
cache = LRU_Cache(2)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
assert cache.get(1) == -1  # Expected output: -1 (1 was evicted)
assert cache.get(2) == 2
assert cache.get(3) == 3  # Expected output: 3 (most recently used)

print("All test cases passed successfully!")
