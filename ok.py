import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
import mysql.connector



def insert_to_database():
    empname = e1.get()
    phone = e2.get()
    salary = e3.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="password", database="payroll")
    mycursor = mysqldb.cursor()
    try:
        try:
            sql = "INSERT INTO records (id,empname,phone,salary) VALUES (null, %s, %s, %s)"
            val = (empname, phone, salary)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("訊息", "資料新增成功!")
        except Exception as e:
            messagebox.showinfo("訊息", e)
            mysqldb.rollback()
            mysqldb.close()
        finally:
            if mysqldb.is_connected():
                mycursor.close()
                mysqldb.close()
                messagebox.showinfo("訊息", "已斷開連線")
    except UnboundLocalError:
        messagebox.showinfo("訊息", "發生錯誤，請重新再試!")


def delete_to_database():
    print("coding......")


root = Tk()
root.title("員工資料系統")
root.geometry("260x205")
global e1
global e2
global e3

lb_fontStyle = tkFont.Font(family="microsoft yahei", size=16)
btn_fontStyle = tkFont.Font(family="microsoft yahei", size=12)
Label(root, text="員工姓名", font=lb_fontStyle).place(x=10, y=10)
Label(root, text="電話", font=lb_fontStyle).place(x=10, y=60)
Label(root, text="薪資", font=lb_fontStyle).place(x=10, y=110)

e1 = Entry(root)
e1.place(x=120, y=10, width=130, height=40)

e2 = Entry(root)
e2.place(x=120, y=60, width=130, height=40)

e3 = Entry(root)
e3.place(x=120, y=110, width=130, height=40)

Button(root, text="新增至資料庫", command=insert_to_database, height=0, width=10, font=btn_fontStyle).place(x=10, y=160)
Button(root, text="刪除", command=delete_to_database, height=0, width=10, font=btn_fontStyle).place(x=140, y=160)

root.mainloop()

if __name__ == '__main__':
    insert_to_database()