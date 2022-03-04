import tkinter as tk
from tkinter import *
from datetime import *
from PIL import Image, ImageTk
import datetime
from datetime import *
import time
from tkinter import messagebox
from tkinter import ttk
class lector(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=4000, height=4000, bg='white')
        self.master=master
        self.pack()
        self.datos()
    def calc1(self):
        un=float(self.f1.get())
        self.resul=un/3.2814
        if self.resul!=0:
           self.r1.delete(0,'end')
           self.r1.insert(0, self.resul)
        else:
             pass
    def calc3(self):
        un=float(self.f1.get())
        self.resul=un/39.37
        if self.resul!=0:
           self.r1.delete(0,'end')
           self.r1.insert(0, self.resul)
        else:
             pass
    def calc4(self):
        un=float(self.f1.get())
        self.resul=un*(1609.344)
        if self.resul!=0:
           self.r1.delete(0,'end')
           self.r1.insert(0, self.resul)
        else:
             pass
        
    def longitud(self):
        self.venta1=tk.Toplevel(app)
        self.venta1.iconbitmap('logouis.ico')
        self.venta1.config(bg='white')
        self.venta1.geometry('4000x4000')
        self.fc1=Label(self.venta1, text='Unidad a convertir')
        self.fc1.place(x=700, y=100)
        self.f1=Entry(self.venta1)
        self.f1.place(x=700, y=150)
        self.re1=Label(self.venta1, text='Conversión a metros')
        self.re1.place(x=1000, y=100)
        self.r1=Entry(self.venta1)
        self.r1.place(x=1000, y=150)
        self.def1=Label(self.venta1, text='''El metro (símbolo: m)1​ es la unidad coherente de longitud
del Sistema Internacional de Unidades.
​ Se define como la distancia que recorre
la luz en el vacío en un intervalo de 1/299 792 458 s.3​4
El metro se definió originalmente en 1793 como una diez
millonésima parte de la distancia desde el Ecuador hasta
el polo norte a lo largo de un gran círculo,
por lo que la circunferencia de la Tierra es aproximadamente
40 000 kilómetros. En 1799, el medidor se redefinió en
términos de una barra de medidor prototipo
(la barra real utilizada se cambió en 1889).
En 1960, el medidor se redefinió en términos
de un cierto número de longitudes de onda de
una cierta línea de emisión de kriptón-86.
La definición actual se adoptó en 1983 y se modificó
ligeramente en 2002 para aclarar que el metro
es una medida de longitud adecuada ''')
        self.def1.place(x=20, y=150)
        self.titulo1=Label(self.venta1, text='''METRO (m) ''')
        self.bot=Button(self.venta1, text='Convertir pies a Metros', command=self.calc1)
        self.bot.place(x=800, y=300,width=400,heigh=50)
        self.bot1=Button(self.venta1, text='Convertir pulgadas a Metros', command=self.calc3)
        self.bot1.place(x=800, y=400,width=400,heigh=50)
        self.bot2=Button(self.venta1, text='Convertir millas a Metros', command=self.calc4)
        self.bot2.place(x=800, y=500,width=400,heigh=50)
        self.titulo1.place(x=800 , y=0)
        self.bot.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",20))
        self.bot1.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",20))
        self.bot2.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",20))
        self.titulo1.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",20))
        self.def1.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",15))

        self.fc1.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",15))
        self.f1.config(fg='white',
                            bg='#42426F',
                            font=("Comic Sans MS",15))
        self.re1.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",15))
        self.r1.config(fg='white',
                            bg='#42426F',
                            font=("Comic Sans MS",15))
        
        
        
    def calc2(self):
        uni=float(self.f2.get())
        self.resul=uni/2.2046
        if self.resul!=0:
            
           self.r2.delete(0,'end')
           self.r2.insert(0, self.resul)
        else:
             pass
    def calc5(self):
        uni=float(self.f2.get())
        self.resul=uni*453.59/16
        if self.resul!=0:
            
           self.r2.delete(0,'end')
           self.r2.insert(0, self.resul)
        else:
             pass
    def calc6(self):
        uni=float(self.f2.get())
        self.resul=uni*1000
        if self.resul!=0:
            
           self.r2.delete(0,'end')
           self.r2.insert(0, self.resul)
        else:
             pass
    def masa(self):
        self.venta2=tk.Toplevel(app)
        self.venta2.iconbitmap('logouis.ico')
        self.venta2.config(bg='white')
        self.venta2.geometry('4000x4000')
        self.fc2=Label(self.venta2, text='Unidad a convertir:')
        self.fc2.place(x=700, y=100)
        self.f2=Entry(self.venta2)
        self.f2.place(x=700, y=150)
        self.re2=Label(self.venta2, text='Unidad en Kilogramos:')
        self.re2.place(x=1000, y=100)
        self.r2=Entry(self.venta2)
        self.r2.place(x=1000, y=150)
        self.def1=Label(self.venta2, text='''El kilogramonota  (símbolo: kg),
es la unidad básica de masa del Sistema Internacional de Unidades (SI).
Es una medida ampliamente utilizada en la ciencia, la ingeniería
y el comercio en todo el mundo, y a menudo simplemente se le llama
kilo en el habla cotidiana.
Es la única unidad básica que emplea un prefijo y la última unidad
del SI que siguió definiéndose por un objeto patrón y no por una
característica física fundamental.​ El 20 de mayo de 2019 su
definición pasó a estar ligada con la constante de Planck,
una constante natural que describe los paquetes de energía
emitidos en forma de radiación. Esto permite que un laboratorio
de metrología debidamente equipado calibre un instrumento de medición
de masa como una balanza de potencia.5''')
        self.def1.place(x=20, y=150)
        self.titulo1=Label(self.venta2, text='''KILOGRAMO (Kg)''')
        self.bot=Button(self.venta2, text='Libras a Kilogramos', command=self.calc2)
        self.bot.place(x=800, y=300,width=400,heigh=50)
        self.bot1=Button(self.venta2, text='Onzas a Kilogramos', command=self.calc5)
        self.bot1.place(x=800, y=400,width=400,heigh=50)
        self.bot2=Button(self.venta2, text='Toneladas a Kilogramos', command=self.calc6)
        self.bot2.place(x=800, y=500,width=400,heigh=50)
        self.titulo1.place(x=500 , y=0)
        self.bot.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",20))
        self.bot1.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",20))
        self.bot2.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",20))
        self.titulo1.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",20))
        self.def1.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",15))
        self.fc2.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",15))
        self.f2.config(fg='white',
                            bg='#42426F',
                            font=("Comic Sans MS",15))
        self.re2.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",15))
        self.r2.config(fg='white',
                            bg='#42426F',
                            font=("Comic Sans MS",15))
    def datos(self):
          
          self.imagenuis = ImageTk.PhotoImage(Image.open("e3t.jpeg"))
          self.imbLabel=Label(self,image=self.imagenuis)
          self.imbLabel.config(bg='white')
          self.imbLabel.place(x=0, y=0)
          self.imagen = ImageTk.PhotoImage(Image.open("figura14.png"))
          self.imbLabel=Label(self,image=self.imagen)
          self.imbLabel.config(bg='white')
          self.imbLabel.place(x=500, y=100,width=370,heigh=370)
          self.imagen1 = ImageTk.PhotoImage(Image.open("hola.gif"))
          self.imbLabel1=Label(self,image=self.imagen1)
          self.imbLabel1.config(bg='white')
          self.imbLabel1.place(x=1000, y=100)
          self.nom=Label(self, text='''--------
Estudiante de ingenieria electronica
UIS 2021-1
programación de computadores 2''')
          self.nom.place(x=10, y=300)
          self.filtro=Label(self, text='''UNIDADES SISTEMA INTERNACINAL''')
          self.filtro.place(x=400, y=30)
          self.cre=Label(self, text='CREADO POR :')
          self.cre.place(x=10, y=250)
          self.boton1=Button(text='UNIDADES DE LONGITUD',command=self.longitud)
          self.boton1.place(x=10, y=450)
          self.boton2=Button(text='UNIDADES DE MASA',command=self.masa)
          self.boton2.place(x=10, y=500)
          self.filtro.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",20)) 
          self.nom.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",15))
          self.boton1.config(fg='white',
                            bg='#42426F',
                            font=("Comic Sans MS",15))
          self.boton2.config(fg='white',
                            bg='#42426F',
                            font=("Comic Sans MS",15))
          self.cre.config(bg='white',
                            fg='#42426F',
                            font=("Comic Sans MS",15))

          
          

vent=Tk()
vent.wm_title('UNIVERSIDAD INDSUTRIAL DE SANTANDER SEDE BARBOSA')
vent.geometry('2000x2000')
app=lector(vent)
vent.iconbitmap('logouis.ico')
INTERVALO_REFRESCO_RELOJ = 100
def obtener_hora_actual():
    return datetime.now().strftime("%H:%M:%S")
def refrescar_reloj(): 
    variable_hora_actual.set(obtener_hora_actual())
    vent.after(INTERVALO_REFRESCO_RELOJ, refrescar_reloj)
variable_hora_actual = tk.StringVar(vent, value=obtener_hora_actual())
hora = Label(vent, textvariable=variable_hora_actual, font=(f"Consolas 60",12 ), fg='#42426F', bg='white')
hora.place(x=1200, y=30)
refrescar_reloj()
import datetime
from datetime import date
Fech = Label(text="",font=("Comic Sans MS",12),fg="#42426F",bg="white")
Fech.place(x=1130,y=0, width=175, height=35)
datetime = datetime.datetime.now()
day = datetime.strftime("%A")

Hoy = date.today()
d1 = Hoy.strftime("%d / %m / %Y")
Fech.configure(text = d1 )


app.mainloop()
