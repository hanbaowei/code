import Array

def reversingArray(start, end, myArray):
    while start < end:
        myArray[start], myArray[end - 1] = myArray[end - 1], myArray[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    myArray = Array.Array(10)
    myArray.insert(2, 2)
    myArray.insert(1, 3)
    myArray.insert(3, 1)
    print('Array before reversing:', myArray.__str__())
    reversingArray(0, len(myArray), myArray)
    print('Array after reversing:', myArray.__str__())
