def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

# Función principal
if __name__ == "__main__":
    # Solicitar entrada del usuario para el rectángulo
    base_rectangulo = float(input("Introduce la base del rectángulo: "))
    altura_rectangulo = float(input("Introduce la altura del rectángulo: "))
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    print("El area del rectángulo es10:", area_rectangulo)

    # Solicitar entrada del usuario para el triángulo
    base_triangulo = float(input("Introduce la base del triángulo: "))
    altura_triangulo = float(input("Introduce la altura del triángulo: "))
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("El area del triángulo es:", area_triangulo)
