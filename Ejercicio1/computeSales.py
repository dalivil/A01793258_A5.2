import json
import sys
import time


def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON en el archivo {archivo}.")
        return {}


def calcular_costo_total(precios, ventas):
    costo_total = 0
    for venta in ventas:
        producto = venta['Product']
        cantidad = venta['Quantity']
        for precio in precios:
            try:
                title = precio['title']
                if producto in title:
                    costo_total += precio['price'] * cantidad
                    print(f"{producto} {title} {cantidad} {costo_total}")
                    break
            except KeyError:
                print("Venta con formato inválido.")

    return costo_total



def main():
    # Nombre del archivo de resultados
    archivo_salida = '/Users/dalinaaideevillaocelotl/Desktop/Ejercicio1/SalesResults.txt'

    precios = cargar_datos("TC1.Productlist.json")
    ventas = cargar_datos("TC1.Sales.json")

    start_time = time.time()

    costo_total = calcular_costo_total(precios, ventas)

    print(f"Costo total de todas las ventas: ${costo_total:.2f}")

    with open("SalesResults.txt", 'w') as file:
        file.write(f"Costo total de todas las ventas: ${costo_total:.2f}\n")
        file.write(f"Tiempo de ejecución: {time.time() - start_time:.2f} segundos\n")

    print(f"Tiempo de ejecución: {time.time() - start_time:.2f} segundos")



if __name__ == "__main__":
    main()