# fizzbuzz.py

for i in range(1, 100+1):
    if i % 3 == 0:
        print('fizz')
    if i % 5 == 0:
        print('buzz')
    else:    
        print(i, end='\t')

print('')
