# fizzbuzz.py

for i in range(1, 300+1):
    if i % 3 == 0:
        print('fizz')
    if i % 5 == 0:
        print('buzz')
    if i % 15 == 0:
        print('fizzbuzz')
    else:    
        print(i, end='\t')

print('')
