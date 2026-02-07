import tkinter as tk


class ResultPanel:
    def __init__(self, parent):
        frame = tk.Frame(parent)
        frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(frame, text="NER Results").pack(anchor="w")
        self.output_box = tk.Text(frame, height=15)
        self.output_box.pack(fill=tk.BOTH, expand=True)
