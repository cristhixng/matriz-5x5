matriz = [[0 for _ in range (5)]for _ in range(5)]

print("--- Ingreso de valores para la matriz 5x5 ---")
for i in range(5):
    for j in range(5):
        matriz[i][j]= int(input(f"Ingrese el valor para la posicion [{i}][{j}]: "))

print("\nMatriz ingresada:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()