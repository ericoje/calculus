# cartesian products list comprehension

colors = ['black', 'white']
sizes  =  ['s', 'm', 'l', 'xl']
tshirts = [(colors,size) for color in colors for size in sizes]
tshirts = [(color,size) for color in colors 
           for size in sizes]
print (tshirts)

# cartesian product generator expressions 


for tshirt in  (f'{c}  {s}' for c in colors for s in sizes):
    print (tshirt)

# tuples used as records

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country,_ in traveler_ids:
    print(country)

# tuples 

a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(a) 
print (b)
b[-1].append(99)
b[-1].append(220)

print(b)

# this is to test my commit
print (b)

# i was finally able to commit this file
