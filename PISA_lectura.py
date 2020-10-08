#PISA_lectura
from tkinter import Tk,Label

proceso = 0

def Cronometro(x):
    
    def iniciar(x):
        global proceso
     
        # mostramos la variable contandor
        time['text'] = x
     
        #Este es el cronometro que cada 1000 ejecuta la
        #funcion iniciar() con el argumento x restado menos uno
        proceso = time.after(1000, iniciar, (x - 1))
        #si el contador llega a 0, ejecutar parar()
        if x == 0:
            parar()
            
    def parar(): #Cuando el cronometro llega a 0, se cierra la ventana
        global proceso
        time.after_cancel(proceso) 
        root.destroy()
        
    #Diseño de la ventana del cronometro
    root = Tk()
    root.title('Cronometro')
    time = Label(root, fg = 'red', width = 10, font = ("","30"))
    time.pack()
     

    iniciar(x)

def Empieza(dif):
    if dif == "hard":
        Cronometro(25)
    elif dif == "med":
        Cronometro(45)
    elif dif == "easy":
        Cronometro(60)
        
        
 

#limCron = 4
#Cronometro(limCron)
