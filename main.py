def imprimir_torres(torres):
    for i, torre in enumerate(torres):
        print(f'Torre {i + 1}: {torre}')

def torres_de_hanoi(n):
    torres = [[] for _ in range(3)]

    for disco in range(n, 0, -1):
        torres[0].append(disco)

    movimientos = 0
    while len(torres[2]) != n:
        imprimir_torres(torres)
        origen = int(input("Desde que torre quieres mover (1/2/3): ")) - 1
        destino = int(input("Hacia que torre (1/2/3): ")) - 1

        if origen < 0 or origen > 2 or destino < 0 or destino > 2 or len(torres[origen]) == 0:
            print("Movimiento inválido. Inténtalo de nuevo.")
            continue

        disco = torres[origen][-1]
        if len(torres[destino]) == 0 or disco < torres[destino][-1]:
            torres[origen].pop()
            torres[destino].append(disco)
            movimientos += 1
        else:
            print("Movimiento inválido. El disco no puede ser colocado sobre otro más pequeño.")

    imprimir_torres(torres)
    print(f"¡Juego completado en {movimientos} movimientos!")

if __name__ == "__main__":
    n = int(input("Ingresa el número de discos: "))
    torres_de_hanoi(n)
