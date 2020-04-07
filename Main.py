
import Functions.Distance

f = open('./data/matrix.txt')
data = f.read().strip()
f.close()

fs = open('./output/output.txt', "w")


M = [[float(num) for num in line.strip().split()] for line in data.split('\n')]

M_dist = Functions.Distance.Euclidean_Dist(M)
Cluster = 0


print('Initial distance matrix: ')
fs.write('Initial distance matrix: \n')
for v in M_dist:
    print(v)
    fs.write(str(v) + '\n')

i = 0
m = len(M) - 1
m2 = m-1
Dend = []

while i < m:
    Cluster = Functions.Distance.Simple_Link(M_dist)
    fs.write('\n')
    print('Cluster: "C' + str(i) + '" made up of the following clusters:')
    print(M_dist[Cluster][0])
    print(M_dist[Cluster][1])
    fs.write('Cluster: "C' + str(i) + '" made up of the following clusters: \n' + \
             str(M_dist[Cluster][0]) + '\n' + \
             str(M_dist[Cluster][1]) + '\n')
    Dend.append([i, M_dist[Cluster][0], M_dist[Cluster][1]])

    M_dist = Functions.Distance.Update_Matrix(i, M_dist[Cluster][0], M_dist[Cluster][1], M_dist)
    if i < m2:
        print('New distance matrix: ')
        for v in M_dist:
            print(v)

    i += 1


fs.close()