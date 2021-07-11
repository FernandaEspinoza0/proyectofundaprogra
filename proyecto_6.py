import matplotlib.pyplot as plt #funcion que nos permitio crear los graficos y que se despliegaron gracias a las funciones que ocuparemos mas adelante
datos = []
regionCodigo = []
fila = []
fila.append(0)
def archivo(): 
    with open("CasosActivosPorComuna.csv","r") as f : #abre el archivo mediante la carpeta guardada en documentos, luego guarda los datos en la carpeta de github con la cual se trabajara y luego cierra el archivo
     lineas = f.readlines()
    f.close()
    contador = 0
    for linea in lineas: #formara una lista con las columnas ordenadas 
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

def grafico(x): # funcion que nos despliega el primer grafico y nos generara un grafico circular con el cual se abrira mediante el matplotlib
    labels = 'personas contagiadas', 'personas sanas'
    sizes = [x, 100-x]
    explode = (0, 0)  # grafico no tenga espacios vacios
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # grafica un grafico circular f
    plt.show()

def menu(): # funcion que despliegara el menu con las opciones que ingresara el usuario 
    bandera = [False, False, False, False, False] # ocupamos el primer i segundo booleano como variables de control para saber si el usuario ingreso el codigo o el nombre de la comuna correctamente
   #la tercera y cuarta bandera son variables de control para saber si el usuario ingreso ambas fechas correctamente
    menu = "0"
    while menu != "5" : #nos dan 4 opciones en el menu, se despliegara 
        menu = input("Ingrese una de las opciones del 1 al 5: ")
        if menu == "1" : 
            opcion1()
        elif menu == "2" :  
            opcion2(bandera)
        elif menu == "3": 
            opcion3()
        elif menu == "4": 
            opcion4(bandera)
        elif menu == "5" : # se le notifica al usuario que el programa ha finalizado 
            print("Fin del programa")
        else : # si el usuario ingresa una opcion equivocada se le da una notificacion
            print("Opción invalida") 

def fcomuna(bandera): # funcion que permite desplegar el codigo de la comuna, si esta comuna es bien ingresada se mostrara su codigo, si el codigo es incorrecto lo tomara como invalido
    codigoComunas = input("Ingrese la comuna: ")
    if(codigoComunas.isnumeric() == True):
        for i in range(len(datos)):
            if datos[i][3] == codigoComunas:
                print("comuna encontrada: ", datos[i][2])
                bandera[0] = True # 
                fila[0] = i
        if bandera[0] == False:
            print("codigo invalido.")
    else:
        for i in range(len(datos)): #nos señala que el nombre de la comuna debe estar bien escrita sino sera invalido
            if datos[i][2] == codigoComunas:
                print("comuna confirmada, codigo es: ", datos[i][3])
                bandera[1] = True
                fila[0] = i
        if bandera[1] == False:
            print("nombre de comuna invalido.")
    return bandera;

def opcion1(): #funcion que señala la opcion 1 la cual despliega los codigos de las regiones 
    for i in regionCodigo:
        print(i)
def opcion2(bandera): # funcion que nos permitira ingresar el periodo de tiempo inicial y final con los datos 
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
                if bandera[4] == False: # busca la primera fecha ingresada por el usuario y al encontrarla cambaimos la variable de control bandera[4], la quinta bandera en la lista
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
        print(grafico2)  #despliega graficos
        plt.plot(grafico1,grafico2)
        plt.show()

def opcion3(): # funcion que permite mostar region con mas y menos densidad de tasa de contagios con los graficos
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
    grafico(menor) #mostrara el grafico con el mayor porcentaje 
    grafico(mayor) #mostrara el grafico con el menor porcentaje

def opcion4(bandera): #funcion de metrica de comparacion del total de pacientes infectados por mes 
    bandera = fcomuna(bandera)
    if bandera[0] == True or bandera[1] == True:
        promedio = 0.0
        for i in range(5, len(datos[fila[0]])):
            promedio = promedio + float(datos[fila[0]][i])
        promedio = int(promedio/len(datos[fila[0]]))
        print("el promedio de pacientes infectados por mes en ", datos[fila[0]][2], " es: ", promedio, " pacientes.")

archivo()
menu()
