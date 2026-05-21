while True:
    print("Selecciona un numero")
    print("1) Calcular comision")
    print("2) Ver mi sueldo")
    print("3) Salir")
    
    try:
        opcion = int(input())
        match opcion:
            #Comisiones
            case 1:
                nombre = input("Ingresa tu nombre: ")
                cant_ventas = int(input("Ingresa la cantidad de ventas que realizaste este mes: "))
                monto = int(input("Ingresa el monto total: "))
                #Calculo de comision
                if cant_ventas >= 1 and cant_ventas <= 10:
                    print("Comision del 5%")
                    sueldo = monto * 1.05
                    print(f"Tu sueldo es de {sueldo}")
                elif cant_ventas >= 11 and cant_ventas <= 20:
                    print("Comision del 8%")
                    sueldo = monto * 1.08
                    print(f"Tu sueldo es de {sueldo}")
                elif cant_ventas > 20:
                    print("Comision del 12% mas bono")
                    sueldo = monto * 1.12
                    print(f"Tu sueldo es de {sueldo} mas el bono")
            #Ver sueldo
            case 2:
                pass
            #Salir
            case 3:
                print("|----------|")
                print("Saliendo...")
                print("|----------|")
                break
            case _:
                print("|-----------------------|")
                print("Ingresa un numero valido")
                print("|-----------------------|")
    except ValueError:
        print("|-------------------------|")
        print("Ingresa un caracter valido")
        print("|-------------------------|")