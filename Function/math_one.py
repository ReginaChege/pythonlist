def add(a,b):
    addition =a+b
    return addition

def subtract(c,d):
    subtract=c-d
    return 

def division(e,f):
    division=e/f
    return  division

def multiplication(g,h):
    multiplication=g*h
    return  multiplication

def remainder(i,j):
    remainder=i%j
    return remainder

def concatenate_arg(*names):
    answer=""
    for name in names:
        answer+=name
    return answer

def concatenate_kwargs(**kwargs):
    answer=""
    for name in kwargs.values():
        answer+=name
    return answer



