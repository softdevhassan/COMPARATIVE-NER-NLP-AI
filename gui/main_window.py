import tkinter as tk
import os
import re
from gui.input_panel import InputPanel
from gui.result_panel import ResultPanel

# Mudassir note: abhi sirif spaCy connect kiya ha
from models.spacy.spacy_ner import SpacyNER


# main user interfacce (Mudassir's version - Week 4)
class MainWindow:
    def __init__(self):
        # window setup
        self.root = tk.Tk()
        self.root.title("Comparative NER System NLP SEMESTER PROJECT")
        self.root.geometry("1100x650")

        # Models initialize kar rahe yahan
        # [MUDASSIR'S TASK]: Mere spaCy Model ki initialization
        print("Mudassir: Loading my spaCy Model...")
        self.spacy_m = SpacyNER()

        # Heading label for project
        self.heading = tk.Label(
            self.root,
            text="Comparative NER System NLP SEMESTER PROJECT",
            font=("Arial", 18, "bold"),
        )
        self.heading.grid(row=0, column=0, columnspan=2, pady=10)

        # grid setup
        self.root.columnconfigure(0, weight=7, uniform="group1")
        self.root.columnconfigure(1, weight=3, uniform="group1")
        self.root.rowconfigure(1, weight=1)

        self.in_p = InputPanel(self.root)
        self.in_p.frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        self.res_p = ResultPanel(self.root)
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
        results = {"entities": [], "processing_time": 0}

        # --- PROCESSING LOGIC (Mudassir Only for now) ---

        if ml == "spaCy Model":
            # [MUDASSIR]: I connected my spaCy process here
            results = self.spacy_m.process(txt)
        else:
            self.status.config(text="Model not supported yet!")
            return

        self.res_p.display_results(ml, results)
        self.status.config(text="Done!")

    def run(self):
        self.root.mainloop()
