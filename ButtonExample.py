from tkinter import *

#window = Tk()

#window.title('button example')

def Exit():
	print('ByeBye!')
	window.destroy()

btn_end = Button( window, text = 'Close', command = Exit)

def tog():
	if window.cget('bg') == 'yellow':
		window.configure(bg = 'gray')
	else:
		window.configure(bg = 'yellow')

btn_tog = Button(window, text = 'Switch', command = tog)

btn_tog.pack(side = LEFT, padx = 60, pady = 20)
btn_end.pack(side = LEFT, padx = 60, pady = 20)



#window.mainloop()