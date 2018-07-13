ages = {'Meg':24, 'Tsemaye':17, 'Caroline':19, 'Matt':29}

ages['Caroline'] = 20

ages['Carly'] = 16



for name in ages:
    x = ages[name]
    ages[name] = x + 1
    print(x)

print(ages)
