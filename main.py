from cenario import *
from game import *

#COMANDO DO JOGO (TECLA ESPACO)

# Caminho 1: Inicio, 1,2,3, final
# Caminho 2: Inicio, 1,3,2, final
# Caminho 3: Inicio, 2,1,3, final
# Caminho 4: Início, 2,3,1,final
# Caminho 5: Início, 3,1,2,final
# Caminho 6: Inicio,3,2,1,final

soma = 0  

def exibir(custo, matriz, caminho):
    global soma  
    soma += custo  # Adiciona o custo do nó visitado 
    print("Custo do caminho -> {}".format(custo))
    print("Custo acumulado -> {}".format(soma))
    trocar_tela(matriz,caminho) 
      
     
def main():

   mapa_0 = "mapa_principal.txt"
   mapa_1 = "dungeons1.txt" 
   mapa_2 = "dungeons2.txt" 
   mapa_3 = "dungeons3.txt" 

   
   # Caminho 1: Inicio(25, 28), 1(6, 33),2(40, 18),3(25, 2), final(7, 6)
   def caminho_1(running=False):
      trechos = [((25, 28), (6, 33), mapa_0),
                  ((15, 27), (14, 4), mapa_1), #inicio da dg 1
                  ((14, 4), (15, 27), mapa_1),
                  ((6, 33), (40, 18), mapa_0), #volta pra o inicio da dg1 indo ao dg2
                  ((14, 26), (14, 3), mapa_2),
                  ((14, 3), (14, 26), mapa_2),
                  ((40, 18), (25, 2), mapa_0),
                  ((15, 26), (16, 20), mapa_3),
                  ((16, 20), (15, 26), mapa_3),
                  ((25, 2), (7, 6), mapa_0)]
      
      total_custo = 0
      for inicio, fim, mapa in trechos:
         caminho, matriz, custo = principal(*inicio, *fim, mapa)
         total_custo += custo
         if running:
               exibir(custo, matriz, caminho)
               
      return total_custo


   # Caminho 2: Inicio(25, 28), 1(6, 33),3(25, 2),2(40, 18), final(7, 6)
   def caminho_2(running = False):
      trechos = [
         ((25, 28), (6, 33), mapa_0),
         ((15, 27), (14, 4), mapa_1),
         ((14, 4), (15, 27), mapa_1),
         ((6, 33), (25, 2), mapa_0),
         ((14, 26), (14, 3), mapa_2),
         ((14, 3), (14, 26), mapa_2),
         ((25, 2), (40, 18), mapa_0),
         ((15, 26), (16, 20), mapa_3),
         ((16, 20), (15, 26), mapa_3),
         ((40, 18), (7, 6), mapa_0)]
      
      total_custo = 0
      for inicio, fim, mapa in trechos:
         caminho, matriz, custo = principal(*inicio, *fim, mapa)
         total_custo += custo
         if running:
               exibir(custo, matriz, caminho)
               
      return total_custo
   

   # Caminho 3: Inicio(25, 28), 2(40, 18),1(6, 33), 2(25, 2), final(7, 6)
   def caminho_3(running=False):    
     trechos = [
         ((25, 28), (40, 18), mapa_0),    
         ((15, 27), (14, 4), mapa_1),  
         ((14, 4), (15, 27), mapa_1),
         ((40, 18), (6, 33), mapa_0),
         ((14, 26), (14, 3), mapa_2), 
         ((14, 3), (14, 26), mapa_2),             
         ((6, 33), (25, 2), mapa_0),
         ((15, 26), (16, 20), mapa_3),   
         ((16, 20), (15, 26), mapa_3),  
         ((25, 2), (7, 6), mapa_0)]

     total_custo = 0
     for inicio, fim, mapa in trechos:
         caminho, matriz, custo = principal(*inicio, *fim, mapa)
         total_custo += custo
         if running:
               exibir(custo, matriz, caminho)
               
     return total_custo
       
   
   # Caminho 4: Início(25, 28), 2(40, 18),3(25, 2),(6, 33),final(7, 6)
   def caminho_4(running=False):
      trechos = [
        ((25, 28), (40, 18), mapa_0),
        ((15, 27), (14, 4), mapa_1),
        ((14, 4), (15, 27), mapa_1),
        ((40, 18), (25, 2), mapa_0),
        ((14, 26), (14, 3), mapa_2),
        ((14, 3), (14, 26), mapa_2),
        ((25, 2), (6, 33), mapa_0),
        ((15, 26), (16, 20), mapa_3),
        ((16, 20), (15, 26), mapa_3),
        ((6, 33), (7, 6), mapa_0)]
      total_custo = 0
      for inicio, fim, mapa in trechos:
          caminho, matriz, custo = principal(*inicio, *fim, mapa)
          total_custo += custo
          if running:
               exibir(custo, matriz, caminho)
               
      return total_custo
      

   
   # Caminho 5: Início(25, 28), 3(25, 2),1(6, 33),2(40, 18),final(7, 6)
   def caminho_5(running=False):
       trechos = [
              ((25, 28), (25, 2), mapa_0),  
              ((15, 27), (14, 4), mapa_1), 
              ((14, 4), (15, 27), mapa_1),
              ((25, 2), (6, 33), mapa_0),  
              ((14, 26), (14, 3), mapa_2),  
              ((14, 3), (14, 26), mapa_2),
              ((6, 33), (40, 18), mapa_0),  
              ((15, 26), (16, 20), mapa_3),  
              ((16, 20), (15, 26), mapa_3),
              ((40, 18), (7, 6), mapa_0)
              ] 
       total_custo = 0
       for inicio, fim, mapa in trechos:
            caminho, matriz, custo = principal(*inicio, *fim, mapa)
            total_custo += custo
            if running:
                  exibir(custo, matriz, caminho)
                  
       return total_custo      


   # Caminho 6: Inicio(25, 28),3(25, 2),2(40, 18),1(6, 33),final(7, 6)

   def caminho_6(running=False):
        trechos = [
        ((25, 28), (25, 2), mapa_0),  # inicio
        ((15, 27), (14, 4), mapa_1),  # dungeon 1
        ((14, 4), (15, 27), mapa_1),
        ((25, 2), (40, 18), mapa_0),
        ((14, 26), (14, 3), mapa_2),  # dungeon 2
        ((14, 3), (14, 26), mapa_2),
        ((40, 18), (6, 33), mapa_0),
        ((15, 26), (16, 20), mapa_3),  # dungeon 3
        ((16, 20), (15, 26), mapa_3),
        ((16, 33), (7, 6), mapa_0),  # Entrada de Lost Woods
    ]      
        total_custo = 0
        for inicio, fim, mapa in trechos:
            caminho, matriz, custo = principal(*inicio, *fim, mapa)
            total_custo += custo
            if running:
                  exibir(custo, matriz, caminho)
                  
        return total_custo      

     
   resultados = []


   resultados.append({"caminho": "1 -> Inicio, 1,2,3, final ","nome":"caminho_1", "custo": caminho_1()})
   resultados.append({"caminho": "2 -> Inicio, 1,3,2, final", "nome":"caminho_2", "custo": caminho_2()})
   resultados.append({"caminho": "3 -> Inicio, 2,1,3, final","nome":"caminho_3", "custo": caminho_3()})
   resultados.append({"caminho": "4 -> Início, 2,3,1,final", "nome":"caminho_4", "custo": caminho_4()})
   resultados.append({"caminho": "5 -> Início, 3,1,2,final","nome":"caminho_5", "custo": caminho_5()})
   resultados.append({"caminho": "6 -> Inicio,3,2,1,final", "nome":"caminho_6","custo": caminho_6()})
   
   resultados_ordenados = sorted(resultados, key=lambda k: k['custo']) #coloca em ordem crescente os caminhos e imprime

    # Imprime os resultados
   for resultado in resultados_ordenados:
        print(f"Caminho {resultado['caminho']}: Custo = {resultado['custo']}")
        

   # Obtém o menor custo
   menor_custo = resultados_ordenados[0]['custo']
   nome = resultados_ordenados[0]['nome']
   
   # Imprime o menor custo
   print(f"Menor custo encontrado: {menor_custo}")
   print(f"Caminho Escolhido: {nome}")
    
   if nome == "caminho_1": #gambiarra se for caminho 1, ele chama e executa o caminho 1.
        caminho_1(True)    #só executa se tiver o true dentro do argumento da funcao
   elif nome == "caminho_2":
        caminho_2(True)   
   elif nome == "caminho_3":
        caminho_3(True)
   elif nome == "caminho_4":
        caminho_4(True)
   elif nome == "caminho_5":
        caminho_5(True)    
   elif nome == "caminho_6":
        caminho_6(True)    
   else:
        print("Invalid nome.")

    #fechar_janela("") 

if __name__ == "__main__":
    main()

    


