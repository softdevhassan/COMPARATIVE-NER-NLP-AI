## Root Files

### `app.py`

- Target: Ye poori application ka entry point hai.
- Role: GUI ko launch karna aur backend modules ko connect karna.
- Task Lead: Hassan

---

### `requirements.txt`

- Target: Project ki zaroori Python libraries list karna.
- Role: Environment setup asaan banana.
- Task Lead: Hassan

---

### `README.md`

- Target: Project overview, features aur quick setup instructions.
- Role: Team project background.
- Task Lead: Team

---

## `gui/` – Tkinter Frontend (Saad)

### `main_window.py`

- Window layout aur menu structure.

### `input_panel.py`

- Text input area aur model select karne ka option.

### `result_panel.py`

- Result display karne k liye side area.

Lead: Saad Ilyas
Focus: Interface design aur experience.

---

## `models/crf/` – CRF Model (Hassan)

### `features.py`

- Feature engineering logic (capitalization, context, shapes).

### `crf_model.py`

- Model class aur prediction logic.

### `trainer.py`

- Dataset se model train karne ka script.

Lead: Hassan Ali
Focus: Backend ML processing.

---

## `models/spacy/` – spaCy Model (Mudassir)

### `spacy_ner.py`

- spaCy model load karna aur text process karna.

Lead: Mudassir
Focus: Neural network model integration.

---

## `comparison/` – Model Comparison

### `comparator.py`

- Dono models ka result compare karna.

Lead: Team (lead Hassan)

---

## `data/`

### `raw/`

- Mehnge dataset (CoNLL2003) k raw files.

### `processed/`

- Cleaned files training k liye.

Lead: Hassan

---

## `utils/`

### `timer.py`

- Execution time measure karne k liye.

### `highlighter.py`

- Entities ko color code highlight karna.

Lead: Hassan

---

## `docs/` – Final Documentation

### `UsageGuide.md`

- Installation aur use karne ka tarika.

Lead: Saad

### `CodingGuide.md`

- Technical documentation developers k liye.

Lead: Everyone
