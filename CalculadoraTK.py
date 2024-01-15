""" Importação da biblioteca Tkinter """
from tkinter import *

expression = ''

""" Definição das Funções de Comando """

def keystroke(event):
    if event.char.isnumeric() or event.char in '-+/*':
        press(event.char)


def press(num, event=None):
    global expression
    expression += str(num)
    equation.set(expression)
    

def clear():
    global expression
    expression = ''
    equation.set('')
    pass


def equalpress(event=None):
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        if len(total) < 10:
            equation.set(total)
        else:
            equation.set(total[:10])
        expression = total
    except:
        equation.set(' error ')
        expression = ''


def backspace(event):
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Início da interface

janela = Tk()
janela.title("Calculadora")
janela.resizable(False, False)

""" Definições Gráficas do Módulo """

equation = StringVar()


# Criando os botões

display = Entry(
    master=janela,
    state='readonly',
    justify='right',
    font=('Arial', 80),
    width=11,
    fg='black',
    textvariable=equation
)
# O "Grid" posiciona os elementos na tela
display.grid(
    row=0, 
    column=0, 
    columnspan=4
)
""" Manipulando as informações digitadas no display """
display.bind('<KeyPress>', keystroke)
display.bind('<Return>', equalpress)
display.bind('<BackSpace>', backspace)
display.focus()

botao7 = Button(
    text='7',
    font=('Arial', 16),
    height=2,
    bg= 'white',
    activebackground='#4287f5',
    command=lambda: press(7)
)
botao7.grid(row=1, column=0, sticky=EW)


botao8 = Button(
    text='8',
    font=('Arial', 16),
    height=2,
    bg= 'white',
    activebackground='#4287f5',
    command=lambda: press(8)
)
botao8.grid(row=1, column=1, sticky=EW)


botao9 = Button(
    text='9',
    font=('Arial', 16),
    height=2,
    bg= 'white',
    activebackground='#4287f5',
    command=lambda: press(9)
)
botao9.grid(row=1, column=2, sticky=EW)


botao4 = Button(
    text='4',
    font=('Arial', 16),
    height=2,
    bg= 'white',
    activebackground='#4287f5',
    command=lambda: press(4)
)
botao4.grid(row=2, column=0, sticky=EW)


botao5 = Button(
    text='5',
    font=('Arial', 16),
    height=2,
    bg= 'white',
    activebackground='#4287f5',
    command=lambda: press(5)
)
botao5.grid(row=2, column=1, sticky=EW)


botao6 = Button(
    text='6',
    font=('Arial', 16),
    height=2,
    bg= 'white',
    activebackground='#4287f5',
    command=lambda: press(6)
)
botao6.grid(row=2, column=2, sticky=EW)


botao3 = Button(
    text='3',
    font=('Arial', 16),
    height=2,
    bg= 'white',
    activebackground='#4287f5',
    command=lambda: press(3)
)
botao3.grid(row=3, column=2, sticky=EW)


botao2 = Button(
    text='2',
    font=('Arial', 16),
    height=2,
    bg= 'white',
    activebackground='#4287f5',
    command=lambda: press(2)
)
botao2.grid(row=3, column=1, sticky=EW)


botao1 = Button(
    text='1',
    font=('Arial', 16),
    height=2,
    bg= 'white',
    activebackground='#4287f5',
    command=lambda: press(1)
)
botao1.grid(row=3, column=0, sticky=EW)


botao0 = Button(
    text='0',
    font=('Arial', 16),
    height=2,
    bg= 'white',
    activebackground='#4287f5',
    command=lambda: press(0)
)
botao0.grid(row=4, column=1, sticky=EW)    

botao_menos = Button(
    text='-',
    font=('Arial', 16),
    height=2,
    bg= '#4287f5',
    activebackground='white',
    command=lambda: press('-')
)
botao_menos.grid(
    row=1, 
    column=3, 
    sticky=EW
)
botao_mais = Button(
    text='+',
    font=('Arial', 16),
    height=2,
    bg= '#4287f5',
    activebackground='white',
    command=lambda: press('+')
)
botao_mais.grid(
    row=2, 
    column=3, 
    sticky=EW
)
botao_divisao = Button(
    text='/',
    font=('Arial', 16),
    height=2,
    bg= '#4287f5',
    activebackground='white',
    command=lambda: press('/')
)
botao_divisao.grid(
    row=3, 
    column=3, 
    sticky=EW
)
botaoC = Button(
    text='C',
    font=('Arial', 16),
    height=2,
    bg= '#f2f542',
    activebackground='white',
    command=clear
)
botaoC.grid(
    row=4, 
    column=0, 
    sticky=EW
)
botao_igual= Button(
    text='=',
    font=('Arial', 16),
    height=2,
    bg= '#4bf542',
    activebackground='white',
    command=equalpress
)
botao_igual.grid(
    row=4, 
    column=2, 
    sticky=EW
)
botao_multiplicar = Button(
    text='*',
    font=('Arial', 16),
    height=2,
    bg= '#4287f5',
    activebackground='white',
    command=lambda: press('*')
)
botao_multiplicar.grid(
    row=4, 
    column=3, 
    sticky=EW
)

# Rodar o programa
janela.mainloop()