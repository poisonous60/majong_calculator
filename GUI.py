from tkinter import *
import cal5_function as cal5

def __InitialSetting():
    pass

if __name__ == "__main__":

    __InitialSetting()
    #1번
    def ReloadText1():
        try:
            txt1.delete('1.0', END)
            label = cal5.GUI_SHOW(target_ent.get())
            txt1.insert(END,label)
            txt_reload_btn.configure(text="Show")
        except:
            txt1.delete('1.0', END)
            txt1.insert(END,"ERROR!")
    
    root = Tk()
    root.title("GUI test")
    root.geometry("1000x600")
    root.config(bg="#F0F0F0")
    __frame_root = root

    frame0 = Frame(__frame_root, width=80, height=100,bg="light blue")
    frame0.grid(column=1,rowspan=2, row=0)

    txt1 = Text(frame0, width=120, height=40,bg="light grey")
    txt1.grid(row=3)
    txt_reload_btn = Button(frame0, width=25,text="Show",command=ReloadText1)
    txt_reload_btn.grid(row=1)

    target_ent = Entry(frame0, width=20,bg="#99ff99")
    target_ent.insert(0,"2345")
    target_ent.grid(row=0)

    def A():
        print("hello")

    all_butten = Button(frame0, text="set ALL", width=10, command=A)
    all_butten.grid(row=1,column=2)

    root.mainloop()