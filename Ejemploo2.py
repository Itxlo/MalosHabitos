def calcular(x, y, z):
    resultado = x * y + z
    return resultado

if __name__ == "__main__":
    valor1 =  float(input("Ingrese el valor 1: "))
    valor2 =  float(input("Ingrese el valor 2: "))
    valor3 =  float(input("Ingrese el valor 3: "))
    resultado = calcular(valor1, valor2, valor3)
    print(f"{valor1} * {valor2} - {valor3} = {resultado}")

