from tkinter import *
from PIL import Image,ImageTk 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#creating window
window= Tk()
window.title('dashboard')
window.geometry('1200x700+0+0')
#adding image to title 
pil_image = Image.open('inventory-management.png')
pil_image = pil_image.resize((100, 100))
bg_image = ImageTk.PhotoImage(pil_image)
#creating functioning logout button
logout_button=Button(window,text='logout',font=( 'Calabri', 20 ,'bold' ),bg='red',fg='white',command=window.destroy)
logout_button.place(x=1000,y=20,width=100,height=40)
#creating title 
title_label =Label(window,text='stock management System',image=bg_image, font =('Calabri',40,'bold'),compound='left')
title_label.place(x=0,y=0)
#creating menu 
menubar = Frame(window, bg='#009688')
menubar.place(x=0, y=100, relwidth=1, height=50)
#buttons along menu
menu_label = Label(menubar, text='Menu', font=('Calibri', 20, 'bold'),bg='#009688', fg='white')
menu_label.pack(side=LEFT, padx=20)

employee_button = Button(menubar, text='Employee', font=('Calibri', 16, 'bold'), bd=3,)
employee_button.pack(side=LEFT, padx=5, pady=5)

supplier_button = Button(menubar, text='Supplier', font=('Calibri', 16, 'bold'), bd=3,)
supplier_button.pack(side=LEFT, padx=5, pady=5)

category_button = Button(menubar, text='Category', font=('Calibri', 16, 'bold'), bd=3,)
category_button.pack(side=LEFT, padx=5, pady=5)

product_button = Button(menubar, text='Product', font=('Calibri', 16, 'bold'), bd=3,)
product_button.pack(side=LEFT, padx=5, pady=5)

sales_button = Button(menubar, text='Sales', font=('Calibri', 16, 'bold'), bd=3,)
sales_button.pack(side=LEFT, padx=5, pady=5)

#creating graph 
graph_frame = Frame(window, bg='white')
graph_frame.place(x=0, y=150, relwidth=1, height=550)

categories=['employees', 'suppliers', 'categories', 'products', 'sales']
values=[10, 5, 8, 12,7]
fig = Figure(figsize=(8, 4.5), dpi=100)
ax = fig.add_subplot(111)
bars = ax.bar(categories, values)   
ax.set_title('System Statistics') 
ax.bar_label(bars)    

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill=BOTH, expand=True)

window.mainloop()
