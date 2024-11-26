import customtkinter as ctk
#GUI calculator by Hirad Fakouri

class Number_worker:

    def __init__(self):
        self.loutput_chars = []
        self.chars = ""
        self.cal_chars = ""
        self.result = ""
        self.output = ""
        self.btnControl = True
        
    def char_printer(self):
        self.chars = "".join(self.loutput_chars)
        self.output = self.chars
        draw()

    def add_zero(self):
        self.zero_num = "0"
        self.loutput_chars.append(self.zero_num)
        self.char_printer()
    
    def add_one(self):
        self.one_num = "1"
        self.loutput_chars.append(self.one_num)
        self.char_printer()
    
    def add_two(self):
        self.two_num = "2"
        self.loutput_chars.append(self.two_num)
        self.char_printer()

    def add_three(self):
        self.three_num = "3"
        self.loutput_chars.append(self.three_num)
        self.char_printer()
    
    def add_four(self):
        self.four_num = "4"
        self.loutput_chars.append(self.four_num)
        self.char_printer()

    def add_five(self):
        self.five_num = "5"
        self.loutput_chars.append(self.five_num)
        self.char_printer()

    def add_six(self):
        self.six_num = "6"
        self.loutput_chars.append(self.six_num)
        self.char_printer()
    
    def add_seven(self):
        self.seven_num = "7"
        self.loutput_chars.append(self.seven_num)
        self.char_printer()

    def add_eight(self):
        self.eight_num = "8"
        self.loutput_chars.append(self.eight_num)
        self.char_printer()

    def add_nine(self):
        self.nine_num = "9"
        self.loutput_chars.append(self.nine_num)
        self.char_printer()
    
    def add_dot(self):
        self.dot_char = "."
        self.loutput_chars.append(self.dot_char)
        self.char_printer()
    
    def add_plus(self):
        self.plus_char = "+"
        self.loutput_chars.append(self.plus_char)
        self.char_printer()
    
    def add_minus(self):
        self.minus_char = "-"
        self.loutput_chars.append(self.minus_char)
        self.char_printer()

    def add_times(self):
        self.times_char = "x"
        self.loutput_chars.append(self.times_char)
        self.char_printer()
    
    def add_divide(self):
        self.divide_char = "÷"
        self.loutput_chars.append(self.divide_char)
        self.char_printer()
    
    def add_power(self):
        self.divide_char = "^"
        self.loutput_chars.append(self.divide_char)
        self.char_printer()

    def equal(self):
        self.list_chars = self.loutput_chars

        for i in range(len(self.list_chars)):
            if self.list_chars[i] == "x":
                self.list_chars[i] = "*"
            elif self.list_chars[i] == "÷":
                 self.list_chars[i] = "/"
            elif self.list_chars[i] == "^":
                 self.list_chars[i] = "**"

        self.cal_chars = "".join(self.list_chars)

        self.result = eval(self.cal_chars)
        self.output = self.result

        draw()
        
        self.btnControl = False
    
    def clear(self):
        self.loutput_chars = []
        self.chars = ""
        self.cal_chars = ""
        self.result = ""
        self.output = ""
        self.btnControl = True

        draw()

ctk.set_appearance_mode("dark")  # Modes: system (default), light,"ctk.set_default_color_theme("blue")  # Themes: blue (default),"blue, green
ctk.set_default_color_theme("blue")


nw = Number_worker()

def draw():
    output = ctk.CTkLabel(master=win, text=nw.output, height=50, width=500, text_font=("Arial", 60))
    output.place(x=0, y=0)

    equl_btn = ctk.CTkButton(master=win, text="=", height=200, width=100, text_font=("Arial", 50), command=nw.equal)
    equl_btn.place(x=400, y=350)

    zero_btn = ctk.CTkButton(master=win, text="0", height=100, width=100, text_font=("Arial", 50), command=nw.add_zero)
    zero_btn.place(x=100, y=450)

    one_btn = ctk.CTkButton(master=win, text="1", height=100, width=100, text_font=("Arial", 50), command=nw.add_one)
    one_btn.place(x=0, y=350)

    two_btn = ctk.CTkButton(master=win, text="2", height=100, width=100, text_font=("Arial", 50), command=nw.add_two)
    two_btn.place(x=100, y=350)

    three_btn = ctk.CTkButton(master=win, text="3", height=100, width=100, text_font=("Arial", 50), command=nw.add_three)
    three_btn.place(x=200, y=350)

    four_btn = ctk.CTkButton(master=win, text="4", height=100, width=100, text_font=("Arial", 50), command=nw.add_four)
    four_btn.place(x=0, y=250)

    five_btn = ctk.CTkButton(master=win, text="5", height=100, width=100, text_font=("Arial", 50), command=nw.add_five)
    five_btn.place(x=100, y=250)

    six_btn = ctk.CTkButton(master=win, text="6", height=100, width=100, text_font=("Arial", 50), command=nw.add_six)
    six_btn.place(x=200, y=250)

    seven_btn = ctk.CTkButton(master=win, text="7", height=100, width=100, text_font=("Arial", 50), command=nw.add_seven)
    seven_btn.place(x=0, y=150)

    eight_btn = ctk.CTkButton(master=win, text="8", height=100, width=100, text_font=("Arial", 50), command=nw.add_eight)
    eight_btn.place(x=100, y=150)

    nine_btn = ctk.CTkButton(master=win, text="9", height=100, width=100, text_font=("Arial", 50), command=nw.add_nine)
    nine_btn.place(x=200, y=150) 

    dot_btn = ctk.CTkButton(master=win, text=".",  height=100, width=100, text_font=("Arial", 50), command=nw.add_dot)
    dot_btn.place(x=200, y=450)

    plus_btn = ctk.CTkButton(master=win, text="+", height=100, width=100, text_font=("Arial", 50), command=nw.add_plus)
    plus_btn.place(x=300, y=450)

    minus_btn = ctk.CTkButton(master=win, text="-", height=100, width=100, text_font=("Arial", 50), command=nw.add_minus)
    minus_btn.place(x=300, y=350)

    times_btn = ctk.CTkButton(master=win, text="x", height=100, width=100, text_font=("Arial", 50), command=nw.add_times)
    times_btn.place(x=300, y=250)

    divide_btn = ctk.CTkButton(master=win, text="÷", height=100, width=100, text_font=("Arial", 50), command=nw.add_divide)
    divide_btn.place(x=400, y=250)

    power_btn = ctk.CTkButton(master=win, text="^", height=100, width=100, text_font=("Arial", 50), command=nw.add_power)
    power_btn.place(x=0, y=450)

    clear_btn = ctk.CTkButton(master=win, text="C", height=100, width=200, text_font=("Arial", 50), command=nw.clear)
    clear_btn.place(x=300, y=150)

win = ctk.CTk()

win.title("Calculator")
win.geometry("500x550")

draw()

win.mainloop()

