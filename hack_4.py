"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    
    result = s
    fristlast = ["f","b","n"]
    _ls = []

    for texto in result:
        if texto not in fristlast:
            _ls.append(texto)

    result = "".join(_ls)
    
    return result
