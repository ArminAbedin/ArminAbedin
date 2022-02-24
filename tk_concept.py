from distutils   import command
from tkinter     import *
from tkinter.tix import COLUMN
from tkinter.ttk import Combobox

win = Tk()


win.title('First concept project with tkinter')
win.geometry("450x450")


name      = Label(win , text = "Enter Name"        )
email     = Label(win , text = "Enter Email"       )
contact   = Label(win , text = "Contact Number"    )
gender    = Label(win , text = "Select Gender"     )
country   = Label(win , text = "Select Country"    )
password  = Label(win , text = "Enter Password"    )
repass    = Label(win , text = "Re-Enter Password" )


namee     = Entry(win)
emaile    = Entry(win)
contacte  = Entry(win)
gendere   = Radiobutton(win)
passworde = Entry(win)
repasse   = Entry(win)
registerb = Button(win,text="Register",width=17,height=1)
quitb     = Button(win,text="Quit")

selected  = StringVar()
gendere1  = Radiobutton(win , text = 'Male'   , value='Value 1' , variable=selected)
gendere2  = Radiobutton(win , text = 'Female' , value='Value 2' , variable=selected)
gendere3  = Radiobutton(win , text = 'Other'  , value='value 3' , variable=selected)


countrye  = Combobox(win,width=27,textvariable=None)
countrye['values']=('Iran',
'Qatar'   ,
'UAE'     ,
'England' ,
'German'  ,
'Russia'  ,
'France'  ,
'China'   ,
'Japan')
countrye.grid(column=1,row=5)
countrye.current()



name.place      ( x  =  30  , y = 30  )
email.place     ( x  =  30  , y = 80  )
contact.place   ( x  =  30  , y = 130 )
gender.place    ( x  =  30  , y = 180 )
country.place   ( x  =  30  , y = 230 )
password.place  ( x  =  30  , y = 280 )
repass.place    ( x  =  30  , y = 330 )

namee.place     ( x  =  170 , y = 30  )
emaile.place    ( x  =  170 , y = 80  )
contacte.place  ( x  =  170 , y = 130 )
gendere1.place  ( x  =  170 , y = 180 )
gendere2.place  ( x  =  240 , y = 180 )
gendere3.place  ( x  =  320 , y = 180 )
countrye.place  ( x  =  170 , y = 230 ) 
passworde.place ( x  =  170 , y = 280 )
repasse.place   ( x  =  170 , y = 330 )
registerb.place ( x  =  160 , y = 380 )
quitb.place     ( x  =  400 , y = 420 )


name.config     ( font  = ( 'Helvetica bold' , 10 ))
email.config    ( font  = ( 'Helvetica bold' , 10 ))
contact.config  ( font  = ( 'Helvetica bold' , 10 ))
gender.config   ( font  = ( 'Helvetica bold' , 10 ))
country.config  ( font  = ( 'Helvetica bold' , 10 ))
password.config ( font  = ( 'Helvetica bold' , 10 ))
repass.config   ( font  = ( 'Helvetica bold' , 10 ))



win.mainloop()