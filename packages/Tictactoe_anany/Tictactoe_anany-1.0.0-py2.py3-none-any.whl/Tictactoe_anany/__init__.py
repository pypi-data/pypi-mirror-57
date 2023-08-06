'''Tic Tac Toe game just for fun, made by Anany Singh'''
__version__ = '1.0.0'
from tkinter import *
import tkinter.messagebox as mbox
from tkinter import ttk


class tictactoe:
    last = ['O']
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.configure(bg = 'old lace')
        self.root.title('Developer : ANANY  SINGH   ,   Sacred Heart Higher Secondary School   ,   Sitapur')
        self.l = Label(self.root,text = 'Tic - Tac - Toe',font = 'algerian 30 bold underline',fg = 'red',bg = 'old lace')
        self.l.pack()
        self.fr = Frame(self.root,bg = 'yellow')
        self.fr.pack(pady = 100)
        global a1,a2,a3,a4,a5,a6,a7,a8,a9
        self.a1 = Button(self.fr,command = lambda: self.select_a1(self.root),width = 2,relief = 'ridge')
        self.a2 = Button(self.fr,command = lambda: self.select_a2(self.root),width = 2,relief = 'ridge')
        self.a3 = Button(self.fr,command = lambda: self.select_a3(self.root),width = 2,relief = 'ridge')
        self.a4 = Button(self.fr,command = lambda: self.select_a4(self.root),width = 2,relief = 'ridge')
        self.a5 = Button(self.fr,command = lambda: self.select_a5(self.root),width = 2,relief = 'ridge')
        self.a6 = Button(self.fr,command = lambda: self.select_a6(self.root),width = 2,relief = 'ridge')
        self.a7 = Button(self.fr,command = lambda: self.select_a7(self.root),width = 2,relief = 'ridge')
        self.a8 = Button(self.fr,command = lambda: self.select_a8(self.root),width = 2,relief = 'ridge')
        self.a9 = Button(self.fr,command = lambda: self.select_a9(self.root),width = 2,relief = 'ridge')

        self.a1.grid(row = 0,column = 0,ipadx = 10,ipady = 5,padx = 5,pady = 5)
        self.a2.grid(row = 0,column = 1,ipadx = 10,ipady = 5,padx = 5,pady = 5)
        self.a3.grid(row = 0,column = 2,ipadx = 10,ipady = 5,padx = 5,pady = 5)
        self.a4.grid(row = 1,column = 0,ipadx = 10,ipady = 5,padx = 5,pady = 5)
        self.a5.grid(row = 1,column = 1,ipadx = 10,ipady = 5,padx = 5,pady = 5)
        self.a6.grid(row = 1,column = 2,ipadx = 10,ipady = 5,padx = 5,pady = 5)
        self.a7.grid(row = 2,column = 0,ipadx = 10,ipady = 5,padx = 5,pady = 5)
        self.a8.grid(row = 2,column = 1,ipadx = 10,ipady = 5,padx = 5,pady = 5)
        self.a9.grid(row = 2,column = 2,ipadx = 10,ipady = 5,padx = 5,pady = 5)

        self.s = ttk.Style()
        self.s.configure('ttt.TButton',foreground = 'saddle brown',font = 'ravie 10 bold')
        self.restart = ttk.Button(self.root,text = 'Restart',style = 'ttt.TButton',command = lambda:self.restarts(self.root))
        self.restart.pack(pady = 15,ipadx = 5,ipady = 5)
        self.exitt = ttk.Button(self.root,text = 'Exit',style = 'ttt.TButton',command = lambda:self.exittt(self.root))
        self.exitt.pack(pady = 15,ipadx = 5,ipady = 5)

        self.root.mainloop()
    def exittt(self,root = None):
        if mbox.askyesno('QUIT','Do you really want to exit ?'):
            self.root.destroy()

    def restartss(self,root):
        self.root.destroy()
        tictactoe.last.clear()
        tictactoe.last.append('O')
        main()
    def restarts(self,root):
        if mbox.askyesno('RESTART','Do you really want to restart ?'):
            self.root.destroy()
            tictactoe.last.clear()
            tictactoe.last.append('O')
            main()
    def select_a1(self,root):
        if tictactoe.last[-1] == 'X':
            self.a1.configure(text = 'O',state = 'disabled')
            tictactoe.last.append('O')
            self.see_win(root)
        else:
            self.a1.configure(text = 'X',state = 'disabled')
            tictactoe.last.append('X')
            self.see_win(root)
    def select_a2(self,root):
        if tictactoe.last[-1] == 'X':
            self.a2.configure(text = 'O',state = 'disabled')
            tictactoe.last.append('O')
            self.see_win(root)
        else:
            self.a2.configure(text = 'X',state = 'disabled')
            tictactoe.last.append('X')
            self.see_win(root)
    def select_a3(self,root):
        if tictactoe.last[-1] == 'X':
            self.a3.configure(text = 'O',state = 'disabled')
            tictactoe.last.append('O')
            self.see_win(root)
        else:
            self.a3.configure(text = 'X',state = 'disabled')
            tictactoe.last.append('X')
            self.see_win(root)
    def select_a4(self,root):
        if tictactoe.last[-1] == 'X':
            self.a4.configure(text = 'O',state = 'disabled')
            tictactoe.last.append('O')
            self.see_win(root)
        else:
            self.a4.configure(text = 'X',state = 'disabled')
            tictactoe.last.append('X')
            self.see_win(root)
    def select_a5(self,root):
        if tictactoe.last[-1] == 'X':
            self.a5.configure(text = 'O',state = 'disabled')
            tictactoe.last.append('O')
            self.see_win(root)
        else:
            self.a5.configure(text = 'X',state = 'disabled')
            tictactoe.last.append('X')
            self.see_win(root)
    def select_a6(self,root):
        if tictactoe.last[-1] == 'X':
            self.a6.configure(text = 'O',state = 'disabled')
            tictactoe.last.append('O')
            self.see_win(root)
        else:
            self.a6.configure(text = 'X',state = 'disabled')
            tictactoe.last.append('X')
            self.see_win(root)
    def select_a7(self,root):
        if tictactoe.last[-1] == 'X':
            self.a7.configure(text = 'O',state = 'disabled')
            tictactoe.last.append('O')
            self.see_win(root)
        else:
            self.a7.configure(text = 'X',state = 'disabled')
            tictactoe.last.append('X')
            self.see_win(root)
    def select_a8(self,root):
        if tictactoe.last[-1] == 'X':
            self.a8.configure(text = 'O',state = 'disabled')
            tictactoe.last.append('O')
            self.see_win(root)
        else:
            self.a8.configure(text = 'X',state = 'disabled')
            tictactoe.last.append('X')
            self.see_win(root)
    def select_a9(self,root):
        if tictactoe.last[-1] == 'X':
            self.a9.configure(text = 'O',state = 'disabled')
            tictactoe.last.append('O')
            self.see_win(root)
        else:
            self.a9.configure(text = 'X',state = 'disabled')
            tictactoe.last.append('X')
            self.see_win(root)

    def see_win(self,root):
        if (self.a1['text'] == 'X') and (self.a2['text'] == 'X') and (self.a3['text'] == 'X'):
            if mbox.askyesno('WINNER','Player with "X" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a4['text'] == 'X') and (self.a5['text'] == 'X') and (self.a6['text'] == 'X'):
            if mbox.askyesno('WINNER','Player with "X" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a7['text'] == 'X') and (self.a8['text'] == 'X') and (self.a9['text'] == 'X'):
            if mbox.askyesno('WINNER','Player with "X" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a1['text'] == 'X') and (self.a4['text'] == 'X') and (self.a7['text'] == 'X'):
            if mbox.askyesno('WINNER','Player with "X" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a2['text'] == 'X') and (self.a5['text'] == 'X') and (self.a8['text'] == 'X'):
            if mbox.askyesno('WINNER','Player with "X" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a3['text'] == 'X') and (self.a6['text'] == 'X') and (self.a9['text'] == 'X'):
            if mbox.askyesno('WINNER','Player with "X" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a1['text'] == 'X') and (self.a5['text'] == 'X') and (self.a9['text'] == 'X'):
            if mbox.askyesno('WINNER','Player with "X" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a3['text'] == 'X') and (self.a5['text'] == 'X') and (self.a7['text'] == 'X'):
            if mbox.askyesno('WINNER','Player with "X" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()


        elif (self.a1['text'] == 'O') and (self.a2['text'] == 'O') and (self.a3['text'] == 'O'):
            if mbox.askyesno('WINNER','Player with "O" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a4['text'] == 'O') and (self.a5['text'] == 'O') and (self.a6['text'] == 'O'):
            if mbox.askyesno('WINNER','Player with "O" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a7['text'] == 'O') and (self.a8['text'] == 'O') and (self.a9['text'] == 'O'):
            if mbox.askyesno('WINNER','Player with "O" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a1['text'] == 'O') and (self.a4['text'] == 'O') and (self.a7['text'] == 'O'):
            if mbox.askyesno('WINNER','Player with "O" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a2['text'] == 'O') and (self.a5['text'] == 'O') and (self.a8['text'] == 'O'):
            if mbox.askyesno('WINNER','Player with "O" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a3['text'] == 'O') and (self.a6['text'] == 'O') and (self.a9['text'] == 'O'):
            if mbox.askyesno('WINNER','Player with "O" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a1['text'] == 'O') and (self.a5['text'] == 'O') and (self.a9['text'] == 'O'):
            if mbox.askyesno('WINNER','Player with "O" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()
        elif (self.a3['text'] == 'O') and (self.a5['text'] == 'O') and (self.a7['text'] == 'O'):
            if mbox.askyesno('WINNER','Player with "O" has WON the game.\nRestart?'):
                self.restartss(root)
            else:
                self.root.destroy()

def main():
    '''Just write:\n\tfrom Tictactoe_anany import main\n\tmain()'''
    game = tictactoe()
    del game
def help():
    '''Just write:\n\tfrom Tictactoe_anany import main\n\tmain()'''
    print('Just write:\n\tfrom Tictactoe_anany import main\n\tmain()')

if __name__ == '__main__':
    help()
