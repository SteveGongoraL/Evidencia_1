import pandas as pd
import time
separador = ("°°°" * 40) + "\n"
nomAlumnos=["Steve","Diana","Fernando","Gabriela","Krista","Sarahi","Cindy","Nayeli","Isaac","Mariana","Brayton","Jordan","Dinah","Oliver","Wally","Barton","Frank","Matthew","Wilson","Bruce","Clark","Barry","Arthur","Cisco","Tawne","Tony","Natasha","Billy","Scott","Wanda"]
calificacionesAlumnos={}

darInicio = input("\n\nPresione '0' para desplegar el menu: \n")
while darInicio=="0":
    print("\nMENU de opciones: \n\n1)- Mostrar los nombres de alumnos.\n2)- Capturar calificaciones.\n3)- Comprobar las asignaturas con el menor desempeño.\n4)- Calificaciones de estudiantes que reprobaron las materias.\n5)- Mostrar datos completos.\n6)- Para salir.\n")
    print(separador)
    opcion = input("¿Que operacion deseas realizar?: \n")
    if opcion == "1":
        print("Se cargaron los siguientes nombres de alumnos: ")
        print(nomAlumnos)
        longitud=(len(nomAlumnos))
        print('\n', longitud, "Alumnos registrados")
        time.sleep(3)
    elif opcion =="2":
        for elemento in nomAlumnos:
            calificacion1= float(input(f"Dime la calificacion en Programacion para {elemento}: "))
            while calificacion1<0 or calificacion1>100:
                print("Debes seleccionar una calificacion valida")
                calificacion1= float(input(f"Dime la calificacion en Programacion para {elemento}: "))
            else:
                print()
            calificacion2= float(input(f"Dime la calificacion en Base De Datos para {elemento}: "))
            while calificacion2<0 or calificacion2>100:
                print("Debes seleccionar una calificacion valida")
                calificacion2= float(input(f"Dime la calificacion en Base De Datos para {elemento}: "))
            else:
                print()
            calificacion3= float(input(f"Dime la calificacion en Contabilidad para {elemento}: "))
            while calificacion3<0 or calificacion3>100:
                print("Debes seleccionar una calificacion valida")
                calificacion3= float(input(f"Dime la calificacion en Contabilidad para {elemento}: "))
            else:
                print()
            calificacion4= float(input(f"Dime la calificacion en Redes para {elemento}: "))
            while calificacion4<0 or calificacion4>100:
                print("Debes seleccionar una calificacion valida")
                calificacion4= float(input(f"Dime la calificacion en Redes para {elemento}: "))
            else:
                print()
            calificacion5= float(input(f"Dime la calificacion en Estadistica para {elemento}: "))
            while calificacion5<0 or calificacion5>100:
                print("Debes seleccionar una calificacion valida")
                calificacion5= float(input(f"Dime la calificacion en Estadistica para {elemento}: "))
            else:
                print()
                print(separador)
                calificacionesAlumnos[elemento]=[calificacion1,calificacion2,calificacion3,calificacion4,calificacion5]
                notasEnDiccionario=pd.DataFrame(calificacionesAlumnos)
        notasEnDiccionario.index = ["Programacion", "Base de datos", "Contabilidad", "Redes", "Estadistica"]
    elif opcion =="3":
        print("Estadistica descriptiva calificacion mas baja de cada materia: ")
        print(notasEnDiccionario.T.min())
        print("\nMedia de todas las calificaciones por materia")
        print(notasEnDiccionario.T.mean())
        print("\nDesviacion estandar por todas las materias")
        print(notasEnDiccionario.T.std())
        print(separador)
        time.sleep(6)
    elif opcion =="4":
        print("Calificaciones de los estudiantes que reprobaron")
        aprodabos = notasEnDiccionario.T[notasEnDiccionario.T<70]
        print(aprodabos)
        print(separador)
        time.sleep(6)
    elif opcion =="5":
        print(notasEnDiccionario.T)
        print(separador)
        time.sleep(6)
    elif opcion =="6":
        break
    else:
        print("Debes de elegir una opción valida >:v\n ")
else:
    print("Programa Terminado.\nDebes presionar el numero '0' para iniciar >:v")