#Pedir tres números y mostrarlos ordenados de mayor a menor.

print('Digite 3 números')
x = int(input())
y = int(input())
z = int(input())

if x > y and x > z and y > z:
    print(str(x) + ' > ' + str(y) + ' > ' + str(z))
elif x > y and x > z and z > y:
    print(str(x) + ' > ' + str(z) + ' > ' + str(y))
elif y > x and y > z and x > z:
    print(str(y) + ' > ' + str(x) + ' > ' + str(z))
elif y > x and y > z and z > x:
    print(str(y) + ' > ' + str(z) + ' > ' + str(x))
elif z > x and z > y and y > x:
    print(str(z) + ' > ' + str(y) + ' > ' + str(x))
elif z > x and z > y and x > y:
    print(str(z) + ' > ' + str(x) + ' > ' + str(y))
elif x == y and x == z:
    print('Los 3 números son iguales')

#OPCION 2

if x > y and x > z:
    if y > z:
        print(str(x) + ' > ' + str(y) + ' > ' + str(z))
    else:
        print(str(x) + ' > ' + str(z) + ' > ' + str(y))
if y > x and y > z:
    if x > z:
        print(str(y) + ' > ' + str(x) + ' > ' + str(z))
    else:
        print(str(y) + ' > ' + str(z) + ' > ' + str(x))
if z > x and z > y:
    if x > y:
        print(str(z) + ' > ' + str(x) + ' > ' + str(y))
    else:
        print(str(z) + ' > ' + str(y) + ' > ' + str(x))
if x == y and x == z:
    print('Los 3 números son iguales')

#OPCION 3

num1 = int(input('Ingrese un número \n')) #\n es salto de linea
num2 = int(input('Ingrese un número \n'))
num3 = int(input('Ingrese un número \n'))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 > num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
