import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image
from tkinter import filedialog
from PIL import Image,ImageTk
import random
import time
import pygame

import time
import pygame
ventana=Tk()
ventana.geometry("900x800")
ventana.resizable(0,0)
ventana.title("Lógica")
blanco=PhotoImage(file="imagenes_programa/blanca.png")
Fondo_Juego=PhotoImage(file="imagenes_programa/Group 1.png")
#--------------------------------Variables globales------------------------------------
Pistas=[["Mejor amigo(a)","Novio(a)","Vecino(a)","El mensajero","El extraño","Hermanastro(a)","Colega de trabajo"],
            ["Pistola","Cuchillo","Machete","Pala","Bate","Botella","Tubo","Cuerda"],
            ["Venganza","Celos","Dinero","Accidente","Drogas","Robo"],
            ["Cabeza","Pecho","Abdomen","Espalda","Piernas","Brazos"],
            ["Sala","Comedor","Baño","Terraza","Cuarto","Garaje","Patio","Balcón","Cocina"]]

Pistas_Fuerza_Bruta=[["Mejor amigo(a)","Novio(a)","Vecino(a)","El mensajero","El extraño","Hermanastro(a)","Colega de trabajo"],
            ["Pistola","Cuchillo","Machete","Pala","Bate","Botella","Tubo","Cuerda"],
            ["Venganza","Celos","Dinero","Accidente","Drogas","Robo"],
            ["Cabeza","Pecho","Abdomen","Espalda","Piernas","Brazos"],
            ["Sala","Comedor","Baño","Terraza","Cuarto","Garaje","Patio","Balcón","Cocina"]]

Pistas_Backtracking=[["Mejor amigo(a)","Novio(a)","Vecino(a)","El mensajero","El extraño","Hermanastro(a)","Colega de trabajo"],
            ["Pistola","Cuchillo","Machete","Pala","Bate","Botella","Tubo","Cuerda"],
            ["Venganza","Celos","Dinero","Accidente","Drogas","Robo"],
            ["Cabeza","Pecho","Abdomen","Espalda","Piernas","Brazos"],
            ["Sala","Comedor","Baño","Terraza","Cuarto","Garaje","Patio","Balcón","Cocina"]]
Cantidad_Restricciones= 0
Intentos_Fuerza_Bruta=0
Intentos_Backracking=0
Restricciones_Cartas=[]
Sugerencia_Fuerza_Bruta=None
Sugerencia_Backtracking=None
Fin_BT=False
Fin_FB=False
Pista_Actual_BT=None
Pista_Actual_FB=None
#Solución aleatoria
Asesino=Pistas[0][random.randint(0, 6)]
Arma=Pistas[1][random.randint(0, 7)]
Motivo=Pistas[2][random.randint(0, 5)]
ParteCuerpo=Pistas[3][random.randint(0, 5)]
Lugar=Pistas[4][random.randint(0, 8)]
#Lista_Solucion
Solucion=[Asesino,Arma,Motivo,ParteCuerpo,Lugar]
    
def Iniciar_Variables():
    global Pistas_Fuerza_Bruta,Pistas_Backtracking,Cantidad_Restricciones,Intentos_Fuerza_Bruta,Intentos_Backracking,Restricciones_Cartas,Sugerencia_Fuerza_Bruta,Sugerencia_Backtracking, Fin_BT,Fin_FB, Pista_Actual_BT,Pista_Actual_FB,Asesino,Arma,Motivo,ParteCuerpo,Lugar
    #Lista_Solucion
    Solucion=[Asesino,Arma,Motivo,ParteCuerpo,Lugar]
    Pistas_Fuerza_Bruta=[["Mejor amigo(a)","Novio(a)","Vecino(a)","El mensajero","El extraño","Hermanastro(a)","Colega de trabajo"],
            ["Pistola","Cuchillo","Machete","Pala","Bate","Botella","Tubo","Cuerda"],
            ["Venganza","Celos","Dinero","Accidente","Drogas","Robo"],
            ["Cabeza","Pecho","Abdomen","Espalda","Piernas","Brazos"],
            ["Sala","Comedor","Baño","Terraza","Cuarto","Garaje","Patio","Balcón","Cocina"]]

    Pistas_Backtracking=[["Mejor amigo(a)","Novio(a)","Vecino(a)","El mensajero","El extraño","Hermanastro(a)","Colega de trabajo"],
            ["Pistola","Cuchillo","Machete","Pala","Bate","Botella","Tubo","Cuerda"],
            ["Venganza","Celos","Dinero","Accidente","Drogas","Robo"],
            ["Cabeza","Pecho","Abdomen","Espalda","Piernas","Brazos"],
            ["Sala","Comedor","Baño","Terraza","Cuarto","Garaje","Patio","Balcón","Cocina"]]
    Cantidad_Restricciones= 0
    Intentos_Fuerza_Bruta=0
    Intentos_Backracking=0
    Restricciones_Cartas=[]
    Sugerencia_Fuerza_Bruta=None
    Sugerencia_Backtracking=None
    Fin_BT=False
    Fin_FB=False
    Pista_Actual_BT=None
    Pista_Actual_FB=None
    #Solución aleatoria
    Asesino=Pistas[0][random.randint(0, 6)]
    Arma=Pistas[1][random.randint(0, 7)]
    Motivo=Pistas[2][random.randint(0, 5)]
    ParteCuerpo=Pistas[3][random.randint(0, 5)]
    Lugar=Pistas[4][random.randint(0, 8)]
    #Lista_Solucion
    Solucion=[Asesino,Arma,Motivo,ParteCuerpo,Lugar]


#E:recibe la cancion
#S:retorna la cancion escogida 
#R:debe recibir la cancion en string
#O:reproducir cancion 
def play(cancion):
    pygame.mixer.init()
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(-1)
    
#E:-----
#S:Gráfica
#R:----.
#O:Representar la primera pantalla del juego 
def inicio():
    global ventana
    Fondo=Label(ventana,image=blanco).place(x=0,y=0)
    contenedor=crearframe()
    contenedor.config(bg="white")
    contenedor.place(x=170,y=200)
    titulo=Label(contenedor,text="Juego de Lógica",bg="white",fg="#e03f3f",font=("Bradley Hand ITC",60))
    titulo.grid(row=0,column=0)
    #boton informacion del programa
    img_info=PhotoImage(file="imagenes_programa/info.png")
    btn_info=Button(ventana,bd=0,activebackground="white",bg="white",cursor="hand2",image=img_info,\
                    command=lambda:info())
    btn_info.place(x=10,y=625)
    #Boton que inicia el juego
    img_jugar=PhotoImage(file="imagenes_programa/jugar.png")
    btn_jugar=Button(contenedor,bd=0,activebackground="white",bg="white",cursor="hand2",image=img_jugar,\
                     command=lambda:(contenedor.destroy(),ventana_Restricciones()))
    btn_jugar.grid(row=2,column=0,padx=(180))
    ventana.mainloop()

#E:-----
#S:Gráfica
#R:----.
#O: Obtener la cantidad de soluciones que va a tener el sistema par aresolver el problema 
def ventana_Restricciones():
    global Catidad_Restricciones, ventana
    Iniciar_Variables()
    ventana.title("Restricciones")
    ventana.geometry("900x800")
    Fondo=Label(ventana,image=blanco).place(x=0,y=0)
    contenedor=crearframe()
    contenedor.config(bg="white")
    contenedor.place(x=210,y=200)
    label_3=Label(contenedor,bg="white",text="abcdef",fg="white",font=("Bradley Hand ITC",20))
    label_3.grid(row=0,column=0)
    label_1=Label(contenedor,bg="white",text="abcdef",fg="white",font=("Bradley Hand ITC",20))
    label_1.grid(row=1,column=1)
    label_2=Label(contenedor,bg="white",text="abcdef",fg="white",font=("Bradley Hand ITC",20))
    label_2.grid(row=2,column=2)
    label_4=Label(contenedor,bg="white",text="abcdef",fg="white",font=("Bradley Hand ITC",20))
    label_4.grid(row=3,column=3)
    label_5=Label(contenedor,bg="white",text="abcdef",fg="white",font=("Bradley Hand ITC",20))
    label_5.grid(row=4,column=4)
    label_6=Label(contenedor,bg="white",text="abcdef",fg="white",font=("Bradley Hand ITC",20))
    label_6.grid(row=5,column=5)
    label=Label(contenedor,bg="white",text="abcdef",fg="white",font=("Bradley Hand ITC",20))
    label.grid(row=6,column=6)  
    #texto de la ventana
    label_resticciones=Label(contenedor,text="DIGITE LA CANTIDAD DE \n RESTRICCIONES",bg="white",fg="#e03f3f",font=("Bradley Hand ITC",24))
    label_resticciones.place(x=90,y=15)
    #Restricciones
    restricciones=Entry(contenedor,width=18,bg="#f6dfba")
    restricciones.place(x=200,y=120)
    restricciones.focus_force()
    #boton de volver
    img_volver=PhotoImage(file="imagenes_programa/atras.png")
    btn_volver=Button(contenedor,bd=0,activebackground="white",bg="white",cursor="hand2",image=img_volver,\
                      command=lambda:(contenedor.destroy(),inicio()))
    btn_volver.place(x=10,y=150)
    #boton de siguiente
    img_sigue=PhotoImage(file="imagenes_programa/sigue.png")
    btn_inicia=Button(contenedor,bd=0,image=img_sigue,activebackground="white",bg="white",cursor="hand2",\
                          command=lambda:(comienzo_Juego(contenedor,restricciones.get())))
    btn_inicia.place(x=415,y=150)
    ventana.mainloop()


#E:-----
#S:Gráfica
#R:----.
#O:Representar la primera pantalla del juego 
def ventana_Juego():
    global ventana, Intentos_Fuerza_Bruta, Intentos_Backracking,Asesino, Arma, Motivo, ParteCuerpo, Lugar, Fondo_Juego, Cantidad_Restricciones,Pista_Actual_BT,Pista_Actual_FB
    ventana.geometry("1350x800")
    Fondo=Label(ventana,image=Fondo_Juego).place(x=0,y=0)
    #-----------------------------Intentos-------------------------------------
    label_intentos_fb=Label(ventana,text=str(Intentos_Fuerza_Bruta),bg="#C8B013",fg="Black",font=("Bradley Hand ITC",24))
    label_intentos_fb.place(x=1050,y=30)

    label_intentos_BT=Label(ventana,text=str(Intentos_Backracking),bg="#C8B013",fg="Black",font=("Bradley Hand ITC",24))
    label_intentos_BT.place(x=1050,y=85)

    label_Restrcciones=Label(ventana,text=str(Cantidad_Restricciones),bg="#C8B013",fg="Black",font=("Bradley Hand ITC",24))
    label_Restrcciones.place(x=1080,y=155)

    label_Pista_BT=Label(ventana,text=Pista_Actual_BT,bg="#C8B013",fg="Black",font=("Bradley Hand ITC",24))
    label_Pista_BT.place(x=1130,y=280)

    label_Pista_FB=Label(ventana,text=Pista_Actual_FB,bg="#C8B013",fg="Black",font=("Bradley Hand ITC",24))
    label_Pista_FB.place(x=1130,y=215)
    #-----------------------------imagenes fuerza bruta---------------------------------
    
    imagen1= PhotoImage(file="Cartas/cartas sospechosos/"+Sugerencia_Fuerza_Bruta[0]+".png")
    lbl_imagen1= Label(ventana,image=imagen1).place(x=150,y=50)

    imagen2= PhotoImage(file="Cartas/cartas armas/"+Sugerencia_Fuerza_Bruta[1]+".png")
    lbl_imagen2= Label(ventana,image=imagen2).place(x=260,y=50)
    
    imagen3= PhotoImage(file="Cartas/cartas motivo/"+Sugerencia_Fuerza_Bruta[2]+".png")
    lbl_imagen3= Label(ventana,image=imagen3).place(x=370,y=50)
    
    imagen4= PhotoImage(file="Cartas/cartas parte del cuerpo/"+Sugerencia_Fuerza_Bruta[3]+".png")
    lbl_imagen4= Label(ventana,image=imagen4).place(x=480,y=50)
    
    imagen5= PhotoImage(file="Cartas/cartas lugar/"+Sugerencia_Fuerza_Bruta[4]+".png")
    lbl_imagen5= Label(ventana,image=imagen5).place(x=590,y=50)

    #-----------------------------imagenes backtracking------------------------------
    
    imagen6= PhotoImage(file="Cartas/cartas sospechosos/"+Sugerencia_Backtracking[0]+".png")
    lbl_imagen6= Label(ventana,image=imagen6).place(x=150,y=250)

    imagen7= PhotoImage(file="Cartas/cartas armas/"+Sugerencia_Backtracking[1]+".png")
    lbl_imagen7= Label(ventana,image=imagen7).place(x=260,y=250)
    
    imagen8= PhotoImage(file="Cartas/cartas motivo/"+Sugerencia_Backtracking[2]+".png")
    lbl_imagen8= Label(ventana,image=imagen8).place(x=370,y=250)
    
    imagen9= PhotoImage(file="Cartas/cartas parte del cuerpo/"+Sugerencia_Backtracking[3]+".png")
    lbl_imagen9= Label(ventana,image=imagen9).place(x=480,y=250)
    
    imagen10= PhotoImage(file="Cartas/cartas lugar/"+Sugerencia_Backtracking[4]+".png")
    lbl_imagen10= Label(ventana,image=imagen10).place(x=590,y=250)

    #-----------------------------imagenes solucion------------------------------
    imagen11= PhotoImage(file="Cartas/cartas sospechosos/"+Asesino+".png")
    lbl_imagen11= Label(ventana,image=imagen11).place(x=150,y=530)

    imagen12= PhotoImage(file="Cartas/cartas armas/"+Arma+".png")
    lbl_imagen12= Label(ventana,image=imagen12).place(x=260,y=530)
    
    imagen13= PhotoImage(file="Cartas/cartas motivo/"+Motivo+".png")
    lbl_imagen13= Label(ventana,image=imagen13).place(x=370,y=530)
    
    imagen14= PhotoImage(file="Cartas/cartas parte del cuerpo/"+ParteCuerpo+".png")
    lbl_imagen14= Label(ventana,image=imagen14).place(x=480,y=530)
    
    imagen15= PhotoImage(file="Cartas/cartas lugar/"+Lugar+".png")
    lbl_imagen15= Label(ventana,image=imagen15).place(x=590,y=530)
    #----------------------------Listbox de restricciones------------------------------
    contenedor=crearframe()
    contenedor.config(bg="white")
    contenedor.place(x=1080,y=380)

    listNodes = Listbox(contenedor, width=20, height=10, bg="#1F1E1A",fg="white", font=("Helvetica", 12))
    listNodes.pack(side="left")

    scrollbar = Scrollbar(contenedor, orient="vertical")
    scrollbar.config(command=listNodes.yview)
    scrollbar.pack(side="left", fill="y")

    listNodes.config(yscrollcommand=scrollbar.set)
    x=0
    while x < len(Restricciones_Cartas):
        listNodes.insert(END, (str(x+1)+") "+Restricciones_Cartas[x][0]+" - "+Restricciones_Cartas[x][1]))
        x+=1
    #-------------------------------imagenes solucion---------------------------
    img_sigue=PhotoImage(file="imagenes_programa/siguiente.png")
    btn_sigue=Button(ventana,bd=0,activebackground="white",bg="white",cursor="hand2",image=img_sigue,\
                     command=lambda:(siguiente_Intento()))
    btn_sigue.place(x=1150,y=600)
     
    img_reiniciar=PhotoImage(file="imagenes_programa/Reiniciar.png")
    btn_reiniciar=Button(ventana,bd=0,activebackground="white",bg="white",cursor="hand2",image=img_reiniciar,\
                         command=lambda:(contenedor.destroy(), ventana_Restricciones()))
    btn_reiniciar.place(x=1050,y=600)
    ventana.mainloop()

#Funion comienzo_Juego
#Entrada: Un contenedor, y las restricciones 
#salida: Retorna a la grafica Juego o Volver a la ventana de restriccion
#Restricciones: que sea una ventana existente
#objetivo: si el usuario dejo en blanco o relleno con letras la casilla de restricciones le informa al usuario y vuelve a solicitar las restricciones,
#si las resfriciones esta bien comienza los algoritmos 
def comienzo_Juego(contenedor,restricciones):
    global Cantidad_Restricciones, Restricciones_Cartas, Solucion
    if verifica_enteros(restricciones):
        Cantidad_Restricciones=eval(restricciones)
        Restricciones_Cartas=get_Restricciones()
        contenedor.destroy()
        fuerza_Bruta()
        backtracking()
        return ventana_Juego()
    else:
        return ventana_Restricciones()

#Funion siguiente_Intento
#Entrada: ----
#salida: Mensaje informativo que terminaron los ambos algoritmos o la grafica de las funciones
#Restricciones: que sea una ventana existente
#objetivo: volver a correr los algorimos de resolución
def siguiente_Intento():
    global Solucion, Fin_BT, Fin_FB
    if Fin_BT and Fin_FB: #si ambos terminaron le informa al usuario
        Pista_Actual_FB=""
        Pista_Actual_BT=""
        messagebox.showinfo("FIN"," ♦Ambos han llegado a la solución♦")
        return ventana_Juego()
    elif Fin_BT and Fin_FB==False : # si el de BT ya termino solo manda a correr fueza bruta
        Pista_Actual_BT=""
        fuerza_Bruta()
        return ventana_Juego()
    else:
        fuerza_Bruta()  #si no se ha resolvido ninguna, manda a correr ambos algoritmos
        backtracking()
        return ventana_Juego()

#-------------------------------- fuerza_Bruta -----------------------------------------
#Funion fuerza_Bruta
#Entrada: ----
#salida: Una lista de pistas menos 1 elemento que seria la pista actual
#Restricciones: 
#objetivo: Obtener una sgerencia y eliminar una sugerencia incorrecta
def fuerza_Bruta():
    global Pistas_Fuerza_Bruta,Intentos_Fuerza_Bruta, Sugerencia_Fuerza_Bruta, Restricciones_Cartas, Fin_FB,Pista_Actual_FB
    Sugerencia_Fuerza_Bruta=obtener_Sugerencia_Fuerza_Bruta() #obtiene una sugerencia 
    if Sugerencia_Fuerza_Bruta!=Solucion:
        Intentos_Fuerza_Bruta+=1
        sugerencias_equivocadas=get_Equivocadas(Sugerencia_Fuerza_Bruta)#obtiene las sugerencia que no son parte de la solucion 
        Pista_Actual_FB=sugerencias_equivocadas[random.randint(0,len(sugerencias_equivocadas)-1)] #obtiene una pista de las incorrectas al azar
        Pistas_Fuerza_Bruta= eliminar_Pista(Pista_Actual_FB)#elimina la pista de la matriz de pistas
    else:
        Fin_FB=True
        Pista_Actual_FB=""
        

#Funion obtener_Sugerencia_Fuerza_Bruta
#Entrada: ----
#salida: Una lista de sugerencias con las pistas pertenecentes a la lista de fuerza Bruta
#Restricciones: -----
#objetivo: Enviar una lista con sugerencias
def obtener_Sugerencia_Fuerza_Bruta():
    global Pistas_Fuerza_Bruta
    #Adquiere la sugerencia con solo randoms
    sugerencia_asesino = Pistas_Fuerza_Bruta[0][random.randint(0, len(Pistas_Fuerza_Bruta[0])-1)]
    sugerencia_arma    = Pistas_Fuerza_Bruta[1][random.randint(0, len(Pistas_Fuerza_Bruta[1])-1)]
    sugerencia_motivo  = Pistas_Fuerza_Bruta[2][random.randint(0, len(Pistas_Fuerza_Bruta[2])-1)]
    sugerencia_cuerpo  = Pistas_Fuerza_Bruta[3][random.randint(0, len(Pistas_Fuerza_Bruta[3])-1)]
    sugerencia_lugar   = Pistas_Fuerza_Bruta[4][random.randint(0, len(Pistas_Fuerza_Bruta[4])-1)]
    Sugerencia_Fuerza_Bruta=[sugerencia_asesino,sugerencia_arma,sugerencia_motivo,sugerencia_cuerpo,sugerencia_lugar]               
    return Sugerencia_Fuerza_Bruta


#Funion get_Equivocadas
#Entrada: La lista con la segerencias
#salida: Una lista con las sugerencias equivocadas
#Restricciones: -----
#objetivo: Enviar una lista con sugerencias equivocadas
def get_Equivocadas(lista):
    malas=[]
    for i in lista: #recorre la lista obtenida
        if existe_en_solucion(i)==False:
            malas+=[i] #si la psta no esta en la solucion la agrega a las incorrectas
    return malas


#Funion eliminar_Pista
#Entrada: Una pista
#salida: La lista de las pistas sin la pista ingresada
#Restricciones: -----
#objetivo: Enviar una lista con las pistas sin la pista ingresada
def eliminar_Pista(dato):
    global Pistas_Fuerza_Bruta
    fila=0
    for i in Pistas_Fuerza_Bruta:
        columna=0
        for j in i:
            if dato==j:
                Pistas_Fuerza_Bruta[fila]=Pistas_Fuerza_Bruta[fila][:columna]+Pistas_Fuerza_Bruta[fila][columna+1:] #aca elimina la pista y deja las demas elementos
            columna+=1
        fila+=1
    return Pistas_Fuerza_Bruta


#---------------------------------------Backtracking------------------------------
#Funion backtracking
#Entrada: -------
#salida: -------
#Restricciones: -----
#objetivo: el agoritmo se encarga de escoger una carta de las sugerencias al azar y verificar si esta en la lista o no
# si pertenece a solucion, eimina todas las pistas pertenecientes a la misma categoria , si no pertenece a la solución,
#envia una lista con las pistas sin la pista ingresada
def backtracking():
    global Intentos_Backracking, Pistas_Backtracking, Sugerencia_Backtracking, Fin_BT,Pista_Actual_BT
    Sugerencia_Backtracking=obtener_Sugerencia_Backtracking() #adquiere la sugerencia
    if Sugerencia_Backtracking!=Solucion:
        Intentos_Backracking+=1
        if len(Pistas_Backtracking[0])==1 or len(Pistas_Backtracking[1])==1 or len(Pistas_Backtracking[2])==1 or len(Pistas_Backtracking[3])==1 or len(Pistas_Backtracking[4])==1:
            posicion=obtener_pista_no_encontrada()
            Pista_Actual_BT=Sugerencia_Backtracking[posicion]#si ya hay una categoría con solo una opción el sistema se encarga de escoger otar categoria que no tena un asola opción
            if existe_en_solucion(Pista_Actual_BT):
                Pistas_Backtracking=pista_encontrada(Pista_Actual_BT) #si pertenece a solucion, eimina todas las pistas pertenecientes a la misma categoria
            else:
                Pistas_Backtracking=eliminar_Pista_Backtracking(Pista_Actual_BT)#no pertenece a la solución, envia una lista con las pistas sin la pista ingresada
        else:
            Pista_Actual_BT=Sugerencia_Backtracking[random.randint(0, 4)]
            if existe_en_solucion(Pista_Actual_BT):
                Pistas_Backtracking=pista_encontrada(Pista_Actual_BT)#si pertenece a solucion, eimina todas las pistas pertenecientes a la misma categoria
            else:
                Pistas_Backtracking=eliminar_Pista_Backtracking(Pista_Actual_BT)#no pertenece a la solución, envia una lista con las pistas sin la pista ingresada
    else:
        Fin_BT=True
        Pista_Actual_BT=""


#Funion obtener_pista_no_encontrada
#Entrada: 
#salida: True o False
#Restricciones: -----
#objetivo: Esta funcion tiene el obejtivo de realizar el backtracking más inteligente, si ya en una categoría solo hay una opción, pues que esta categoría no se tome
#en cuenta para la seleccion de la carta al azar
def obtener_pista_no_encontrada():
    global Pistas_Backtracking
    valido=False
    while valido==False:
        opcion=random.randint(0, 4)
        if len(Pistas_Backtracking[opcion])!=1:  #Mientras valido sea falso es porque el random escogio una opción que pertenece a una categoría aque solo tiene una opcion
            return opcion

            
#Funion pista_encontrada
#Entrada: Una pista
#salida: La lista de piestas con solo la carta correspondiente
#Restricciones: -----
#objetivo: Si la pista seleecionada al azar de la sugerencia pertenece a "x" categoria solo deja esa pista de la categoria las demás las elimina
def pista_encontrada(pista):
    global Pistas_Backtracking
    i=0
    while i <5:
        j=0
        while j<len(Pistas_Backtracking[i]):
            if Pistas_Backtracking[i][j]==pista:
                Pistas_Backtracking[i]= [pista]
                return Pistas_Backtracking
            j+=1
        i+=1


#Funion eliminar_Pista
#Entrada: Una pista
#salida: La lista de las pistas sin la pista ingresada
#Restricciones: -----
#objetivo: Enviar una lista con las pistas sin la pista ingresada
def eliminar_Pista_Backtracking(dato):
    global Pistas_Backtracking
    fila=0
    for i in Pistas_Backtracking:
        columna=0
        for j in i:
            if dato==j:
                Pistas_Backtracking[fila]=Pistas_Backtracking[fila][:columna]+Pistas_Backtracking[fila][columna+1:]
            columna+=1
        fila+=1
    return Pistas_Backtracking


#Funion obtener_Sugerencia_Backtracking
#Entrada: ----
#salida: una lista con las sugerencias válida
#Restricciones: -----
#objetivo: Enviar una lista con las sugerencias válida, l alista de segerencias se confromaria con randoms
def obtener_Sugerencia_Backtracking():
    global Pistas_Backtracking,Sugerencia_Backtracking
    sugerencia_Incorrecta=True
    while sugerencia_Incorrecta:
        sugerencia_asesino = Pistas_Backtracking[0][random.randint(0, len(Pistas_Backtracking[0])-1)]
        sugerencia_arma    = Pistas_Backtracking[1][random.randint(0, len(Pistas_Backtracking[1])-1)]
        sugerencia_motivo  = Pistas_Backtracking[2][random.randint(0, len(Pistas_Backtracking[2])-1)]
        sugerencia_cuerpo  = Pistas_Backtracking[3][random.randint(0, len(Pistas_Backtracking[3])-1)]
        sugerencia_lugar   = Pistas_Backtracking[4][random.randint(0, len(Pistas_Backtracking[4])-1)]
        if validar_Sugerencia(sugerencia_asesino,sugerencia_arma,sugerencia_motivo,sugerencia_cuerpo,sugerencia_lugar):
            Sugerencia_Backtracking=[sugerencia_asesino,sugerencia_arma,sugerencia_motivo,sugerencia_cuerpo,sugerencia_lugar]
            sugerencia_Incorrecta=False        
    return Sugerencia_Backtracking


#Funion obtener_Sugerencia_Backtracking
#Entrada: una segerenia de asesino,una segerenia de arma,una segerenia de motivo, una segerenia de parte del cuerpo y una segerenia de lugar
#salida: true o false
#Restricciones: -----
#objetivo: Si 2 de las sugerencias se encuentra en la lista de recciones se retornara false para que mande otras sugerencias
def validar_Sugerencia(asesino,arma,motivo,cuerpo,lugar):
    global Restricciones_Cartas
    restricciones=Restricciones_Cartas
    i=0
    while i < len(restricciones):
        #Validar todas las cambinaciones de las restrrones y las sugerencia
        if (restricciones[i][0]==asesino and restricciones[i][1]==arma)   or (restricciones[i][0]==asesino and restricciones[i][1]==motivo) or\
           (restricciones[i][0]==asesino and restricciones[i][1]==cuerpo) or (restricciones[i][0]==asesino and restricciones[i][1]==lugar)  or\
           (restricciones[i][0]==arma    and restricciones[i][1]==motivo) or (restricciones[i][0]==arma    and restricciones[i][1]==cuerpo) or\
           (restricciones[i][0]==arma    and restricciones[i][1]==lugar)  or (restricciones[i][0]==motivo  and restricciones[i][1]==cuerpo) or\
           (restricciones[i][0]==motivo  and restricciones[i][1]==lugar)  or (restricciones[i][0]==cuerpo  and restricciones[i][1]==lugar)  or\
           (restricciones[i][1]==asesino and restricciones[i][0]==arma)   or (restricciones[i][1]==asesino and restricciones[i][0]==motivo) or\
           (restricciones[i][1]==asesino and restricciones[i][0]==cuerpo) or (restricciones[i][1]==asesino and restricciones[i][0]==lugar)  or\
           (restricciones[i][1]==arma    and restricciones[i][0]==motivo) or (restricciones[i][1]==arma    and restricciones[i][0]==cuerpo) or\
           (restricciones[i][1]==arma    and restricciones[i][0]==lugar)  or (restricciones[i][1]==motivo  and restricciones[i][0]==cuerpo) or\
           (restricciones[i][1]==motivo  and restricciones[i][0]==lugar)  or (restricciones[i][1]==cuerpo  and restricciones[i][0]==lugar):
            return False
        i+=1
    return True

#------------------------------------------Restricciones---------------------------------------
#Funion get_Restricciones
#Entrada: 
#salida: Una lista con la cantidad de restricciones digitadas por el usuario
#Restricciones: -----
#objetivo: Sacar todas las restrrciones que el usuario digito
def get_Restricciones():
    global Cantidad_Restricciones
    lista=[]
    puesto=0
    while puesto<Cantidad_Restricciones:
        restricciones_Iguales=True
        while restricciones_Iguales: 
            i1=random.randint(0, 4)
            i2=random.randint(0, 4)
            if i1 != i2: #verifica que ambas opciones random no sean de la misma categoría
                restriccion1=get_Restricion_aux(i1)
                restriccion2=get_Restricion_aux(i2)
                if restriccion1==restriccion2 : #verifica que ambas opciones random no sean las mismas cartas
                    restricciones_Iguales=True
                else:
                    if existe_en_solucion(restriccion2) and existe_en_solucion(restriccion2): #verifica que ambas opciones no sean del conjunto de la solución
                        restricciones_Iguales=True
                    else:
                        lista+=[[restriccion1,restriccion2]] #si ambas no son iguales, no pertenescan a la misma categotia y no ambas no pertenecen a la solucion se
                        restricciones_Iguales=False          # se agrega a la lista de restricciones 
                        break
            else:
                restricciones_Iguales=True
        puesto+=1
    return lista

#Funion get_Restricion_aux
#Entrada: Un número de una categoría
#salida: Una pista
#Restricciones: -----
#objetivo: En viar un aparta random que pertecenca al numero de categoríarecibida
def get_Restricion_aux(num):
    global Pistas
    if num==0:
        return Pistas[0][random.randint(0, 6)]
    elif num==1:
        return Pistas[1][random.randint(0, 7)]
    elif num==2:
        return Pistas[2][random.randint(0, 5)]
    elif num==3:
        return Pistas[3][random.randint(0, 5)]
    else:
        return Pistas[4][random.randint(0, 8)]

#Funion existe_en_solucion
#Entrada: Una pista
#salida: True o False
#Restricciones: -----
#objetivo: saber si la pista ingresada pertenece a la solucion
def existe_en_solucion(pista):
    x=0
    while x<5:
        if pista==Solucion[x]:
            return True
        x+=1
    return False


#O: Crear un frame para colocar elementos dentro de el
#E: la ventana global 
#S: Un frame que puede contener elementos en su interio
#R: se tiene que recibir la ventana en donde se va a colocar el frame 
def crearframe():
    global ventana
    contenedor=Frame(ventana)
    return contenedor


#entrada:un dato
#salida: con un boleano se sabe si el dato es un entero o no 
#restricciones: que sean datos válidos
def verifica_enteros(dato):
    try:
        numero=eval(dato) #convierte el número a entero
        if isinstance(numero,int) :
            if numero>0:
                return True
            else:
                messagebox.showerror("ERROR","El número de restrcciones debe ser mayor a 0")
        else:
            messagebox.showerror("ERROR","La casilla no puede ser en letras")
            return False
    except:
            messagebox.showerror("ERROR","La casilla esta vacia")
            return False


#Funion cerrar una ventana
#Entrada: una ventana
#salida: cierra la ventana por completo
#Restricciones: que sea una ventana existente
def cerrar_ventana(a):
    a.destroy()
    

#E:Recibe una ventana.
#S:La salida es que regresa a la ventana del menú principal.
#R:Debe de enviar el nombre de la ventana en donde se estaba trabajando.
def volver_inicio(ventana):
    ventana.destroy()
    return inicio()


#E:-----
#S: Informacion sobre de mi persona
#R:----
def info():
    return messagebox.showinfo("Laberinto"," ♦ Autores: Bayron Barrios S."+" \n" + "\t" + "   Andyer Alpízar S." +"\n"
                               " ♦ Version 1.0.0"+"\n"
                               " ♦ Contactos: "+"\n"+"          bayronbs.03@hotmail.com"+"\n" +"          andyer.1@hotmail.com"+"\n"
                               " ♦ Nos reservamos la distribucion del juego"+"\n"
                               " ♦ Análsis de algoritmos, 2021")

play("Funny Detective.mp3")
inicio()
