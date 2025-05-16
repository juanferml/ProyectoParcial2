MOD = 1000000007

def inicializar(n):
    padre = []
    tamano = []
    i = 0
    while i <= n:
        padre.append(i)
        tamano.append(1)
        i = i + 1
    return padre, tamano

def buscar(padre, x):
    while padre[x] != x:
        padre[x] = padre[padre[x]]
        x = padre[x]
    return x

def unir(padre, tamano, x, y):
    raizX = buscar(padre, x)
    raizY = buscar(padre, y)
    if raizX != raizY:
        if tamano[raizX] < tamano[raizY]:
            padre[raizX] = raizY
            tamano[raizY] = tamano[raizY] + tamano[raizX]
        else:
            padre[raizY] = raizX
            tamano[raizX] = tamano[raizX] + tamano[raizY]

def contar_particiones(num, memo):
    if num == 0:
        return 1
    if num < 0:
        return 0
    if num in memo:
        return memo[num]

    total = 0
    i = 1
    terminar = False
    while not terminar:
        signo = 1
        if i % 2 == 0:
            signo = -1
        primer = num - i * (3 * i - 1) // 2
        segundo = num - i * (3 * i + 1) // 2

        if primer < 0 and segundo < 0:
            terminar = True
        else:
            if primer >= 0:
                total = (total + signo * contar_particiones(primer, memo)) % MOD
            if segundo >= 0:
                total = (total + signo * contar_particiones(segundo, memo)) % MOD
            i = i + 1

    while total < 0:
        total = total + MOD

    memo[num] = total
    return total

def main():
    T = int(input())
    caso = 0
    while caso < T:
        valores = input().split()
        n = int(valores[0])
        m = int(valores[1])
        padre, tamano = inicializar(n)
        memo = {}
        operacion = 0
        while operacion < m:
            partes = input().split()
            if partes[0] == "union":
                x = int(partes[1])
                y = int(partes[2])
                unir(padre, tamano, x, y)
            if partes[0] == "partitions":
                x = int(partes[1])
                raiz = buscar(padre, x)
                tam = tamano[raiz]
                print(contar_particiones(tam, memo))
            operacion = operacion + 1
        caso = caso + 1

main()
