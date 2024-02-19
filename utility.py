from typing import Dict, List
from collections import defaultdict


    
def top_freq_list(xs, top):
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]

def get_file(file_obj):
    f_name = file_obj.filename    
    file_obj.save(f_name)
    file = open(f_name,'r')
    return f_name

  
def frequent_tuple(tuples):
    count_tuple={}
    for tup in tuples:
        length=len(tup[0].split(" "))
        if length in count_tuple.keys():
            count_tuple[length]+=1
        else:
            count_tuple[length]=1
    sorted_dct=dict(sorted(count_tuple.items(), reverse=True,key=lambda item: item[1]))
    return next(iter( sorted_dct.items() ))[0] 
    
    

def identyfy_maxs_index(x,bar): 
    return x > bar





