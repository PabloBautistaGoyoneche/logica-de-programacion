# Mostrar la carta en pantalla
# El usuario debe escoger sus platos e indicar cuántos platos desea
# Sumar los precios de los platos
# Imprimir resumen de la compra

print('RESTAURANT CON PYTHON')

print('''------------------------CARTA-----------------------------
# PLATOS:
Ceviche de pescado = s/12
Arroz con marisco = s/20
Jalea = s/30
Chicharron de Pota = s/10
Lomo saltado = s/20
Pollo broaster = s/15

# BEBIDAS:
Jarra de chicha = s/10
Jarra de limonada = s/8
Botella de cerveza = s/12
''')

# Definiendo funciones
def calcular_platos(numero_de_platos):
    total_platos = 0
    for i in range(numero_de_platos):
        precio = int(input(f"Ingrese el precio del plato {i + 1}: "))
        total_platos += precio
    return total_platos

def calcular_bebidas(numero_de_bebidas):
    total_bebidas = 0
    for i in range(numero_de_bebidas):
        precio_bebida = int(input(f"Ingrese el precio de la bebida {i + 1}: "))
        total_bebidas += precio_bebida
    return total_bebidas

# Solicitar pedido
print("----------------------------------------------------------")
print("Ahora que ya viste la carta")
nombre_cliente = str(input("Ingrese su nombre: "))
numero_de_platos = int(input("Ingrese el número de comensales: "))
confirmacion_de_bebidas = input("¿Desea bebidas? Colocar 'si' o 'no': ")

if confirmacion_de_bebidas.lower() == "no":
    total_platos = calcular_platos(numero_de_platos)
    print(f'{nombre_cliente}, el pedido vale s/{total_platos}')
else:
    total_platos = calcular_platos(numero_de_platos)
    numero_de_bebidas = int(input("Ingrese el número de bebidas: "))
    total_bebidas = calcular_bebidas(numero_de_bebidas)
    print(f'{nombre_cliente}, el pedido vale s/{total_platos + total_bebidas}')
