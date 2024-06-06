'Revisar mi lista de contactos'
import random

# Función para generar un número de teléfono aleatorio
def generar_numero_aleatorio():
    return f"+52 {random.randint(100, 999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

# Lista de nombres reales
nombres = [
    "Carlos García", "María Hernández", "Luis Martínez", "Ana López",
    "Jorge González", "Laura Pérez", "Ricardo Ramírez", "Patricia Sánchez",
    "David Torres", "Mónica Rivera"
]

# Generar contactos aleatorios
def generar_contactos(n):
    contactos = []
    for _ in range(n):
        nombre = random.choice(nombres)
        numero = generar_numero_aleatorio()
        contactos.append((nombre, numero))
    return tuple(contactos)

# Mostrar contactos ocultando los números
def mostrar_contactos_ocultos(contactos):
    for i, (nombre, _) in enumerate(contactos, 1):
        print(f"{i}. {nombre} - ***-****-****")

# Buscar un contacto por nombre y mostrar su número
def buscar_contacto(contactos, nombre):
    for contacto in contactos:
        if contacto[0] == nombre:
            return contacto[1]
    return None

# Generar 10 contactos aleatorios inicialmente
contactos = generar_contactos(10)

# Mostrar contactos con números ocultos
print("Lista de contactos:")
mostrar_contactos_ocultos(contactos)

# Ejemplo de búsqueda de un contacto por nombre
nombre_a_buscar = input("Introduce el nombre del contacto que deseas buscar: ")
numero = buscar_contacto(contactos, nombre_a_buscar)

if numero:
    print(f"El número de {nombre_a_buscar} es {numero}")
else:
    print(f"Contacto {nombre_a_buscar} no encontrado.")

# Generar más contactos aleatorios y agregarlos a la lista existente
nuevos_contactos = generar_contactos(5)
contactos += nuevos_contactos

