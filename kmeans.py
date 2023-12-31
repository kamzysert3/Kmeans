# @AURTHOR: KAMSICHO RAYMOND NNAEGBUNA
# KMEANS CLUSTERING ALGORITHM 

import math
import random
from statistics import mean

# APP NAME AND DESCRIPTION
print("\033[1m Kmeans Clustering\033[0m")
print("\033[1m Note:\033[0m The dataset is filled with randomly generated data")

# INITIALIZING KMEANS VARIABLES
dataset_no = int(input("How many data do you want in your dataset: \n"))
dataset = [random.randint(1, 100) for _ in range(dataset_no)]
all_clusters = []
all_cluster_mean = []
all_cluster_lmean = []

while True:
    cluster = int(input("How many Clusters do you want: \n"))
    if cluster > (len(dataset) / 2):
        print("clusters cannot exceed half the dataset")
    else:
        break

split_dataset = len(dataset) // cluster

# ASSIGNING DATASET TO CLUSTERS
for i in range(cluster):
    start_index = i * split_dataset
    end_index = (i + 1) * split_dataset if i < cluster - 1 else None
    part = dataset[start_index:end_index]
    all_clusters.append(part)
    locals()[f"Cluster_{i + 1}"] = part

# CALCULATING KMEAN (MEAN OF CLUSTERS)
for j, arr in enumerate(all_clusters):
    kmean = math.ceil(mean(arr))
    all_cluster_mean.append(kmean)

# KMEANS ALGORITHM 
while all_cluster_mean != all_cluster_lmean:
    all_cluster_lmean = all_cluster_mean.copy()

    for m in all_clusters:
        m.clear()

    for l in dataset:
        cluster_put = 0
        acc_cluster = 1000000
        for n in range(cluster):
            close_cluster = abs(l - all_cluster_mean[n])
            if close_cluster < acc_cluster:
                acc_cluster = close_cluster
                cluster_put = n
        all_clusters[cluster_put].append(l)

    all_cluster_mean.clear()

    try:
        for _, arry in enumerate(all_clusters):            
            kmean = math.ceil(mean(arry))
            all_cluster_mean.append(kmean)
    except:
        print("AN ERROR WAS ENCOUNTERED")
        break
   
# DISPLAY FINAL CLUSTERS
for p, arry in enumerate(all_clusters):
    arry.sort()
    print(f"Cluster_{p + 1}: {arry}")