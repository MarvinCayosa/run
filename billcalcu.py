from tkinter import *

window = Tk()
window.title("Bill Calculator")
window.geometry("400x570")


def get_total():
    bill = float(txt_bill.get())
    tip = float(txt_tip.get())
    tax = float(txt_tax.get())
    tip_total = (tip / 100) * bill
    tax_total = (tax / 100) * bill

    total_bill = tip_total + tax_total + bill

    total.config(text=round(total_bill, 2))
    tip_tot.config(text=round(tip_total, 2))
    tax_tot.config(text=round(tax_total, 2))


roundbox = PhotoImage(file="wextbox.png")
calculate = PhotoImage(file="calculate.png")

lbl_title = Label(window, text="BILL CALCULATOR", bg='#586F6B', fg='white', font=("MOON GET!", 20),
                  highlightbackground='white', highlightthickness=5, width=100, height=2)
lbl_title.pack()

bg = Label(window, bg='#DE847B', width=300, height=500, highlightbackground='white', highlightthickness=5)
bg.pack()

image = Label(window, image=roundbox, bg='#DE847B').place(x=55, y=140)
image1 = Label(window, image=roundbox, bg='#DE847B').place(x=55, y=195)
image2 = Label(window, image=roundbox, bg='#DE847B').place(x=55, y=250)

txt_bill = Entry(window, font=("Courier", 10), text="", bd=0, width=10)
txt_bill.place(x=200, y=158)
txt_tip = Entry(window, font=("Courier", 10), text="", bd=0, width=10)
txt_tip.place(x=200, y=213)
txt_tax = Entry(window, font=("Courier", 10), text="", bd=0, width=10)
txt_tax.place(x=200, y=268)

lbl_bill = Label(window, text="BILL", fg='white', font=("The Bold Font", 16), bd=0, bg='#DE847B').place(x=90, y=155)
lbl_tip = Label(window, text="TIP (%)", fg='white', font=("The Bold Font", 16), bd=0, bg='#DE847B').place(x=90, y=210)
lbl_tax = Label(window, text="TAX (%)", fg='white', font=("The Bold Font", 16), bd=0, bg='#DE847B').place(x=90, y=265)

total_output = Frame(window, bg='#7F9183', width=400, height=170, highlightbackground='white', highlightthickness=5)
total_output.place(x=0, y=400)

total = Label(total_output, text='0000.00', bg='#7F9183', fg='white', font=("The Bold Font", 20))
total.place(x=230, y=78)
tip_tot = Label(total_output, text='00.00', bg='#7F9183', fg='white', font=("The Bold Font", 16))
tip_tot.place(x=90, y=38)
tax_tot = Label(total_output, text='000.00', bg='#7F9183', fg='white', font=("The Bold Font", 16))
tax_tot.place(x=270, y=38)

Label(total_output, text='P', bg='#7F9183', fg='white', font=("The Bold Font", 20)).place(x=200, y=78)
Label(total_output, text='P', bg='#7F9183', fg='white', font=("The Bold Font", 16)).place(x=70, y=38)
Label(total_output, text='P', bg='#7F9183', fg='white', font=("The Bold Font", 16)).place(x=250, y=38)


Label(total_output, text="TOTAL BILL:", fg='white', font=("The Bold Font", 20), bd=0, bg='#7F9183').place(x=30, y=80)
Label(total_output, text="TIP:", fg='white', font=("The Bold Font", 16), bd=0, bg='#7F9183').place(x=30, y=40)
Label(total_output, text="TAX:", fg='white', font=("The Bold Font", 16), bd=0, bg='#7F9183').place(x=200, y=40)

btn_comp = Button(window, image=calculate, command=get_total, bg='#DE847B', borderwidth=0)
btn_comp.place(x=45, y=320)

window.mainloop()
