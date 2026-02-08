import tkinter as tk


class ResultPanel:
    def __init__(self, parent):
        # expose frame so PanedWindow can manage it
        self.frame = tk.Frame(parent, bd=2, relief=tk.GROOVE)
        self.frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(self.frame, text="NER Results", font=("Helvetica", 12, "bold")).pack(anchor="w")

        # Result text with scrollbar
        result_container = tk.Frame(self.frame)
        result_container.pack(fill=tk.BOTH, expand=True)
        self.result_box = tk.Text(result_container, height=18, wrap=tk.WORD)
        rsb = tk.Scrollbar(result_container, command=self.result_box.yview)
        self.result_box.configure(yscrollcommand=rsb.set)
        self.result_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        rsb.pack(side=tk.RIGHT, fill=tk.Y)

        # small signature to show student version
        footer = tk.Label(self.frame, text="Saad - GUI v0.1", anchor="e", fg="#666")
        footer.pack(fill=tk.X, pady=(4,0))

    def display_results(self, model_choice, text):
        # Very simple placeholder NER: pick capitalized words (student-ish)
        words = [w.strip('.,') for w in text.split() if w.strip('.,')]
        candidates = [w for w in words if w[0].isupper() and len(w) > 1]

        self.result_box.delete('1.0', tk.END)
        if model_choice == 'Both':
            self.result_box.insert(tk.END, 'spaCy (Mudassir) output:\n')
            self.result_box.insert(tk.END, self._format_fake_output(candidates, style='spacy'))
            self.result_box.insert(tk.END, '\nCRF (Hassan) output:\n')
            self.result_box.insert(tk.END, self._format_fake_output(candidates, style='crf'))
        elif 'spaCy' in model_choice:
            self.result_box.insert(tk.END, 'spaCy (Mudassir) output:\n')
            self.result_box.insert(tk.END, self._format_fake_output(candidates, style='spacy'))
        else:
            self.result_box.insert(tk.END, 'CRF (Hassan) output:\n')
            self.result_box.insert(tk.END, self._format_fake_output(candidates, style='crf'))

    def _format_fake_output(self, ents, style='spacy'):
        if not ents:
            return ' (no entities detected — placeholder)\n'
        lines = []
        for e in ents:
            if style == 'spacy':
                # spaCy-like guess: longer names grouped
                lines.append(f" - {e} \t[TYPE: ORG/PERSON]")
            else:
                # CRF-like guess: sometimes misses multi-word names (studentish)
                lines.append(f" - {e} \t[TYPE: MISC]")
        return '\n'.join(lines) + '\n'
