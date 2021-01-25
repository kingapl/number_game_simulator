import tkinter as tk


class NumberGameSimulator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Number Game Simulator")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Number Game")
        self.title_label.grid(row=0, column=2)

        self.text_label = tk.Label(self, 
            text="Podaj kolejno 5 liczb z zakresu 1-30")
        self.text_label.grid(row=1, column=2)

        # User numbers entries
        self.user_number1 = tk.StringVar()
        self.number1 = tk.Entry(self, textvariable=self.user_number1, width=2)
        self.number1.grid(row=2, column=0)

        self.user_number2 = tk.StringVar()
        self.number2 = tk.Entry(self, textvariable=self.user_number2, width=2)
        self.number2.grid(row=2, column=1)

        self.user_number3 = tk.StringVar()
        self.number3 = tk.Entry(self, textvariable=self.user_number3, width=2)
        self.number3.grid(row=2, column=2)

        self.user_number4 = tk.StringVar()
        self.number4 = tk.Entry(self, textvariable=self.user_number4, width=2)
        self.number4.grid(row=2, column=3)

        self.user_number5 = tk.StringVar()
        self.number5 = tk.Entry(self, textvariable=self.user_number5, width=2)
        self.number5.grid(row=2, column=4)
        # User numbers entries - end

        self.play_button = tk.Button(self, text="Zagraj", command=self.play)
        self.play_button.grid(row=4, column=2)

        self.draw_info = tk.Label(self, text="Losowanie pięciu liczb z zakresu 1-30.\nWylosowane liczby")
        self.draw_info.grid(row=5, column=2)

        # Computer numbers entries
        self.comp_number1 = tk.StringVar()
        self.computer_number1 = tk.Entry(self, text=self.comp_number1, width=2)
        self.computer_number1.grid(row=6, column=0)

        self.comp_number2 = tk.StringVar()
        self.computer_number2 = tk.Entry(self, text=self.comp_number2, width=2)
        self.computer_number2.grid(row=6, column=1)

        self.comp_number3 = tk.StringVar()
        self.computer_number3 = tk.Entry(self, text=self.comp_number3, width=2)
        self.computer_number3.grid(row=6, column=2)

        self.comp_number4 = tk.StringVar()
        self.computer_number4 = tk.Entry(self, text=self.comp_number4, width=2)
        self.computer_number4.grid(row=6, column=3)

        self.comp_number5 = tk.StringVar()
        self.computer_number5 = tk.Entry(self, text=self.comp_number5, width=2)
        self.computer_number5.grid(row=6, column=4)
        # Computer numbers entries - end

    def play(self):
        u_number1 = self.number1.get()
        u_number2 = self.number2.get()
        u_number3 = self.number3.get()
        u_number4 = self.number4.get()
        u_number5 = self.number5.get()

        user_numbers = [int(u_number1), int(u_number2), int(u_number3), int(u_number4), int(u_number5)]

        for number in user_numbers:
            if number <= 0 or number > 30:
                invalid_number = tk.Label(self, text="Nie można wybrać liczby spoza zakresu.")
                invalid_number.grid(row=3, column=2)
                print("Nie można wybrać liczby spoza zakresu.")

        print(user_numbers)
        """
        quantity = 0
        numbers = []

        while quantity < 5:
            try:
                number = int(input("Wybrano: "))
                if number <= 0 or number > 30:
                    print("Nie można wybrać liczby spoza zakresu.")
                elif number not in numbers:
                    numbers.append(number)
                    quantity += 1
                else:
                    print("Liczba została już wybrana, podaj inną.")
            except ValueError:
                print("Nie wybrano liczby. Podaj liczbę.")

        print(f"\nWybrane liczby: {sorted(numbers)}.") 

        return numbers
        """


root = tk.Tk()
number_game_simulator = NumberGameSimulator(master=root)
number_game_simulator.mainloop()