#ex 1.1
def call(g, a, b):
    #f()
    return g(a, b)

def hello():
    print('hello')

def add(a, b):
    return a + b

print(call(add, 2, 9))

#ex 1.2