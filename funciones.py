with open("CasosActivosPorComuna.csv","r") as f :
    for i in f.readlines() :
        linea = i.split(",")
        print(linea)