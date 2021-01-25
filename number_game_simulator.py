import tkinter as tk


class NumberGameSimulator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Number Game Simulator")
        self.pack()


root = tk.Tk()
number_game_simulator = NumberGameSimulator(master=root)
number_game_simulator.mainloop()