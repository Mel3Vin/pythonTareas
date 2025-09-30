#Variable entera
#a=10 
#Variable boolaneo
#b=3.5
#Cadena de caracteres 
#name="melvin"
#Variable logica 
#is_active= True


#print(a,b, name , is_active)

#print(type(a))
#print(type(name))
#print(type(is_active))


#device = "Router"
#id = 101

#print(f ´device : {device} and id : {id}´)

#Operaciones basicas 
Ab = 1
AA = 2

#Suma
resul=Ab+AA
print("El resultado de la suma es : " , Ab+ AA)
print("El resultado de la resta es : ", Ab-AA)
print("El resultado de la multiplicacion es : ", Ab*AA)
print("El resultado de la potencia es : ", Ab**AA)
print("El resultado de la divicion es : ", Ab/AA)
print("El resultado del modulo es : ", Ab//AA)

#STRING
print("#STRINGS")
name= "melvinzambrano"
print(name.upper())
print(name.capitalize())
name2=name.upper()
print(name2.lower())


language = "PYTHON"
print(language[0])
print(language[-1])
print(language[-2])
print(len(language))


#listas
print("#Lista")
device=["router", "switch", "cable", 45, True, False]
print(len(device))

print(device[0])
print(device[-1])

device.append("server")
print(device)

names=list()
names.append("melvin")
names.append("sexto")
names.append("carlo")
names.append("julio")
names.append("emilio")
print(names)
names[1]="Sebastian"
print(names)


print(names.pop())
print(names)

numbres=list(range(10))
print(numbres)
selectednumbres=numbres[2:4]
print(selectednumbres)

print(numbres[:-1])
print(numbres[:3])

numbres [2:3]=[100,100]
print(numbres)

#TUPLES
#containertuple = containertuple + (30, 40, 50 )

print("TUPLES")

containertuple=(10,20)
print(containertuple[0])
containerlist=list(containertuple)
print(type(containerlist))
containerlist.append(30)
print(containerlist)


# #DICTIONARY
# print("DICTIONARY")
# animal={"dog": "nice", "cat": "pretty", "snake": "dangerous", "turtle": "slow"}
# print(animal ["snake"])

# animal["snake"]="lovely"
# print(animal)

# print("turtle" in animal)


# del animal["cat"]
# print(animal)

# animal["dog"]="ugly"
# animal["mouse"]="ugly"
# animal["donkey"]="big"

# for iten in animal:
#     feature=animal[iten]
#     print("%iten has %feature"(iten, feature))



mydictionary=dict()
mydictionary["humans"]=2
mydictionary["mouse"]=4
mydictionary["spider"]=8

for iten in mydictionary:
    feature=mydictionary[iten]
    print("the %s has %d" % (iten, feature))


#LOOPS
# print("LOOPS")
# counter=0
# while counter<10:
#     print(counter)
#     counter+=1
    
# name=input("Enter your name: \n")
# print("Hello , " + name)


# #Creacionpn de numeros pares en for
# for i in range(0,100,2):
#     print(i)

myList=list()
for i in range(100):
    if i%2==0:
        myList.append(i)
print(myList)


#Lista en una sola linea
print("LISTAS EN UNA SOLA LINEA")

myList=[i for i in range(10) if i%3==0]
print(myList)


#Numero del 1 al 100 elevados al cuadrado
myList=[i*i for i in range(100)]
print(myList)



# #Funciones en python
# def greetings():
#     return f"hello my friend....."


# tmp=greetings()
# print(tmp)

# def greetings2(name):
#     greetings2=f"hello {name} my friend....."
#     return
# name=input("Enter your name: \n")


# tmp=greetings2(name)
# print(tmp)


# #list de numeros 
# listnum=[10,11,12,13,14,15,14,16,17,18,19,20]
# def numeroAlto(listnum):
#     alto=listnum[0]
#     for i in listnum:
#         if i>alto:
#             alto=i
#     return alto
# def numeroBajo(listnum):
#     bajo=listnum[0]
#     for i in listnum:
#         if i<bajo:
#             bajo=i
#     return bajo
# tmp=numeroAlto(listnum)
# tmp2=numeroBajo(listnum)
# print("El numero mayor es ")
# print(tmp)  
# print("El numero menor es ")
# print(tmp2)


def greetings2(name="melvin"):
    print(f"hello , {name}")
    return
greetings2()


#Calculadora basica
while True:
    print("Seleccione la operacion")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Divicion")
    print("5.Salir")

    choice=input("Ingrese su opcion (1/2/3/4/5): \n")

    if choice in ('1','2','3','4'):
        num1=float(input("Ingrese el primer numero: \n"))
        num2=float(input("Ingrese el segundo numero: \n"))

        if choice=='1':
            print(num1, "+", num2, "=", num1+num2)

        elif choice=='2':
            print(num1, "-", num2, "=", num1-num2)

        elif choice=='3':
            print(num1, "*", num2, "=", num1*num2)

        elif choice=='4':
            if num2==0:
                print("Error: Division por cero no es permitida.")
            else:
                print(num1, "/", num2, "=", num1/num2)
    
    elif choice=='5':
        print("Saliendo de la calculadora. Adios!")
        break
    else:
        print("Opcion invalida. Por favor ingrese una opcion valida.")  
            







print("OK  TODO ESTA FUNCIONADNO CORRECTAMENTE")

