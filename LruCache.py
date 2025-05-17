class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}

    def get(self, key: int) -> int:
        val = self.cache_dict.pop(key, -1)
        if val != -1:
            self.cache_dict[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if len(self.cache_dict) == self.capacity:
            # self.cache_dict.popitem(last = False)
            first_key = next(iter(self.cache_dict))
            del self.cache_dict[first_key]

        else:
            self.cache_dict.pop(key, -1)
        self.cache_dict[key] = value


["LRUCache", [2], "get", [2], "put", [2, 6], "get", [1], "put", [1, 5], "put", [1, 2], "get", [1], "get", [2]]
l = LRUCache(2)
print(l.get(2))
print(l.put(2,6))
print(l.get(1))
print(l.put(1,5))
print(l.put(1,2))
print(l.get(1))
print(l.get(2))
