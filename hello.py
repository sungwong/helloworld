
#_coding: utf-8
from __future__ import print_function

'''age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('why is {0} playing with that python?'.format(name))

print('{0:.5f}'.format(1.0/3))
# 对于浮点数0.33333，保留小数点后5位

print('{0:_^11}'.format('hello'))

print('{name} wrote {book}'.format(name = 'sungwong', book = '我是一颗无人知道的小草' ))

print('a', end=' ')
print('b', end=' ')
print('c')

print("what are you fucking doing?\
      are you kidding what\'s up?")
      '''

'''i = 5
print(i)
i = i + 1
print(i)
'''
'''s = this is a multi-line string. \
this is the second line.
print(s)'''

'''length = 5
breadth = 2

area = length * breadth
print('Area is', area)
print('B is', 2 * (length + breadth))'''


# if_elif_else
'''number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # 新块从这里开始

    print('Congratulation, you guessed it!')
    print('(But you don\'t any prizes!)')
    #新块在这里结束

elif guess < number:
    print('No,it is a little higher than that')

else:
    print('No,it is a little lower than that')

print('Done')'''

#while函数
'''number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('恭喜你，回答正确！')
        # 这里会让while循环中止
        running = False
    elif guess < number:
        print('数字太小')
    else:
        print('数字太大')

else:
    print('循环结束')


print('Done')'''

# for_in的使用
'''for i in range(1, 6, 2):
    print(i)
else:
    print('over')'''

'''while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')'''

# while的使用
''' while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')'''

'''def say_hello():
    #这里是一个函数
    print('heloo world')
#函数结束

say_hello()
say_hello()'''

# 函数定义
'''def print_max(a, b):
    if a > b:
        print(a, '更大')
    elif a == b:
        print(a, '等于', b)
    else:
        print(b, '更小')

print_max(4, 12)

x = 5
y = 7

print_max(x, y)'''

# global定义全局变量
'''x = 10


def func():
    global x

    print('x is', x)
    x = 5
    print('Change x to', x)


func()
print('Value of X is', x)'''

# 默认参数值
'''def say(message, times=1):
    print(message * times)


say('hello')
say('world', 4)'''

# 关键字参数
'''def func(a, b=10, c=21):
    print('a is', a, 'and b is', b, ',', 'c is', c)

func(2, 3)
func(34, c=2)
func(c=21, a= 213)'''

# return

'''def maximum(x, y):
    if x > y:
        return X
    elif x == y:
        return 'equal'
    else:
        return y

print(maximum(52,123))'''

def print_max(x, y):
    '''Prints the maximum of two numbers.打印两个数值中的最大数。

    The two values must be integers.这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
        
print_max(3, 5)
print(print_max.__doc__)
