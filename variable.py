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


#DICTIONARY
print("DICTIONARY")
animal={"dog": "nice", "cat": "pretty", "snake": "dangerous"}
print(animal ["snake"])

animal["snake"]="lovely"
print(animal)

print("turtle" in animal)


del animal["cat"]
print(animal)

animal["dog"]="ugly"
animal["mouse"]="ugly"
animal["donkey"]="big"

for iten in animal:
    feature=animal[iten]
    print("%iten has %feature"(iten, feature))





print("OK")

