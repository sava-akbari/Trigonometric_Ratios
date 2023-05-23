import tkinter as tk
from tkinter import ttk
import subprocess 
from tkinter import messagebox


# Create main window
# ایجاد پنجره‌ی اصلی
root = tk.Tk()
root.geometry("650x450")
root.title("مثلثات")

# Create tabs
# ایجاد برگه‌ها
tab_control = ttk.Notebook(root)

# Tab 1 - Home
# برگه‌ی اول - خانه
tab_home = ttk.Frame(tab_control)
tab_control.add(tab_home, text='خانه')

# Create title label
# ساختن عنوان صفحه‌ی خانه
title_label = tk.Label(tab_home, text="تاریخچه‌ای مختصر از پیدایش مثلثات", font=("B Titr", 25), fg="#7300bf")
title_label.pack(pady=5)

#Create a canvas object
# ایجاد یک شی در بوم
Canvas= tk.Canvas(tab_home, width= 580, height=300, bg="#c0ecbf")

#Add a text in Canvas
# اضافه کردن توضیحات به بوم
Canvas.create_text(280, 130, text="""   مثلثات شاخه ای از ریاضیات است که به روابط بین اضلاع و زوایای مثلث ها می‌پردازد
             منشأ آن را می توان در تمدن های باستانی مانند بابلی ها، مصری ها و یونانی‌ها 
            جست‌وجو کرد. که از مفاهیم اولیه مثلثاتی برای اهداف عملی مانند اندازه گیری 
  زمین و سازه های ساختمانی استفاده می کردند. هیپارخوس، ریاضیدان یونانی،  اولین
                 جدول مثلثاتی را توسعه داد؛ و بعدها، ریاضیدانان مسلمانی مانند خوارزمی و
     بیرونی سهم قابل توجهی در این زمینه داشتند. امروزه از مثلثات در زمینه هایی مانند
                                                                .مهندسی، فیزیک و نجوم بسیار استفاده می شود""", fill="navy", font=("B Titr", 14))
Canvas.pack()


# Tab 2 - Program 1
#برگه دوم - برنامه‌ی اول، دایره‌ی مثلثاتی
tab_program1 = ttk.Frame(tab_control)
tab_control.add(tab_program1, text='دایره‌ی مثلثاتی')

# Create title label
# ساختن یک عنوان برای برنامه‌ی اول
program1_label = tk.Label(tab_program1, text="دایره‌ی مثلثاتی", font=("B Titr", 24), fg="#7300bf")
program1_label.pack(padx=10, pady=10)

#Create a canvas object
# ایجاد فضایی برای اضافه کردن متن توضیحات
Canvas= tk.Canvas(tab_program1, width= 570, height= 200, bg="#c0ecbf")

#Add a text in Canvas
# اضافه کردن متن توضیحات
Canvas.create_text(280,95, text="""                  .این برنامه به کاربر امکان محاسبه‌ی نسبت‌های مثلثاتی مختلف را می‌دهد
       با اجرای برنامه، دایره‌ی مثلثاتی که زوایای مختلف در اطراف آن علامت گذاری
                   شده‌اند، نمایش داده می‌شود. کاربران می‌توانند با کشیدن دکمه‌ی شروع      
        به موقعیت دلخواه روی محیط دایره، یک زاویه را انتخاب کنند. با اجرای برنامه 
                            .نسبت‌های مثلثاتی مربوطه را محاسبه شده و به کاربر نشان می‌دهد""", fill="navy", font=("B Titr", 14))
Canvas.pack()


# Tab 3 - Program 2
# برگه سوم - برنامه‌ی دوم،محاسبه‌ی نسبت‌ها
tab_program2 = ttk.Frame(tab_control)
tab_control.add(tab_program2, text='محاسبه‌ی نسبت‌ها به کمک یک نسبت')

# Create title label
# ساختن یک عنوان برای برنامه‌ی دوم
program1_label = tk.Label(tab_program2, text="محاسبه‌ی نسبت‌ها به کمک یک نسبت", font=("B Titr", 24), fg="#7300bf")
program1_label.pack(padx=10, pady=10)

#Create a canvas object
# ایجاد فضا برای اضاقه کردن توضیحات برنامه‌ی دوم
Canvas= tk.Canvas(tab_program2, width= 570, height= 200, bg="#c0ecbf")

#Add a text in Canvas
# اضافه کردن خود متن
Canvas.create_text(280,95, text="""       این برنامه به کاربر امکان محاسبه‌ی نسبت‌های مثلثاتی، به کمک داشتن یک نسبت 
       را می‌دهد. با اجرا کردن برنامه، پنجره‌ای برای کاربر باز می‌شود.از بین گزینه‌ها   
            نسبتی که مقدار آن موجود است توسط کاربر انتخاب شده، و ورودی مربوط به
       همان نسبت ظاهر می‌شود (بقیه‌ی ورود‌ها برای جلوگیری از خطا حذف می‌شوند)
    .با وارد کردن عدد، برنامه باقی نسبت‌‌ها را محاسبه کرده و به کاربر نمایش می‌دهد""", fill="navy", font=("B Titr", 14))
Canvas.pack()

# Pack tab control to main window

tab_control.pack(expand=1, fill='both')


# Function to run other project
# دستور اجرا‌ی برنامه‌ها در صفحات دوم و سوم
def run_Trigonometric_Circle():
    subprocess.call(["python","Trigonometric_Ratios\Trigonometric_Circle.py"])

# Add button to run other project
# ایجاد دکمه برای اجرا‌ی برنامه
run_project_button = tk.Button(tab_program1, text="اجرای‌ برنامه", font=("B Titr", 14), fg="#7300bf", command=run_Trigonometric_Circle)
run_project_button.pack(padx=10, pady=10)

def run_Equations():
    subprocess.call(["python","Trigonometric_Ratios\Equations.py"])

# Add button to run other project
# ایجاد دکمه برای اجرای برنامه
run_project_button = tk.Button(tab_program2, text="اجرای‌ برنامه", font=("B Titr", 14), fg="#7300bf", command=run_Equations)
run_project_button.pack(padx=10, pady=10)

# پیام خوش آمد به کاربر
messagebox.showinfo(title='Information Box', message='خوش آمدید! روش محاسبه‌ی مورد نظر را انتخاب کنید')

# Run main loop
root.mainloop()
