from pystyle import *

print(Box.Lines('this program for calculator',Colors.purple_to_blue ))

while True:
    number1= int(Write.Input('inter the first number:',Colors.green,interval=0.1))
    opretor = Write.Input('Inter the opreator:',Colors.white, interval=0.1)
    number2 = int(Write.Input('inter the secand number:', Colors.green, interval=0.1))

    if opretor == '+':
        Write.Print(' the result is :',Colors.green,interval=0.1)
        print(number1 + number2)
        break

    elif opretor == '-':
         Write.Print(' the result is :',Colors.green,interval=0.1)
         print(number1 - number2)
         break

    elif opretor == '*':
         Write.Print(' the result is :',Colors.green,interval=0.1)
         print(number1 * number2)
         break

    elif opretor == '/':
         Write.Print(' the result is :',Colors.green,interval=0.1)
         print(number1 / number2)
         break


    else:
         print('invalid opreator please inter one of these only + , - ,* , /')     
     
     




