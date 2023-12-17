from tkinter import *

window=Tk()
window.geometry("400x500")
window.configure(bg="#797ef6")

def calculate_interest():
    p=int(principal.get())
    r=int(rate_of_interest.get())
    t=int(time.get())
    i=(p*t*r)/100
    interest=round(i,2)
    
    result_label.destroy()
    msg=Label(result_frame,text='Interest on Rs. '+str(p)+ 'at rate of '+str(r)+' in time '+str(t)+' is '+str(interest))
    msg.place(x=20,y=20)
    msg.pack()

app_label=Label(window,text="      SI CALCULATOR     ",bg="white",fg="black",font="Calibri 20")
app_label.place(relx=0.23,y=20)

principal_label=Label(window,text="PRINCIPAL : ",bg="#797ef6",fg="white",font=("Calibri 17 bold"))
principal_label.place(x=20,y=90)

principal=Entry(window,text="",width=25,bd=2)
principal.place(x=140,y=97)

rate_of_interest_label=Label(window,text="RATE : ",bg="#797ef6",fg="white",font=("Calibri 17 bold"))
rate_of_interest_label.place(x=20,y=150)

rate_of_interest=Entry(window,text="",width=25,bd=2)
rate_of_interest.place(x=140,y=157)

time_label=Label(window,text="TIME : ",bg="#797ef6",fg="white",font=("Calibri 17 bold"))
time_label.place(x=20,y=210)

time=Entry(window,text="",width=25,bd=2)
time.place(x=140,y=217)

calculate_button=Button(window,text="CALCULATE",fg="black",bg="white",command=calculate_interest)
calculate_button.place(x=160,y=270)

result_frame=LabelFrame(window,text="Result",bg="white",fg="black",font=("Calibri",12))
result_frame.pack(padx=40,pady=40)
result_frame.place(x=20,y=350)

result_label=Label(result_frame,text="",bg="white",fg="black",font=("Calibri",15),width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()