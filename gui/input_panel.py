import tkinter as tk


class InputPanel:
    def __init__(self, parent):
        # expose frame for PanedWindow
        self.frame = tk.Frame(parent, bd=2, relief=tk.GROOVE)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(self.frame, text="Input Text", font=("Helvetica", 12, "bold")).pack(anchor="w")

        # Text area with a scrollbar
        text_container = tk.Frame(self.frame)
        text_container.pack(fill=tk.BOTH, expand=True)
        self.text_area = tk.Text(text_container, height=18, wrap=tk.WORD)
        scrollbar = tk.Scrollbar(text_container, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=scrollbar.set)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Controls: model select and buttons
        controls = tk.Frame(self.frame)
        controls.pack(fill=tk.X, pady=6)

        tk.Label(controls, text="Model:", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=(2,6))
        self.model_var = tk.StringVar(value="spaCy (Mudassir)")
        choices = ["spaCy (Mudassir)", "CRF (Hassan)", "Both"]
        self.model_menu = tk.OptionMenu(controls, self.model_var, *choices)
        self.model_menu.config(width=16)
        self.model_menu.pack(side=tk.LEFT)

        # Buttons
        self.run_button = tk.Button(controls, text="Run Comparison")
        self.run_button.pack(side=tk.RIGHT, padx=4)

        self.clear_button = tk.Button(controls, text="Clear", command=self.clear_text)
        self.clear_button.pack(side=tk.RIGHT)

        self.sample_button = tk.Button(controls, text="Insert Sample", command=self.insert_sample)
        self.sample_button.pack(side=tk.RIGHT, padx=(0,6))

    def get_text(self):
        return self.text_area.get("1.0", tk.END)

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)

    def insert_sample(self):
        sample = (
            "John Doe visited New York in April to attend a conference at Columbia University. "
            "He met with Dr. Alice Smith from Google."
        )
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, sample)

    def get_model_choice(self):
        return self.model_var.get()

