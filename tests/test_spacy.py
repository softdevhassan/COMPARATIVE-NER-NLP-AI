import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.spacy.spacy_ner import SpacyNER


def test():
    print("Testing spaCy Model...")
    ner = SpacyNER()
    text = "Hassan Ali from Google is visiting London in 2026."
    result = ner.process(text)

    print(f"Model: {result['model_name']}")
    print(f"Time: {result['processing_time']}s")
    print("Entities found:")
    for ent in result["entities"]:
        print(f" - {ent['text']} ({ent['label']})")


if __name__ == "__main__":
    test()
