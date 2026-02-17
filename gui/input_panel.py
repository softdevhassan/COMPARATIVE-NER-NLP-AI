import tkinter as tk


# very big box for text input
class InputPanel:
    def __init__(self, parent):
        # input box frame
        self.frame = tk.Frame(
            parent, bd=2, relief="groove"
        )  # parent is liye becuase isko main window k andar place karna hai

        tk.Label(self.frame, text="Paste Text Here:", font=("Arial", 11)).pack(
            anchor="w", padx=5, pady=2
        )

        text_frame = tk.Frame(self.frame)
        text_frame.pack(fill="both", expand=True, padx=5)

        self.txt = tk.Text(text_frame, height=18, width=60)
        self.sbar = tk.Scrollbar(text_frame)
        self.txt.config(yscrollcommand=self.sbar.set)
        self.sbar.config(command=self.txt.yview)

        self.txt.pack(side="left", fill="both", expand=True)
        self.sbar.pack(side="right", fill="y")

        self.opts = tk.Frame(self.frame)
        self.opts.pack(fill="x", pady=20)  # below space for buttons

        tk.Label(self.opts, text="Model:").pack(side="left")

        self.choice = tk.StringVar(value="spaCy Model")
        self.menu = tk.OptionMenu(self.opts, self.choice, "spaCy Model")
        self.menu.pack(side="left", padx=5)

        # Buttons
        self.run_button = tk.Button(self.opts, text="RUN", width=12, bg="lightblue")
        self.run_button.pack(side="right", padx=5)

        self.clr_btn = tk.Button(self.opts, text="Clear", command=self.saaf_karo)
        self.clr_btn.pack(side="right", padx=5)

        self.sample_btn = tk.Button(
            self.opts, text="Sample Text", command=self.add_sample
        )
        self.sample_btn.pack(side="right", padx=5)

    def add_sample(self):  # default text hassan bhai ka order ha...
        s = "Apple is looking at buying U.K. startup for $1 billion in 2026. "
        s += "Hassan Ali from Google is visiting London."
        self.txt.delete("1.0", "end")
        self.txt.insert("end", s)

    def get_text(self):
        return self.txt.get("1.0", "end-1c")

    def saaf_karo(self):
        self.txt.delete("1.0", "end")

    def get_model_choice(self):
        return self.choice.get()
