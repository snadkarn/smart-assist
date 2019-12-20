import tkinter as tk

m=tk.Tk()
m.title('Smart assist') 
w = tk.Label(m, text="SMART ASSIST")
w.pack()
w.config(font=("Courier", 44))
m.configure(background='black')

button2 = tk.Button(m, text='home automation',font=("Courier", 30)) 

button2.pack(padx=50, pady=10, side=tk.LEFT)

button1 = tk.Button(m, text='movement',font=("Courier", 30))
#button1.invoke() 

button1.pack(padx=50, pady=10, side=tk.LEFT)

button3 = tk.Button(m, text='distress message',font=("Courier", 30)) 

button3.pack(padx=50, pady=10, side=tk.LEFT)



m.mainloop()