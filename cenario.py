from heapq import heappush, heappop


def criar_pesos():
    grama = 10
    areia = 20
    floresta = 100 
    montanha = 150
    agua = 180
    claro = 10

    # Define os pesos para cada caractere
    pesos = {
        "g": grama,
        "a": areia,
        "f": floresta,
        "m": montanha,
        "w": agua,
        "q": claro,
        }
    return pesos

# Define a matriz

import heapq


class Node:
    def __init__(self, x, y, g=0, h=0, parent=None):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.parent = parent

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.g + self.h < other.g + other.h

    def __hash__(self):
        return hash((self.x, self.y))


def heuristic(current, fim):
    return abs(current.x - fim.x) + abs(current.y - fim.y)


def astar(matriz, pesos, inicio, fim):
    open_list = []
    closed_list = set()

    inicio_node = Node(*inicio)
    fim_node = Node(*fim)

    heapq.heappush(open_list, inicio_node)
    primeiro_passo = True
    while open_list:
        current = heapq.heappop(open_list)

        if current == fim_node:
            caminho = []
            custo = 0
            while current is not None:
                caminho.append(current)
                if primeiro_passo == True:
                     custo += 0
                     primeiro_passo = False
                else:     
                 custo += pesos.get(matriz[current.x][current.y], 0)
                current = current.parent
            caminho.reverse()
            return caminho, custo

        closed_list.add(current)

        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor = Node(current.x + x, current.y + y)
            if neighbor.x < 0 or neighbor.x >= len(matriz) or neighbor.y < 0 or neighbor.y >= len(matriz[0]):
                continue
            if matriz[neighbor.x][neighbor.y] not in pesos:
                continue
            if matriz[neighbor.x][neighbor.y] in ["n"]:
                continue
            neighbor.g = current.g + pesos[matriz[neighbor.x][neighbor.y]]
            neighbor.h = heuristic(neighbor, fim_node)

            if neighbor in closed_list:
                continue

            if neighbor in open_list:
                index = open_list.index(neighbor)
                if open_list[index].g > neighbor.g:
                    open_list[index].g = neighbor.g
                    open_list[index].parent = current
            else:
                neighbor.parent = current
                heapq.heappush(open_list, neighbor)

    return None

        
def principal(fim1,fim2,inicio1,inicio2,mapa):

    def criar_matriz():
    
        with open(mapa, "r") as f:
            content = f.readlines()

        # Criando uma matriz vazia com as dimensões apropriadas
        num_linhas = len(content)
        num_colunas = len(content[0].strip())
        matriz = [[0] * num_colunas for _ in range(num_linhas)]

        # Preenchendo a matriz com os valores do arquivo
        for i in range(num_linhas):
            for j in range(num_colunas):
                matriz[i][j] = content[i][j]

        return matriz


    matriz = criar_matriz()
    pesos = criar_pesos()
    inicio = (inicio2-1, inicio1-1)
    fim = (fim2-1, fim1-1)
    caminho, custo = astar(matriz, pesos, inicio, fim)
    #imprimir_caminho(matriz, caminho, custo)
    return caminho, matriz, custo

# def imprimir_caminho(matriz, caminho, custo):
#     print(f"\nCusto do caminho: {custo}")

#     if caminho is not None:
#         for node in caminho:
#             matriz[node.x][node.y] = "x"        
#         for row in matriz:
#             print("".join(row)) 
#         print("\n\n")                
#     else:
#         print("No caminho found.") 
         

     


    



