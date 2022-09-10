print("***MENU***")
print("1. Agregar 1 producto")
print("2. Mostrar productos")
print("3. Editar precio")
print("4. eliminar producto")

opcion=100
#DATOS producto
#codigo
#caracrteristicas (x3)
#Precio Fabircación
#Precio venta


productos=[]

while(opcion!=0):
    producto={}
    opcion =int(input("Digite una opcion: "))
    if(opcion==1):
        producto['codigo']=input("digite su codigo: ")
        producto['caracteristicas']=[]
        for i in range(2):
            
            producto['caracteristicas'].append(input("Digita las caracteristicas: "))
        
        productos.append(producto)
        print("agregando productos")
    elif(opcion==2):
        
        print(productos)
        print("Mostrando productos")
    elif(opcion==3):
        print
    else:
        print("digite una opcion valida")
else:
    print("fin")
