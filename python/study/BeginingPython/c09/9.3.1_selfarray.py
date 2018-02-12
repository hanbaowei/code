def checkIndex(key):
    """
    check the index range
    :param key:
    :return:
    """
    if not isinstance(key, (int, long)): raise TypeError
    if key<0: raise IndexError

class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        Init the array
        :param start:
        :param step:
        """
        self.start=start
        self.step = step
        self.changed={}

    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence
        :param key:
        :return:
        """
        checkIndex(key)
        try: return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):
        """
        modify an item
        :param key:
        :param value:
        :return:
        """
        checkIndex(key)
        self.changed[key]=value

if __name__ == '__main__':
    s = ArithmeticSequence(1,2)
    print s[4
    ]