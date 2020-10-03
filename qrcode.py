import time
import pyqrcode
from PIL import Image
#generate QR:
print("Enter the Credential for QR")
print("Enter your Name")
name=input()
print("Enter your Age")
age=input()
print("Enter your E-mail")
email=input()
print("Enter your City")
city=input()
print("Enter your State")
state=input()
print("Enter your Nationality")
country=input()
qr=pyqrcode.create(f" NAME        : { name} \n"
                   f" AGE         : { age} \n"
                   f" E-MAIL      : { email} \n"
                   f" LOCATION    : { city},{state} \n"
                   f" NATIONALITY : { country} \n")
qr.png('abc.png',scale=7)
print("QR is generated succesfully")
print("Please wait displaying QR Code...")
time.sleep(10)
im = Image.open("abc.png")
im.show()
