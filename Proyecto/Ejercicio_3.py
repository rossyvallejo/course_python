import datetime

def calcular_edad(fecha_nacimiento):
    hoy = datetime.date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def calcular_dias_vida(fecha_nacimiento):
    hoy = datetime.date.today()
    dias_vida = (hoy - fecha_nacimiento).days
    return dias_vida

def obtener_signo_zodiacal(fecha_nacimiento):
    dia = fecha_nacimiento.day
    mes = fecha_nacimiento.month

    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        return "Aries"
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
        return "Géminis"
    elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
        return "Escorpio"
    elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
        return "Capricornio"
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
        return "Acuario"
    else:
        return "Piscis"

def main():
    fecha_str = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")
    fecha_nacimiento = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()

    edad = calcular_edad(fecha_nacimiento)
    dias_vida = calcular_dias_vida(fecha_nacimiento)
    signo_zodiacal = obtener_signo_zodiacal(fecha_nacimiento)

    print("Tu edad es:", edad)
    print("Días de vida:", dias_vida)
    print("Tu signo zodiacal es:", signo_zodiacal)

if __name__ == "__main__":
    main()
