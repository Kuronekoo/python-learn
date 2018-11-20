#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('test','print');
print('hello python');
name = input('please enter your name: ');
print('hello',name);
a = 100;
if a >= 0:
	print(a);
else:
	print(-a);

print('i\'m leaning \n python');
print(r'\\\t\\');
print('''line1
line2
line3''');

print(r'''hello,\n
world''')
print('''python''');
bol=3>2;
print(bol);
a = 'ABC'
b = a
a = 'XYZ'
print('b = ',b)
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n);
print(f);
print(s1);
print(s2);
print(s3);
print(s4);
nonce=None;
print(nonce);
print(ord('中'));
print(chr(25991));
print('\u4e2d\u6587');
print(b'ABC');
print('hello,%s your account is %.3f' %(name,3.33));
print('Hi, %s, you have $%d.' % ('Michael', 1000000));
print('%2d-%02d' % (3, 1));
print('growth rate: %d %%' % 7);
s1 = 72
s2 = 85
r=(s2/s1-1)*100
print('%s,去年成绩是%d,今年成绩是%d,提升了%.2f%%' % ('小明',s1,s2,r));