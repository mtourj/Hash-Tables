# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        if self.next:
            return f"<{self.value} + more ({self.next})>"
        return f"<{self.value}>"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.size = 0
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value, no_resize=False):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''

        if self.size >= self.capacity and no_resize is False:
            self.resize()

        self.size += 1

        target_index = self._hash_mod(key)

        bucket = self.storage[target_index]

        if bucket is None:
            self.storage[target_index] = LinkedPair(key, value)
        else:
            prev_bucket = None
            while bucket is not None:
                if bucket.key == key:
                    bucket.value = value
                    return
                prev_bucket = bucket
                bucket = bucket.next

            prev_bucket.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        self.size = self.size - 1

        target_index = self._hash_mod(key)

        prev_node = None
        node = self.storage[target_index]

        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.storage[target_index] = prev_node
                else:
                    prev_node.next = node.next
                
                return
            else:
                prev_node = node
                node = node.next
            

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        target_index = self._hash_mod(key)

        bucket = self.storage[target_index]

        while bucket is not None:
            if bucket.key == key:
                return bucket.value
            else:
                bucket = bucket.next

        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        if self.size < self.capacity:
            # We do not need to resize, just return
            return

        self.size = 0
        self.capacity *= 2
        old_storage = self.storage

        self.storage = [None] * self.capacity

        for item in [_ for _ in old_storage if old_storage is not None]:
            next_node = item
            while next_node is not None:
                self.insert(next_node.key, next_node.value, True)
                next_node = next_node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    print(ht.storage)
    ht.insert("line_2", "Filled beyond capacity")
    print(ht.storage)
    old_capacity = len(ht.storage)
    ht.insert("line_3", "Linked list saves the day!")
    print(ht.storage)

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

# ======================================================================================================================