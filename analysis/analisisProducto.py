from  generators.generadorProductos import generadorDatosProductos
import pandas as pd
 
def analizarDatos():
    datos=generadorDatosProductos()
    tabla=pd.DataFrame(datos,columns=["producto","categoria"])
    tabla.to_csv("./data/productos.csv",index=False)
analizarDatos()