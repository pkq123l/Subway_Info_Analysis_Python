import sqlite3
import tkinter as tk
from tkinter import scrolledtext

# 存储查询到的结果
infomation = [] 

# 查询地铁线路
def search_line(sstr):
    global infomation
    result = sstr.split(",")
    print(result)
    
    sql = "select city,line,name from info where city="+ "'" + result[0] +"'" + " and " + "line=" +"'" + result[1] +"'"
    print(sql)
    s = conn.cursor().execute(sql)
    for i in s:
        infomation.append(str(i[0])+'  '+str(i[1])+'  '+str(i[2]))
        
    scr = scrolledtext.ScrolledText(root, width=62, height=43) 
    scr.place(x=75, y=200) 

    n = len(infomation)
    print(n)
    ss = ''
    for i in range(n):
        print(infomation[i])
        ss = ss + infomation[i] + '\n'
    scr.insert('end',ss)   
    infomation = []
    src.pack()

# 查询站点
def search_station(sstr):    
    global infomation
    sql = "select city,line,name from info where name="+ "'" + sstr +"'"
    print(sql)
    s = conn.cursor().execute(sql)
    for i in s:
        infomation.append(str(i[0])+'  '+str(i[1])+'  '+str(i[2]))
        
    scr = scrolledtext.ScrolledText(root, width=62, height=43)  #滚动文本框（宽，高（以行数为单位））
    scr.place(x=75, y=200) #滚动文本框在页面的位置

    n = len(infomation)
    print(n)
    ss = ''
    for i in range(n):
        print(infomation[i])
        ss = ss + infomation[i] + '\n'
    scr.insert('end',ss)   
    infomation = []
    src.pack()


if __name__ == '__main__':
    conn = sqlite3.connect('city_line11.db', check_same_thread=False)
    cur = conn.cursor()
    HEIGHT = 800
    WIDTH = 600

    root = tk.Tk()
    root.title("2004010618彭伟楠")
    #root.geometry("600x900")
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    background_image = tk.PhotoImage(file='./bg1.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    search_text = tk.StringVar()
    search_text1 = tk.StringVar()

    lower_frame = tk.Frame(root, bg='#80c1ff',bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7,anchor='n')

    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=40,textvariable=search_text)
    entry.place(relwidth=0.65, relheight=1)

    button = tk.Button(frame, text="查线路", font=40, command=lambda: search_line(search_text.get()))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    entry1 = tk.Entry(root, font=40,bg='#80c1ff',textvariable=search_text1)
    entry1.place(x=82, y=5,width=280,height=60)
    
    button1 = tk.Button(text="查站点", font=40,bg='#80c1ff', command=lambda: search_station(search_text1.get()))
    button1.place(x=390, y=5,width=135,height=60)
    
    root.mainloop()

    
