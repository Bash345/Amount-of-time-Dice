import random

D1 = 0
D2 = 0
D3 = 0
D4 = 0
D5 = 0
D6 = 0

for i in range (0 ,100):
    D = random.randint(1,6)
    
    if D == 1:
        D1 += 1
    elif D == 2:
        D2 += 1
    elif D == 3:
        D3 += 1
    elif D == 4:
        D4 += 1
    elif D == 5:
        D5 += 1
        
    else:
        D6 += 1
        
print ('Dice 1:', D1, 'times')
print ('Dice 1:', D2, 'times')
print ('Dice 1:', D3, 'times')
print ('Dice 1:', D4, 'times')
print ('Dice 1:', D5, 'times')
print ('Dice 1:', D6, 'times')
