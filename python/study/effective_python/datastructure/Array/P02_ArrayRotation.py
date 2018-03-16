import Array

def rotation(rotateBy, myArray):
    for i in range(0, rotateBy):
        rotateOne(myArray)
    return myArray

def rotateOne(myArray):
    for i in range(len(myArray) - 1):
        myArray[i], myArray[i + 1] = myArray[i + 1], myArray[i]

if __name__ == '__main__':
    myArray = Array.Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    print('Before Rotation:', myArray.__str__())
    print('After Rotation:', rotation(3, myArray).__str__())