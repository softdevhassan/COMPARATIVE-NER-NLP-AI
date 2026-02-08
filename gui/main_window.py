import tkinter as tk
from gui.input_panel import InputPanel
from gui.result_panel import ResultPanel


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Comparative NER System - Saad (GUI) v0.1")
        self.root.geometry("1000x560")

        # Title
        title = tk.Label(
            self.root,
            text="Comparative Named Entity Recognition System",
            font=("Helvetica", 16, "bold")
        )
        title.pack(pady=8)

        # Main content uses a PanedWindow so user can resize panels
        content_pane = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        content_pane.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0,8))

        # Left: Input
        self.input_panel = InputPanel(content_pane)
        content_pane.add(self.input_panel.frame)

        # Right: Results
        self.result_panel = ResultPanel(content_pane)
        content_pane.add(self.result_panel.frame)

        # Footer / status
        footer = tk.Frame(self.root)
        footer.pack(fill=tk.X)
        self.status_var = tk.StringVar(value="Ready — enter text and choose model then press Run")
        status_label = tk.Label(footer, textvariable=self.status_var, anchor="w")
        status_label.pack(fill=tk.X, padx=6, pady=4)

        # Wire run button to handler
        self.input_panel.run_button.config(command=self.run_comparison)

    def run_comparison(self):
        text = self.input_panel.get_text()
        model = self.input_panel.get_model_choice()
        if not text.strip():
            self.status_var.set("No input text — please type or paste some text.")
            return
        self.status_var.set(f"Running comparison ({model})... (placeholder)")
        # Display basic placeholder results — models not yet integrated
        self.result_panel.display_results(model, text)
        self.status_var.set("Done. (placeholder results shown)")

    def run(self):
        self.root.mainloop()
