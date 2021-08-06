name = input("Ingrese su nombre: ")
carrer = input("Ingrese la carrera a la que se quiere inscribir: ")
city = input("Ingrese su ciudad: ")
cuota = 4500
if carrer == "electromecanica" and city != "rio cuarto":
    print(name,"obtuviste un beneficio del 15 en tu cuota.")
    print("Tu carrera es: ", carrer)
    print("Vivis en: ", city)
    print("Tu monto final a abonar es ", cuota - cuota * 0.15)
else:
    print("Hola", name)
    print("Tu carrera no cuenta con ningun beneficio, el monto que tenes que abonar es de: ", cuota)