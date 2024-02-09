# Explanation for LRU Cache Solution

## Reasoning Behind Decisions:

### Data Structure:

The solution utilizes an OrderedDict from the collections module in Python. OrderedDict is chosen for its ability to maintain the order of elements, which is essential for implementing the Least Recently Used (LRU) cache eviction policy. This data structure allows efficient access and manipulation of cache entries while preserving their insertion order.

### Initialization:

In the constructor **init**(), an OrderedDict named cache is created to store key-value pairs. The choice of OrderedDict ensures that the order of elements reflects their access history. Additionally, the capacity of the cache is stored to ensure efficient eviction of least recently used items when the cache reaches its maximum capacity.

### Retrieving Values:

The get() method checks if the requested key exists in the cache. If the key is found, it moves the corresponding key-value pair to the end of the OrderedDict, indicating recent access. This approach ensures that frequently accessed items remain towards the end of the cache, improving access time for subsequent requests.

### Setting Values:

The set() method updates the cache with a new key-value pair. If the key already exists in the cache, its value is updated, and the key is moved to the end of the OrderedDict to reflect recent access. If the cache exceeds its capacity after inserting the new key-value pair, the method evicts the least recently used item by removing the first item inserted into the OrderedDict.

## Time Efficiency:

Both get() and set() operations have a time complexity of O(1). This is because accessing, updating, and moving elements in an OrderedDict can be performed in constant time.
The efficient handling of cache operations ensures that the time complexity remains constant, irrespective of the size of the cache or the number of items stored.

## Space Efficiency:

The space complexity of the solution depends on the number of key-value pairs stored in the cache and the capacity of the cache.
If the capacity of the cache is limited to N items, and the cache contains M items, the space complexity would be O(N + M), as the cache and the OrderedDict can together contain at most N + M elements.
