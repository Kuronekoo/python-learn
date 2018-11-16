#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a='hello , %s';
b='world';
print(a % b);
print('3/2 is ' , 3/2);
print(3//2);
classmates = ['Michael', 'Bob', 'Tracy'];
print('classmates is ' ,classmates);
print(len(classmates));
print(classmates[0]);
print('classmates[-1] is ',classmates[-1]);
classmates.append(1);
print('classmates is ' ,classmates);
classmates.pop();
print('classmates is ' ,classmates);
classmates.sort();
print('sorted classmates is ' ,classmates);
age = 10
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
	
#s = input('birth: ')
#birth = int(s)
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')

for name in classmates:
	print(name)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello,',name,'!')
	
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

print(1==1)
print('a'=='a')
d = {'Michael': 95, 'Bob': 75, 'Tracy': '85',12:11}
d.get('Thomas')
print(d.get('dd'))
print(d.get(12))
key='a';
d[key]='b'
print(d)
key='c'
print(d)
print(hex(27))

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-1));