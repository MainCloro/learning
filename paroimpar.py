repeat = True
while repeat == True: 

    num = int(input("Dime un numero del 1 al 1000 \n"))

    while num<1 or num>1000:
        print("Ese numero no sirve.\nDame otro por favor")
        num = int(input("Dime un otro numero, que este entre el 1 y el 1000, vale el 1 y el 1000\n"))

    resultado = num % 2

    if resultado == 0:
        print("El número " + str(num) + " es par")
    else:
        print("El número " + str(num) + " es impar")
    
    respuesta = str(input("Quieres volver a jugar? Si/No\n"))

    if respuesta == "Si" or respuesta == "si" or respuesta == "SI" or respuesta == "sI":
        repeat = True
    else:
        repeat = False