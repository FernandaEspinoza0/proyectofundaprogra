import matplotlib.pyplot as plt

datos = []
regionCodigo = []
fila = []
fila.append(0)
def archivo():
    with open("CasosActivosPorComuna.csv","r") as f :
     lineas = f.readlines()
    f.close()
    contador = 0
    for linea in lineas:
        linea = linea.strip("\n")
        palabras = linea.split(",")
        datos.append(palabras)
        if contador == 0:
            aux = palabras
            contador = contador + 1
            continue
        else:
            if (aux[0] != palabras[0]):
                regionCodigo.append(palabras[0] +" - "+ palabras[1])
        aux = palabras

def grafico(x):
    labels = 'personas contagiadas', 'personas sanas'
    sizes = [x, 100-x]
    explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def menu():
    menu = "0"
    while menu != "5" :
        bandera = [False, False, False, False, False]
        menu = input("Ingrese una de las opciones del 1 al 5: ")
        if menu == "1" :
            opcion1()
        elif menu == "2" :
            opcion2(bandera)
        elif menu == "3":
            opcion3()
        elif menu == "4":
            opcion4(bandera)
        elif menu == "5" :
            print("Fin del programa")
        else :
            print("Opción invalida")

def fcomuna(bandera):
    codigoComunas = input("Ingrese la comuna: ")
    if(codigoComunas.isnumeric() == True):
        for i in range(len(datos)):
            if datos[i][3] == codigoComunas:
                print("comuna encontrada: ", datos[i][2])
                bandera[0] = True
                fila[0] = i
        if bandera[0] == False:
            print("codigo invalido.")
    else:
        for i in range(len(datos)):
            if datos[i][2] == codigoComunas:
                print("comuna confirmada, codigo es: ", datos[i][3])
                bandera[1] = True
                fila[0] = i
        if bandera[1] == False:
            print("nombre de comuna invalido.")
    return bandera;

def opcion1():
    for i in regionCodigo:
        print(i)
def opcion2(bandera):
    grafico1 = []
    grafico2 = []
    bandera = fcomuna(bandera)
    if bandera[0] == True or bandera[1] == True:
        print("Ingrese el periodo de tiempo que quiere revisar")
        fecha1 = input("fecha inicio: ")
        fecha2 = input("fecha final: ")
        for i in datos[0]:
            if fecha1 == i:
                bandera[2] = True
            if fecha2 == i:
                bandera[3] = True
        if bandera[2] == False or bandera[3] == False:
            print("fecha incorrecta")
        else:
            for i in range(len(datos[0])):
                if bandera[4] == False:
                    if fecha1 == datos[0][i]:
                        grafico1.append(datos[0][i])
                        grafico2.append(float(datos[fila[0]][i]))
                        bandera[4] = True
                else:
                    grafico1.append(datos[0][i])
                    grafico2.append(float(datos[fila[0]][i]))
                    if fecha2 == datos[0][i]:
                        bandera[4] = False
            print(grafico1)
            print(grafico2)
            plt.plot(grafico1,grafico2)
            plt.show()

def opcion3():
    region = []
    porcentaje = []
    for i in range(len(datos)):
        promedio = 0.0
        if datos[i][2] == "Total":
            region.append(datos[i][0])
            for j in range(5, len(datos[i])):
                promedio = promedio + float(datos[i][j])
            porcentaje.append(int((promedio/float(datos[i][4]))*100))
    menor = porcentaje[0]
    mayor = porcentaje[0]
    posicion1 = 0
    posicion2 = 0
    for l in range(len(porcentaje)):
        if menor > porcentaje[l+1]:
            menor = porcentaje[l+1]
            posicion1 = l
        if mayor < porcentaje[l+1]:
            mayor = porcentaje[l+1]
            posicion2 = l
        if l == len(porcentaje)-2:
            break
    print("la region con menor densidad de contagio es: ",region[posicion1], " con un porcentaje de ", menor, "%" )
    grafico(menor)
    grafico(mayor)

def opcion4(bandera):
    bandera = fcomuna(bandera)
    if bandera[0] == True or bandera[1] == True:
        promedio = 0.0
        for i in range(5, len(datos[fila[0]])):
            promedio = promedio + float(datos[fila[0]][i])
        promedio = int(promedio/len(datos[fila[0]]))
        print("el promedio de pacientes infectados por mes en ", datos[fila[0]][2], " es: ", promedio, " pacientes.")

archivo()
menu()
