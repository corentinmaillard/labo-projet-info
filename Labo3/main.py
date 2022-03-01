import time
#ex 1.1
def call(g, *args , **kwargs):
    #f()
    #return g(*args)
    return g(*args, **kwargs)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def compute(a, b, op=add):
    return op(a, b)

def hello():
    print('hello')



print(call(compute , 2, 9))
print(call(compute , 2, 9, op=sub))

#ex 2
def sleep(t):
    def decorator(f):
        def wrapper(*args):
            #time.sleep(t)
            return f(*args)
        return wrapper
    return decorator
    

@sleep(1)
def printnum(i):
    print(i)

cnt = 3
while cnt > 0:
    printnum(cnt)
    cnt -= 1
print('KA-BOOM')

#ex 3

def binrep(number):
    bitlist = []
    numbit = testbit(number)
    bitlist.add(numbit)
    return bitlist

def testbit(number):
    numbit = 0
    while number > 1:
        number /= 2
        numbit +=1
    return numbit-1

b = binrep(12)
while True:
    try:
        print(next(b))
    except StopIteration:
        break