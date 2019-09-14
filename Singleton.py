#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      estudiantes
#
# Created:     22/08/2019
# Copyright:   (c) estudiantes 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Singleton(object):
    __valor1=0
    __valor2=0
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    def getValor1(self):
        return self.__valor1
    def setValor1(self, v1):
        self.__valor1 = v1
    def getValor2(self):
        return self.__valor2
    def setValor2(self, v2):
        self.__valor2 = v2
def main():
    A=Singleton()
    A.setValor1(4)
    B=Singleton()
    B.setValor1(3)
    print(A.getValor1() is B.getValor1())
    pass

if __name__ == '__main__':
    main()
