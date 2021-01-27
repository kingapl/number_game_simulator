import tkinter as tk
from random import randint


class NumberGameSimulator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("450x550")
        self.master.title("Number Game Simulator")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Number Game", 
                                font="Arial 20 bold", fg="#3e8a04", pady=20)
        self.title_label.grid(row=0, column=0, columnspan=5)

        self.text_label = tk.Label(self, 
            text="Podaj kolejno 5 liczb z zakresu 1-30", 
            font="Arial 12", pady=20)
        self.text_label.grid(row=1, column=0, columnspan=5)

        # User numbers entries
        self.user_number1 = tk.StringVar()
        self.number1 = tk.Entry(self, textvariable=self.user_number1, 
                                width=2, font="Arial 12")
        self.number1.grid(row=2, column=0)

        self.user_number2 = tk.StringVar()
        self.number2 = tk.Entry(self, textvariable=self.user_number2, 
                                width=2, font="Arial 12")
        self.number2.grid(row=2, column=1)

        self.user_number3 = tk.StringVar()
        self.number3 = tk.Entry(self, textvariable=self.user_number3, 
                                width=2, font="Arial 12")
        self.number3.grid(row=2, column=2)

        self.user_number4 = tk.StringVar()
        self.number4 = tk.Entry(self, textvariable=self.user_number4, 
                                width=2, font="Arial 12")
        self.number4.grid(row=2, column=3)

        self.user_number5 = tk.StringVar()
        self.number5 = tk.Entry(self, textvariable=self.user_number5, 
                                width=2, font="Arial 12")
        self.number5.grid(row=2, column=4)
        # User numbers entries - end

        self.invalid_number = tk.Label(self, text=" ", fg="#b51818")
        self.invalid_number.grid(row=3, column=0, columnspan=5)

        self.play_button = tk.Button(self, text="Zagraj", command=self.play, 
            font="Arial 14", bg="#54ba06", padx=10, pady=10)
        self.play_button.grid(row=4, column=0, columnspan=5, pady=20)

        self.draw_info1 = tk.Label(self, text=" ", font="Arial 12")
        self.draw_info1.grid(row=5, column=0, columnspan=5)

        self.draw_info2 = tk.Label(self, text="Wylosowane liczby:", 
            font="Arial 12", pady=20)
        self.draw_info2.grid(row=6, column=0, columnspan=5)

        # Computer numbers entries
        self.comp_number1 = tk.StringVar()
        self.computer_number1 = tk.Entry(self, text=self.comp_number1, 
                                        width=2, font="Arial 12")
        self.computer_number1.grid(row=7, column=0)

        self.comp_number2 = tk.StringVar()
        self.computer_number2 = tk.Entry(self, text=self.comp_number2, 
                                        width=2, font="Arial 12")
        self.computer_number2.grid(row=7, column=1)

        self.comp_number3 = tk.StringVar()
        self.computer_number3 = tk.Entry(self, text=self.comp_number3, 
                                        width=2, font="Arial 12")
        self.computer_number3.grid(row=7, column=2)

        self.comp_number4 = tk.StringVar()
        self.computer_number4 = tk.Entry(self, text=self.comp_number4, 
                                        width=2, font="Arial 12")
        self.computer_number4.grid(row=7, column=3)

        self.comp_number5 = tk.StringVar()
        self.computer_number5 = tk.Entry(self, text=self.comp_number5, 
                                        width=2, font="Arial 12")
        self.computer_number5.grid(row=7, column=4)
        # Computer numbers entries - end

        self.matching_label = tk.Label(self,text=" ", font="Arial 12", pady=10)
        self.matching_label.grid(row=8, column=0, columnspan=5)

        self.matching_numbers_label = tk.Label(self, text=" ", font="Arial 12")
        self.matching_numbers_label.grid(row=9, column=0, columnspan=5)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset, 
            font="Arial 14", bg="#54ba06", padx=10, pady=10)
        self.reset_button.grid(row=10, column=0, columnspan=5, pady=20)

    def play(self):
        def check_numbers(self):
            u_number1 = self.number1.get()
            u_number2 = self.number2.get()
            u_number3 = self.number3.get()
            u_number4 = self.number4.get()
            u_number5 = self.number5.get()

            selected_numbers = [int(u_number1), int(u_number2), int(u_number3), 
                                int(u_number4), int(u_number5)]
            user_numbers = []

            for number in selected_numbers:
                if number <= 0 or number > 30:
                    #self.invalid_number['text'] = "Nie można wybrać liczby spoza zakresu."
                    #break
                    continue
                elif number not in user_numbers:
                    user_numbers.append(number)

            if len(user_numbers) == 5:
                drawn_numbers = draw_numbers(self)
                return user_numbers, drawn_numbers


        def draw_numbers(self):
            quantity = 0
            drawn_numbers = []

            while quantity < 5:
                drawn_number = randint(1, 30)
                if drawn_number not in drawn_numbers:
                    drawn_numbers.append(drawn_number)
                    quantity += 1
                else:
                    continue

            self.draw_info1['text']="Losowanie pięciu liczb z zakresu 1-30."

            self.comp_number1.set(drawn_numbers[0])
            self.comp_number2.set(drawn_numbers[1])
            self.comp_number3.set(drawn_numbers[2])
            self.comp_number4.set(drawn_numbers[3])
            self.comp_number5.set(drawn_numbers[4])

            return drawn_numbers


        def verify_matching_numbers(self, user_numbers, drawn_numbers):
            matching = 0
            matching_numbers = []

            for number in user_numbers:
                for drawn_number in drawn_numbers:
                    if number == drawn_number:
                        matching += 1
                        matching_numbers.append(number)
                    else:
                        continue

            self.matching_label['text'] = f"Ilość trafień: {matching}"
            self.matching_numbers_label['text'] = f"Trafione liczby: {matching_numbers}"


        try:
            user_numbers, drawn_numbers = check_numbers(self)
            #drawn_numbers = draw_numbers(self)
            verify_matching_numbers(self, user_numbers, drawn_numbers)

        except ValueError:
            self.invalid_number['text'] = "Nieprawidłowa wartość"

        except TypeError:
            self.invalid_number['text'] = "Liczba spoza zakresu lub występuje więcej niż raz."

    def reset(self):
        self.number1.delete(0, 'end')
        self.number2.delete(0, 'end')
        self.number3.delete(0, 'end')
        self.number4.delete(0, 'end')
        self.number5.delete(0, 'end')

        self.computer_number1.delete(0, 'end')
        self.computer_number2.delete(0, 'end')
        self.computer_number3.delete(0, 'end')
        self.computer_number4.delete(0, 'end')
        self.computer_number5.delete(0, 'end')

        self.matching_label['text'] = " "
        self.matching_numbers_label['text'] = " "
        self.draw_info1['text'] = " "


root = tk.Tk()
number_game_simulator = NumberGameSimulator(master=root)
number_game_simulator.mainloop()