
import numpy as np
from collections import Counter
from time_lapse import time_time
import matplotlib.pyplot as plt

@time_time
def count_tweets(file):
    '''
            Dictionary method to count words frequency
    Input:
        file : name of the file containing a text
    Output:
        result: a dictionary mapping each word to it frequency
    '''
    data = open(file).read()
    corpus=data.lower().replace('\n', ' ').split(" ")
    
    result = {}

    for word in corpus:

            # if the key exists in the dictionary, increment the count
        if word in result:
            result[word]+=1

            # else, if the key is new, add it to the dictionary and set the count to 1
        else:
            result[word]=1

    return result

@time_time
def counter(file):
    '''
            Counter module method to count words frequency
    Input:
        file : name of the file containing a text
    Output:
        result: a dictionary mapping each word to it frequency
    '''
    data = open(file).read()
    return(Counter(data.split()))


def compare(file):
    method1=count_tweets(file)
    method2=counter(file)
    if method1<method2:
        print ("The method using a dictionnary is faster than the one using the Python's Counter.")
        print("Time for the dictionnary method :",method1,"." )
        print("Time for the Python's Counter method :",method2,"." )
    else: 
        print ("The method using the Python's Counter is faster than the one using a dictionnary.")
        print("Time for the dictionnary method :",method1,"." )
        print("Time for the Python's Counter method :",method2,"." )


if __name__ == "__main__":
    file='shakespeare.txt'
    compare(file)

