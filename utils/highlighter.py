class EntityHighlighter:
    """
    Advanced highlighter logic for Tkinter Text widgets.
    Uses tag configuration for different entity types.
    """

    def __init__(self, text_widget):
        self.text_widget = text_widget
        self._setup_tags()

    def _setup_tags(self):
        # Professional color palette for NER
        colors = {
            "PER": "#E1F5FE",  # Blue
            "ORG": "#F3E5F5",  # Purple
            "LOC": "#E8F5E9",  # Green
            "MISC": "#FFF3E0",  # Orange
        }
        for label, color in colors.items():
            self.text_widget.tag_configure(
                label, background=color, borderwidth=1, relief="ridge"
            )

    def highlight(self, entities):
        # Clear existing highlights
        for tag in ["PER", "ORG", "LOC", "MISC"]:
            self.text_widget.tag_remove(tag, "1.0", "end")

        for ent in entities:
            label = ent.get("label", "MISC")
            # Normalize label (B-PER -> PER)
            base_label = label.split("-")[-1] if "-" in label else label

            start_idx = f"1.0 + {ent['start']} chars"
            end_idx = f"1.0 + {ent['end']} chars"

            self.text_widget.tag_add(base_label, start_idx, end_idx)
