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
