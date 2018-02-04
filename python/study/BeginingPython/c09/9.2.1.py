class A:
    def hello(self):
        print "hello, I'm A"
class B(A):
    pass

if __name__ == '__main__':
    a = A()
    a.hello()
    b = B()
    b.hello()
