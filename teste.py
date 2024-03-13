from tkinter import *
from tkinter import ttk

cor1="#1e1f1e"#preto
cor2="#03fcf8"#azul bebe
cor3="#EB5915" #laranja
cor4="#828585" #cinza
cor5="#ffffff" #branco



#criando janela
janela=Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

#separando as telas
frame_display=Frame(janela,width=235,height=62, bg=cor4)
frame_display.grid(row=0,column=0)

frame_corpo=Frame(janela,width=235,height=256)
frame_corpo.grid(row=1,column=0)

#criando label
valor_texto= StringVar()
app_label = Label(frame_display, textvariable=valor_texto,width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor4)
app_label.place(x=0,y=0)



#variavel todos valores
todos_valores=' '

#criando função
def entrar_valores(event):


    global todos_valores

    todos_valores= todos_valores+str(event)


    #passando valor pra tela
    valor_texto.set(todos_valores)

#calculo
def calcular():
    try:
        global todos_valores
        todos_valores = todos_valores.replace('x', '*')
        todos_valores = todos_valores.replace('÷', '/')
        if '**' in todos_valores:
            valor_texto.set('Equação Inválida.')
        if '*-+' in todos_valores:
            valor_texto.set('Equação Inválida.')
        if '*+-' in todos_valores:
            valor_texto.set('Equação Inválida.')
        else:
            resultado = eval(todos_valores)
            valor_texto.set(resultado)
    except SyntaxError:
        valor_texto.set('Equação Inválida.')
    except ZeroDivisionError:
        valor_texto.set('É um fresco é')

#limpar tela
def limpar_tela():
    global todos_valores
    todos_valores=""
    valor_texto.set("")

#criando botoes

b2=Button(frame_corpo,command=limpar_tela,text="C", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=0,y=0)

b3=Button(frame_corpo, command=lambda:entrar_valores('%'), text="%", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=118,y=0)

b4=Button(frame_corpo,  command=lambda:entrar_valores('/'),text="/", width=5, bg=cor3, fg=cor5 ,height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=177,y=0)

b5=Button(frame_corpo,  command=lambda:entrar_valores('9'),text="9", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=0,y=51)

b6=Button(frame_corpo,  command=lambda:entrar_valores('8'),text="8", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=59,y=51)

b7=Button(frame_corpo,  command=lambda:entrar_valores('7'),text="7", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=118,y=51)

b8=Button(frame_corpo,  command=lambda:entrar_valores('x'),text="x", width=5, bg=cor3, fg=cor5 ,height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=177,y=51)

b9=Button(frame_corpo,  command=lambda:entrar_valores('6'),text="6", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=0,y=102)

b10=Button(frame_corpo,  command=lambda:entrar_valores('5'),text="5", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=59,y=102)

b11=Button(frame_corpo,  command=lambda:entrar_valores('4'),text="4", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=118,y=102)

b12=Button(frame_corpo,  command=lambda:entrar_valores('+'),text="+", width=5, bg=cor3, fg=cor5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=177,y=102)

b13=Button(frame_corpo,  command=lambda:entrar_valores('3'),text="3", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=0,y=153)

b14=Button(frame_corpo,  command=lambda:entrar_valores('2'),text="2", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=59,y=153)

b15=Button(frame_corpo,  command=lambda:entrar_valores('1'),text="1", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=118,y=153)

b16=Button(frame_corpo, command=lambda:entrar_valores('-'), text="-", width=5,bg=cor3, fg=cor5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=177,y=153)

b17=Button(frame_corpo,  command=lambda:entrar_valores('0'),text="0", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=0,y=204)

b18=Button(frame_corpo, command=lambda:entrar_valores('.'), text=".", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=118,y=204)

b16=Button(frame_corpo,  command=calcular,text="=", width=5,bg=cor3, fg=cor5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=177,y=204)


janela.mainloop()
