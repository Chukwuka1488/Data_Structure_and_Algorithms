class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Hashmap:
    def __init__(self):
        self.storage = [None for _ in range(16)]
        self.size = 0

    def hashStr(self, key):
        if isinstance(key, int):
            return key

        result = 5381
        for char in key:
            result = 33 * result + ord(char)
        return result

    def position(self, key_hash):
        return key_hash % 16

    def set(self, key, val):
        p = Node(key, val)
        key_hash = self.hashStr(key)
        index = self.position(key_hash)

        if not self.storage[index]:
            self.storage[index] = [p]
            self.size += 1
        else:
            list_at_index = self.storage[index]
            if p not in list_at_index:
                self.storage[index] = [p]
                self.size += 1
            else:
                for i in self.storage[index]:
                    if i == p:
                        i.value = val
                        break

    def get(self, key):
        key_hash = self.hashStr(key)
        index = self.position(key_hash)

        if not self.storage[index]:
            return None
        else:
            list_at_index = self.storage[index]
            for i in self.storage[index]:
                if i.key == key:
                    return i.value
        return None


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        dict = Hashmap()
        dict.set("jess", "213-559-6840")
        dict.set("james", "123-456-7890")
        assert dict.get("james") == "123-456-7890"
        print("PASSED: Instantiate a `Hashmap`, and set keys.")

    def test_2(self):
        dict = Hashmap()
        dict.set("jess", "213-559-6840")
        dict.set("james", "123-456-7890")
        assert dict.get("jake") == None
        print("PASSED: `Hashmap` will return `None` if nothing found")

    def test_3(self):
        dict = Hashmap()
        assert callable(dict.set) == True
        print("PASSED: Hashmap class has a `set` method")

    def test_4(self):
        dict = Hashmap()
        dict.set("jess", "213-559-6840")
        assert callable(dict.get) == True
        assert dict.get("jess") == "213-559-6840"
        print("PASSED: Hashmap class has a `get` method")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
