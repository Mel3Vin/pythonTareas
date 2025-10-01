print("Ejercicios Basicos")

# #Ingresar un numero y detectar si es par o impar 
# number=int(input("INGRESE UN NUMERO: \n"))

# if number % 2==0:
#     print("EL NUMERO ", number ,"ES PAR ")
# else:
#     print("EL NUMERO ", number , "ES IMPAR")

#Sistema de login
# user= "Melvin"
# password= "123"

# user = input("Ingrese su user de login. \n")
# password = input("Ingrese su contraseña de login. \n")

# if user==userDefault and password==passwordDefault:
#     print("Puedes entar al sistema")
# else:
#     print("No puedes entrar al sistema")


# repository=list()
# ramdonNumber=int(input("Ingrese un numero: \n"))

# for i in range(ramdonNumber):
#     repository.append(i)

# for i in repository:
#     sum=sum + i

# print("el total de la suma es", sum)

#Banco 3 Obciones

# ...existing code...

# saldo = 1000

# choice = input("1 > deposito \n2 > retiro \n3 > Saldo \n")
# choice = int(choice)
# money = 0

# while True:
#     if choice == 1:
#         money = int(input("Ingrese la cantidad de deposito:  \n"))
#         saldo = money + saldo
#         print("Tu saldo ha sido depositado")
#     elif choice == 2:
#         money = int(input("Ingrese el dinero a retirar: \n"))
#         if saldo >= money:  
#             print("Retiro realizado")
#         else:
#             print("Tienes poco dinero")
#         saldo = money - saldo
#     elif choice == 3:
#         print("Tu saldo es ", saldo)
#     else:
#         print("Opcion invalida, no se que quieres hacer.......!!!!!!")
#     choice = input("1 > deposito \n2 > retiro \n3 > Saldo \n")
#     choice = int(choice)



#Clases
# class Students:
#     def __init__(self, name, course="Python"):
#         print("The student been registered")
#         self.name=name
#         self.course=course
#     def dataStudent(self):
#         print("Name: ", self.name)
#         print("Course: ", self.course)
#         return


# students1=Students("Melvin")
# students2=Students("Emilio", "Distributed sytems")

# students1.dataStudent()
# students2.dataStudent()



#Clases 2 
class Students:
    def __init__(self, name, course="Python"):
        print("The student been registered")
        self.name=name
        self.course=course
    def dataStudent(self, status="No active"):
        print("Name: ", self.name)
        print("Course: ", self.course)
        print("Status: ", status)
        return 


students1=Students("Melvin")
students2=Students("Emilio", "Distributed sytems")

students1.dataStudent()
students2.dataStudent()
        




