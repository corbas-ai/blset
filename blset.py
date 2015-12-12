#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
from tkinter import *
import tkinter.messagebox as mbox

import subprocess as sbp

try:
    lastv = int(float(sbp.check_output(['xbacklight','-get'])))
except FileNotFoundError:
    mbox.showerror("Нет зависимой утилиты","Установите утилиту xbacklight. До свидания.")
    sys.exit(1)


def main():
    global lastv
    tk = Tk()
    tk.title( u'Настройка подсветки экрана')
    w,h = tk.winfo_screenwidth(),tk.winfo_screenheight()
    tk.geometry('300x50+{}+{}'.format(w//2-150,h//2-40))
    scale = Scale(tk,orient=HORIZONTAL, length=100, from_=1, to=100)
    scale.config(showvalue=1)
    scale.set(lastv)
    scale.pack(expand=1,fill=X,padx=10)
    scale.focus()
    def f():
        global lastv
        value = int(scale.get())
        if value != lastv:
            lastv = value
            sbp.call(['xbacklight','-set','%d'%lastv])
        tk.after(100,f)
    tk.bind('<Key-Escape>',lambda e: tk.destroy())    
    f()    
    tk.mainloop()


if __name__ == '__main__':
    main()
