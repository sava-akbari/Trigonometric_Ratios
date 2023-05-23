import tkinter as tk
from tkinter import *
from tkinter import Radiobutton
from math import sin, cos, tan, asin, acos, atan, radians

# Define constants  
#تعریف مقادیر ثابت
WIDTH = 450 
HEIGHT = 20

# Create the main window
# ایجاد کردن پنجره‌ی اصلی 
root = tk.Tk()
root.title("محاسبه‌ی نسبت‌های مثلثاتی با داشتن یک نسبت")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT) 
canvas.pack() 

# Create a radio button group for the trigonometric ratios
# ایجاد گزینه‌ها برای انتخاب نسبت مثلثاتی
ratio_var = tk.StringVar(value="sine")
ratio_frame = tk.Frame(root)
ratio_frame.pack(padx=10, pady=(5,10))

label = tk.Label(ratio_frame, text="نسبت مثلثاتی‌ای که دارید را انتخاب کرده و در جای خالی وارد کنید", font=("B Titr", 16), fg ="navy")
label.pack(padx=(0,0), pady=(5, 3))

rb_sine = Radiobutton(ratio_frame, text="sine", variable=ratio_var, value="sine", padx=35, pady=3, font=("Arial Rounded MT Bold", 14), fg="#7300bf")
rb_sine.pack(side=tk.RIGHT)

rb_cosine = Radiobutton(ratio_frame, text="cosine", variable=ratio_var, value="cosine", padx=35, pady=3, font=("Arial Rounded MT Bold", 14), fg="#7300bf")
rb_cosine.pack(side=tk.RIGHT)

rb_tangent = Radiobutton(ratio_frame, text="tangent", variable=ratio_var, value="tangent", padx=35, pady=3, font=("Arial Rounded MT Bold", 14), fg="#7300bf")
rb_tangent.pack(side=tk.RIGHT)

rb_tangent = Radiobutton(ratio_frame, text="Cotangent", variable=ratio_var, value="Cotangent", padx=35, pady=3, font=("Arial Rounded MT Bold", 14), fg="#7300bf")
rb_tangent.pack(side=tk.RIGHT)
