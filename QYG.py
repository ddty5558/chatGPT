from tkinter import *
root = Tk()
root.title("千衣阁")

def show_main_menu():
    # 清空屏幕上的所有组件
    for widget in root.winfo_children():
        widget.destroy()

    # 添加标签
    title_label = Label(root, text="东莞市千衣阁服饰", font=("宋体", 54), foreground="purple")
    title_label.pack(side=TOP, fill=X, padx=0, pady=80)

    # 添加按钮
    button1 = Button(root, text="下单", font=("宋体", 18), bg="white", fg="black", command=show_order_menu)
    button2 = Button(root, text="裁货", font=("宋体", 18), bg="white", fg="black", command=show_cut_menu)
    button3 = Button(root, text="出货", font=("宋体", 18), bg="white", fg="black", command=show_shipping_menu)
    button4 = Button(root, text="查询", font=("宋体", 18), bg="white", fg="black", command=show_query_menu)

    # 添加按键位置和比例
    button1.place(relx=0.25, rely=0.4, relwidth=0.2, relheight=0.2)
    button2.place(relx=0.55, rely=0.4, relwidth=0.2, relheight=0.2)
    button3.place(relx=0.25, rely=0.7, relwidth=0.2, relheight=0.2)
    button4.place(relx=0.55, rely=0.7, relwidth=0.2, relheight=0.2)
def show_cut_menu():
    # 清空屏幕上的所有组件
    for widget in root.winfo_children():
        widget.destroy()

    # 添加标签
    title_label = Label(root, text="裁货", font=("宋体", 54), foreground="purple")
    title_label.pack(side=TOP, fill=X, padx=0, pady=80)

    # 添加按钮
    new_button = Button(root, text="新增", font=("宋体", 18), bg="white", fg="black")
    search_button = Button(root, text="查询", font=("宋体", 18), bg="white", fg="black")
    find_button = Button(root, text="搜索", font=("宋体", 18), bg="white", fg="black")

    # 添加按键位置和比例
    new_button.place(relx=0.5, rely=0.4, anchor=CENTER, relwidth=0.4, relheight=0.2)
    search_button.place(relx=0.5, rely=0.6, anchor=CENTER, relwidth=0.4, relheight=0.2)
    find_button.place(relx=0.5, rely=0.8, anchor=CENTER, relwidth=0.4, relheight=0.2)

    # 添加返回按钮
    return_button = Button(root, text="返回", font=("宋体", 18), bg="white", fg="black", command=show_main_menu, bd=0)
    return_button.place(relx=0.95, rely=0.95)

def show_shipping_menu():
    # 清空屏幕上的所有组件
    for widget in root.winfo_children():
        widget.destroy()

    # 添加标签
    title_label = Label(root, text="出货", font=("宋体", 54), foreground="purple")
    title_label.pack(side=TOP, fill=X, padx=0, pady=80)

    # 添加按钮
    new_button = Button(root, text="新增", font=("宋体", 18), bg="white", fg="black")
    search_button = Button(root, text="查询", font=("宋体", 18), bg="white", fg="black")
    find_button = Button(root, text="搜索", font=("宋体", 18), bg="white", fg="black")

    # 添加按键位置和比例
    new_button.place(relx=0.5, rely=0.4, anchor=CENTER, relwidth=0.4, relheight=0.2)
    search_button.place(relx=0.5, rely=0.6, anchor=CENTER, relwidth=0.4, relheight=0.2)
    find_button.place(relx=0.5, rely=0.8, anchor=CENTER, relwidth=0.4, relheight=0.2)

    # 添加返回按钮
    return_button = Button(root, text="返回", font=("宋体", 18), bg="white", fg="black", command=show_main_menu, bd=0)
    return_button.place(relx=0.95, rely=0.95)


def show_order_menu():
    # 清空屏幕上的所有组件
    for widget in root.winfo_children():
        widget.destroy()

    # 添加标签
    title_label = Label(root, text="下单", font=("宋体", 54), foreground="purple")
    title_label.pack(side=TOP, fill=X, padx=0, pady=80)

    # 添加按钮
    new_button = Button(root, text="新增", font=("宋体", 18), bg="white", fg="black", command=show_order_confirm)

    search_button = Button(root, text="查询", font=("宋体", 18), bg="white", fg="black")
    find_button = Button(root, text="搜索", font=("宋体", 18), bg="white", fg="black")

    # 添加表格
    frame = Frame(root)
    frame.pack(side=TOP, fill=X, padx=20, pady=20)

    # 设置按钮位置和比例
    new_button.place(relx=0.5, rely=0.4, anchor=CENTER, relwidth=0.4, relheight=0.2)
    search_button.place(relx=0.5, rely=0.6, anchor=CENTER, relwidth=0.4, relheight=0.2)
    find_button.place(relx=0.5, rely=0.8, anchor=CENTER, relwidth=0.4, relheight=0.2)

    # 添加按钮
    return_button = Button(root, text="返回", font=("宋体", 18), bg="white", fg="black", command=show_main_menu, bd=0)
    return_button.place(relx=0.95, rely=0.95, relwidth=0.05, relheight=0.05)


from tkinter import *


def show_order_confirm():
    # 清空屏幕上的所有组件
    for widget in root.winfo_children():
        widget.destroy()

    # 添加标签
    title_label = Label(root, text="确认下单", font=("宋体", 54), foreground="purple")
    title_label.pack(side=TOP, fill=X, padx=0, pady=80)

    # 添加表格
    frame = Frame(root)
    frame.pack(side=TOP, fill=X, padx=20, pady=20)

    # 表格标题
    header = ["日期", "客人", "款号", "面料", "颜色", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL", "6XL", "7XL",
              "合计", "总数", "裁货日期", "裁货数量", "发货日期", "交货日期", "备注"]

    # 表格数据
    data = [["2023-04-30", "客人1", "001", "面料1", "白色", 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 550, 5500,
             "2023-05-01", 5000, "2023-05-02", "2023-05-03", "备注1"],
            ["2023-04-29", "客人2", "002", "面料2", "黑色", 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 275, 2750,
             "2023-04-30", 2500, "2023-05-01", "2023-05-02", "备注2"]]

    # 创建表格
    rows = len(data)
    cols = len(header)

    for i in range(rows):
        for j in range(cols):
            if i == 0:
                # 表头
                label = Label(frame, text=header[j], font=("宋体", 14, "bold"), padx=5, pady=5, relief=RIDGE,
                              bg="lightgray")
            else:
                # 表格数据
                label = Label(frame, text=data[i][j], font=("宋体", 12), padx=5, pady=5, relief=RIDGE)

            label.grid(row=i, column=j, sticky=NSEW)

    # 添加按钮
    edit_button = Button(root, text="修改", font=("宋体", 18), bg="white", fg="black")
    confirm_button = Button(root, text="确认", font=("宋体", 18), bg="white", fg="black")
    return_button = Button(root, text="返回", font=("宋体", 18), bg="white", fg="black", command=show_order_menu, bd=0)

    # 设置按钮位置和比例


def show_query_menu():
    # 清空屏幕上的所有组件
    for widget in root.winfo_children():
        widget.destroy()

    # 添加标签
    title_label = Label(root, text="查询", font=("宋体", 54), foreground="purple")
    title_label.pack(side=TOP, fill=X, padx=0, pady=80)

    # 添加按钮
    name_button = Button(root, text="按客人名称", font=("宋体", 18), bg="white", fg="black")
    date_button = Button(root, text="按下单日期", font=("宋体", 18), bg="white", fg="black")
    order_button = Button(root, text="按裁床单号", font=("宋体", 18), bg="white", fg="black")

    # 添加按键位置和比例
    name_button.place(relx=0.5, rely=0.4, anchor=CENTER, relwidth=0.4, relheight=0.2)
    date_button.place(relx=0.5, rely=0.6, anchor=CENTER, relwidth=0.4, relheight=0.2)
    order_button.place(relx=0.5, rely=0.8, anchor=CENTER, relwidth=0.4, relheight=0.2)

    # 添加返回按钮
    return_button = Button(root, text="返回", font=("宋体", 18), bg="white", fg="black", command=show_main_menu, bd=0)
    return_button.place(relx=0.95, rely=0.95)


# 设置窗口标题和大小
root.title("My App")
root.geometry("1080x1024")

# 显示主菜单
show_main_menu()

# 运行窗口循环
root.mainloop()

