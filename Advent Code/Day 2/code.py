def verificar(lista):
    if not lista:
        return 0  # Lista vazia não é válida

    # Verifica se a lista está aumentando ou diminuindo
    esta_aumentando = all(lista[i] < lista[i+1] for i in range(len(lista)-1))
    esta_diminuindo = all(lista[i] > lista[i+1] for i in range(len(lista)-1))

    if not (esta_aumentando or esta_diminuindo):
        return 0  # A lista não está nem aumentando nem diminuindo

    # Verifica a diferença entre níveis adjacentes
    for i in range(len(lista)-1):
        diferenca = abs(lista[i] - lista[i+1])
        if diferenca < 1 or diferenca > 3:
            return 0  # A diferença não está dentro do intervalo permitido

    return 1  # A lista atende a todas as condições

# Pega os dados do aquivo input
caminho_txt = r"C:\\Users\\Heitor Frainer\\Documents\\Projetos\\Advent Code\\Day 2\\input.txt"
with open(caminho_txt , "r" , encoding = "UTF-8") as arquivo:
  reports_str = arquivo.read()

linhas = reports_str.strip().split('\n')

# Criar a matriz
matriz = []
for linha in linhas:
    # Dividir os números e convertê-los em inteiros
    numeros = list(map(int, linha.split()))
    matriz.append(numeros)

# Verificar as condições para cada linha
soma = 0
for i in range(len(matriz)):
   soma = soma + verificar(matriz[i])
   
print(soma)