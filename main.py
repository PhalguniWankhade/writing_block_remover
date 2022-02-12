from tkinter import *
from tkinter import ttk, Text

class Writing_Block_Remover:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry("800x400")
        self.root.title("Writing Block Remover")
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.style = ttk.Style()

        # Instructions Label
        self.instruction_label = ttk.Label(text="Once you start, keep writing for 5 minutes. If you stop for more than 5 seconds, everything you have typed will disappear.")
        self.instruction_label.grid(row=0, column=0, columnspan=4, padx=15, pady=10)

        # Start Restart button
        self.start_restart_button = ttk.Button(text="Start/Restart", command=self.restart_test)
        self.start_restart_button.grid(row=1, column=0, padx=5, pady=5)
        # timer
        self.timer = None
        # time label
        self.time_label = ttk.Label(text="Time: 00:00")
        self.time_label.grid(row=1, column=3, padx=15, pady=5)

        # Input Text
        self.user_text = Text(self.root,width=105, height=20, wrap= "word")
        self.user_text.grid(row=2, column=0, columnspan=4, padx=20, pady=5)
        self.user_text.bind('<KeyPress>', self.typing)
        self.user_text.config(state=DISABLED)

        # TODO: export button


    # timer
    def update_time_label(self, mins, secs):
        self.time_label.config(text=f"Time: {mins:02}:{secs:02}")
        self.time_label.update()

    def start_restart_timer(self, timer_value_in_seconds):
        mins, secs = divmod(timer_value_in_seconds, 60)
        self.update_time_label(mins, secs)
        if timer_value_in_seconds > 1:
            self.timer = self.root.after(1000, self.start_restart_timer, timer_value_in_seconds - 1)
        else:
            self.time_label.config(text=f"Time's up!")
            self.time_label.update()
            self.root.after_cancel(self.five_sec_timer)
            self.start_restart_button['state'] = "normal"
            self.user_text.config(state=DISABLED)
            self.timer = None
    
    def five_second_timer(self, timer_value_in_seconds):
        print(timer_value_in_seconds)
        if timer_value_in_seconds > 0:
            self.five_sec_timer = self.root.after(1000, self.five_second_timer, timer_value_in_seconds - 1)
        else:
            self.user_text.delete('1.0', END)
            self.five_sec_timer = self.root.after(1000, self.five_second_timer, 5)

    
    def typing(self, key):
        if self.timer is not None:
            self.root.after_cancel(self.five_sec_timer)
            self.five_second_timer(5)

    # Start and Restart text
    def restart_test(self):
        if self.timer is not None:
            self.root.after_cancel(self.timer)
        self.start_restart_button['state'] = "disabled"
        self.user_text.config(state="normal")
        self.user_text.delete('1.0', END)
        self.timer = None
        self.start_restart_timer(300)
        self.five_second_timer(5)

writing_block_remover = Writing_Block_Remover()
writing_block_remover.root.mainloop()
