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
    while x <=


class Maxi:
    def f(self):
        return "Maxi ist cool."
    looks = "amazemalls"
    intelligence ="smort"
    def __init__(self, lastname, age, studies):
        self.lastname = lastname
        self.age = age
        self.studies = studies

    def getolder(self):
        self.age += 1





    def main():
        count(6)
        countup(6)



if __name__ == '__main__':
    main()