import tkinter as tk

class InputPanel:
    def __init__(self, parent):
        frame = tk.Frame(parent)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(frame, text="Input Text").pack(anchor="w")
        self.text_box = tk.Text(frame, height=15)
        self.text_box.pack(fill=tk.BOTH, expand=True)

        self.run_button = tk.Button(frame, text="Run NER")
        self.run_button.pack(pady=10)
