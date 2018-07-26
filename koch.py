############################
#Fractals
#The idea of this project is to learn how to plot some fractals, using their iterative definitions
#In this first part, we will work with the Koch's snowflake



############################
#####Koch's snowflake#######
############################

import numpy as np
import matplotlib.pyplot as plt



#The first question is what kind of object will the fractal be.
#In this case, since each step of the construction is made out of 1-dimensional lines
#we will construct each step by listing the set of vertices of the fractal and joining
#them with straight lines.

#Then, the function that takes two points and constructs three additional points in the middle 
#of the segment will be the essential function of the script.
#We implement the function in a vectorized form


#The input of the function will be a pair of two dimensional vectors
#The output will be five vectors, corresponding to the vertices of the 
#new triangle

def third(a,b):
    #Rotation matrix to compute normal vectors:
    R = np.array([[0,-1],[1,0]])
    x = np.array(a)
    y = np.array(b)
    #Now we compute the new pairs of lines
    return [x,((2/3)*x+(1/3)*y),(x+y)/2+ (np.sqrt(3)/6)*R.dot(y-x),((1/3)*x+(2/3)*y),y]


#Sanity check
#print(third([0,0],[1,0]))


#Define a function that takes a list of pairs of points and returns two vectors containing
#all the x coordinates and the y coordinates of the vectors of the list

def conver(L):
    xCoord = []
    yCoord = []
    for i in range(len(L)):
        xCoord.append(L[i][0])
        yCoord.append(L[i][1])
    return [xCoord,yCoord]

#Note that the above function returns a list of two vectors
#Below, plot wants to receive each vector, not the list

#Sanity check
#print(convers([[1,7],[2,8],[3,9]]))
#print(conver(third([0,0],[1,0]))[0],conver(third([0,0],[1,0]))[1])
#plt.plot(conver(third([0,0],[1,0]))[0],conver(third([0,0],[1,0]))[1])


#Now we define the iterative process

def koch(n):
    L = [[0,0],[3,0]]
    for i in range(0,n):
        K = []
        l = len(L)
        for s in range(0,l-1):
            t = third(L[s],L[s+1])
            del t[-1]
            K = K + t
        K.append([3,0])
        L = K
    plt.xlim(0, 3)
    plt.ylim(0, 3)
    plt.axis('equal')
    plt.plot(conver(L)[0],conver(L)[1])



#Now we can see the result
koch(3)


#We can adapt this to plot the whole snowflake


def flake(n):
    L = [[0,0],[3,0],[1.5,-3*np.sqrt(3)/2],[0,0]]
    for i in range(0,n):
        K = []
        l = len(L)
        for s in range(0,l-1):
            t = third(L[s],L[s+1])
            del t[-1]
            K = K + t
        K.append([0,0])
        L = K
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.axis('equal')
    plt.plot(conver(L)[0],conver(L)[1])


#flake(4)


