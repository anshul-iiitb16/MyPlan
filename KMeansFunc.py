#import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt1

def Kmean(FileName, itr):
    plt1.clf()
    print("\n\nSTARTED K-MEANS CLUSTERING")
    data = pd.read_csv(FileName)
    X = data[["Bytes Upload","Bytes Download"]]
    
    #Visualise data points
    plt1.scatter(X["Bytes Download"],X["Bytes Upload"],c='black')
    plt1.xlabel('Bytes Download')
    plt1.ylabel('Bytes Upload')
    K = 5
    Centroids = (X.sample(n=K))
    plt1.title('Clustering Plot')
    plt1.scatter(Centroids["Bytes Download"],Centroids["Bytes Upload"],c='red')
    plt1.show()

# Step 3 - Assign all the points to the closest cluster centroid
# Step 4 - Recompute centroids of newly formed clusters
# Step 5 - Repeat step 3 and 4

    diff = 1
    j=0

    while(diff!=0):
        XD=X
        i=1
        for index1,row_c in Centroids.iterrows():
            ED=[]
            for index2,row_d in XD.iterrows():
                d1=(row_c["Bytes Download"]-row_d["Bytes Download"])**2
                d2=(row_c["Bytes Upload"]-row_d["Bytes Upload"])**2
                d=np.sqrt(d1+d2)
                ED.append(d)
            X[i]=ED
            i=i+1

        C=[]
        for index,row in X.iterrows():
            min_dist=row[1]
            pos=1
            for i in range(K):
                if row[i+1] < min_dist:
                    min_dist = row[i+1]
                    pos=i+1
            C.append(pos)
        X["Cluster"]=C
        Centroids_new = X.groupby(["Cluster"]).mean()[["Bytes Upload","Bytes Download"]]
        if j == 0:
            diff=1
            j=j+1
        else:
            diff = (Centroids_new['Bytes Upload'] - Centroids['Bytes Upload']).sum() + (Centroids_new['Bytes Download'] - Centroids['Bytes Download']).sum()
            print(diff.sum())
        Centroids = X.groupby(["Cluster"]).mean()[["Bytes Upload","Bytes Download"]]

    color=['blue','green','cyan','pink','yellow']
    plt1.title('Clustering Plot')
    for k in range(K):
        data=X[X["Cluster"]==k+1]
        plt1.scatter(data["Bytes Upload"],data["Bytes Download"],c=color[k])
        plt1.scatter(Centroids["Bytes Upload"],Centroids["Bytes Download"],c='red')

    print("\nSHOWING FINAL CLUSTERING PLOT\n")
    plt1.show()

    print("--------------- ITERATION NO. " + str(itr + 1), "COMPLETED ---------------\n")

