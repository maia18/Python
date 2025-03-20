''' Exercício - Lista de tarefas com desfazer e refazer
Música para codar =) Everybody wants to rule the world - Tears for fears
todo = [] -> lista de tarefas
todo = ['fazer café'] -> Adicionar fazer café
todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
desfazer = ['fazer café',] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar'] 
'''

def tarefas(lista_tarefas = None):
    if lista_tarefas is None: 
        lista_tarefas = []
    
    print('Comandos: [1] Listar | [2] Desfazer | [3] Refazer')
    while True:    
        tarefa = input('\nTarefa / Comando: ').capitalize()
        if tarefa != '1' and tarefa != '2' and tarefa != '3':
            lista_tarefas.append(tarefa)
        else:
            if tarefa == '1':
                print('Tarefas: ')
                for itens in lista_tarefas:
                    print(itens)
                    
            elif tarefa == '2':
                lista_tarefas.pop()
                
            elif tarefa == '3':
                ...
                
  
        
t1 = tarefas()
# print(t1)