import random


i = 1
tombola = []
for k in range(1,91):
    tombola.append(i)
    i=i+1

my_set = set(tombola)
my_set1 = set()
while True:
    input('Press any key\n')
    sampled_item = random.sample(list(my_set), 1)[0]
    print("Estratto")
    print(sampled_item)
    my_set.remove(sampled_item)
    my_set1.add(sampled_item)
    print("Restanti")
    print(my_set)
    print("Estratti")
    print(my_set1)

