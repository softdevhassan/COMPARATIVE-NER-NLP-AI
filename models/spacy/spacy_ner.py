import spacy
import time


# spaCy integration for Mudassir (semester project)
# This file does NOT depend on CRF code. spaCy pre-trained model + heuristics used.
# Comments are casual pakistani-english, small grammar slips (as requested)
class SpacyNER:
    def __init__(self):
        # load small english model, keep it light
        self.nlp = spacy.load("en_core_web_sm")

    def _span_to_dict(self, doc, start, end, label):
        span = doc[start:end]
        return {
            "text": span.text,
            "label": label,
            "start": span.start_char,
            "end": span.end_char,
            "token_start": start,
            "token_end": end,
            "tokens": [t.text for t in span],
        }

    def process(self, text):
        # start timer
        start_time = time.time()

        doc = self.nlp(text)

        # collect spaCy entities first
        spans = []
        covered = set()
        for ent in doc.ents:
            spans.append((ent.start, ent.end, ent.label_))
            for i in range(ent.start, ent.end):
                covered.add(i)

        # heuristic: single PROPN tokens missed by spaCy -> PERSON
        for i, token in enumerate(doc):
            if i in covered:
                continue
            if token.pos_ == "PROPN" and token.text.istitle() and len(token.text) > 1:
                spans.append((i, i + 1, "PERSON"))
                covered.add(i)

        # merge nearby spans if separated by filler tokens like & , -
        spans = sorted(spans, key=lambda s: (s[0], s[1]))
        merged = []
        i = 0
        while i < len(spans):
            s0 = spans[i]
            j = i + 1
            cur_start, cur_end, cur_label = s0
            while j < len(spans):
                s1 = spans[j]
                filler_ok = False
                if cur_end == s1[0]:
                    filler_ok = True
                elif cur_end + 1 == s1[0] and cur_end < len(doc):
                    tok_between = doc[cur_end]
                    if tok_between.text in ["&", ",", "-"]:
                        filler_ok = True
                if filler_ok:
                    cur_end = s1[1]
                    cur_label = cur_label if cur_label != "" else s1[2]
                    j += 1
                else:
                    break
            merged.append((cur_start, cur_end, cur_label))
            i = j

        # expand companies with suffixes
        company_suffixes = {"Inc", "Inc.", "Ltd", "Ltd.", "LLC", "Corp", "Corp."}
        final_spans = []
        for (s, e, lab) in merged:
            if e < len(doc) and doc[e].text in company_suffixes:
                e = e + 1
            final_spans.append((s, e, lab))

        # build result entities (no CRF dependency)
        seen = set()
        entities = []
        for s, e, lab in final_spans:
            key = (s, e)
            if key in seen:
                continue
            seen.add(key)
            ent = self._span_to_dict(doc, s, e, lab)
            ent["method"] = "spacy+heuristics"
            entities.append(ent)

        end_time = time.time()

        return {
            "entities": entities,
            "processing_time": round(end_time - start_time, 4),
            "enhanced": True,
            "method": "spacy+heuristics",
        }
