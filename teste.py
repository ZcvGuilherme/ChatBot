num = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
       num += i


print(f'A soma de todos os numeros impares é {num}')