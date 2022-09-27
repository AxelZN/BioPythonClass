#0:primero cambié el 0 del url por 238, siguiendo la pista, pero eso te manda a una página donde dice que el 38 está
#arriba del 2, sugiriendo que es una potencia. La siguiente línea de código te da el resultado de dicha operación, el
#cual reemplacé en el url.

print(2**38)

#1:primero intenté hacer las conversiones de la foto con el siguiente código:
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text.replace("k","m").replace("o","q").replace("e","g")
# pero seguía teniendo algo incomprensible. Después de analizar la foto, encontré un patrón usando la pista, que cada
#letra se convertía a la letra dos números después.
#hice la traducción usando un diccionario asignándole valores a cada letra, para luego hacer una cadena con las
#letras respectivas del valor agregado. Esto nos da un mensaje diciendo que lo que acabo de hacer fue muy ineficiente,
#lo cual es cierto.
#aplicando esto a la palabra "map" del url nos da "ocr" que nos lleva al nivel 2
letras = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26,
    " ":30
}
text2 = "g fmnc wms bgblr rpylqjyrc gr zw fylb rfyrq ufyr amknsrcpq ypc dmp bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle sqgle qrpglekyicrpylq gq pcamkkclbcb lmu ynnjw ml rfc spj"
traduccion = []
key_list = list(letras.keys())
val_list = list(letras.values())

for char in text2:
    value = letras.get(char)
    value = value + 2
    if value == 32:
        value = 30
    elif value == 27:
        value = 1
    elif value == 28:
        value = 2
    traduccion.append((key_list[val_list.index(value)]))
cadena = ""
print(cadena.join(traduccion))

#3: el siguiente acertijo dice que el código fuente de la página tiene la respuesta, en dicho código podemos encontrar
#un texto lleno de caracteres, donde hay que encontrar un mensaje secreto, posiblemente siendo palabras ocultas.
#aprovechando que ya tengo un diccionario con todas las letras, voy a recorrer el texto para encontrar cada instancia
# de cada elemento de mi diccionario.

file=open("challenge.txt","r")
leyendo_archivo=file.read()

#http://www.pythonchallenge.com/pc/def/ocr.html
