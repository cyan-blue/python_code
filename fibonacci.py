# coding: utf-8
def fib(max):
   """复用性差"""
   n, a, b =0, 0, 1
   while n < max:
       print b
       a, b =b, a +b
       n =n +1

def fib2(max):
   n, a, b =0, 0, 1
   L =[]
   while n < max:
       L.append(b)
       a, b =b, a +b
       n =n +1
   print L
   return L

class Fib(object):
    
   def __init__(self, max):
       self.max=max
       self.n, self.a, self.b =0, 0, 1
    
   def __iter__(self):
       return self
    
   def next(self):
       if self.n < self.max:
           r =self.b
           self.a, self.b =self.b, self.a +self.b
           self.n =self.n +1
           return r
       raiseStopIteration()

def fib4(max):
    n, a, b =0, 0, 1
    while n < max:
        yield b
        # print b
        a, b =b, a +b
        n =n +1
for a in fib4(5):
    print a
