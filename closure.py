#coding:utf-8
def line_conf():
    def line(x):
        return 2*x+1
    print(line(5))   # within the scope
                     
#line_conf()
#print(line(5))  NameError is not defined

def line_conf():
    b = 15
    def line(x):
        return 2*x+b
    return line       # return a function object
                     
b = 5
my_line = line_conf()
print dir(line_conf)
print line_conf().func_closure[0].cell_contents, len(line_conf().func_closure)
print(my_line(5))

print 'Example 3##################'


def line_conf(a, b):
    def line(x):
        return a*x + b
    return line
 
line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))

print 'Example 4 #################'

def plus_out(number):
    def plus_in(number_in):
        print str(number_in) + "\r\n"
        return number+number_in
    return plus_in
import pdb
pdb.set_trace()

