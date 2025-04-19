caminho_txt = r"C:\\Users\\Heitor Frainer\\Documents\\Projetos\\Advent Code\\Day1\\numbers.txt"

with open(caminho_txt , "r" , encoding = "UTF-8") as arquivo:
  numbers_str = arquivo.read()

numbers_str = numbers_str.split()

numbers =  list(map(int, numbers_str))

list1 = []
list2 = []
list_new = []
total = 0

for i in range(len(numbers)):
  if i % 2 == 0:
    list1.append(numbers[i])
  else:
    list2.append(numbers[i])

list1.sort()
list2.sort()

def mod(num):
  if(num < 0):
    return -num
  else: 
    return num

for x in range(len(list1)):
  new = list2[x] - list1[x]
  total += mod(new)

print(total)