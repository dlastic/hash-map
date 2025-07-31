class HashMap:
    def __init__(self, capacity=16, load_factor=0.75) -> None:
        self.load_factor = load_factor
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def hash(self, key):
        hash_code = 0
        prime = 31
        for char in key:
            hash_code = (prime * hash_code + ord(char)) % self.capacity
        return hash_code

    def resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for bucket in old_table:
            if bucket:
                for k, v in bucket:
                    self.set(k, v)

    def set(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = []

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])
        self.size += 1

        if self.size / self.capacity > self.load_factor:
            self.resize()

    def get(self, key):
        index = self.hash(key)
        bucket = self.table[index]
        if bucket:
            for k, v in bucket:
                if k == key:
                    return v
        return None

    def has(self, key):
        index = self.hash(key)
        bucket = self.table[index]
        if bucket:
            for k, _ in bucket:
                if k == key:
                    return True
        return False

    def remove(self, key):
        index = self.hash(key)
        bucket = self.table[index]
        if bucket:
            for i, (k, _) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    self.size -= 1
                    return True
        return False

    def clear(self):
        self.table = [None] * self.capacity
        self.size = 0

    def keys(self):
        result = []
        for bucket in self.table:
            if bucket:
                for k, _ in bucket:
                    result.append(k)
        return result

    def values(self):
        result = []
        for bucket in self.table:
            if bucket:
                for _, v in bucket:
                    result.append(v)
        return result

    def entries(self):
        result = []
        for bucket in self.table:
            if bucket:
                for pair in bucket:
                    result.append(pair)
        return result
