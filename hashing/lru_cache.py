class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.recent_used = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            del self.recent_used[key]
            self.recent_used[key] = key
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.recent_used[key]
            self.recent_used[key] = key
            self.cache[key] = value
            return

        if len(self.cache) == self.capacity:
            least_used_key = self.recent_used[next(iter(self.recent_used))]
            del self.recent_used[least_used_key]
            del self.cache[least_used_key]

        self.cache[key] = value
        self.recent_used[key] = key

# Time complexity is O(1) for both get and put operations
# Space complexity is O(n) where n is the capacity of the cache

# Test cases

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
cache.put(5, 5)
assert cache.get(3) == -1
assert cache.get(4) == 4
assert cache.get(5) == 5

print("All test cases passed successfully.")
