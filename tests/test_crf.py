import sys
import os
import unittest
import re

# Add project root to path so we can import models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.crf.crf_model import CRFModel
from models.crf.features import extract_features


class TestCRFModel(unittest.TestCase):
    def test_initialization(self):
        """Test that the CRFModel can be initialized"""
        print("\nTesting CRFModel Initialization...")
        model = CRFModel()
        self.assertIsNotNone(model)
        print("CRFModel initialized successfully.")

    def test_methods_exist(self):
        """Test that train and predict methods exist"""
        print("Testing CRFModel methods existence...")
        model = CRFModel()
        # This is just to check if the methods can be called without crashing
        # Implementation is already expert levels in Hassan's part
        try:
            model.predict([])
            print("predict() method exists.")
        except Exception as e:
            self.fail(f"predict() error: {e}")


def run_interactive_test():
    model_path = os.path.join("data", "processed", "crf_model.joblib")
    if not os.path.exists(model_path):
        print("Error: Trained model not found! Please run trainer.py first.")
        return

    print("Loading Hassan's Expert CRF Model...")
    model = CRFModel()
    model.load(model_path)

    print("\n--- Interactive NER Test ---")
    print(
        "READY: Tokenizer v2.0 active (Handles special characters and punctuation separately)"
    )

    while True:
        try:
            sentence = input("\nEnter text (or 'exit'): ")
            if sentence.lower() in ["exit", "quit"]:
                break

            if not sentence.strip():
                continue

            words = re.findall(r"[A-Z]\.(?:[A-Z]\.)+|[\w']+|[^\w\s]", sentence)

            features = [extract_features(words, i) for i in range(len(words))]
            labels = model.predict([features])[0]

            print("\nResults:")
            print(f"{'Token':<15} | {'Label'}")
            print("-" * 25)
            for w, l in zip(words, labels):
                print(f"{w:15} | {l}")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        run_interactive_test()
    else:
        unittest.main()
