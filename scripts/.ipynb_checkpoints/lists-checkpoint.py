druzina = ['jan', 'anja', 'miha']

print(druzina.append('leo'))
print(druzina.__contains__('anja'))
print(druzina.__getitem__(3))
print(druzina.__len__())

x = range(10)
for i in range(len(druzina)):
    print(i)
