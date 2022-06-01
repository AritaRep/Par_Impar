# Introducir por consola un número
# Devolver si el número es par o impar

while True:
    try:
        num = abs(int(input("Introduce un número: ")))

        if(num%2 == 0):
            print(f"El número {num} es par")
            if input("¿Desea agregar otro número? si/no \n").lower() == "no":
                break
        elif(num%2 == 1):
            print(f"El número {num} es impar\n ¿Desea agregar otro número? si/no")
            if input("¿Desea agregar otro número? si/no \n").lower() == "no":
                break
    except Exception as e:
        print("Ocurrió en siguiente error", type(e).__name__)