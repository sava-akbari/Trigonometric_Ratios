import tkinter as tk
from math import sin, cos, tan, radians

# Define constants  
#تعریف مقادیر ثابت
WIDTH = 500
HEIGHT = 20

# create GUI
# ایجاد رابط کاربری گرافیکی
root = tk.Tk()
root.title("Trigonometric Ratio Comparator")
root.configure(background='#F4F4F4')
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT) 
canvas.pack() 

def compare_ratios():
    ratio1 = entry1.get().lower()
    ratio2 = entry2.get().lower()

    # check if input format is valid
    # چک کردن فُرم صحیح ورودی کاربر
    if len(ratio1.split()) != 2 or len(ratio2.split()) != 2:
        result_label.config(text="!لطفاً بین نسبت مثلثاتی و مقدار زاویه فاصله بدهید", font=("B Titr", 16), pady=5, fg="#0ca2a4")
        return
    
    # check if ratios are in correct format
    #چک کردن فرم درست نسبت‌های مثلثاتی ورودی
    if not ("sin" in ratio1 or "cos" in ratio1 or "tan" in ratio1 or "cot" in ratio1 or 
            "sine" in ratio1 or "cosine" in ratio1 or "tangent" in ratio1 or "cotangent" in ratio1):
        result_label.config(text="خطا : ورودی نامعتبر", font=("B Titr", 14), pady=5, fg="#0ca2a4")
        return
    if not ("sin" in ratio2 or "cos" in ratio2 or "tan" in ratio2 or "cot" in ratio2 or 
            "sine" in ratio2 or "cosine" in ratio2 or "tangent" in ratio2 or "cotangent" in ratio2):
        result_label.config(text="خطا : ورودی نامعتبر", font=("B Titr", 14), pady=5, fg="#0ca2a4")
        return
    
    # extract x value from ratios
    # استخراج زاویه مورد نظر کاربر از ورودی
    x1 = int(ratio1.split(" ")[-1])
    x2 = int(ratio2.split(" ")[-1])
    
    # check if angle value is valid 
    # چک کردن معتبر بودن مقدار ورودی کاربر
    if abs(x1) > 360 or abs(x2) > 360 or abs(x1) < -360 or abs(x2) < -360: 
        result_label.config(text="خطا: مقدار زاویه باید در بازه‌ی [360, 360-] باشد", font=("B Titr", 17), pady=5, fg="#0ca2a4")
    elif ratio1.startswith("tan") and int(ratio1.split()[-1]) % 180 == 90:
        result_label.config(text="!ورودی تعریف نشده است", font=("B Titr", 17), pady=5, fg="#0ca2a4")
    elif ratio2.startswith("tan") and int(ratio2.split()[-1]) % 180 == 90:
        result_label.config(text="!ورودی تعریف نشده است", font=("B Titr", 17), pady=5, fg="#0ca2a4")
    elif ratio1.startswith("cot") and int(ratio1.split()[-1]) % 180 == 0:
        result_label.config(text="!ورودی تعریف نشده است", font=("B Titr", 17), pady=5, fg="#0ca2a4")
    elif ratio2.startswith("cot") and int(ratio2.split()[-1]) % 180 == 0:
        result_label.config(text="!ورودی تعریف نشده است", font=("B Titr", 17), pady=5, fg="#0ca2a4")
    else: 
        # convert ratios to numerical values
        # تبدیل نسبت‌های مثلثاتی به مقدار عددی مربوطه 
        if "sin" in ratio1 or "sine" in ratio1: 
            val1 = round(sin(float(radians(x1))), 2) 
        elif "cos" in ratio1 or "cosine" in ratio1: 
            val1 = round(cos(float(radians(x1))), 2) 
        elif "tan" in ratio1 or "tangent" in ratio1: 
            val1 = round(tan(float(radians(x1))), 2) 
        else: 
             val1 = 1 / round(tan(float(radians(x1))), 2) 
 
    if "sin" in ratio2 or "sine" in ratio2: 
        val2 = round(sin(float(radians(x2))), 2) 
    elif "cos" in ratio2 or "cosine" in ratio2: 
        val2 = round(cos(float(radians(x2))), 2) 
    elif "tan" in ratio2 or "tangent" in ratio2: 
        val2 = round(tan(float(radians(x2))), 2) 
    else: 
        val2 = round(1 /tan(float(radians(x2))), 2) 
 
    # compare ratios and display result
    # مقایسه مقادیر و نمایش نتیجه 
    if val1 < val2: 
        result_label.config(text=f"{ratio1} < {ratio2}",font=("Arial Rounded MT Bold", 17), fg="navy", bg='#F4F4F4') 
    elif val1 > val2: 
        result_label.config(text=f"{ratio1} > {ratio2}",font=("Arial Rounded MT Bold", 17), fg="navy", bg='#F4F4F4') 
    else: 
        result_label.config(text=f"{ratio1} = {ratio2}",font=("Arial Rounded MT Bold", 17), fg="navy", bg='#F4F4F4')

# نوشتن متن سوال و نمایش به کاربر
q_label = tk.Label(root, text="مقادیر مورد نظر را برای مقایسه وارد کنید",font=("B Titr", 23), fg="navy", bg='#F4F4F4')
q_label.pack(pady=(0,3))
inf_label = tk.Label(root, text="FORMAT = sin/cos/tan/cot x",font=("Arial Rounded MT Bold", 15), fg="navy", bg='#F4F4F4')
inf_label.pack(pady=(0,20))

#ایجاد برچسب برای ورودی اول
label1 = tk.Label(root, text=":نسبت مثلثاتی اول را وارد کنید", font=("B Titr", 16), fg="#7300bf", bg='#F4F4F4')
label1.pack()

# ساخت اولین ورودی برای دریافت نسبت مثلثاتی اول
entry1 = tk.Entry(root, font=("Arial Rounded MT Bold", 14),fg="navy", bd=2, bg="#c0ecbf")
entry1.pack(pady=(2,25))

#ایجاد برچسب برای ورودی دوم
label2 = tk.Label(root, text=":نسبت مثلثاتی دوم را وارد کنید", font=("B Titr", 16), fg="#7300bf", bg='#F4F4F4')
label2.pack()

# ساخت دومین ورودی برای دریافت نسبت مثلثاتی دوم
entry2 = tk.Entry(root, font=("Arial Rounded MT Bold", 14), fg="navy", bd=2, bg="#c0ecbf")
entry2.pack(pady=(2,25))

# ایجاد دکمه‌ی مقایسه
compare_button = tk.Button(root, text="مقایسه", font=("B Titr", 14), command=compare_ratios, pady=0.05, bd=3, width=8, fg="#7300bf")
compare_button.pack(pady=10)

# چاپ نتیجه
result_label = tk.Label(root, text="", font=("Arial Rounded MT Bold", 17), fg="navy", bg='#F4F4F4')
result_label.pack(pady=10)

root.mainloop()
