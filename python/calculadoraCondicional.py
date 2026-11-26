print("===========================")
print("     MI CALCULADORA        ")
print("===========================")
while True:
    print("")
    print("¿QUÉ OPERACIÓN QUIERES REALIZAR?")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")
    print("-------------------------------")
    opción = input("elige una opcion:")
    if opción == "1":
        num1 = input("ingresa el primer numero:")
        num1 = int(num1)
        num2 = input("ingresa el segundo numero:")
        num2 = int(num2)
    print("el resultado de la suma es",num1 + num2)



