import sys #para o sys.exit funcionar
print('Digite um numero para ser reduzido:')
try:
    number = int(input())
except ValueError:
    print('ERROR: Somente números inteiros.')
    sys.exit()
    
def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    elif n % 2 == 1:
        return  int(n * 3 + 1)

while number != 1 and number != 0 and number > 0:
    number = collatz(number)
    print(number)
    
