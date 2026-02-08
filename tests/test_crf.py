import sys
import os
import unittest

# Add project root to path so we can import models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.crf.crf_model import CRFModel


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
        try:
            model.train([], [])
            print("train() method called successfully (empty implementation).")
        except Exception as e:
            self.fail(f"train() raised an exception: {e}")

        try:
            res = model.predict([])
            print("predict() method called successfully.")
            self.assertEqual(res, [])
        except Exception as e:
            self.fail(f"predict() raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
