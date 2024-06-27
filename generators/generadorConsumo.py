import random

import random
def generarDatos ():
    datos=[]
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referenica=random.choice(["ACH01","ACH022","ACH43"])
        marca=random.choice(["SONY","Kalley","RICO"])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(["Medellin","Bogota","Cali","Pereira","Bucaramanga"])
        responsable=random.choice(["Juan Jose","Jennifer","Jose Cano","Camila B","Juan P"])
 
        dato=[id,referenica,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos
print(generarDatos())