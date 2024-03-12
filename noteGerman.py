# A simple flashcard-like app for learning German. If you like it, edit and use as you wish. P.S. My designing is awful :)
import customtkinter
import sqlite3 
import random 

con = sqlite3.connect('Deutsch_Words.db')

cur = con.cursor()

cur.execute("select * from GermanW")
results = cur.fetchall()
nrow = len(results) 
print(nrow)
global l_nrow
l_nrow = list(range(1,int(nrow)+1))
print(l_nrow)
random.shuffle(l_nrow)
customtkinter.set_appearance_mode("system")

root = customtkinter.CTk()
root.title('LearnGermanWithRawley')



def sub_func():
    if len(l_nrow) == 0:
        root.destroy()
    else:
        global val
        val = l_nrow[0] # l_nrow[random.randint(0,len(l_nrow))-1]
        login(val)
        del l_nrow[0]
    

def login(val):
    #random.shuffle(l_nrow)
    print(l_nrow)
    cons = sqlite3.connect('Deutsch_Words.db')
    curs = cons.cursor()
    curs.execute("SELECT * FROM GermanW where id=?", (val,))
    txt = curs.fetchone()
    label.configure(text = str(txt[0]))
    tlabel.configure(text = str(txt[1]))
    slabel.configure(text= 'Meaning')
    cons.close()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

global label
label = customtkinter.CTkLabel(master=frame, text="Welcome", font=("Comic Sans MS", 14, "bold"))
label.pack(pady=12, padx=10)

global slabel 
slabel = customtkinter.CTkLabel(master=frame, text="To")
slabel.pack(pady=12, padx=10)

global tlabel 
tlabel =  customtkinter.CTkLabel(master=frame, text="Learning", font=("Comic Sans MS", 14, "bold"))
tlabel.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text='Next', command=sub_func)
button.pack(pady=12, padx=10)

con.close()
root.mainloop()
