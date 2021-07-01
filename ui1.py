import tkinter as tk
import webbrowser as wb
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.web = tk.Button(self)
        self.web["text"] = "Open My Websites\n(click me)"
        self.web["command"] = self.open_websites
        self.web.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    def open_websites(self):
        #import webbrowser as wb
        print("-----------Welcome to your Browser Assistant---------------")

        dict={}

        dict['Google']='https://google.com'
        dict['Youtube'] = 'http://www.youtube.com'

        print(dict)

        for i in dict.keys():
            print("Opening: " + i)
            wb.open(dict[i],new=2)



root = tk.Tk()
app = Application(master=root)
app.mainloop()
