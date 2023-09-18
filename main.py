#task1
print(4, 8, 15, 16, 23, 42, sep=' ')

#task2
print(4, 8, 15, 16, 23, 42, sep='\n')

#task3
a = int(input())
for i in range(1, 3):
    print(a+i)

#task4
sum = 0
for i in range(int(input())):
    n = int(input())
    sum += n
print(sum)

#task5
e_l = float(input("Enter the edge length of the cube: "))

volume = e_l ** 3
surface_area = 6 * (e_l ** 2)

print(f"Volume of the cube: {volume}")
print(f"Surface area of the cube: {surface_area}")

#2
#task 1
n,k = int(input()), int(input())
print(k // n)
print(k % n)

#task 2
a = int(input())
r = []
while a:
    r.append(a % 10)
    a //= 10
print(*reversed(r))

#task3
n = int(input())
print(round(n/2))

#task 5
firs_num = int(input('Please enter the first number: '))
second_num = int(input('Please enter the second number:'))
ops = input('Please choose the operation (+, -, *, /):')

if ops == '+':
    print(firs_num + second_num)
elif ops == '-':
    print(firs_num - second_num)
elif ops == '*':
    print(firs_num * second_num)
elif ops == '/':
    print(firs_num / second_num)
else:
    print("ты не то выбрал")

#task 4
a=int(input())
result = a << 1
if(result) == 0:
    print('WARNING')
else:
    print('The result of << is', a)
