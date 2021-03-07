class HashMapBucketNode:
    def __init__(self, key: int or None, val: int or None):
        self.val = val
        self.key = key
        self.next: HashMapBucketNode or None = None
        self.prev: HashMapBucketNode or None = None

class HashMapBucketArray:
    def __init__(self):
        self.list = []

    def add(self, key: int, val: int) -> None:
        for item in self.list:
            if item[0] == key:
                item[1] = val
                return

        self.list.append([key, val])

    def get(self, key: int) -> int:
        for item in self.list:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        for i, item in enumerate(self.list):
            if item[0] == key:
                del self.list[i]


class HashMapBucketList:
    def __init__(self):
        self.head = HashMapBucketNode(None, None)
        self.tail = HashMapBucketNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_node(self, key: int) -> HashMapBucketNode or None:
        curr = self.head.next
        while curr and curr.next:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    def add(self, key: int, val: int) -> None:
        curr = self.get_node(key)
        if curr:
            curr.val = val
            return

        new_node = HashMapBucketNode(key, val)

        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def get(self, key: int) -> int:
        curr = self.get_node(key)
        return curr.val if curr else -1

    def remove(self, key: int) -> int:
        curr = self.get_node(key)
        if curr:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.next = None
            curr.prev = None
            return curr.val
        return -1


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.modulo = 2069
        self.buckets = [HashMapBucketArray() for _ in range(self.modulo)]


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.modulo
        self.buckets[index].add(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.modulo
        return self.buckets[index].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.modulo
        self.buckets[index].remove(key)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
