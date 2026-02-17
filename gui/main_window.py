import tkinter as tk
from gui.input_panel import InputPanel
from gui.result_panel import ResultPanel


# main user interfacce
class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Comparative NER System NLP SEMESTER PROJECT")
        self.root.geometry("1100x650") # q k bara text bhi add karna hoskta ha...

        # Heading label for project
        self.heading = tk.Label(
            self.root, text="Comparative NER System NLP SEMESTER PROJECT", font=("Arial", 18, "bold")
        )
        self.heading.grid(row=0, column=0, columnspan=2, pady=10)
        # grid mein rows/columns ki madad sy 70/30 wala layout banaya
        self.root.columnconfigure(0, weight=7, uniform="group1")
        self.root.columnconfigure(1, weight=3, uniform="group1")
        self.root.rowconfigure(1, weight=1) 

        self.in_p = InputPanel(self.root) # input panel add kiya
        self.in_p.frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        self.res_p = ResultPanel(self.root) # result panel add kiya
        self.res_p.frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

        self.status = tk.Label(
            self.root, text="System is Ready...", bd=1, relief=tk.SUNKEN, anchor=tk.W
        )
        self.status.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.in_p.run_button.config(command=self.button_click)

    def button_click(self):
        txt = self.in_p.get_text()
        ml = self.in_p.get_model_choice()

        if len(txt.strip()) == 0:
            self.status.config(text="Error: Text box is empty!")
            return

        self.status.config(text="Processing... please wait")
        self.res_p.display_results(ml, txt)
        self.status.config(text="Done!")

    def run(self):
        self.root.mainloop()
