import random

def helloreturn():
    return "Hello World, Fabi sucks!"

def hello():
    print helloreturn()

def count(number):
    while (number > 0):
        print str(number) + ": " + helloreturn()
        number -= 1
    hello()

def countup(number):
    for i in range(0,number+1):
        print helloreturn() + ": %i" %(i)


def listeohne50():
    l = [i for i in range(1,101,1) if i != 50]
    return l

def randomlist():
    l = [(int(random.random()*10)+1) for i in range(1,101)]
    return l

def sort(l):
    n = l.length()
    for i in range(1,n):
        for j in range(1, n-1):
            


class Maxi:
    looks = "amazemalls"
    intelligence ="smort"
    def __init__(self, lastname, age, studies):
        self.lastname = lastname
        self.age = age
        self.studies = studies


    def beolder(self):
        self.age += 1

class Fabi(Maxi):
    def __init__(self, lastname, age, studies):
        Maxi.__init__(self)

def main():
        count(6)
        countup(6)
        print listeohne50()
        CoolerTyp = Maxi("Wuehr", 21, "VWL")
        print CoolerTyp.age
        CoolerTyp.beolder()
        print CoolerTyp.age
        print randomlist()



if __name__ == '__main__':
    main()