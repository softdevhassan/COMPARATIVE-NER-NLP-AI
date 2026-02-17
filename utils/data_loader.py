import os


class DataLoader:
    """
    DataLoader class for CoNLL2003 formatted NER datasets.
    Dataset format: Word POS-tag Chunk-tag NER-tag
    Sentences are separated by blank lines.
    """

    def __init__(self):
        pass

    def load_data(self, file_path):
        """
        Loads the CoNLL2003 data from a file.

        Args:
            file_path (str): Path to the CoNLL formatted file.

        Returns:
            list: A list of sentences, where each sentence is a list of tuples (word, pos, chunk, label).
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset file not found at: {file_path}")

        sentences = []
        current_sentence = []

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                # Check for blank lines or document separators
                if not line or line.startswith("-DOCSTART-"):
                    if current_sentence:
                        sentences.append(current_sentence)
                        current_sentence = []
                    continue

                # Split the line by whitespace
                parts = line.split()
                if len(parts) >= 4:
                    word = parts[0]
                    pos = parts[1]
                    chunk = parts[2]
                    label = parts[3]
                    current_sentence.append((word, pos, chunk, label))

            # Add the last sentence if it exists and wasn't followed by a blank line
            if current_sentence:
                sentences.append(current_sentence)

        return sentences


if __name__ == "__main__":
    # Quick sanity check
    loader = DataLoader()
    try:
        # Using a relative path that should resolve correctly if run from project root
        test_file = os.path.join("data", "raw", "conll2003", "eng.train")
        data = loader.load_data(test_file)
        print(f"Loaded {len(data)} sentences from {test_file}")
        if data:
            print("Example first sentence:")
            for item in data[0]:
                print(item)
    except Exception as e:
        print(f"Error: {e}")
