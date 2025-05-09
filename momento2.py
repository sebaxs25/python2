import pandas as pd 

pagos =[]

def registrar_pagos(nombre, metodo, monto):
    pago = {
        "nombre": nombre,
        "metodo": metodo,
        "monto": monto
    }
    pagos.append(pago)
    print(f"\n pago registrado:{nombre} pago ${monto} por {metodo} \n")

def mostrar_pagos():
    if not pagos:
        print("\n no hay registrados.\n")
        return
    print("\n pagos registrados: ")
    for i, pago in enumerate (pagos, 1):
        print(f"{i}. {pago['nombre']} -")