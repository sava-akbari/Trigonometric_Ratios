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

# Create entry fields for the ratios
# ایجاد ورودی مربوط به هر زاویه‌ی مثلثاتی
sine_entry = tk.Entry(root, font=("Arial Rounded MT Bold", 11), bd=3, bg="#c0ecbf")
cosine_entry = tk.Entry(root, font=("Arial Rounded MT Bold", 11), bd=3, bg="#c0ecbf")
tangent_entry = tk.Entry(root, font=("Arial Rounded MT Bold", 11), bd=3, bg="#c0ecbf")
Cotangent_entry = tk.Entry(root, font=("Arial Rounded MT Bold", 11), bd=3, bg="#c0ecbf")

# Create labels for the entry fields
# ایجاد عنوان برای هر ورودی 
sine_label = tk.Label(root, text="sine:", font=("Arial Rounded MT Bold", 14), fg ="navy")
cosine_label = tk.Label(root, text="cosine:", font=("Arial Rounded MT Bold", 14), fg ="navy")
tangent_label = tk.Label(root, text="tangent:", font=("Arial Rounded MT Bold", 14), fg ="navy")
Cotangent_label = tk.Label(root, text="Cotangent:", font=("Arial Rounded MT Bold", 14), fg ="navy")

# Set the positions of the labels and entry fields using pack
#مشخص کردن مکان قرار گیری ورودی و عنوان مربوط به آن 
sine_label.pack(side=tk.TOP, padx=10, pady=5)
sine_entry.pack(side=tk.TOP, padx=10, pady=5)
cosine_label.pack(side=tk.TOP, padx=10, pady=5)
cosine_entry.pack(side=tk.TOP, padx=10, pady=5)
tangent_label.pack(side=tk.TOP, padx=10, pady=5)
tangent_entry.pack(side=tk.TOP, padx=10, pady=5)
Cotangent_label.pack(side=tk.TOP, padx=10, pady=5)
Cotangent_entry.pack(side=tk.TOP, padx=10, pady=5)

# Create a function to calculate the remaining ratios
# ساختن تابعی برای محاسبه‌ی نسبت ها
def calculate_ratios():

    # Get the selected ratio
    #دریافت نسبت انتخاب شده
    ratio = ratio_var.get()

    # Get the entered value
    # دریافت مقدار وارد شده برای آن نسبت
    try:
        if ratio == "sine":
            value = float(sine_entry.get())
        elif ratio == "cosine":
            value = float(cosine_entry.get())
        elif ratio == "tangent":
            value = float(tangent_entry.get())
        elif ratio == "Cotangent":
            value = float(Cotangent_entry.get())
    except ValueError:
        result_label.config(text="خطا: ورودی نامعتبر", font=("B Titr", 14), pady=5, fg="#0ca2a4")
        return

    # Check if the value is within range for sine and cosine
    # چک کردن ورودی معتبر برای مقادیر سینوس و کسینوس
    if ratio in ["sine", "cosine"] and (value > 1 or value < -1):
        result_label.config(text="خطا: مقدار ورودی باید در بازه‌ی [1, 1-] باشد", font=("B Titr", 14), pady=10, fg="#0ca2a4")
        return

    # Calculate the remaining ratios
    #محاسبه‌ی بقیه‌ی نسبت‌ها
    if ratio == "sine":
        cosine = cos(asin(value))
        tangent = tan(asin(value))
        Cotangent = 1/tan(asin(value))

    elif ratio == "cosine":
        sine = sin(acos(value))
        tangent = tan(acos(value))
        Cotangent = 1/tan(acos(value))

    elif ratio == "tangent":
        sine = sin(atan(value))
        cosine = cos(atan(value))
        Cotangent = 1/value

    elif ratio == "Cotangent":
        sine = cos(atan(value))
        cosine = sin(atan(value))
        tangent = (1/value)

    # Display the results
    # نمایش جواب ها
    if ratio == "sine":
        result_label.config(text=f"cosine: {cosine:.3f}, tangent: {tangent:.3f}, Cotangent: {Cotangent:.3f}", font=("Arial Rounded MT Bold", 14), pady=10, fg="navy")
    elif ratio == "cosine":
        result_label.config(text=f"sine: {sine:.3f}, tangent: {tangent:.3f}, Cotangent: {Cotangent:.3f}", font=("Arial Rounded MT Bold", 14), pady=10, fg="navy")
    elif ratio == "tangent":
        result_label.config(text=f"sine: {sine:.3f}, cosine: {cosine:.3f}, Cotangent: {Cotangent:.3f}", font=("Arial Rounded MT Bold", 14), pady=10, fg="navy")
    elif ratio == "Cotangent":
        result_label.config(text=f"sine: {sine:.3f}, cosine: {cosine:.3f}, tangent: {tangent:.3f}", font=("Arial Rounded MT Bold", 14), pady=10, fg="navy")

# Create a button to calculate the ratios
# ایجاد دکمه برای اجرای برنامه
calculate_button = tk.Button(root, text="محاسبه", font=("B Titr", 14), command=calculate_ratios, pady=0.05, bd=3, width=8, fg="#7300bf")
calculate_button.pack()
