from os import name
import tkinter as tk
from Variables import names


#CReates a window, and assigns it a variable,
#  title, and dimensions, as well as position
tink = tk.Tk()
tink.title("Student Ranking")
tink.geometry("450x450+650+200")



#Creates the testbox in the tink wibndow(container)
textbox = tk.Entry(tink)

#Creates a function to append the persons 
#name into the names list, and clears the input tab
def username():
    names.append(textbox.get())
    textbox.delete(0, tk.END)
    print(names)



#Creates the button to Submit the data, which 
# then calls the comand to clear the tab, and append
#the data to the names list
button = tk.Button(tink, text = "Submit", command = username )
textbox.pack()
button.pack()
#Loops all the functions to output. INITILISES IT SO PLACE LAST
tink.mainloop()





