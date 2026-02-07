import tkinter as tk
from gui.input_panel import InputPanel
from gui.result_panel import ResultPanel


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Comparative NER System")
        self.root.geometry("900x500")

        self.input_panel = InputPanel(self.root)
        self.result_panel = ResultPanel(self.root)

    def run(self):
        self.root.mainloop()
