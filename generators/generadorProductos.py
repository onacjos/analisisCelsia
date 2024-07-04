import random

def generadorDatosProductos():
    
    productos=["Musica","TV","Aplicaciones","PC","Celulares","Tablets","Accesorios"]
    datos=[]
    for producto in productos:
        prodCat={}
        categoria=random.choice(["Plus","Mega","Basic"])
        prodCat=[producto,categoria]
        datos.append(prodCat)
    return datos
print(generadorDatosProductos())