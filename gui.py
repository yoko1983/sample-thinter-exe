import tkinter as tk
import tkinter.ttk as ttk

def func():
    print("test")


class Application(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)

        self.master.geometry("640x250") 

        frame01 = tk.Frame(self.master)
        frame02 = tk.Frame(self.master)
        frame03 = tk.Frame(self.master)
        frame04 = tk.Frame(self.master)
        frame05 = tk.Frame(self.master)
        frame06 = tk.Frame(self.master)
        frame07 = tk.Frame(self.master)
        frame_status_bar = tk.Frame(self.master, borderwidth = 2, relief = tk.SUNKEN)

        combo_title_label1 = tk.Label(root, text="テスト1")

        combo_option1 = ["A", "B", "C", "D"]
        combo_variable1 = tk.StringVar()
        combo1 = ttk.Combobox ( root , values = combo_option1 , textvariable = combo_variable1 )
        combo1.set("A")

        combo_title_label2 = tk.Label(root, text="テスト2")

        combo_option2 = ["A", "B", "C", "D"]
        combo_variable2 = tk.StringVar ( )
        combo2 = ttk.Combobox ( root , values = combo_option2 , textvariable = combo_variable2 )
        combo2.set("B")

        chk_title_label1 = tk.Label(root, text="チェックT1")

        chk1 = tk.Checkbutton(root, text='チェック1')
        chk2 = tk.Checkbutton(root, text='チェック2')

        chk_title_label2 = tk.Label(root, text="チェックT2")

        chk3 = tk.Checkbutton(root, text='チェック3')

        button = tk.Button()
        button["text"] = "実行"
        button["command"] = lambda: func()

        status_bar_label = tk.Label(root, text="")


        combo_title_label1.pack(fill = 'x', padx=20, side = 'left', in_ = frame01)
        combo1.pack(fill = 'x', padx=20, side = 'left', in_ = frame01)
        combo_title_label2.pack(fill = 'x', padx=20, side = 'left', in_ = frame02)
        combo2.pack(fill = 'x', padx=20, side = 'left', in_ = frame02)

        chk_title_label1.pack(fill = 'x', padx=20, side = 'left', in_ = frame03)
        chk1.pack(fill = 'x', padx=20, side = 'left', in_ = frame03)
        chk2.pack(fill = 'x', padx=20, side = 'left', in_ = frame03)

        chk_title_label2.pack(fill = 'x', padx=20, side = 'left', in_ = frame04)
        chk3.pack(fill = 'x', padx=20, side = 'left', in_ = frame04)

        button.pack(fill = 'x', padx=20, side = 'left', in_ = frame07)

        status_bar_label.pack(side = 'left', in_ = frame_status_bar)

        # フレームの配置
        frame01.pack(pady=2, anchor=tk.W)
        frame02.pack(pady=2, anchor=tk.W)
        frame03.pack(pady=2, anchor=tk.W)
        frame04.pack(pady=2, anchor=tk.W)
        frame07.pack(pady=2, anchor=tk.W)
        frame_status_bar.pack(side = tk.BOTTOM, fill = tk.X)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()