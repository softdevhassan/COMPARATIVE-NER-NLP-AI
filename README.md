# Entify | Comparative NER Engine Lab

[![Status](https://img.shields.io/badge/Status-Operational-emerald?style=for-the-badge)](https://entify.orbin.dev)
[![Deployment](https://img.shields.io/badge/Deployment-AWS_EC2-orange?style=for-the-badge)](https://entify.orbin.dev)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

**Entify** is a high-performance research laboratory designed to benchmark and compare two fundamental architectural shifts in Natural Language Processing: **Statistical (CRF)** vs **Neural (spaCy)** Named Entity Recognition.

## 🚀 Key Features
- **Dual-Engine Comparison**: Real-time side-by-side analysis of CRF and spaCy models.
- **Advanced Confidence Metrics**: Probabilistic scores for both engines (CRF Marginals vs Neural Heuristics).
- **Localized Presets**: Specialized inference samples for **News, Tech, Finance, and Business** from a Pakistani perspective.
- **Context-Aware Analytics**: Intelligent metrics board that toggles between "Quality Leader" and "Unique Labels" based on mode.
- **Export Capabilities**: Seamlessly export findings in **JSON** or **TXT** formats.

## 🛠️ Technical Stack
- **Backend**: Flask (Python 3.9+)
- **NLP Core**: 
  - **Statistical**: Custom Conditional Random Fields (CRF) trained on CoNLL2003 (90.3% F1).
  - **Neural**: spaCy `en_core_web_sm` (Efficient ~12MB CNN architecture).
- **Frontend**: Modern Glassmorphism UI (Tailwind CSS, Alpine.js, AOS).
- **Deployment**: AWS EC2 with Gunicorn + Apache.

## 📖 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/softdevhassan/entify.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment:
   - Create a `.env` file based on project metadata.
4. Run the lab locally:
   ```bash
   python app.py
   ```

## 🎓 Project Credit
- **Institution**: ILM College Sargodha (UOS Affiliated)
- **Course**: Artificial Intelligence (BSCS Semester 3)
- **Mentor**: Sir Abdur-Rehman
- **Lead Developer**: Hassan Ali
- **Core Team**: Mudassir Ali (Inference Analysis), Saad Ilyas (Design Systems).

---
*For more details, visit the [official documentation](https://entify.orbin.dev/docs/user).*