import matplotlib.pyplot as plt

menu = "0"
while menu != "5" :
    menu = input("Ingrese una de las opciones del 1 al 5: ")
    if menu == "1" :
        print("si")
    elif menu == "2" :
        print("yes")
    elif menu == "3" :
        print("Hola")
    elif menu == "4" :
        print("Holito")
    elif menu == "5" :
        print("Hello")
    else :
        print("Opción invalida")

#Grafico de lineas 
ejex = [4, 8, 13, 17, 20]
ejey = [54, 67, 98, 78, 45]
plt.plot(ejex,ejey)
plt.show()

#Grafico de barras
x = [1,1,1,2,2,3]
plt.hist(x)
plt.show()

#open , read 