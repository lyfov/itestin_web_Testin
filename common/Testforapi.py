import pysnooper

class Test():
    @pysnooper.snoop()
    def add(a=7,b=7):
        a=7
        a=a+7
        b=a
        b=a+b
        print(a,b)

if __name__=="__main__":
    Test.add()