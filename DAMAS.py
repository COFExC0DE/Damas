from tkinter import *
import sys
import random
import tkinter.messagebox as mbox

matriz_juego=[[1,'a',50,20,'red','green'],[1,'b',100,20,'black',''],[1,'c',150,20,'red','green'],[1,'d',200,20,'black',''],[1,'e',250,20,'red','green'],[1,'f',300,20,'black',''],[1,'g',350,20,'red','green'],[1,'h',400,20,'black',''],
              [2,'a',50,70,'black',''],[2,'b',100,70,'red','green'],[2,'c',150,70,'black',''],[2,'d',200,70,'red','green'],[2,'e',250,70,'black',''],[2,'f',300,70,'red','green'],[2,'g',350,70,'black',''],[2,'h',400,70,'red','green'],
              [3,'a',50,120,'red','green'], [3,'b',100,120,'black',''],[3,'c',150,120,'red','green'],[3,'d',200,120,'black',''],[3,'e',250,120,'red','green'],[3,'f',300,120,'black',''],[3,'g',350,120,'red','green'],[3,'h',400,120,'black',''],
              [4,'a',50,170,'black',''],[4,'b',100,170,'red',''],[4,'c',150,170,'black',''],[4,'d',200,170,'red',''],[4,'e',250,170,'black',''],[4,'f',300,170,'red',''],[4,'g',350,170,'black',''],[4,'h',400,170,'red',''],
              [5,'a',50,220,'red',''], [5,'b',100,220,'black',''],[5,'c',150,220,'red',''],[5,'d',200,220,'black',''],[5,'e',250,220,'red',''],[5,'f',300,220,'black',''],[5,'g',350,220,'red',''],[5,'h',400,220,'black',''],
              [6,'a',50,270,'black',''],[6,'b',100,270,'red','blue'],[6,'c',150,270,'black',''],[6,'d',200,270,'red','blue'],[6,'e',250,270,'black',''],[6,'f',300,270,'red','blue'],[6,'g',350,270,'black',''],[6,'h',400,270,'red','blue'],
              [7,'a',50,320,'red','blue'], [7,'b',100,320,'black',''],[7,'c',150,320,'red','blue'],[7,'d',200,320,'black',''],[7,'e',250,320,'red','blue'],[7,'f',300,320,'black',''],[7,'g',350,320,'red','blue'],[7,'h',400,320,'black',''],
              [8,'a',50,370,'black',''],[8,'b',100,370,'red','blue'],[8,'c',150,370,'black',''],[8,'d',200,370,'red','blue'],[8,'e',250,370,'black',''],[8,'f',300,370,'red','blue'],[8,'g',350,370,'black',''],[8,'h',400,370,'red','blue']]

class Tablero:
    def __init__(self,canvas,x1,y1,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(50, 50, 0, 0, outline = color, fill = color)
        self.canvas.move(self.id, x1, y1)
        
class Piezas:
    def __init__(self,canvas,x1,y1,color):
        self.canvas = canvas
        self.id = canvas.create_oval(50, 50, 0, 0, outline = color, fill = color)
        self.canvas.move(self.id, x1, y1)
        
class Letras:
    def __init__(self,canvas,x1,y1,letra):
        self.canvas = canvas
        self.id = canvas.create_text(x1,y1,fill="darkblue",font="Times 30 italic bold",text=letra)
        self.canvas.move(self.id, x1, y1)
        
def empezar_juego(quiere_jugar):#arma el tablero y empieza el juego
    if  quiere_jugar == "YES":
        crear_tablero(matriz_juego)
        ordenar_piezas(matriz_juego)
        crear_caracteres()
    elif quiere_jugar =='NO':
        canvas.delete("all")
        canvas.create_text(200,90,fill="darkblue",font="Times 30 italic bold",text="NO \n QUIERE JUGAR :(")
        
def crear_caracteres():#Pone las letras de los rangos del tablero
    Letras(canvas,15,20,'1')
    Letras(canvas,15,47,'2')
    Letras(canvas,15,73,'3')
    Letras(canvas,15,98,'4')
    Letras(canvas,15,123,'5')
    Letras(canvas,15,148,'6')
    Letras(canvas,15,176,'7')
    Letras(canvas,15,200,'8')
    Letras(canvas,38,220,'a')
    Letras(canvas,62,220,'b')
    Letras(canvas,88,220,'c')
    Letras(canvas,109,220,'d')
    Letras(canvas,138,220,'e')
    Letras(canvas,162,220,'f')
    Letras(canvas,188,220,'g')
    Letras(canvas,210,220,'h')

def mover_piezas2(num1,letra1,num2,letra2):#movimientos PC
    boo = movimiento_proivido(num2,letra2,matriz_juego)
    boo2 = cantidad_espacios(num1,num2)
    if boo==True:
        if boo2==True:
            new = comer_pieza(matriz_juego,num1,letra1,num2,letra2)
            movimiento = aux_mover_piezas(num1,letra1,num2,letra2,new)
            canvas.delete("all")
            empezar_juego("YES")
            crear_caracteres()
            marcador_ficha(movimiento)
            ordenar_piezas(movimiento)
        elif boo2==False:
            new = matriz_juego
            movimiento = aux_mover_piezas(num1,letra1,num2,letra2,new)
            canvas.delete("all")
            empezar_juego("YES")
            crear_caracteres()
            marcador_ficha(movimiento)
            ordenar_piezas(movimiento)
        else:
            canvas.delete("all")
            empezar_juego("YES")
            crear_caracteres()
            marcador_ficha(matriz_juego)
            ordenar_piezas(matriz_juego)
            
def mover_piezas(num1,letra1,num2,letra2):#Movimientos humano
    boo = movimiento_proivido(num2,letra2,matriz_juego)
    boo2 = cantidad_espacios(num1,num2)
    if boo==True:
        if boo2==True:
            new = comer_pieza(matriz_juego,num1,letra1,num2,letra2)
            movimiento = aux_mover_piezas(num1,letra1,num2,letra2,new)
            canvas.delete("all")
            empezar_juego("YES")
            crear_caracteres()
            marcador_ficha(movimiento)
            ordenar_piezas(movimiento)
            jugar_inteligente(movimiento)
        elif boo2==False:
            new = matriz_juego
            movimiento = aux_mover_piezas(num1,letra1,num2,letra2,new)
            canvas.delete("all")
            empezar_juego("YES")
            crear_caracteres()
            marcador_ficha(movimiento)
            ordenar_piezas(movimiento)
            jugar_inteligente(movimiento)
        else:
            canvas.delete("all")
            empezar_juego("YES")
            crear_caracteres()
            marcador_ficha(matriz_juego)
            ordenar_piezas(matriz_juego)

def crear_tablero(matriz):#Crea el Tablero
    i=0
    num=0
    while i <len(matriz):
        w=0
        while w < len(matriz[i])-4:
            tabla = Tablero(canvas,matriz[i][w+2],matriz[i][w+3],matriz[i][w+4])
            w+=2    
        i+=1
            
def marcador_ficha(matriz_juego):#lleva el marcador del juego y dice quien gana
    i=0
    marcador_verde=0
    marcador_azul=0
    while i <len(matriz_juego):
        if matriz_juego[i][5] == 'green':
            marcador_verde+=1
        if matriz_juego[i][5] == 'blue':
            marcador_azul+=1    
        i+=1
    if marcador_verde > 0 and marcador_azul > 0:
        Letras(canvas,110,250,'Marcador Verde ='+str(marcador_verde))
        Letras(canvas,110,270,'Marcador Azul ='+str(marcador_azul))
    else:
        if marcador_verde == 1 and marcador_verde<marcador_azul:
            Letras(canvas,110,270,'Game Over'+'\n'+'Ganador Azul')
        if marcador_azul == 1 and marcador_verde>marcador_azul:
            Letras(canvas,110,250,'Game Over'+'\n'+'Ganador Verde')
        if matriz_juego[0][5]=='azul' and matriz_juego[2][5]=='azul' and matriz_juego[4][5]=='azul' and matriz_juego[6][5]=='azul':
            Letras(canvas,110,270,'Game Over'+'\n'+'Ganador Azul')
        if matriz_juego[58][5]=='green' and matriz_juego[60][5]=='green' and matriz_juego[62][5]=='green' and matriz_juego[64][5]=='green':
            Letras(canvas,110,250,'Game Over'+'\n'+'Ganador Verde')
        if marcador_verde>marcador_azul:
           Letras(canvas,110,250,'Game Over'+'\n'+'Ganador Verde')
        elif marcador_verde<marcador_azul:
           Letras(canvas,110,270,'Game Over'+'\n'+'Ganador Azul')

def aux_mover_piezas(num1,letra1,num2,letra2,matriz_juego):#Mover piezas tanto para pc como para humano   
    i=0
    color=''
    while i <len(matriz_juego):
        w=0
        while w < len(matriz_juego[i])-3:
            if matriz_juego[i][w] == int(num1) and matriz_juego[i][w+1]==letra1:
                color = matriz_juego[i][w+5]
                matriz_juego[i][w+5]=''
            if matriz_juego[i][w] == int(num2) and matriz_juego[i][w+1]==letra2:
                if color == 'green':
                    matriz_juego[i][w+5]+='green'
                else:
                    matriz_juego[i][w+5]+='blue'
            w+=3    
        i+=1

    return matriz_juego
           
def cantidad_espacios(num1,num2):#Movimientos vaidos de piezas
    if str(int(num1)+1)==num2 or str(int(num2)+1)==num1:
        return False
    if str(int(num1)+2)==num2 or str(int(num2)+2)==num1:
        return True

def movimiento_proivido(num2,letra2,matriz_juego):#Mas movimientos invalidos
    i=0
    num=0
    while i < len(matriz_juego):
        w=0
        while w < len(matriz_juego[i])-4:
            if matriz_juego[i][w] == int(num2) and matriz_juego[i][w+1]==letra2:
                if matriz_juego[i][w+4] == 'black' or matriz_juego[i][w+5]=='green'or matriz_juego[i][w+5]=='blue':
                    return False
                else:
                    return  True
            w+=2    
        i+=1 
  
def ordenar_piezas(matriz_juego):#arma de nuevo tablero con las piezas en orden
    i=0
    while i <len(matriz_juego):
        w=0
        while w < len(matriz_juego[i])-3:
            pieza = Piezas(canvas,matriz_juego[i][w+2],matriz_juego[i][w+3],matriz_juego[i][w+5])
            w+=3    
        i+=1   

def comer_pieza(matriz_juego,num1,letra1,num2,letra2):#llama y ordena todas las funciones que hace q coma las fichas
    movimiento_proivido(num2,letra2,matriz_juego)
    numero = encontrar_pieza_Acomer(matriz_juego,num1,letra1,num2,letra2)
    color = saber_color(matriz_juego,num1,letra1,num2,letra2)
    comio=quitar_pieza(numero,matriz_juego,num1,letra1,num2,letra2,color)
    return comio

def encontrar_pieza_Acomer(matriz_juego,num1,letra1,num2,letra2):#encuentra la pieza q se puede comer
    num=0
    boo=False
    i=0
    while i < len(matriz_juego):
        w=0
        while w < len(matriz_juego[i])-4:
            if num1>num2:
                if matriz_juego[i][w] == int(num2) and matriz_juego[i][w+1]==letra2 or boo == True:
                        boo=True
                        num += 1
                if matriz_juego[i][w] == int(num1) and matriz_juego[i][w+1]==letra1:
                        boo = False            
            if num1<num2:    
                if matriz_juego[i][w] == int(num1) and matriz_juego[i][w+1]==letra1 or boo == True:
                        boo=True
                        num += 1
                if matriz_juego[i][w] == int(num2) and matriz_juego[i][w+1]==letra2:
                        boo = False
            w+=2    
        i+=1
    return int(num/2)+1

def saber_color(matriz_juego,num1,letra1,num2,letra2):#sabe el color de la pieza q se va a mover y cambia el color a la casilla a donde se mueve
    color=''
    i=0
    while i < len(matriz_juego):
        w=0
        while w < len(matriz_juego[i])-4:
            if num1>num2:
                if matriz_juego[i][w] == int(num1) and matriz_juego[i][w+1]==letra1:
                    color = matriz_juego[i][w+5]                                     
            if num1<num2:    
                if matriz_juego[i][w] == int(num2) and matriz_juego[i][w+1]==letra2:
                    color = matriz_juego[i][w+5]
            w+=2    
        i+=1
    return color

def quitar_pieza(numero,matriz_juego,num1,letra1,num2,letra2,color): #quita la pieza q comio sea verde o azul   
    num=0
    boo=False
    i=0
    while i < len(matriz_juego):
        w=0
        while w < len(matriz_juego[i])-4:
            if num1>num2:
                if matriz_juego[i][w] == int(num2) and matriz_juego[i][w+1]==letra2 or boo==True:
                    boo=True
                    num += 1
                if num==numero and boo==True and color != matriz_juego[i][w+5]:
                    boo=False
                    matriz_juego[i][w+5]=''                    
            if num1<num2:    
                if matriz_juego[i][w] == int(num1) and matriz_juego[i][w+1]==letra1 or boo==True:
                    boo=True
                    num += 1
                if num==numero and boo==True and color != matriz_juego[i][w+5]:
                    boo=False
                    matriz_juego[i][w+5]='' 
            w+=2    
        i+=1
    return matriz_juego

def jugar_inteligente(movimiento):#llama a todas las funciones, para hacer los movimientos inteligentes.
    comer=[]
    comer = comer_verdesPC(movimiento)
    if comer ==[]:
        lista1 = loPueden_comerLosVerdes(movimiento)
        lista2 = espaciosVacios_azules(movimiento)
        result1 =verDondeNo_moverPC(lista1,lista2)
        result2 = verDondeMover_pc(result1,lista2)
        result3 = verDondeMover_pc2(result2,movimiento,lista1)
        mover_piezas2(str(result3[0][0]),str(result3[0][1]),str(result2[0][0]),str(result2[0][1]))
    else:
        mover_piezas2(str(comer[0][0]),str(comer[0][1]),str(comer[1][0]),str(comer[1][1]))
        
def loPueden_comerLosVerdes(matriz_juego):#Determina donde los verdes pueden comer a los azules
    num=0
    new_lista=[]
    i=0
    while i < len(matriz_juego):
        w=0
        while w < len(matriz_juego[i])-4:
            if i<57:
                if matriz_juego[i][w+5]=='green' and matriz_juego[i+7][w+5]=='' and matriz_juego[i+9][w+5]==''and matriz_juego[i+7][w+4]!='black' and matriz_juego[i+9][w+4]!='black':
                    new_lista+=[[matriz_juego[i+7][w],matriz_juego[i+7][w+1]],[matriz_juego[i+9][w],matriz_juego[i+9][w+1]]]
                elif matriz_juego[i][w+5]=='green' and matriz_juego[i+7][w+5]==''and matriz_juego[i+7][w+4]!='black' and matriz_juego[i+9][w+4]!='black':
                    new_lista+=[[matriz_juego[i+7][w],matriz_juego[i+7][w+1]]]
                elif matriz_juego[i][w+5]=='green' and matriz_juego[i+9][w+5]==''and matriz_juego[i+7][w+4]!='black' and matriz_juego[i+9][w+4]!='black':    
                    new_lista+=[[matriz_juego[i+9][w],matriz_juego[i+9][w+1]]]     
            w+=2    
        i+=1
    return new_lista

def espaciosVacios_azules(matriz_juego):#determina donde los azules no lo pueden comer los verdes
    i=0
    new_lista=[]
    while i < len(matriz_juego):
        w=0
        while w < len(matriz_juego[i])-4:
            if i>8:
                if matriz_juego[i][w+5]=='blue' and matriz_juego[i-7][w+5]=='' and matriz_juego[i-9][w+5]=='' and matriz_juego[i-7][w+4]!='black' and matriz_juego[i-9][w+4]!='black':
                    new_lista+=[[matriz_juego[i-7][w],matriz_juego[i-7][w+1]],[matriz_juego[i-9][w],matriz_juego[i-9][w+1]]]
                elif matriz_juego[i][w+5]=='blue' and matriz_juego[i-7][w+5]=='' and matriz_juego[i-7][w+4]!='black' and matriz_juego[i-9][w+4]!='black':
                    new_lista+=[[matriz_juego[i-7][w],matriz_juego[i-7][w+1]]]
                elif matriz_juego[i][w+5]=='blue' and matriz_juego[i-9][w+5]=='' and matriz_juego[i-7][w+4]!='black' and matriz_juego[i-9][w+4]!='black':
                    new_lista+=[[matriz_juego[i-9][w],matriz_juego[i-9][w+1]]]
            w+=2    
        i+=1
    return new_lista
def verDondeNo_moverPC(lista1,lista2):#valida loPueden_comerLosVerdes con espaciosVacios_azules, y guarda la o las concidencias en la matriz
    i=0
    new_lista=[]
    while i < len(lista1):
        if (lista1[i] in lista2)==True :
            new_lista+= [lista1[i]]
        i+=1
    return new_lista

def verDondeMover_pc(lista1,lista2):#valida verDondeNo_moverPC con espaciosVacios_azules, para determinar el mejor movimiento
    i=0
    j=0
    new_lista=[]    
    while j < len(lista2):
        if (lista2[j] in lista1)==False :
            new_lista+= [lista2[j]]
        j+=1
    if new_lista != []:
        return random.sample(new_lista,1)
    else:
        return random.sample(lista1,1)
    
def verDondeMover_pc2(result,matriz_juego,lista1):#Realiza la movida inteligente de la pieza azul
    i=0
    new_lista=[]
    respuesta = []
    while i < len(matriz_juego):
        w=0
        while w < len(matriz_juego[i])-4:
            if matriz_juego[i][w]==result[0][0] and matriz_juego[i][w+1]==result[0][1]:
                if matriz_juego[i+7][w+5]=='blue':
                    new_lista = [[matriz_juego[i+7][w],matriz_juego[i+7][w+1]]] 
                elif matriz_juego[i+9][w+5]=='blue':
                    new_lista = [[matriz_juego[i+9][w],matriz_juego[i+9][w+1]]]
            w+=2    
        i+=1
    if new_lista != []:
        return new_lista    
    else:
        respuesta = random.sample(lista1,1)
        if (respuesta in result)==True:
            return random.sample(lista1,1)
        return respuesta
    
def comer_verdesPC(matriz_juego):#Valida si la pieza o ficha azul puede comer a la verde y regresa a cual va a comer
    i=0
    new_lista=[]
    respuesta = []
    while i < len(matriz_juego):
        w=0
        while w < len(matriz_juego[i])-4:
            if matriz_juego[i][w+5]=='blue' and matriz_juego[i-7][w+5]=='green' and matriz_juego[i-14][w+5]=='' and matriz_juego[i-7][w+4]!='black' and matriz_juego[i-14][w+4]!='black':
                new_lista=[[matriz_juego[i][w],matriz_juego[i][w+1]],[matriz_juego[i-14][w],matriz_juego[i-14][w+1]]]
            elif matriz_juego[i][w+5]=='blue' and matriz_juego[i-9][w+5]=='green' and matriz_juego[i-18][w+5]=='' and matriz_juego[i-9][w+4]!='black' and matriz_juego[i-18][w+4]!='black':
                new_lista=[[matriz_juego[i][w],matriz_juego[i][w+1]],[matriz_juego[i-18][w],matriz_juego[i-18][w+1]]]
            w+=2    
        i+=1
    return new_lista
#botones y espacio de texto para jugar
def button():
    quiere_jugar = text1.get()
    mbox.showinfo('DAMAS','EMPIEZA HUMANO CON LAS FICHAS VERDES')
    mlabel2 = empezar_juego(quiere_jugar)
def button2():
    num1 = text2.get()
    letra1 = text3.get()
    num2 = text4.get()
    letra2 = text5.get()
    mlabel2 = mover_piezas(num1,letra1,num2,letra2)
    

root = Tk()
text1 =StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
text5 = StringVar()
root.geometry("600x800")#tama;o de la ventana
root.title("Damas")#nombre de la ventana
#BOTON 1
label = Label(root,text='Desea empezar el juego?(YES,NO)').pack()#Mensaje en ventana
entry = Entry(root,textvariable=text1).pack()#espacio para escribir texto
button = Button(root,text='Jugar',command = button ,fg = 'white',bg='black').pack()
#BOTON 2
label = Label(root,text='Ingrese cordenadas de la pieza a mover').pack()#Mensaje en ventana
entry = Entry(root,textvariable=text2).pack()#espacio para escribir texto
entry = Entry(root,textvariable=text3).pack()#espacio para escribir texto
label = Label(root,text='Ingrese cordenadas donde desea mover la pieza').pack()#Mensaje en ventana
entry = Entry(root,textvariable=text4).pack()#espacio para escribir texto
entry = Entry(root,textvariable=text5).pack()#espacio para escribir texto
button2 = Button(root,text='Mover',command = button2 ,fg = 'white',bg='black').pack()
canvas = Canvas(root, width=600, height=800, bd=0, highlightthickness=0)#canvas, para crear los margenes de la ventana
canvas.pack()
root.update()
mainloop()        
