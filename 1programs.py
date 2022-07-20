
Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello World")
Hello World
a = 10  
# Two objects are passed in print() function  
print("a =", a)
SyntaxError: multiple statements found while compiling a single statement
print('a=', a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print('a=', a)
NameError: name 'a' is not defined
print("a = ",a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("a = ",a)
NameError: name 'a' is not defined
print("a = ", a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("a = ", a)
NameError: name 'a' is not defined
a = 10
print("a=", a)
a= 10
a = 0o7
print(a)
7
val = 0xa0c
print(val)
2572
oct(8)
'0o10'
hex(A)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    hex(A)
NameError: name 'A' is not defined. Did you mean: 'a'?
hex(0xa0c)
'0xa0c'
bin(12)
'0b1100'
hex(0xaoc)
SyntaxError: invalid hexadecimal literal
hex(15)
'0xf'
s = "Hello world"
s[0]
'H'
s[len(s)-1]
'd'
s[-1]
'd'
s[-10]
'e'
item='key\
board'
print(item)
keyboard
s = "raama\'s laptop"
print(s)
raama's laptop
s = "raama's laptop"
print(s)
raama's laptop
print("\"python programming\"")
"python programming"
print(""python programming"")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a = 4
b,c = 5,10
print('a=',a,'b=',b,'c=',c)
a= 4 b= 5 c= 10
cost=5678.923
print(cost)
5678.923
cost
5678.923
c=(int)input(Enter the value)
SyntaxError: invalid syntax
c=int(input("Enter the value"))
Enter the value65
c
65
y=float(input("Enter float value"))
Enter float value34.89
y=float(input("Enter float value\n"))
Enter float value
64.76
y
64.76
y=float(input("Enter float value\n"))
Enter float value to calc y
89.232
y
89.232
