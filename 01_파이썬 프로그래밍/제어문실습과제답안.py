# 제어문 실습 과제 답안

# 1번
print('{0:=^50}'.format('1-1'))
for x in range(1, 101):
    print('{:4}'.format(x), end='')
    if x % 10 == 0:
        print()

print('{0:=^50}'.format('1-2'))
l = [x for x in range(1, 101)]
for x in l:
    print('{:4}'.format(x), end='')
    if x % 10 == 0:
        print()

# 2번
print('{0:=^50}'.format('2'))
max_number = int(input('Input max number : '))

total = 0
for x in range(1, max_number + 1):
    total = total + x

print('1 ~ {0:^6} = {1:<8}'.format(max_number, total))

# 3번
print('{0:=^50}'.format('3'))
max_number = int(input('Input max number : '))

even_list = []
odd_list = []
for x in range(1, max_number + 1):
    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)

print('even number : ', even_list)
print('1 ~ {0:^6} = {1:<8d}\n'.format(max_number, sum(even_list)))

print('odd number : ', odd_list)
print('1 ~ {0:^6} = {1:<8d}'.format(max_number, sum(odd_list)))

# 4번
print('{0:=^50}'.format('4'))
max_number = int(input('Input max number : '))

Excluding_Multiple_of_3_5 = []

for x in range(1, max_number + 1):
    if x % 3 != 0 and x % 5 != 0:
        Excluding_Multiple_of_3_5.append(x)

print('Excluding Multiple of 3 and 5 : ', Excluding_Multiple_of_3_5)
print('sum = {0:<6}'.format(sum(Excluding_Multiple_of_3_5)))

# 5번
print('{0:=^50}'.format('5-1'))
for x in range(2, 10):
    for y in range(1, 10):
        print('{:3} * {:3} = {:3}'.format(x,y,x * y))
    print('-'*30)

print('{0:=^50}'.format('5-2'))
multiple_table = [(x,y,x * y) for x in range(2, 10) for y in range(1, 10)]

count = 0
for x in range(8 * 9):
    count = count + 1
    print('{:3} * {:3} = {:3}'.format(multiple_table[x][0],multiple_table[x][1],multiple_table[x][2]))
          
    if count % 9 == 0:
        print('-'*30)
        count = 0


# 6번
print('{0:=^50}'.format('6'))
total_list = [0, 0, 0, 0]
total_title = ('positive', 'negative', 'even', 'odd')

while True:
    number = int(input('Input number : '))
    if number == -999:
        break

    if number != 0:
        if number > 0:
            total_list[0] = total_list[0] + 1
            if number % 2 == 0:
                total_list[2] = total_list[2] + 1
            else:
                total_list[3] = total_list[3] + 1
        else:
            total_list[1] = total_list[1] + 1
    else:
        print('error : input not {}'.format(number))

print()
for x in range(4):
    print('{0:<10} : {1:<5}'.format(total_title[x], total_list[x]))

# 7번
print('{0:=^50}'.format('7'))
op = {1: '+', 2: '-', 3: '*', 4: '/'}

while True:
    number1 = input('Input number1 : ')
    number2 = input('Input number2 : ')
    op_select = int(input('Input operator( 1:+, 2:-, 3:*, 4:/, 0:end ) : '))

    if op_select == 0:
        break;

    result = eval(number1 + op[op_select] + number2)

    print('number1 : {0:^6}'.format(number1))
    print('number2 : {0:^6}'.format(number2))
    print('{0:^6} {2:^3} {1:^6} = {3:<.2f}\n'.format(number1, number2, op[op_select], result))



