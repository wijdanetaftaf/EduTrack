import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import *
import mysql.connector
from datetime import *
S=datetime.now().date()
######################## lisason mysql ##################################################################################################
a0=mysql.connector.connect(
        host="localhost",
        user="root",
        password="20032311",
        database="projet",
        auth_plugin='mysql_native_password',
        use_pure=True
    )
b=a0.cursor()
##################################################### classe d'affichage les ling colonne de la bd ####################################
class Table:
    def __init__(self, c1):
        self.canvas=Canvas(c1,height=800,width=900)
        self.canvas.grid(row=1,column=2,sticky='news')
        sc1=Scrollbar(c1,orient='vertical',command=self.canvas.yview)
        sc1.grid(row=1,column=3,sticky='ns')
        self.canvas.configure(yscrollcommand=Scrollbar.set)
        frame=Frame(self.canvas)
        self.canvas.create_window((0,0),window=frame,anchor='nw')
        for i in range(lnom):
            for j in range(colnom):
                e=Entry(frame,width=13,fg='black',font=('Arial',16,'bold'))
                e.grid(row=i+1,column=j+1)
                e.insert(END,Headstr[i][j])
        for i in range(l):
            for j in range(col):
                e=Entry(frame,width=13,fg='black',font=('Arial',16))
                e.grid(row=i+2,column=j+1)
                e.insert(END,lst[i][j])
def ajouter():
    sql1='INSERT INTO etudiant VALUES (%s,%s,%s,%s,%s,%s,%s)'
    sql2='INSERT INTO inscri VALUES(%s,%s,%s,%s,%s)'
    d1=(v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get())
    d2=(v1.get(),vv2.get(),S,vv4.get(),int(vv4.get())*150)
    b.execute(sql1,d1)
    b.execute(sql2,d2)
    sd1="select count(*) from appartient where id_grp='G_M1CP'"
    b.execute(sd1)
    rM1CP=b.fetchone()
    sd2="select count(*) from appartient where id_grp='G_M2CP'"
    b.execute(sd2)
    rM2CP=b.fetchone()
    sd3="select count(*) from appartient where id_grp='G_M3CP'"
    b.execute(sd3)
    rM3CP=b.fetchone()
    sd4="select count(*) from appartient where id_grp='G_M3CD'"
    b.execute(sd4)
    rM3CD=b.fetchone()
    sd5="select count(*) from appartient where id_grp='G_P3CD'"
    b.execute(sd5)
    rP3CD=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_P1CP'"
    b.execute(sd)
    rP1CP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_P2CP'"
    b.execute(sd)
    rP2CP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_P3CP'"
    b.execute(sd)
    rP3CP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_M1LP'"
    b.execute(sd)
    rM1LP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_M2LP'"
    b.execute(sd)
    rM2LP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_M2LD'"
    b.execute(sd)
    rM2LD=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_M3LP'"
    b.execute(sd)
    rM3LP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_M3LD'"
    b.execute(sd)
    rM3LD=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_P1LP'"
    b.execute(sd)
    rP1LP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_P2LP'"
    b.execute(sd)
    rP2LP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_P3LP'"
    b.execute(sd)
    rP3LP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_P2LD'"
    b.execute(sd)
    rP2LD=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_P3LD'"
    b.execute(sd)
    rP3LD=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_SVT1CP'"
    b.execute(sd)
    rSVT1CP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_SVT2CP'"
    b.execute(sd)
    rSVT2CP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_SVT3CP'"
    b.execute(sd)
    rSVT3CP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_SVT3CD'"
    b.execute(sd)
    rSVT3CD=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_SVT1LP'"
    b.execute(sd)
    rSVT1LP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_SVT2LP'"
    b.execute(sd)
    rSVT2LP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_SVT3LP'"
    b.execute(sd)
    rSVT3LP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_SVT2LD'"
    b.execute(sd)
    rSVT2LD=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_SVT3LD'"
    b.execute(sd)
    rSVT3LD=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_HG'"
    b.execute(sd)
    rHG=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_AR'"
    b.execute(sd)
    rAR=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_EI'"
    b.execute(sd)
    rEI=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_FR'"
    b.execute(sd)
    rFR=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_ANG'"
    b.execute(sd)
    rANG=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_FRL'"
    b.execute(sd)
    rFRL=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_ANGL'"
    b.execute(sd)
    rANGL=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_TRD'"
    b.execute(sd)
    rTRD=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_E_CO'"
    b.execute(sd)
    rECO=b.fetchone()  
    sd="select count(*) from appartient where id_grp='G_DVP'"
    b.execute(sd)
    rDVP=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_D_WEB'"
    b.execute(sd)
    rD_WEB=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_PHILO'"
    b.execute(sd)
    rPHILO=b.fetchone()
    sd="select count(*) from appartient where id_grp='G_CH'"
    b.execute(sd)
    rCH=b.fetchone()                                                                                                                                                                                                                                                         
    sql3="INSERT INTO appartient VALUES(%s,%s)"
    sql4="INSERT INTO assister VALUES(%s,%s,%s,%s)"
    if vv2.get()=='M1CP' and rM1CP[0]<8:
        b.execute(sql3,(v1.get(),'G_M1CP'))
        b.execute(sql4,('4',v1.get(),'0','0'))
        messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='M2CP' and rM2CP[1]<8:b.execute(sql3,(v1.get(),'G_M2CP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='M3CP' and rM3CP[0]<8:b.execute(sql3,(v1.get(),'G_M3CP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='M3CD' and rM3CD[0]<8:b.execute(sql3,(v1.get(),'G_M3CD'));b.execute(sql4,('1',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='P3CD' and rP3CD[0]<8:b.execute(sql3,(v1.get(),'G_P3CD'));b.execute(sql4,('1',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='P1CP' and rP1CP[0]<8:b.execute(sql3,(v1.get(),'G_P1CP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='P2CP' and rP2CP[0]<8:b.execute(sql3,(v1.get(),'G_P2CP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='P3CP' and rP3CP[0]<8:b.execute(sql3,(v1.get(),'G_P3CP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='M1LP' and rM1LP[0]<8:b.execute(sql3,(v1.get(),'G-M1LP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='M2LP' and rM2LP[0]<8:b.execute(sql3,(v1.get(),'G_M2LP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='M2LD' and rM2LD[0]<8:b.execute(sql3,(v1.get(),'G_M2LD'));b.execute(sql4,('1',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='M3LP' and rM3LP[0]<8:b.execute(sql3,(v1.get(),'G_M3LP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='M3LD' and rM3LD[0]<8:b.execute(sql3,(v1.get(),'G_M3LD'));b.execute(sql4,('1',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='P1LP' and rP1LP[0]<8:b.execute(sql3,(v1.get(),'G_P1LP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='P2LD' and rP2LD[0]<8:b.execute(sql3,(v1.get(),'G_P2LD'));b.execute(sql4,('1',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='P3LP' and rP3LP[0]<8:b.execute(sql3,(v1.get(),'G_P3LP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='P2LD' and rP2LD[0]<8:b.execute(sql3,(v1.get(),'G_P2LD'));b.execute(sql4,('1',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='P3LD' and rP3LD[0]<8:b.execute(sql3,(v1.get(),'G_P3LD'));b.execute(sql4,('1',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='SVT1CP' and rSVT1CP[0]<8:b.execute(sql3,(v1.get(),'G_SVT1CP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='SVT2CP' and rSVT2CP[0]<8:b.execute(sql3,(v1.get(),'G_SVT2CP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='SVT3CP' and rSVT3CP[0]<8:b.execute(sql3,(v1.get(),'G_SVT3CP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='SVT3CD' and rSVT3CD[0]<8:b.execute(sql3,(v1.get(),'G_SVT3CD'));b.execute(sql4,('1',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='SVT1LP' and rSVT1LP[0]<8:b.execute(sql3,(v1.get(),'G_SVT1LP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='SVT2LP' and rSVT2LP[0]<8:b.execute(sql3,(v1.get(),'G_SVT2LP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='SVT3LP' and rSVT3LP[0]<8:b.execute(sql3,(v1.get(),'G_SVT3LP'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='SVT2LD' and rSVT2LD[0]<8:b.execute(sql3,(v1.get(),'G_SVT2LD'));b.execute(sql4,('1',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='SVT3LD' and rSVT3LD[0]<8:b.execute(sql3,(v1.get(),'G_SVT3LD'));b.execute(sql4,('1',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='CH' and rCH[0]<8:b.execute(sql3,(v1.get(),'G_CH'));b.execute(sql4,('3',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='HG' and rHG[0]<8:b.execute(sql3,(v1.get(),'G_HG'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='AR' and rAR[0]<8:b.execute(sql3,(v1.get(),'G_AR'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='EI' and rEI[0]<8:b.execute(sql3,(v1.get(),'G_EI'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='FR' and rFR[0]<8:b.execute(sql3,(v1.get(),'G_FR'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='ANG' and rANG[0]<8:b.execute(sql3,(v1.get(),'G_ANG'));b.execute(sql4,('4',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='FRL' and rFRL[0]<8:b.execute(sql3,(v1.get(),'G_FRL'));b.execute(sql4,('3',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='ANGL' and rANGL[0]<8:b.execute(sql3,(v1.get(),'G_ANGL'));b.execute(sql4,('3',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='TRD' and rTRD[0]<8:b.execute(sql3,(v1.get(),'G_TRD'));b.execute(sql4,('2',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='E_CO' and rECO[0]<8:b.execute(sql3,(v1.get(),'G_E_CO'));b.execute(sql4,('2',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='DVP' and rDVP[0]<8:b.execute(sql3,(v1.get(),'G_DVP'));b.execute(sql4,('2',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='D_WEB' and rD_WEB[0]<8:b.execute(sql3,(v1.get(),'G_D_WEB'));b.execute(sql4,('2',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    elif vv2.get()=='PHILO' and rPHILO[0]<8:b.execute(sql3,(v1.get(),'G-PHILO'));b.execute(sql4,('2',v1.get(),'0','0'));messagebox.showinfo('message','inscription terminer')
    else:messagebox.showinfo('error',"le groupd deja remplis,vous allez passer au liste d'attend d'integration au groupe ")
    a0.commit()
######################################### fenetre d'inscription #########################################################################        
def inscrisoutiens():
    global v1,v2,v3,v4,v5,v6,v7,vv4,vv2
    b=Tk()
    b.geometry('2000x900')
    b.title('inscription')
    b.configure(background='#CACFD2')
    f=Frame(b,height='40',bg='#1C2833')
    Label(f,text=' LA SERVISE INSCRIPTION',fg='white',bg='#1C2833',font=('comforta',30),height='2').pack()
    Label(b, text='CIN :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=60, y=150)
    Label(b, text='NOM :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=500, y=150)
    Label(b, text='PRENOM :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=60, y=250)
    Label(b, text='RUE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=500, y=250)
    Label(b, text='NIVEAU :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=500, y=350)
    Label(b, text='TELEPHONE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=60, y=350)
    Label(b, text='VILLE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=350, y=480)
    Label(b, text='FORMATION :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=1000, y=150)
    Label(b, text='LE NOMBRE DE SEANCE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=1000, y=350)
    vv1=StringVar()
    vv2=ttk.Combobox(b,textvariable=vv1,values=('M1CP','M1CD','M2CP','M2CD','M3CP','M3CD','P1CP','P1CD','P2CP','P2CD','P3CP','P3CD',
                                                'SVT1CP','SVT1CD','SVT2CP','SVT2CD','SVT3CP','SVT3CD','M1LP','M1LD','M2LP','M2LD','M3LP','M3LD','P1LP','P1LD','P2LP','P2LD','P3LP','P3LD',
                                                'SVT1LP','SVT1LD','SVT2LP','SVT2LD','SVT3LP','SVT3LD','HG','EI','PHILO','AR','ANG','FR'),width=50,height=8);vv2.place(x=1000,y=190)
    vv2.current(0)
    vv3=IntVar()
    vv4=ttk.Combobox(b,textvariable=vv3,values=(2,3,4),width=50,height=8);vv4.place(x=1000,y=400)
    vv4.current(0)
    v1=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v1.place(x=60, y=190)
    v2=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v2.place(x=500, y=190)
    v3=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v3.place(x=60, y=300,)
    v4=Entry(b,width=20, font=("Comforta", 16),justify=CENTER,bd=2);v4.place(x=500, y=300)
    v5=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v5.place(x=500, y=400)
    v6=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v6.place(x=60, y=400)
    v7=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v7.place(x=350, y=540)
    Button(b,command=ajouter,text='ajouter', fg='white', bg='green', bd=2, cursor='hand2', width='25',height='2',font=('comforta',15)).place(x=400, y=650)
    Button(b,command=b.destroy,text='EXIT', fg='white', bg='red', bd=2, cursor='hand2', width='25', height='2',font=('comforta',15)).place(x=800, y=650)
    f.pack(fill='x',side=TOP)
    b.mainloop()
def inscrilangue():
    global v1,v2,v3,v4,v5,v6,v7,vv4,vv2
    b=Tk()
    b.geometry('2000x900')
    b.title('inscription')
    b.configure(background='#CACFD2')
    f=Frame(b,height='40',bg='#1C2833')
    Label(f,text=' LA SERVISE INSCRIPTION',fg='white',bg='#1C2833',font=('comforta',30),height='2').pack()
    Label(b, text='CIN :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=60, y=150)
    Label(b, text='NOM :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=500, y=150)
    Label(b, text='PRENOM :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=60, y=250)
    Label(b, text='RUE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=500, y=250)
    Label(b, text='NIVEAU :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=500, y=350)
    Label(b, text='TELEPHONE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=60, y=350)
    Label(b, text='VILLE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=350, y=480)
    Label(b, text='FORMATION :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=1000, y=150)
    Label(b, text='LE NOMBRE DE SEANCE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=1000, y=350)
    vv1=StringVar()
    vv2=ttk.Combobox(b,textvariable=vv1,values=('CH','ANGL','FRL'),width=50,height=8);vv2.place(x=1000,y=190)
    vv2.current(0)
    vv3=IntVar()
    vv4=ttk.Combobox(b,textvariable=vv3,values=(8,16,24,32,40,48),width=50,height=8);vv4.place(x=1000,y=400)
    vv4.current(0)
    v1=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v1.place(x=60, y=190)
    v2=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v2.place(x=500, y=190)
    v3=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v3.place(x=60, y=300,)
    v4=Entry(b,width=20, font=("Comforta", 16),justify=CENTER,bd=2);v4.place(x=500, y=300)
    v5=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v5.place(x=500, y=400)
    v6=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v6.place(x=60, y=400)
    v7=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v7.place(x=350, y=540)
    Button(b,command=ajouter,text='ajouter', fg='white', bg='green', bd=2, cursor='hand2', width='25',height='2',font=('comforta',15)).place(x=400, y=650)
    Button(b,command=b.destroy,text='EXIT', fg='white', bg='red', bd=2, cursor='hand2', width='25', height='2',font=('comforta',15)).place(x=800, y=650)
    f.pack(fill='x',side=TOP)
    b.mainloop() 
def inscrisoft():
    global v1,v2,v3,v4,v5,v6,v7,vv4,vv2
    b=Tk()
    b.geometry('2000x900')
    b.title('inscription')
    b.configure(background='#CACFD2')
    f=Frame(b,height='40',bg='#1C2833')
    Label(f,text=' LA SERVISE INSCRIPTION',fg='white',bg='#1C2833',font=('comforta',30),height='2').pack()
    Label(b, text='CIN :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=60, y=150)
    Label(b, text='NOM :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=500, y=150)
    Label(b, text='PRENOM :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=60, y=250)
    Label(b, text='RUE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=500, y=250)
    Label(b, text='NIVEAU :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=500, y=350)
    Label(b, text='TELEPHONE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=60, y=350)
    Label(b, text='VILLE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=350, y=480)
    Label(b, text='FORMATION :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=1000, y=150)
    Label(b, text='LE NOMBRE DE SEANCE :', fg='black',bg='#CACFD2',font=('comforta',15)).place(x=1000, y=350)
    vv1=StringVar()
    vv2=ttk.Combobox(b,textvariable=vv1,values=('E_CO','DVP','D_WEB','TRD'),width=50,height=8);vv2.place(x=1000,y=190)
    vv2.current(0)
    vv3=IntVar()
    vv4=ttk.Combobox(b,textvariable=vv3,values=(8,16,24,32,40,48),width=50,height=8);vv4.place(x=1000,y=400)
    vv4.current(0)
    v1=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v1.place(x=60, y=190)
    v2=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v2.place(x=500, y=190)
    v3=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v3.place(x=60, y=300,)
    v4=Entry(b,width=20, font=("Comforta", 16),justify=CENTER,bd=2);v4.place(x=500, y=300)
    v5=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v5.place(x=500, y=400)
    v6=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v6.place(x=60, y=400)
    v7=Entry(b,width=20, font=("Comforta", 16),bd=2,justify=CENTER);v7.place(x=350, y=540)
    Button(b,command=ajouter,text='ajouter', fg='white', bg='green', bd=2, cursor='hand2', width='25',height='2',font=('comforta',15)).place(x=400, y=650)
    Button(b,command=b.destroy,text='EXIT', fg='white', bg='red', bd=2, cursor='hand2', width='25', height='2',font=('comforta',15)).place(x=800, y=650)
    f.pack(fill='x',side=TOP)
    b.mainloop()   
def selcsoft():
    c=Tk()
    c.geometry('1550x900')
    c.title('liste des etudiant')
    c.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c,text='voici la liste des etudiant inscri',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("select e.nom,e.prenom,f.categorie as choix from etudiant e,inscri i,formation f where e.CIN=i.CIN and i.id_formation=f.id_formation and f.categorie='soft skils'")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c)
    c.mainloop()    
def selclangue():
    c=Tk()
    c.geometry('1550x900')
    c.title('liste des etudiant')
    c.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c,text='voici la liste des etudiant inscri',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("select e.nom,e.prenom,f.categorie as choix from etudiant e,inscri i,formation f where e.CIN=i.CIN and i.id_formation=f.id_formation and f.categorie='langue'")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c)
    c.mainloop()    
def selcsoutiens():
    c=Tk()
    c.geometry('1550x900')
    c.title('liste des etudiant')
    c.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c,text='voici la liste des etudiant inscri',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("select e.nom,e.prenom,f.categorie as choix from etudiant e,inscri i,formation f where e.CIN=i.CIN and i.id_formation=f.id_formation and f.categorie='soutien scolaire'")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c)
    c.mainloop()
def requet():
    r=Tk()
    r.geometry('1550x900')
    r.config(bg='white')
    Button(r,text="supprimer un etudiant",command=supprimerall,bg='#1b4f72',fg='white',bd=4,cursor='hand2',width='40',height='2',font=('comforta',15)).place(x=200,y=150)
    Button(r,text="recherche d'un etudiant",command=recherche,bg='#1b4f72',fg='white',bd=4,cursor='hand2',width='40',height='2',font=('comforta',15)).place(x=200,y=250)
    Button(r,text="nombre des seances restant d'un etudiant",command=rest,bg='#1b4f72',fg='white',bd=4,cursor='hand2',width='40',height='2',font=('comforta',15)).place(x=200,y=450)
    Button(r,text="afficher les etudiants qui ont termine leurs seances",command=aff,bg='#1b4f72',fg='white',bd=4,cursor='hand2',width='40',height='2',font=('comforta',15)).place(x=200,y=350)
    Button(r,text="afficher les etudiants et leurs groupes ",command=affgrp,bg='#1b4f72',fg='white',bd=4,cursor='hand2',width='40',height='2',font=('comforta',15)).place(x=900,y=150)
    Button(r,text="afficher les groupes qui ont deja pleines",command=pleine,bg='#1b4f72',fg='white',bd=4,cursor='hand2',width='40',height='2',font=('comforta',15)).place(x=900,y=250)
    Button(r,text="afficher le jour et le type d'un seance",command=type,bg='#1b4f72',fg='white',bd=4,cursor='hand2',width='40',height='2',font=('comforta',15)).place(x=900,y=350)
    Button(r,command=r.destroy,text='EXIT',fg='#154360',bg='#FFA000',bd=4,cursor='hand2',width='40',height='2',font=('comforta',15)).place(x=900,y=450)
    n=Frame(r,bg='#212121',height='50')
    n.pack(fill='x',side=TOP)
    n1=Frame(r,bg='black',height='90')
    Label(r,height='34',width='1',bg='black').place(x=780,y=51)
    n1.pack(fill='x',side=BOTTOM)
    r.mainloop()
def matiersoft():
    c=Tk()
    c.geometry('1550x900')
    c.title('liste des formation')
    c.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c,text='voici la liste des matires',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("select nom_formation,categorie from formation where categorie='soft skils'")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c)
    c.mainloop()
def matierlangue():
    c=Tk()
    c.geometry('1550x900')
    c.title('liste des formation')
    c.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c,text='voici la liste des matires',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("select nom_formation,categorie from formation where categorie='langue' ")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c)
    c.mainloop()
def matiersoutiens():
    c=Tk()
    c.geometry('1550x900')
    c.title('liste des formation')
    c.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c,text='voici la liste des matires',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("select nom_formation,categorie from formation where categorie='soutien scolaire' ")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c)
    c.mainloop()
def grouplangue():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des groupes')
    c1.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste de nos groupes',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("SELECT g.id_grp,g.nbre_eleve from groupe g,formateur f,formation fr where g.id_formateur=f.id_formateur and f.id_formateur=fr.id_formateur and fr.categorie='langue'")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()    
def groupsoft():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des groupes')
    c1.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste de nos groupes',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute(" SELECT g.id_grp,g.nbre_eleve from groupe g,formateur f,formation fr where g.id_formateur=f.id_formateur and f.id_formateur=fr.id_formateur and fr.categorie='soft skils'")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()    
def groupsoutiens():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des groupes')
    c1.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste de nos groupes',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("SELECT g.id_grp,g.nbre_eleve from groupe g,formateur f,formation fr where g.id_formateur=f.id_formateur and f.id_formateur=fr.id_formateur and fr.categorie='soutien scolaire'")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()
def enattdsoftskills():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des etudiant en attend')
    c1.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste des etudiant qui attend leur integration',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("SELECT e.nom,e.prenom,f.categorie as choix FROM etudiant e,inscri i,formation f WHERE NOT EXISTS (  SELECT 1 FROM appartient WHERE appartient.CIN=e.CIN) and e.CIN=i.CIN and i.id_formation=f.id_formation and f.categorie='soft skils'")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()      
def enattdlangues():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des etudiant en attend')
    c1.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste des etudiant qui attend leur integration',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("SELECT e.nom,e.prenom,f.categorie as choix FROM etudiant e,inscri i,formation f WHERE NOT EXISTS (  SELECT 1 FROM appartient WHERE appartient.CIN=e.CIN) and e.CIN=i.CIN and i.id_formation=f.id_formation and f.categorie='langue'")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()        
def enattdsoutiens():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des etudiant en attend')
    c1.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste des etudiant qui attend leur integration',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("SELECT e.nom,e.prenom,f.categorie as choix FROM etudiant e,inscri i,formation f WHERE NOT EXISTS (  SELECT 1 FROM appartient WHERE appartient.CIN=e.CIN) and e.CIN=i.CIN and i.id_formation=f.id_formation and f.categorie='soutien scolaire'")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()
def lisprosoutiens():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des formateur')
    c1.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste de nos formateurs',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("select * from formateur where specialite in ('maths','pc','svt','anglais','français','hg','ei','philo','arabe') ")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop() 
def lisprosoft():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des formateur')
    c1.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste de nos formateurs',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("select * from formateur where specialite in ('e_commerce','dev_web','dev_personnel','trading') ")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()  
def lisprolangue():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des formateur')
    c1.config(bg='black')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste de nos formateurs',font=('comforta',20),bg='black',fg='white').grid(row=0,column=0)
    b.execute("select * from formateur where specialite in ('anglais_L','français_L','chinois') ")
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop() 
def soutiens_scolaires():
   fnt4= tk.Toplevel(fnt1)
   fnt4.geometry('1550x900')
   fnt4.resizable(False, False)
   fnt4.title("NSWSACADEMY")
   fnt4.config(background='#F2F3F4')
   photo = tk.PhotoImage(file="C:\\Users\\WIJDANE TAFTAF\\PycharmProjects\\Projet SI\\Transparent (1).png")
   p = tk.Label(fnt4, image=photo)
   p.place(x=360, y=100)
   f1 = tk.Frame(fnt4, width='2000', height='100', background='black')
   f1.place(x=0, y=0)
   lb1 = tk.Label(fnt4, text='BIENVENU AU SERVISE DE SOUTIENS SCOLAIRE ', height='2', bg='black', fg='white',font=('comforta', 20))
   lb1.place(x=450, y=10)
   bt1 = tk.Button(fnt4,command=inscrisoutiens,text='inscription', fg='white', bg='#154360', bd=4, cursor='hand2', width='30',height='2', font=('comforta', 14))
   bt1.place(x=50, y=180)
   bt2 = tk.Button(fnt4,command=selcsoutiens,text='liste des etudiants inscris', fg='white', bg='#154360', bd=4, cursor='hand2',width='29', height='2', font=('comforta', 14))
   bt2.place(x=50, y=370)
   bt3 = tk.Button(fnt4,command=groupsoutiens,text='liste des groupes ', fg='white', bg='#154360', bd=4, cursor='hand2', width='29', height='2', font=('comforta', 14))
   bt3.place(x=50, y=530)
   bt4 = tk.Button(fnt4,command=matiersoutiens,text='listes des matieres', fg='white', bg='#154360', bd=4, cursor='hand2',width='30', height='2', font=('comforta', 14))
   bt4.place(x=1100, y=180)
   bt5 = tk.Button(fnt4,command=enattdsoutiens, text='etudiants en attente', fg='white', bg='#154360', bd=4, cursor='hand2',width='30', height='2', font=('comforta', 14))
   bt5.place(x=1100, y=370)
   bt6 = tk.Button(fnt4, command=lisprosoutiens,text='liste des professeurs', fg='white', bg='#154360', bd=4, cursor='hand2',width='30', height='2', font=('comforta', 14))
   bt6.place(x=1100, y=530)
   bt7 = tk.Button(fnt4, text='EXIT', fg='#154360', bg='#FFA000', bd=4, cursor='hand2', width='33', height='2',font=('comforta', 14), command=fnt4.destroy)
   bt7.place(x=570, y=660)
   fnt4.mainloop()

def softskills():
   fnt3= tk.Toplevel(fnt1)
   fnt3.geometry('1550x900')
   fnt3.resizable(False, False)
   fnt3.title("NSWSACADEMY")
   fnt3.config(background='white')
   photo = tk.PhotoImage(file="C:\\Users\\WIJDANE TAFTAF\\Downloads\\Skills.png")
   p = tk.Label(fnt3, image=photo)
   p.place(x=710, y=150)
   f1 = tk.Frame(fnt3, width='1550', height='100', background='#F4D03F')
   f1.place(x=0, y=0)
   lb1 = tk.Label(fnt3, text='BIENVENU AU SERVISE DE SOFTSKILLS', height='2', bg='#F4D03F', fg='#154360',font=('comforta', 25))
   lb1.place(x=450, y=10)
   bt1 = tk.Button(fnt3,command=inscrisoft, text='inscription', fg='white', bg='#154360', width='60', height='3')
   bt1.place(x=150, y=120)
   bt2 = tk.Button(fnt3,command=selcsoft, text='liste des etudiants inscris', fg='white', bg='#154360', width='60', height='3')
   bt2.place(x=150, y=220)
   bt3 = tk.Button(fnt3,command=groupsoft, text='liste des groupes ', fg='white', bg='#154360', width='60', height='3')
   bt3.place(x=150, y=320)
   bt4 = tk.Button(fnt3, command=matiersoft,text='listes des matieres', fg='white', bg='#154360', width='60', height='3')
   bt4.place(x=150, y=420)
   bt5 = tk.Button(fnt3, command=enattdsoftskills,text='etudiants en attente', fg='white', bg='#154360', width='60', height='3')
   bt5.place(x=150, y=520)
   bt6 = tk.Button(fnt3, command=lisprosoft,text='liste des professeurs', fg='white', bg='#154360', width='60', height='3')
   bt6.place(x=150, y=620)
   bt7 = tk.Button(fnt3, text='EXIT', fg='#154360', bg='#F4D03F', bd=2, cursor='hand2', width='60', height='2',font=('comforta', 14), command=fnt3.destroy)
   bt7.place(x=800, y=680)
   fnt3.mainloop()
def langues():
   fnt2 = tk.Toplevel(fnt1)
   fnt2.geometry('1550x900')
   fnt2.resizable(False, False)
   fnt2.title("NSWSACADEMY")
   fnt2.config(background='#F2F3F4')

   photo = tk.PhotoImage(file="C:\\Users\\WIJDANE TAFTAF\Downloads\\0.png")
   p = tk.Label(fnt2, image=photo)
   p.place(x=550, y=350)
   f1 = tk.Frame(fnt2, width='1550', height='120', background='#154360')
   f1.place(x=0, y=0)
   lb1 = tk.Label(fnt2, text='BIENVENU AU SERVISE DE LANGUES', height='2', bg='#154360', fg='white', font=('comforta', 30))
   lb1.place(x=450, y=10)
   bt1 = tk.Button(fnt2,command=inscrilangue, text='inscription', fg='white', bg='#2874A6', width='45', height='4')
   bt1.place(x=300, y=200)
   bt2 = tk.Button(fnt2,command=selclangue, text='liste des etudiants inscris', fg='white', bg='#F39C12', width='45', height='4')
   bt2.place(x=800, y=200)
   bt3 = tk.Button(fnt2, command=grouplangue,text='liste des groupes ', fg='white', bg='#F39C12', width='50', height='4')
   bt3.place(x=100, y=380)
   bt4 = tk.Button(fnt2, command=matierlangue,text='listes des matieres', fg='white', bg='#2874A6', width='50', height='4')
   bt4.place(x=100, y=540)
   bt5 = tk.Button(fnt2,command=enattdlangues, text='etudiants en attente', fg='white', bg='#2874A6', width='50', height='4')
   bt5.place(x=1020, y=380)
   bt6 = tk.Button(fnt2,command=lisprolangue, text='liste des professeurs', fg='white', bg='#F39C12', width='50', height='4')
   bt6.place(x=1020, y=540)
   bt7 = tk.Button(fnt2, text='EXIT', fg='white', bg='#F39C12',bd=2, cursor='hand2', width='40', height='4',font=('comforta', 10), command=fnt2.destroy)
   bt7.place(x=600, y=700)
   fnt2.mainloop()
def supp():
    req_check = 'SELECT COUNT(*) FROM etudiant WHERE CIN=%s'
    req_supp = 'DELETE FROM etudiant WHERE CIN=%s'
    b.execute(req_check, (val.get(),))
    count = b.fetchone()[0]
    if count > 0:
        b.execute(req_supp, (val.get(),))
        a0.commit()
        messagebox.showinfo('Message', 'Suppression terminée avec succès')
    else:
        messagebox.showinfo('Message', "Étudiant avec le CIN spécifié n'existe pas dans la base de données, MERCI")      
def supprimerall():
    global val
    f = tk.Tk()
    f.geometry('1550x900')
    f.title('suppression')
    f.configure(background='#CACFD2')
    lb1 = tk.Label(f, text='CIN :', fg='black', bg='#CACFD2', font=('comforta', 30))
    lb1.place(x=600, y=200)
    val = tk.Entry(f, width=25, font=("Comforta", 18), bd=2)
    val.place(x=600, y=300)
    tk.Button(f, command=supp, text='supprimer', fg='white', bg='red', bd=2, cursor='hand2', width='30', height='2', font=('comforta', 15)).place(x=600, y=350)
    f.mainloop()
def r():
    requete_select = 'SELECT * FROM etudiant WHERE CIN=%s'
    b.execute(requete_select,(vr.get(),))
    resultats =b.fetchall()
    message = "Résultats :\n"
    for row in resultats:
        message +=f"CIN: {row[0]}, NOM: {row[1]}, Prenom: {row[2]}, Rue: {row[3]}, niveau: {row[4]}, tele: {row[5]}, ville: {row[6]}\n"
    messagebox.showinfo('Message',message)
def recherche():
    global vr
    f = tk.Tk()
    f.geometry('1550x900')
    f.title('recherche')
    f.configure(background='#CACFD2')
    lb1 = tk.Label(f, text='CIN :', fg='black', bg='#CACFD2', font=('comforta', 30))
    lb1.place(x=600, y=200)
    vr= tk.Entry(f, width=25, font=("Comforta", 18), bd=2)
    vr.place(x=600, y=300)
    tk.Button(f, command=r, text='rechercher', fg='white', bg='red', bd=2, cursor='hand2', width='30', height='2', font=('comforta', 15)).place(x=600, y=350)
    f.mainloop()    
def rest():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des seance restant pour chaque etudiant')
    c1.config(bg='#263238')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='liste des seance restant pour chaque etudiant',font=('comforta',20),bg='#263238',fg='white').grid(row=0,column=0)
    b.execute("SELECT inscri.CIN AS CIN_etudiant,inscri.id_formation,inscri.nbr_seance,assister.nbr_presence,CASE WHEN COALESCE(assister.nbr_absc, 0) = 0 THEN inscri.nbr_seance - COALESCE(assister.nbr_presence, 0) - COALESCE(assister.nbr_absc, 0) ELSE inscri.nbr_seance - COALESCE(assister.nbr_presence, 0) - COALESCE(assister.nbr_absc, 0) + 1 END AS nombre_restant_de_seances FROM inscri,assister where inscri.CIN=assister.CIN " )
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()
def pleine():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('liste des groupes pleines')
    c1.config(bg='#263238')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste des groupres pleines',font=('comforta',20),bg='#263238',fg='white').grid(row=0,column=0)
    b.execute("SELECT id_grp,nbre_eleve FROM groupe WHERE nbre_eleve = 8 " )
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()
def type():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('la liste  de jour et type des seance')
    c1.config(bg='#263238')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste  de jour et type des seance ',font=('comforta',20),bg='#263238',fg='white').grid(row=0,column=0)
    b.execute("select distinct jour,type from seance" )
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()
def affgrp():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('la liste des etudiants et leurs groupes')
    c1.config(bg='#263238')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste des etudiants et leurs groupes ',font=('comforta',20),bg='#263238',fg='white').grid(row=0,column=0)
    b.execute("SELECT e.cin,e.nom,e.prenom,e.niveau,a.id_grp from etudiant e,appartient a where e.CIN=a.CIN" )
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()
    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()
def aff():
    c1=Tk()
    c1.geometry('1550x900')
    c1.title('la liste des etudiants aui ont terminer leur seances')
    c1.config(bg='#263238')
    global lnom,lst,Headstr,colnom,l,col
    Label(c1,text='voici la liste des etudiants aui ont terminer leur seances ',font=('comforta',20),bg='#263238',fg='white').grid(row=0,column=0)
    b.execute("SELECT inscri.CIN AS cin_etudiant, inscri.id_formation, inscri.nbr_seance, assister.nbr_presence FROM inscri JOIN assister ON inscri.CIN = assister.CIN WHERE (inscri.nbr_seance - COALESCE(assister.nbr_presence, 0) - COALESCE(assister.nbr_absc, 0) + 1) = 0" )
    Headstr=[b.column_names]
    lnom=len(Headstr)
    colnom=len(Headstr[0])
    lst=b.fetchall()










    l=len(lst)
    col=len(lst[0])
    t=Table(c1)
    c1.mainloop()
def check_login():
    username = en1.get()
    password = en2.get()

    if password == "1234":
        show_main_interface()
    else:
        messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

def show_main_interface():
    global fnt1
    fnt1 = tk.Toplevel(fnt)
    fnt1.geometry('1550x900')
    fnt1.resizable(False, False)
    fnt1.title("NSWSACADEMY")
    fnt1.config(background='#F2F3F4')

    photo1 =tk.PhotoImage(file="C:\\Users\\WIJDANE TAFTAF\\Desktop\\professionnelle.png")
    pp1 =tk.Label(fnt1, image=photo1)
    pp1.place(x=40, y=150)

    Lbb1 = tk.Label(fnt1, text='                                                           BIENVENUE                                                             ', fg='#3498DB', bg='black', font=('Comforta', 30))
    Lbb1.place(x=5, y=10)

    btt1 = tk.Button(fnt1, text='Centre de langue', fg='white', bg='#3498DB',font=('Comforta', 15) ,width='50', height='2',command=langues,)
    btt1.place(x=800, y=370)

    btt2 = tk.Button(fnt1, text='Soft skills', fg='white', bg='#3498DB', font=('Comforta',15), width='50', height='2',command=softskills)
    btt2.place(x=800, y=470)

    btt3 = tk.Button(fnt1,text='Cours de soutiens', fg='white',font=('Comforta',15),bg='#3498DB', width='50', height='2',command=soutiens_scolaires)
    btt3.place(x=800, y=570)

    Lbb2 = tk.Label(fnt1, text='Sélectionner une catégorie...!!!', fg='black', bg='#F2F3F4', font=('Comforta', 30))
    Lbb2.place(x=800, y=200)

    Lbb3 = tk.Label(fnt1, text='WITHOUT', fg='black', bg='#F2F3F4', font=('Comforta',30))
    Lbb3.place(x=200, y=450)

    Lbb4 = tk.Label(fnt1, text='EDUCATION', fg='black', bg='#F2F3F4', font=('Comforta',30))
    Lbb4.place(x=200, y=500)

    Lbb5 = tk.Label(fnt1, text='THERE IS', fg='black', bg='#F2F3F4', font=('Comforta',30))
    Lbb5.place(x=200, y=550)

    Lbb6 = tk.Label(fnt1, text='NO FUTURE', fg='black', bg='#F2F3F4', font=('Comforta',30))
    Lbb6.place(x=200, y=600)
    bt4= tk.Button(fnt1,command=requet, text="plus d'information...", fg='white', bg='#3498DB', font=('Comforta', 15), bd=4, cursor='hand2',width='50', height='2').place(x=800, y=670)

    fnt1.mainloop()
fnt = tk.Tk()
fnt.geometry('1550x900')
fnt.resizable(False, False)
fnt.title("centre de formation ")
fnt.config(background='#F2F4F4')

photo = tk.PhotoImage(file="C:\\Users\\WIJDANE TAFTAF\\Desktop\\Learning.png")
p = tk.Label(fnt, image=photo)
p.place(x=10, y=250)

Lb1 = tk.Label(fnt, text='Welcome to our platform', fg='black', bg='#F2F4F4', font=('Comforta', 60), relief="flat")
Lb1.place(x=50, y=70)

f1 = tk.Frame(width='1550', height='200', background='black')
f1.place(x=0, y=700)

Lb1 = tk.Label(fnt, text='E-mail : centredeformation96@gmail.com', fg='white', bg='black', font=('Comforta', 15), relief="flat")
Lb1.place(x=10, y=710)

Lb2 = tk.Label(fnt, text='Telephone : 0548967825 ', fg='white', bg='black', font=('Comforta', 15), relief="flat")
Lb2.place(x=420, y=750)

Lb3 = tk.Label(fnt, text='site web : WWW.centredeformation.ma ', fg='white', bg='black', font=('Comforta', 15), relief="flat")
Lb3.place(x=700, y=710)

Lb4 = tk.Label(fnt, text='Hay Errachad B.P. 81 Khouribga 25000', fg='white', bg='black', font=('Comforta', 15), relief="flat")
Lb4.place(x=1000, y=750)

Lb1 = tk.Label(fnt, text='---------------------------------------------------------------------------NSWSACADEMY-------------------------------------------------------------------------', fg='black', bg='#F2F4F4', font=('Comforta', 20))
Lb1.place(x=5, y=10)

en1 = tk.Entry(fnt, textvariable='username', width=30, font=("Arial", 20), fg="black", bg="#F2F4F4", justify="center", state="normal")
en1.place(x=800, y=300)

en2 = tk.Entry(fnt, textvariable='password', show="*", width=30, font=("Comforta", 20), fg="black", bg="#F2F4F4", justify="center", state="normal")
en2.place(x=800, y=400)

Lb3 = tk.Label(fnt, text='USERNAME ', fg='black', bg='#F2F4F4', font=('Comforta', 20), relief="flat")
Lb3.place(x=800, y=250)

Lb3 = tk.Label(fnt, text='PASSWORD ', fg='black', bg='#F2F4F4', font=('Comforta', 20), relief="flat")
Lb3.place(x=800, y=350)

bt2 = tk.Button(fnt, text=' Login ', fg='white', bg='#154360', width='50', height='3', command=check_login)
bt2.place(x=860, y=500)

fnt.mainloop()    