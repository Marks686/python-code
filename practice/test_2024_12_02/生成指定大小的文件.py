import tkinter as tk

# 应用场景
# 头像上传功能 图片大小边界是1-2M
# 文件上传功能，文件大小边界是1-10M

def generate_file_plus():
    try:
        file_type = e1.get()
        file_name = e2.get()
        size_mb = float(e3.get())
        # 将大小转换为字节
        size_bytes  = size_mb*1024*1024

        if file_type == 'bin':
            with open(file_name + ".bin","wb") as f:
                f.write(b"\x00" * round(size_bytes))

        if file_type == 'text':
            with open(file_name + ".txt","w") as f:
                f.write("A" * round(size_bytes))

    except:
        print("-------------")

# 创建主窗口
window = tk.Tk()

# 给主窗口起名字
window.title('生成指定大小的文件')

# 设置窗口大小
window.geometry('300x300')

# 主程序部分 需要三个输入框 分别输入文件类型 文件名 文件大小 还需要一个按钮触发
# 三个输入框

l1 = tk.Label(window,text="请输入文件类型(bin/text)：")
e1 = tk.Entry(window,width=10)
l2 = tk.Label(window,text="请输入要生成的文件名：")
e2 = tk.Entry(window,width=10)
l3 = tk.Label(window,text="请输入要生成的文件大小(MB)：")
e3 = tk.Entry(window,width=10)


l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()

# 创建一个按钮
b = tk.Button(window,text="生成文件",command=generate_file_plus)
b.pack()

# 主窗口循环显示
window.mainloop()