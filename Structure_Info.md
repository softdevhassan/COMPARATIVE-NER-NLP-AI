## Root Files

### `app.py`

- Purpose: Ye poori desktop application ka entry point hai.
- Kaam: GUI launch karta hai aur backend modules ko connect karta hai.
- Responsible: Hassan

---

### `requirements.txt`

- Purpose: Project ke liye zaroori saari Python libraries define karta hai.
- Kaam: Environment setup easy banana. aaj kal standard ha. better to use it.
- Responsible: Hassan

---

### `README.md`

- Purpose: Project overview, features, aur quick setup instructions.
- Responsible: Team

---

## `gui/` – Tkinter Frontend (Saad)

### `main_window.py`

- Main application window ka layout
- Buttons, headings, overall structure

### `input_panel.py`

- User ka text input area
- Model selection (CRF / spaCy)

### `result_panel.py`

- Side-by-side NER results display
- Highlighted entities + metrics

Handled by: Saad Ilyas
Focus: User experience aur interface

---

## `models/crf/` – CRF Model (Hassan)

### `features.py`

- CRF ke liye feature engineering
- Capitalization, prefix/suffix, word shape, context words

### `crf_model.py`

- CRF model class
- Predict function + inference logic

### `trainer.py`

- CoNLL2003 dataset se model training
- Feature extraction + fitting

Handled by: Hassan Ali
Focus: Transparent, interpretable ML

---

## `models/spacy/` – spaCy Model (Mudassir)

### `spacy_ner.py`

- spaCy `en_core_web_sm` model load
- Text processing + entity extraction

Handled by: Mudassir
Focus: Pre-trained neural NER integration

---

## `comparison/` – Model Comparison (Week-5)

### `comparator.py`

- CRF vs spaCy results comparison
- Processing time
- Confidence score
- Entity overlap

Handled by: Team (lead Hassan)

---

## `data/`

### `raw/`

- Kaggle se downloaded CoNLL2003 dataset

### `processed/`

- Cleaned / parsed dataset for training

Handled by: Hassan

---

## `utils/`

### `timer.py`

- Processing time measurement

### `highlighter.py`

- Text mein entities ko highlight karna (GUI ke liye)

Handled by: Hassan (support to GUI)

---

## `docs/` – Final Documentation

### `UsageGuide.md`

- User ke liye step-by-step guide
- Installation + usage

Handled by: Saad

### `CodingGuide.md`

- Developer documentation
- Architecture, classes, workflows

Handled by: Hassan + Mudassir

---

## Teacher-friendly one-liner

Agar sir pooche:

"Structure kaise design ki?"

Bolo:

"We followed a modular OOP-based structure separating GUI, models, and comparison logic, with clearly assigned responsibilities for each team member."

---

Agar chaho next:

- `README.md` ready likh deta hoon
- CRF `features.py` ka actual Week-3 code
- spaCy class code
- Tkinter GUI skeleton

Bas bolo
