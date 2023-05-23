import tkinter as tk
from tkinter import messagebox
import math 

# Define constants  
#تعریف مقادیر ثابت
WIDTH = 500 
HEIGHT = 450 
RADIUS = 150 
DISTANCE = 25 

# Create the main window and canvas
# ایجاد کردن پنجره‌ی اصلی  
root = tk.Tk()
root.title(' محاسبه‌ی نسبت‌های مثلثاتی به کمک دایره‌ی مثلثاتی')
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT) 
canvas.pack() 

# Draw the circle and its circumference  
# رسم دایره و محیط آن
canvas.create_oval(WIDTH/2-RADIUS, HEIGHT/2-RADIUS, WIDTH/2+RADIUS, HEIGHT/2+RADIUS, outline="black", width=2, fill=("#c0ecbf")) 
for angle in range(0, 360, 30): 
     x = WIDTH/2 + (RADIUS+DISTANCE) * math.cos(math.radians(angle)) 
     y = HEIGHT/2 - (RADIUS+DISTANCE) * math.sin(math.radians(angle)) 
     canvas.create_text(x, y, text=str(angle), font=("Arial Rounded MT Bold", 11), fill=("black")) 
     dot_x = WIDTH/2 + RADIUS * math.cos(math.radians(angle)) 
     dot_y = HEIGHT/2 - RADIUS * math.sin(math.radians(angle))
     canvas.create_oval(dot_x-5, dot_y-5, dot_x+5, dot_y+5, fill="navy")

# Draw the x and y axes
# رسم محورهای مختصات  
canvas.create_line(WIDTH/2-RADIUS, HEIGHT/2, WIDTH/2+RADIUS, HEIGHT/2, width=2) 
canvas.create_line(WIDTH/2, HEIGHT/2-RADIUS, WIDTH/2, HEIGHT/2+RADIUS, width=2) 

# Define the trigonometric function
# تعریف توابع مثلثاتی  
def calculate_trig(angle): 
     sine = round(math.sin(angle), 2) 
     cosine = round(math.cos(angle), 2) 
     tangent = round(math.tan(angle), 2)
     if cosine == 1 or cosine == -1:
         cotangent = "Ꝏ"
     else:
        cotangent = round(1/tangent, 2)
     return sine, cosine, tangent, cotangent 

# Create a label to display the selected angle 
# انتخاب یک برچسب برای نمایش زاویه‌ی انتخاب شده 
angle_label = tk.Label(root, text="Angle: 0", font=("Arial Rounded MT Bold", 12), fg="navy") 
angle_label.pack() 

# Create labels to display the trigonometric ratios
#ایجاد برچسب برای نمایش نسبت‌های مثلثاتی 
sine_label = tk.Label(root, text="Sine: 0", font=("Arial Rounded MT Bold", 12), fg="#7300bf") 
cosine_label = tk.Label(root, text="Cosine: 0", font=("Arial Rounded MT Bold", 12), fg="#7300bf") 
tangent_label = tk.Label(root, text="Tangent: 0", font=("Arial Rounded MT Bold", 12), fg="#7300bf") 
cotangent_label = tk.Label(root, text="Cotangent: 0", font=("Arial Rounded MT Bold", 12), fg="#7300bf") 
sine_label.pack()
cosine_label.pack()
tangent_label.pack() 
cotangent_label.pack()
