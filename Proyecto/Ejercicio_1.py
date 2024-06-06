'Programa de entrada al Acuario Inbursa'

def calcular_descuento(usa_lentes, es_estudiante, usa_tenis, va_de_traje):
    descuento = 0

    if va_de_traje.lower() == 'si':
        return 1.0  # Entrada gratis

    if usa_lentes.lower() == 'si':
        descuento += 0.05
    if es_estudiante.lower() == 'si':
        descuento += 0.10
    if usa_tenis.lower() == 'si':
        descuento += 0.15

    return descuento


def main():
    print("Bienvenido al Acuario Inbursa")
    print("Por favor, selecciona tu tipo de entrada:")
    print("1. Adulto ($1000)")
    print("2. Niño ($500)")
    print("3. Adulto Mayor ($350)")

    while True:
        try:
            opcion = int(input("Inserte el número de la opción: "))
            if opcion == 1:
                costo_base = 1000
                break
            elif opcion == 2:
                costo_base = 500
                break
            elif opcion == 3:
                costo_base = 350
                break
            else:
                print("Opción no válida, por favor selecciona 1, 2 o 3.")
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")

    usa_lentes = input("¿Usa lentes? (si/no): ")
    es_estudiante = input("¿Tiene credencial de estudiante? (si/no): ")
    usa_tenis = input("¿Usa tenis? (si/no): ")
    va_de_traje = input("¿Va de traje? (si/no): ")

    descuento = calcular_descuento(usa_lentes, es_estudiante, usa_tenis, va_de_traje)

    if descuento == 1.0:
        print("¡Felicidades, tu entrada es gratis!")
    else:
        total_descuento = costo_base * descuento
        costo_final = costo_base - total_descuento
        print(f"Descuento total: {total_descuento:.2f}")
        print(f"Costo final: {costo_final:.2f}")


if __name__ == "__main__":
    main()
