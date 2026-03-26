# Entify | Comparative NER Engine Lab

[![Status](https://img.shields.io/badge/Status-Operational-emerald?style=for-the-badge)](https://entify.orbin.dev)
[![Build](https://img.shields.io/badge/Deployment-AWS_EC2-orange?style=for-the-badge)](https://entify.orbin.dev)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

**Entify** is a high-performance research laboratory designed to benchmark and compare two fundamental architectural shifts in Natural Language Processing: **Statistical (CRF)** vs **Neural (spaCy)** Named Entity Recognition.

## 🚀 Key Features
- **Dual-Engine Analysis**: Compare CRF and spaCy models side-by-side.
- **Micro-Benchmark Suite**: Real-time performance tracking (latency, memory, F1 scores).
- **BIO Tagging Visualization**: Deep dive into entity boundary detection.
- **Academic Context**: Developed as a premium research project for BSCS (24-28).

## 🛠️ Technical Stack
- **Backend**: Flask (Python)
- **NLP Core**: 
  - **Statistical**: Custom Conditional Random Fields (CRF) trained on CoNLL2003.
  - **Neural**: spaCy `en_core_web_sm` CNN-based transformer.
- **Frontend**: Modern Glassmorphism UI (Tailwind CSS, Alpine.js, AOS).
- **Deployment**: AWS EC2 with GitHub Actions CI/CD.

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

## 🎓 Academic Credit
- **Institution**: ILM College Sargodha (UOS Affiliated)
- **Course**: Artificial Intelligence
- **Mentor**: Sir Abdur-Rehman
- **Team**: Hassan Ali (Lead), Mudassir Ali, Saad Ilyas.

---
*For more details, visit the [official documentation](https://entify.orbin.dev/docs/user).*