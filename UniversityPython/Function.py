def calc_media(*args):
    soma=0
    contador=0
    for numero in args:
        soma+= numero
        contador+= 1
    media = soma / contador
    
    return media
print(calc_media(1))
print(calc_media(1,2))
print(calc_media(1,2,3))
print(calc_media(1,2,3,4,))
print(calc_media(1,2,3,4,5))