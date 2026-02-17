import tkinter as tk
import os
import re
from gui.input_panel import InputPanel
from gui.result_panel import ResultPanel

# Mudassir ne spaCy kiya, ab me Hassan bhai ka CRF connect kar raha hoon
from models.spacy.spacy_ner import SpacyNER
from models.crf.crf_model import CRFModel
from models.crf.features import extract_features


# main user interfacce
class MainWindow:
    def __init__(self):
        # window setup
        self.root = tk.Tk()
        self.root.title("Comparative NER System NLP SEMESTER PROJECT")
        self.root.geometry("1100x650")

        # Models initialize kar rahe yahan

        # [SAAD'S TASK]: Hassan bhai ka CRF Model connect kiya
        print("Saad: Loading Hassan bhai's CRF Model...")
        self.crf = CRFModel()
        model_path = os.path.join("data", "processed", "crf_model.joblib")
        if os.path.exists(model_path):
            self.crf.load(model_path)
            print("Saad: CRF Loaded successfully!")
        else:
            print("Saad Error: CRF Model not found in data/processed!")

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

        # --- PROCESSING LOGIC (Split Work) ---

        if ml == "spaCy Model":
            results = self.spacy_m.process(txt)

        elif ml == "CRF Model":
            # dots aur abbreviations ko sahi se handle karne ke liye regex se words extract kar rahe hain
            words = re.findall(r"[A-Z]\.(?:[A-Z]\.)+|[\w']+|[^\w\s]", txt)
            import time

            start_t = time.time()

            # Features extract karein ge har word k liye
            feats = [extract_features(words, i) for i in range(len(words))]
            preds = self.crf.predict([feats])[0]

            # Entities list banai gui k liye
            ents_list = []
            for w, p in zip(words, preds):
                if p != "O":
                    ents_list.append({"text": w, "label": p})

            end_t = time.time()
            results = {
                "entities": ents_list,
                "processing_time": round(end_t - start_t, 4),
            }

        elif ml == "Compare Both":
            self.status.config(text="Compare Both: Coming soon in Week 5!")
            return

        else:
            self.status.config(text="Model not supported yet!")
            return

        self.res_p.display_results(ml, results)
        self.status.config(text="Done!")

    def run(self):
        self.root.mainloop()
