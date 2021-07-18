from math import sqrt
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
# Moscow - Paris:
# print(sqrt((550 - 480) ** 2 + (370 - 480) ** 2))
# Moscow - London:
# print(sqrt((550 - 510) ** 2 + (370 - 510) ** 2))
# Paris - London:
# print(sqrt((510 - 480) ** 2 + (510 - 480) ** 2))
distances = {}
coord_list = []
for i in sites.keys():
    for j in sites.get(i):
        coord_list.append(j)
x = coord_list[0::2]
y = coord_list[1::2]
coord_list = []
for i in sites:
    # print(i)
    coord_list.append(i)
# print(coord_list)
for i in range(0, 3):
    distances['{}-{}'.format(coord_list[i - 1], coord_list[i])] = sqrt((x[i-1] - x[i]) ** 2 + (y[i-1] - y[i]) ** 2)
# distances[coord_list[1::3]] = ' '
print(distances)
