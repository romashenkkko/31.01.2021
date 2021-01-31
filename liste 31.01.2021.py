prenume=['Mihai', 'George', 'Ana', 'Dan', 'Ion', 'Geta', 'Vio']
varsta=[14, 23, 15, 14, 12, 41, 39]
#a
for i in range (0, len(prenume)):
    print(prenume[i], 'are varsta de', varsta[i], 'ani')
#b
prenume.extend(['Andreea', 'Ioan'])
varsta.extend([34,23])
print(prenume)
print(varsta)
#c
prenume.pop(2)
varsta.pop(2)
print(prenume)
print(varsta)
#d
print(prenume[0:3])
#e
print(prenume[::-1])
#f
print(prenume[2:4])
print(varsta[2:4])
print(prenume[0:5])
print(varsta[0:5])