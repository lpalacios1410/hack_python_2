"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    
    result = s
    nueva_cadena = []

    txt_ls = [result[i:i+3] for i in range(0, len(result), 3)]

    for txt in txt_ls:
       if len(txt) % 2 != 0:
          content = f"{txt[0]}{txt[1].upper()}{txt[2]}"
          nueva_cadena.append(content)
       else:
          nueva_cadena.append(txt)    
    result = "".join(nueva_cadena)
    
    return result