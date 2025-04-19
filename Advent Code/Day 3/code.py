import re

caminho_txt = r"C:\\Users\\Heitor Frainer\\Documents\\Projetos\\Advent Code\\Day 3\\input.txt"

with open(caminho_txt , "r" , encoding = "UTF-8") as arquivo:
  input_str = arquivo.read()

def extrair_mul(s):
    # Expressão regular para identificar "mul(x,y)" com x e y como inteiros
    padrao = r"mul\((\d+),(\d+)\)"
    return [[int(x), int(y)] for x, y in re.findall(padrao, s)]

def multiplicar(duplas):
   return duplas[0]*duplas[1]

def main(list_num):
  s = 0
  for duplas in list_num:
    s = s + multiplicar(duplas)
  return s

list_num = extrair_mul(input_str)
print(main(list_num))
