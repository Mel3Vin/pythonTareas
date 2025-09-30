#Calculadora basica 
while True:
    operation=input("Escoja que operacion desea realizar")
    print("1 Suma \n ")
    print("1 resta \n ")
    print("1 multiplicacion \n ")
    print("1 divicion \n ")


    numbera=int (input("Ingrese el primer numero: \n"))
    numberb=int(input("Ingrese el segundo numero: \n"))

    operation=input("Escoja que operacion desea realizar \n")
    print("1 Suma \n ")
    print("1 resta \n ")
    print("1 multiplicacion \n ")
    print("1 divicion \n ")

    if operation=="2":
        print(f"La suma de {numbera} + {numberb} es igual a: {float(numbera)+float(numberb)}")
    elif operation=="2":
        print(f"la resta de {numbera}-{numberb} es igual a: {float(numbera)-float(numberb)}")
    elif operation=="3":
        print(f"la multiplicacion de {numbera}*{numberb} es igual a: {float(numbera)*float(numberb)}")
    elif operation=="4":
        print(f"la divicion de {numbera}/{numberb} es igual a: {float(numbera)/float(numberb)}")
    else:
        print("Operacion no valida")
        break

