class Bird(object):
    def __init__(self):
        self.hugury = True

    def eat(self):
        if self.hugury:
            print "KuangchiKuangchi"
            self.hungry = False
        else:
            print "No I'm full"


class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = "Quak"

    def sing(self):
        print self.sound


if __name__ == '__main__':
    b = Bird()
    print b.hugury
    b.eat()
    print b.hugury
    b.eat()
    sb = SongBird()
    sb.sing()
    sb.eat()
