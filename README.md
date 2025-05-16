# ProyectoDiscretas2  
# Documento explicativo

Este programa simula la evolución de clanes mágicos y calcula las particiones enteras del tamaño de cada clan. Utiliza:

- Una estructura de **conjuntos disjuntos (Union-Find)** para agrupar espíritus en clanes mediante operaciones de unión.
- Una función recursiva con **memorización** para contar las formas distintas de distribuir la energía de un clan (particiones enteras).

---

## Funciones

### **inicializar(n: int) -> tuple[list[int], list[int]]**
Inicializa los vectores padre y tamano, donde cada espíritu comienza como su propio clan.

#### Parámetros:
- n: Número de espíritus.

#### Return:
Una tupla con dos listas:
- padre: Donde padre[i] representa el líder del clan del espíritu i.
- tamano: Donde tamano[i] representa el tamaño del clan liderado por i.

---

### **buscar(padre: list[int], x: int) -> int**
Encuentra el representante (líder) del conjunto al que pertenece el espíritu x, con compresión de caminos.

#### Parámetros:
- padre: Lista de líderes.
- x: Espíritu a buscar.

#### Return:
El índice del líder del clan al que pertenece x.

---

### **unir(padre: list[int], tamano: list[int], x: int, y: int)**
Une los clanes de x e y si no están en el mismo, actualizando líderes y tamaños.

#### Parámetros:
- padre: Lista de líderes.
- tamano: Lista de tamaños.
- x, y: Espíritus que desean unirse.

---

### **contar_particiones(num: int, memo: dict[int, int]) -> int**
Cuenta las particiones enteras positivas del número num usando la fórmula de partición de Euler con memorización.

#### Parámetros:
- num: Número entero positivo.
- memo: Diccionario para guardar resultados ya calculados.

#### ¿Cómo funciona?
Usa la **función generatriz de particiones**:
- Recorre números pentagonales generalizados positivos y negativos.
- Aplica signo alternante y acumula resultados recursivos.
- Retorna el número de particiones, módulo 1000000007.

#### Return:
Cantidad de particiones enteras de num.

---

### **main()**
Función principal que maneja la entrada, procesos y salida.

#### ¿Cómo funciona?
- Lee T, el número de casos de prueba.
- Por cada caso:
  - Lee el número de espíritus n y el número de operaciones m.
  - Inicializa las estructuras.
  - Procesa m operaciones de dos tipos:
    - union x y: Une los clanes de x e y.
    - partitions x: Imprime el número de particiones del tamaño del clan de x.

---

## Ejemplo de Entrada y Salida

### Entrada:
- 1
- 5 5
- union 1 2
- union 2 3
- partitions 1
- union 4 5
- partitions 4

### Salida:
- 3
- 2
