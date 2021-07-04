import matplotlib.pyplot as plt

with open("CasosActivosPorComuna.csv","r") as f :
    lineas = f.readlines()
f.close()
contador = 0
datos = []
regioncodigo = []

for linea in lineas :
         linea = linea.strip("/n")
         palabras = linea.split(",")
         datos.append(palabras)
         if contador == 0 :
          aux = palabras
          contador = contador + 1
          print("Región - Codigo-Región")
          continue
         else :
          if (aux[0] != palabras[0]) :
            regioncodigo.append(palabras[0] + " - " + palabras[1])
         aux = palabras

menu = "0"
while menu != "5" :
    fila = 0
    bandera1 = False
    bandera2 = False
    bandera3 = False
    bandera4 = False
    bandera5 = False
    grafico1 = []
    grafico2 = []
    menu = input("Ingrese una de las opciones del 1 al 5: ")
    if menu == "1" :
        for i in regioncodigo :
            print(i)
    elif menu == "2" :
        comuna = input("Ingrese una comuna: ")
        if(comuna.isnumeric() == True) :
            for i in range(len(datos)) :
                if datos[i][3] == comuna :
                    print("Comuna encontrada: ", datos[i][2])
                    bandera1 = True
                    fila = i
            if bandera1 == False :
                print("Codigo invalido")
        else :
            for i in range(len(datos)) :
                if datos[i][2] == comuna :
                    print("Comuna confirmada, codigo es: ", datos[i][3])
                    bandera2 = True
                    fila = i
            if bandera2 == False :
                print("Nombre de la comuna invalido")
        if bandera1 == True or bandera2 == True :
            print("Ingrese el periodo de tiempo que quiere revisar")
            fecha1 = input("Ingrese la fecha de inicio: ")
            fecha2 = input("Ingrese la fecha final: ")
            for i in datos[0] :
                if fecha1 == i :
                    bandera3 = True
                if fecha2 == i :
                    bandera4 = True
            if bandera3 == False or bandera4 == False :
                print("Fecha incorrecta")
            else :
                for i in range(len(datos[0])) :
                    if bandera5 == False :
                        if fecha1 == datos[0][i] :
                            grafico1.append(datos[0][i])
                            grafico2.append(float(datos[fila][i]))
                            bandera5 = True
                    else :
                        grafico1.append(datos[0][i])
                        grafico2.append(float(datos[fila][i]))
                        if fecha2 == datos[0][i] :
                            bandera5 = False
                plt.plot(grafico1, grafico2)
                plt.show()
    elif menu == "3" :
        print("Hola")
    elif menu == "4" :
       print("Holito")
    elif menu == "5" :
        print("Hello")
    else :
       print("Opción invalida")