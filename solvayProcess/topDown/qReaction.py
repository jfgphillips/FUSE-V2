from SolvayIO import *

if __name__ == '__main__':
    my_calciner = calciner.calciner_att()
    emissions = calciner.qMachine(my_calciner)
    print(emissions)



