#m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
m = [[1,2,3],[4,5,6],[7,8,9]]
limite_columna = 3
limite_fila = 3
tope = limite_columna*limite_fila
x=0
fila = 0
columna = 0
while(x < tope):
    for i in range(limite_fila):
        print(m[fila][i+columna])
        x+=1
    for i in range(limite_columna-1):
        print(m[i+fila+1][limite_columna-1+columna])
        x+=1
    for i in range(limite_fila-1):
        print(m[limite_fila-1+fila][limite_columna-2-i+columna])
        x+=1
    for i in range(limite_columna-2):
        print(m[limite_fila-2-i][columna])
        x+=1
    limite_columna-=2
    limite_fila-=2
    fila+=1
    columna+=1
    
