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
        print(f"{i}. {pago['nombre']} - {['pago']} - ${pago['monto']}")
        print()

def buscar_por_nombre (nombre):
    encontrados = [P for p in pagos if p["nombre."].lower()==nombre.lower()]
    if encontrados: 
        print (f"\n resultados para '{nombre}':")
    for pago in encontrados:
        print (f"- {pago ['metodo']} - ${pago['monto']}")
    else:
        print(f"\n no encontraron pagos de '{nombre}'.")
