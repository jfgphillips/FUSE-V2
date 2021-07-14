import tkinter as tk
import solvayProcess.bottomUp.revreactantFlow as rrF


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.myReaction = rrF.revReactionFlow(1000000)
        self.pack()
        self.create_widgets()
        self.return_results()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "hello there"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def return_results(self):
        self.label = tk.Label(text=self.myReaction.requiredreactants())
        #self.test_int = tk.Label(text = self.myReaction.soda_ash)
        #self.test_int.pack(side="right")
        self.label.pack(side="left")
        self.rightLabel = tk.Label(text=self.myReaction.step5())
        self.rightLabel.pack(side="right")

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()