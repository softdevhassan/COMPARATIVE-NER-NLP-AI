import sys
import os
import json

# Add project root to path so we can import models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.spacy.spacy_ner import SpacyNER


def main():
    text = (
        "Barack Obama visited Microsoft Inc. in 2020. He met with John at the office."
    )
    print("Sample text:\n", text)

    sp = SpacyNER()
    try:
        res = sp.process(text)
        print("\n--- spaCy NER (enhanced) ---")
        print(json.dumps(res, indent=2))
    except Exception as e:
        print("spaCy test raised:", e)


if __name__ == "__main__":
    main()
