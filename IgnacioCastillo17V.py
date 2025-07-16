

#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}


print("***** Menu principal *****")

print("1. Stock marca \n2. Busqueda por precio \n3. Actualizar precio \n4. Salir")


while True:
    opcion_menu = int(input("Ingrese una opcion: "))
    
    if opcion_menu == 1:
        print("OPCION 1 STOCK MARCA")
        marca_input = input("Ingrese una marca a consultar: ")
        match = []
        for a,b in productos.items():

         for elemento in b:
            if elemento == marca_input:
                print(f"lo encontre {a}")
                match.append(a)
            
            

        for codigo , modelo_stock in stock.items():
            for elemento_match in match:
                if elemento_match == codigo:
            
                    print(f"modelo stock {modelo_stock}")
        
    elif opcion_menu == 2:
        print("OPCION 3 BUSQUEDA POR PRECIO" )
    
    elif opcion_menu == 3:
        print("OPCION 3 ACTUALIZAR PRECIO")
    
    
    elif opcion_menu == 4:
        print("OPCION 4 SALIR")
        break
    

    #if marca  
















