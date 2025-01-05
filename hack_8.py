"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def recorrer_lista_alfa(result):
    
    result.reverse()
    x = 0
    count = len(result)
    for i in result:
        result[x]= f"{i}-{count}"
        x+=1
        count-=1
    return result


def recorrer_lista_str(result):
    for i in range(len(result)):
        result[i]= f"{i+1}"
    result.reverse()
    return result



def fn_hack_8(result):
    
    if len(result) <= 2:
       result = recorrer_lista_str(result)
    elif len(result) == 3:
        result = recorrer_lista_alfa(result)
    elif len(result) == 4: 
        result = recorrer_lista_str(result)
    elif len(result) >=5:
        result = recorrer_lista_alfa(result)   
    
    return result
