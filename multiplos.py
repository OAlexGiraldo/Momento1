print("EJERCICIO 1")

cant=int(input("Cuantos Numeros va a digitar: "))

if cant <= 0:
        print("¡Imposible!")
else:
        contador2_3 = 0
        contador3=0
        contador2=0
        for i in range(1, cant + 1):
            numero = float(input(f"Escriba el número {i}: "))
            if numero%2==0 and numero%3==0:
                contador2_3 = contador2_3 + 1
                contador3 = contador3 +1 
                contador2 = contador2 +1
        if contador2_3 != 0:
            contador2_3 = contador2_3 + 1
        elif numero%3==0 :
                contador3 = contador3 + 1
        elif numero%2==0:
            contador2 = contador2 +1
        else:
            print("No se digitaron multiplos de 2 y 3")
            
print(f"hay {contador2_3} multiplo de 2 y 3")
print(f"hay {contador3} multiplo de 3")
print(f"hay {contador2} multiplo de 2 ")
            