
def a(a_):
    print("A")
    def b(b_):
        print("B")
        def c(c_):
            print("C")
            return a_, b_, c_
        return c
    return b


result = a(10)
print(result)                         
def a(a_):
    print("A")
    def b(b_):
        print("B")
        def c(c_):
            print("C")
            return a_, b_, c_
        return c
    return b


result = a(10)
print(result)