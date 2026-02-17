import spacy
import time


class SpacyNER:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process(self, text):
        start_t = time.time()
        doc = self.nlp(text)

        entities = []
        for ent in doc.ents:
            e_dict = {
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char,
            }
            entities.append(e_dict)

        end_t = time.time()
        p_time = round(end_t - start_t, 4)
        return {
            "entities": entities,
            "processing_time": p_time,
            "model_name": "en_core_web_sm",
        }
