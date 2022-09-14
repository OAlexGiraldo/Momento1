numero=int(input("Digame cuantas frutas tiene la lista: "))
fruta={}
if numero<1:
    print("Imposible")
else:
    lista=[]
    for i in range(numero):
        fruta=input(f"Digame la fruta  {i+1}: ")
        lista.append(fruta)
        print("agregando frutas")
    print(f"La lista creada es: {lista}")

    inversa = []
    for i in lista:
        inversa =[i] + inversa
    print(f"La lista en orden inverso es: {inversa}")





