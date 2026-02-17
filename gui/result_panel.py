import tkinter as tk


class ResultPanel:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bd=2, relief="sunken")

        tk.Label(self.frame, text="Identified Entities:", font=("Arial", 11)).pack(
            anchor="w"
        )
        self.out = tk.Text(self.frame, height=20, width=25, bg="#f0f0f0")
        self.out.pack(fill="both", expand=True)

    def display_results(self, model_choice, result_data):
        # spacy model now working with gui
        self.out.delete("1.0", "end")

        entities = result_data.get("entities", [])
        p_time = result_data.get("processing_time", 0)

        self.out.insert("end", f"MODEL: {model_choice}\n")
        self.out.insert("end", f"TIME: {p_time} seconds\n")
        self.out.insert("end", "=" * 30 + "\n\n")

        if not entities:
            self.out.insert("end", "No entities found in this text.\n")
        else:
            for ent in entities:
                # Entity format: {'text': '...', 'label': '...'}
                txt = ent.get("text", ent.get("word", ""))
                lbl = ent.get("label", "O")
                self.out.insert("end", f" - {txt:15} | {lbl}\n")

        self.out.insert("end", "\n" + "-" * 30 + "\n")
        self.out.insert("end", "Developed by Saad & Mudassir 😍")
