import math

import pandas as pd

import tkinter as tk

from tkinter import*

root=tk.Tk()
root.title("Create WELLTRACK")

def clickbutton():
    top = int(top_entry.get())  # по вертикали
    a = int(a_entry.get()) # угол при Т1 И Т2
    b = int(b_entry.get())  # угол при Т2 и Т3
    l = int(l_entry.get())  # проходка, длина проекции на х при угле бета до точки T3
    s = int(s_entry.get())  # проекция на Х при угле альфа до точки T2
    Z = int(z_entry.get()) # глубина до Т1
    X0 = int(x_entry.get())
    Y0 = int(y_entry.get())
    wellname = wellname_entry.get()
    wellq='wellq1.txt'
    T0 = {'X': X0, 'Y': Y0, 'Z': 0, 'MD': 0}
    T1 = {'X': X0, 'Y': Y0, 'Z': Z, 'MD': Z}
    T2 = {'X': X0 + math.cos(math.radians(a)) * s, 'Y': Y0 + math.sin(math.radians(a)) * s, 'Z': top,
          'MD': T1.get("MD") + math.sqrt(
              (X0 - math.cos(math.radians(a) * s)) ** 2 + (Y0 - math.sin(math.radians(a) * s)) ** 2 + (Z - top) ** 2)}
    T3 = {'X': T2.get("X") + math.cos(math.radians(b) * l), 'Y': T2.get('Y') + math.sin(math.radians(b)) * l, 'Z': top,
          'MD': T2.get("MD") + math.sqrt(
              (T2.get('X') - T2.get("X") + math.cos(math.radians(b) * l) ** 2) + T2.get('Y') + (
                          T2.get('Y') + math.sin(math.radians(b)) * l) ** 2)}

    combined = [T0, T1, T2, T3]
    df = pd.DataFrame(combined)
    with open('wellq1.txt', 'a') as file:
        file.write('/')
        file.write(f'\n{wellname}' )



        file.write(df.to_csv(index=False, sep=' ', header= False))


   # df.to_csv('wellq1.txt', sep=' ', index=False, header = False)
   # with open(wellq, 'r', encoding='utf-8') as file:
     #   content = file.readlines()
    #new_content = [wellname + '\n']
    #with open('wellq1.txt', 'r', encoding='utf-8') as temp_file:
     #   new_content.extend(temp_file.readlines())
   # new_content.append('/\n')
   # with open(wellq, 'a+', encoding='utf-8') as file:
     #   file.writelines(new_content)
    #file = open('wellq1.txt', 'a')adlines()
    #content.insert(0, wellname +'\n')
    #with open(wellq, 'w', encoding='utf8') as file:
     #   file.writelines(content)
    #with open(wellq, 'r', encoding='utf-8') as file:
     #   content = file.readlines()
    #content.append('/' + '\n')
    #with open(wellq, 'w', encoding='utf8') as file:
    #    file.writelines(content)
    #df.to_csv('wellq1.txt', sep=' ',

    #with open('wellq1.txt', "a") as file:
   #     file.write(df)

    # file.write(wellname + '\n')
   # df.to_csv('wellq1.txt', sep=' ', index=False, header = False)
    #file.write(df + '\n')
  #  file.write('/'+ '\n')
  #  file.close()


    return(df)
def keypress(event):
    ctrl = (event.state & 0x4) !=0
    if event.keycode ==88 and ctrl and event.keysm.lower() !='x':
        event.widget.event_generate('<<Cut>>')
    if event.keycode ==86 and ctrl and event.keysm.lower() !='v':
        event.widget.event_generate('<<Paste>>')
    if event.keycode ==67 and ctrl and event.keysm.lower() !='c':
        event.widget.event_generate('<<Copy>>')
root.bind('<Control-KeyPress>', keypress)
wellname_label =tk.Label(root, text = 'Well Name:')
wellname_label.grid(row=0, column =0, padx =10, pady = 10, sticky ='e')
wellname_entry = tk.Entry(root, width = 30)
wellname_entry.grid(row=0, column = 1, padx = 10, pady = 10)
#
x_label =tk.Label(root, text = 'X_0:')
x_label.grid(row=1, column =0, padx =10, pady = 10, sticky ='e')
x_entry = tk.Entry(root, width = 30)
x_entry.grid(row=1, column = 1, padx = 10, pady = 10)
#
y_label =tk.Label(root, text = 'Y_0:')
y_label.grid(row=2, column =0, padx =10, pady = 10, sticky ='e')
y_entry = tk.Entry(root, width = 30)
y_entry.grid(row=2, column = 1, padx = 10, pady = 10)

l_label =tk.Label(root, text = 'L:')
l_label.grid(row=3, column =0, padx =10, pady = 10, sticky ='e')
l_entry = tk.Entry(root, width = 30)
l_entry.grid(row=3, column = 1, padx = 10, pady = 10)

s_label =tk.Label(root, text = 'S:')
s_label.grid(row=4, column =0, padx =10, pady = 10, sticky ='e')
s_entry = tk.Entry(root, width = 30)
s_entry.grid(row=4, column = 1, padx = 10, pady = 10)

top_label =tk.Label(root, text = 'Top:')
top_label.grid(row=5, column =0, padx =10, pady = 10, sticky ='e')
top_entry = tk.Entry(root, width = 30)
top_entry.grid(row=5, column = 1, padx = 10, pady = 10)
#
a_label =tk.Label(root, text = 'ANG_T2:')
a_label.grid(row=6, column =0, padx =10, pady = 10, sticky ='e')
a_entry = tk.Entry(root, width = 30)
a_entry.grid(row=6, column = 1, padx = 10, pady = 10)

b_label =tk.Label(root, text = 'ANG_T3:')
b_label.grid(row=7, column =0, padx =10, pady = 10, sticky ='e')
b_entry = tk.Entry(root, width = 30)
b_entry.grid(row=7, column = 1, padx = 10, pady = 10)

z_label =tk.Label(root, text = 'Z:')
z_label.grid(row=8, column =0, padx =10, pady = 10, sticky ='e')
z_entry = tk.Entry(root, width = 30)
z_entry.grid(row=8, column = 1, padx = 10, pady = 10)
start_button = tk.Button(root, text = 'Create WELLTRACK', command = clickbutton)
start_button.grid(row = 9, column = 0, columnspan = 2, padx = 10, pady = 10)
root.mainloop()
print('#Welltrack Well_1')
#print(well_1(top, a, b, l, s, Z))