def multiplicacion(multiplicando, multiplicador):
    producto = multiplicando * multiplicador
    return producto


if __name__ == "__main__":
    multiplicando = float(input("Ingrese el multiplicando: "))
    multiplicador = float(input("Ingrese el multiplicador: "))
    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{multiplicando} * {multiplicador} = {resultado}")
12
