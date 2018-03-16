class Array(object):
    """sizeOfArray: total size
        arrayType: data type of the array
        arrayItems: value at each position
        """
    def __init__(self, sizeOfArray, arrayType = int):
        self.sizeofArray = len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems = [arrayType(0)] * sizeOfArray
        self.arrayType = arrayType

    def __str__(self):
        return ' '.join([str(i) for i in self.arrayItems])

    def __len__(self):
        return len(self.arrayItems)

    def __setitem__(self, key, value):
        self.arrayItems[key] = value

    def __getitem__(self, item):
        return self.arrayItems[item]

    def search(self, keyToSearch):
        for i in range(self.sizeofArray):
            if self.arrayItems[i] == keyToSearch:
                return i
        return -1

    def insert(self, keyToInsert, position):
        if self.sizeofArray > position:
            for i in range(self.sizeofArray - 2, position - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]
            self.arrayItems[position] = keyToInsert
        else:
            print('Array size is:' + self.sizeofArray)

    def delete(self, keyToDelete, position):
        if self.sizeofArray > position:
            for i in range(position, self.sizeofArray - 1):
                self.arrayItems[i] = self.arrayItems[i + 1]
            self.arrayItems[i + 1] = self.arrayType(0)
        else:
            print('Array size is:', self.sizeofArray)

if __name__ == '__main__':
    a = Array(10, int)
    a.insert(2, 2)
    a.insert(3, 1)
    a.insert(4, 7)
    print(len(a))
    print(a)
