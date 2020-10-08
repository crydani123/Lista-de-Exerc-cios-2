import random

num = [0,1,2,3,4,5,6,7,8]
random.shuffle(num)
matriz = [[num[0],num[1],num[2]], [num[3],num[4],num[5]], [num[6],num[7],num[8]]]

print('-=' * 30)

for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]}]' , end='')

    print()

try:
  indice1 = 0
  indice2 = matriz[0].index(0)
except:
  try:
    indice1 = 1
    indice2 = matriz[1].index(0)
  except:
    try:
      indice1 = 2
      indice2 = matriz[2].index(0)
    except:
      pass


print("zero",matriz[indice1][indice2])
print("linha", indice1+1)
print("coluna", indice2+1)


