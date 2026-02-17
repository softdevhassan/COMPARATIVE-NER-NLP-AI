import tkinter as tk


class ResultPanel:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bd=2, relief="sunken")

        tk.Label(self.frame, text="Identified Entities:", font=("Arial", 11)).pack(
            anchor="w"
        )
        self.out = tk.Text(self.frame, height=20, width=25, bg="#f0f0f0")
        self.out.pack(fill="both", expand=True)

    def display_results(self, choice, text):
        self.out.delete("1.0", "end")

        self.out.insert("end", f"Results for: {choice}\n")
        self.out.insert("end", "=" * 30 + "\n")
        words = text.split()
        for w in words:
            if len(w) > 0 and w[0].isupper():
                self.out.insert("end", f"Entity Found: {w}\n")

        self.out.insert("end", "\n(Note: actual models will be connected soon)\n")
        self.out.insert("end", "Developed by Saad Ilyas 😍")
