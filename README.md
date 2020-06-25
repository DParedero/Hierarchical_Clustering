# Agglomerative Hierarchical Clustering


## Introduction

The objective is to develop a version of the agglomerative hierarchical clustering algorithm. This algorithm generates a hierarchical structure in the form of a tree, with the root node being the cluster that contains the greatest number of elements and the leaf nodes being the clusters with the least number of elements. Specifically, as it is an agglomerative algorithm, the procedure will start from the leaf nodes to form ever larger clusters until reaching the root node. In order to implement the algorithm, it is also necessary to develop a specific library of functions that calculates the distances within the topologies of the clusters.

This algorithm is one of the machine learning techniques known as unsupervised learning, that looks for previously undetected patterns in a dataset with no pre-existing labels and setting the clusters as labels.

The project is written using Python 3.8.0 and licensed under Apache License 2.0. Full source code is [available on the following link](https://github.com/Dparedero/Hierarchical_Clustering). 

### Use Case
The project looks to address the main objective of given a dataset, obtaining a dendrogram that classifies the records into data clusters from most similar to least similar based on certain established metrics that translate the distance into similarity.

## Input and output
### Input

### Output


## Agglomerative clustering algorithm


[File](https://github.com/DParedero/Hierarchical_Clustering/blob/master/Main.py)


The steps of the algorithm are the following. Given a set of N points (determinated by the N records of the dataset), the algorithm proceeds like this:

1. Each point is assigned to a cluster, so initially there are N clusters of 1 element each one.

2. The distance between the clusters is calculated and those that are the closest, are joined in a single cluster.

3. The distance between the new cluster and the other clusters is calculated.

4. Steps 2 and 3 are repeated until all points are grouped into a single cluster.

Once the hierarchical tree or dendrogram has been completed using this algorithm, if you want to obtain a certain number k of clusters, you simply have to take the clusters of the level with that number of clusters.

The calculation in each iteration of the distances between the new generated cluster and the rest of the clusters, as well as the rest of the metrics that are used in the algorithm are described in the Library section.

The source code of the algorithm is developed in the [main file](https://github.com/DParedero/Hierarchical_Clustering/blob/master/Main.py). This is the explanation of the source code, corresponding to the steps of the algorithm:

1. First, the library Distance is imported to calculate the distance metrics of the algorithm. Then, the dataset and output file are imported to read and write respectivly. Finally, it is initialiced a variable that contains all the records of the dataset, that are de N inicial clusters: 

```python
#Metrics of the algoritm are imported
import Functions.Distance

#Reading the dataset file
f = open('./data/matrix.txt')
data = f.read().strip()
f.close()

#Opening to write the output file
fs = open('./output/output.txt', "w")

#Initializing the matrix variable that contains the initial clusters
M = [[float(num) for num in line.strip().split()] for line in data.split('\n')]
```

2. The distance between the initial clusters is calculated using the euclidean distance function of the library: 

```python
M_dist = Functions.Distance.Euclidean_Dist(M)
Cluster = 0

print('Initial distance matrix: ')
fs.write('Initial distance matrix: \n')
for v in M_dist:
    print(v)
    fs.write(str(v) + '\n')
```

If the clusters are 2 simple points, the distance is calculated by using the euclidean metric, but it one or more of the clusters are complex clusters, the distance is calculated with the simple link metric:  
```python
Cluster = Functions.Distance.Simple_Link(M_dist)
```


3. The distance between the new cluster and the rest of the clusters is calculated and the M variable is updated:

```python
M_dist = Functions.Distance.Update_Matrix(i, M_dist[Cluster][0], M_dist[Cluster][1], M_dist)
```

4. The last step is iterate the 2 and 3 steps until the algorithm obtains a unique cluster. In the source code it is done with the following loop, that contains the previous steps:

```python
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
```            
The number of times that necesary for the loop is calculated as N-1, being N the total number of records.

## Distance Library

The library developed contains 3 functions that are used in the algorithm. These 3 functions are developed in the [library file](https://github.com/DParedero/Hierarchical_Clustering/blob/master/venv/Functions/Distance.py).

### Euclidean_Dist Function

This function receives a matrix of N vectors and calculates the Euclidean distance between each of the vectors, returning as output another matrix with <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\binom{N}{2}\times3" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\binom{N}{2}\times3" title="\binom{N}{2}\times3" /></a> dimensions. The reason of these dimensions is because the output is the combination of the N vectors without repetition and taken 2, including the distance between these 2 vectors.

The function code is as follows:
```python
def Euclidean_Dist(M):

    M_dist = []

    i = 0
    j = 0
    n = len(M)
    while i < n:

        j = i + 1
        while j < n:

            l = []
            cont = 0
            d = 0
            lenV = len(M[i])
            while cont < lenV:

                v = M[i][cont]-M[j][cont]
                d = d + v**2
                cont += 1

            distancia = d**(0.5)
            M_dist.append([i,j,distancia])
            j += 1

        i += 1
    return M_dist
```

### Simple_Link Function

Simple link is the metric used in the algorithm to determine the distance between nodes. According to this metric, given 2 nodes formed by n vectors, the distance between the nodes is equal to the minimum distance between vectors of each of the nodes.

Given a matrix of distances calculated in the Eucliden_Dist function, this function chooses the minimum distance between vectors / nodes to perform the next algorithm iteration. The function code is as follows:
```python
def Simple_Link(M):

    i = 0
    j = 0
    n = len(M)
    dmin = 0
    ind_pos = -1
    
    while i < n:

        if i == 0:
            dmin = M[i][len(M[i])-1]
            ind_pos = i
        else:
            if M[i][len(M[i])-1] < dmin:
                dmin = M[i][len(M[i])-1]
                ind_pos = i

        i += 1
    return ind_pos
```

### Update_Matrix Function

This fuction takes the cluster matrix and the nodes that will join into a cluster as input and updates the matrix for the next iteration of the algorithm.

The function code is as follows:
```python
def Update_Matrix(l,n_v1,n_v2,M):

    i = 0
    n = len(M)
    DISTA = []
    M_final = []
    n_v1 = str(n_v1)
    n_v2 = str(n_v2)

    while i < n:
        if (str(M[i][0]) == n_v1) and (str(M[i][1]) != n_v2):
            DISTA.append([n_v1,M[i][1],M[i][2]])
        elif (str(M[i][1]) == n_v1) and (str(M[i][0]) != n_v2):
            DISTA.append([n_v1, M[i][0], M[i][2]])
        elif (str(M[i][0]) == n_v2) and (str(M[i][1]) != n_v1):
            DISTA.append([n_v2, M[i][1], M[i][2]])
        elif (str(M[i][1]) == n_v2) and (str(M[i][0]) != n_v1):
            DISTA.append([n_v2, M[i][0], M[i][2]])
        else:
            if str(M[i][0]) != n_v1 and str(M[i][0]) != n_v2 and str(M[i][1]) != n_v1 and str(M[i][1]) != n_v2:
                M_final.append(M[i])
        i += 1

    m = len(DISTA)
    j = 0
    d_final = []

    while j < m:
        k = 0
        while k < j:
            if DISTA[k][1] == DISTA[j][1]:
                if DISTA[k][2] < DISTA[j][2]:
                    d_final.append(['C'+str(l),DISTA[k][1],DISTA[k][2]])
                else:
                    d_final.append(['C'+str(l),DISTA[k][1], DISTA[j][2]])
            k += 1
        j += 1

    for v in d_final:
        M_final.append(v)

    return M_final
```