"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(result):
    
    result ={k.capitalize() if k == "foo" else k: (v.capitalize()).replace("ook","oo") for k,v in result.items()}
    result.pop("bar")
    
    return result
