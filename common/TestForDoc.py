def auth(fun):
    def inner(*args,**kwargs):
        fun(*args,**kwargs)
        print("before")
        fun(*args,**kwargs)
    return inner



@auth
def f1(args):
    print("done")
    print(args)