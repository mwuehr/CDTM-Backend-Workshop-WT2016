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


def main():
    count(6)
    countup(6)

def Maxi(object):
    

if __name__ == '__main__':
    main()