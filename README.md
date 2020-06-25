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


3. The distance between the new cluster and the rest of the clusters is calculated and the M variable y updated:

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
The the number of times that necesary for the loop is calculated as N-1, being N the total number of records.

## Distance Library

The library developed contains 3 functions that are used in the algorithm.

### Euclidean_Dist Function

### Simple_Link Function

### Update_Matrix Function


