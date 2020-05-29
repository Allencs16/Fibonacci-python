n = int(input('quantos numeros deseja que apareça?'))

n1 = 0
n2 = 1
n3 = 0

while n3 <= n:
    print('{}'.format (n3))
    n3 = n1 + n2
    n1 = n2
    n2 = n3
print('fim')