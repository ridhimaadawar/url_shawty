# ------ Libraries to be used for the project ------
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from ttkthemes import ThemedStyle
from pyshorteners import Shortener
import pyperclip
import qrcode
# Create a QR code instance
qr = qrcode.QRCode(
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=10,
border=4,
)
# Data to be encoded in the QR code
data = "https://youtu.be/vLqTf2b6GZw?si=KJ6--K13pZUuzOso"
# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)
# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")
# Save the image or display it
img.save("qrcode.png")
img.show()
tiny_url = "" #IT is a global variable where the tiny url will store
# ------ THIS FUNCTION WILL BE CALLED WHEN GENERATE BUTTON WILL BE
CLICKED ------
def short():
global tiny_urlx
url = str(url_input.get())
if len(url) <= 0 :
messagebox.showwarning("not input","Please insert url to continue")
else:
21
try:
short = Shortener()
tiny_url = short.tinyurl.short(url)
output_entry.delete(0,END)
output_entry.insert(0,tiny_url)
short_frame.pack(expand=1,fill=BOTH)
except:
messagebox.showwarning("Invalid URL","Please enter valid url")
# ------ THIS FUCTION WILL BE CALLED WHEN COPY BUTTON WILL BE
CLICKED ------
def copy():
pyperclip.copy(tiny_url)
# ------ CONFIGRATIONS FOR THE UI WINDOW ------
root = Tk()
root.geometry("1000x400")
root.maxsize("800","560")
root.minsize("700","400")
root.title("URL SHORTENER AND QR CODE GENERATOR")
style = ThemedStyle(root)
style.set_theme("yaru")
# ------ MAIN FRAME UNDER WHICH ALL THE WIDGETS WILL APPEAR ------
main_frame = ttk.Frame(root)
main_frame.pack(fill="both",expand=True)
# ------ CODE FOR HEADING ------
heading_frame = ttk.Frame(main_frame,padding=60)
heading_frame.pack()
heading_label = ttk.Label(heading_frame,text = "URL SHORTNER AND QR CODE
GENERATOR",font=("verdana",25,"bold"))
heading_label.pack()
# ------ CODE FOR INPUT FRAME ------
input_frame = ttk.Frame(main_frame,padding=20)
input_frame.pack(fill="both")
input_frame.columnconfigure([0,2],weight=1) 
input_frame.columnconfigure(1,weight=3)
# ------ CODE FOR TAKING URL AS INPUT ------
url_label = ttk.Label(input_frame,text="ENTER URL HERE = ")
url_label.grid(row = 0,column = 0)
22
url_input = ttk.Entry(input_frame)
url_input.grid(row = 0,column=1,ipadx=100)
generate_btn = ttk.Button(input_frame,text = "GENERATE",command=short)
generate_btn.grid(row=0,column=2)
# ------ CODE FOR DISPLAYING THE OUTPUT AS SHORT URL ------
short_frame = ttk.Frame(main_frame)
short_frame.pack_forget()
output_label = ttk.Label(short_frame,text= "Your output : ",font=("verdana",16,"bold"))
output_label.pack(anchor="center",pady=(10,0))
output_frame = ttk.Frame(short_frame)
output_frame.pack(anchor=CENTER, expand = 1,pady=(0,60))
output_entry = ttk.Entry(output_frame)
output_entry.grid(row = 0,column=0,ipadx=50)
copy_button = ttk.Button(output_frame,text="COPY",command= copy)
copy_button.grid(row = 0,column=1,padx=(10,0))
# ------ CUSTOMISE YOUR CREDITS (OFFICIALLY CREATED BY Ridhimaa Dawar and
Ram Tanwar) ------
credit = ttk.Label(main_frame,text="Copyright © 2023 Ridhimaa Dawar and Ram Tanwar")
credit.pack(side="bottom",expand=0,anchor="center",pady=(0,5))
root.mainloop()
