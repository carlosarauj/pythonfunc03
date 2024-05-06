def maior_num(lista):
    lista.sort()
    lista.reverse()
    maior_num = lista[0]
    return maior_num

res = maior_num([143342,321453,675846, 32424,375463,352,57475,235])

print(res)


#usa o terminal com: python nomedoarquivo.py