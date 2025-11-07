from helpers import filtre_csv
import numpy as np

#rendement journalier
def rt(p1,p2):
    return (p1-p2) / p2

def create_rt_list(price_list):
    n = price_list
    rt_list =[]
    for i in range(0,n-1):
        p = (price_list[i+1] - price_list[i]) / price_list[i]
        rt_list.append(p)
    return rt_list

# moyenne des rendement journaliers
def mean_rt(rt_list):
    sum = 0
    n = len(rt_list)
    for p in rt_list:
        sum += p
    return sum / n


# variance des rendements journaliers 
def standard_deviation(rt_list):
    sum = 0
    n = len(rt_list)
    m = np(rt_list)
    for p in rt_list:
        sum += np.pow(p-m, 2)
    
    
    sd = np.sqrt(sum/ (n-1))
    return sd


    
    
    
        

