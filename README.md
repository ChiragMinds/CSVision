<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python" />
  <img src="https://img.shields.io/badge/Framework-LangChain-blueviolet.svg" alt="LangChain" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red.svg" alt="Streamlit" />
  <img src="https://img.shields.io/badge/AI-Google%20Gemini-purple.svg" alt="Google Gemini" />
  <img src="https://img.shields.io/badge/Vector%20Search-FAISS-green.svg" alt="FAISS" />
</p>

<h1 align="center">📊 CSVision — AI-Powered CSV Analysis Platform</h1>

---

## Project Summary

CSVision is an **AI-powered data analysis application** built using **Streamlit and Google Gemini** that enables users to interact with CSV files using natural language. The application allows users to explore datasets, generate summaries, analyze data, and extract meaningful insights without writing SQL queries or Python code.

The project demonstrates how **large language models** can be integrated with structured data workflows to simplify data understanding and decision-making. CSVision is designed as a **modular, extensible, and portfolio-ready application**.

This repository is intended for **educational, demonstration, and portfolio use**.

---

## 🔧 Features and Components

- Interactive **Streamlit-based UI**
- **Chat with CSV** using natural language
- Automated **CSV summarization**
- **AI-generated insights** and observations
- Dataset profiling (rows, columns, data types, missing values)
- Modular service-based backend structure
- Environment variable–based API key management

---

## 🧰 Project Structure

```bash
CSVision/
│
├── app.py                     # Streamlit application entry point
├── services/                  # Core application logic
│   ├── gemini_client.py       # Google Gemini client wrapper
│   ├── insights.py            # Insight generation logic
│   ├── summarizer.py          # CSV summarization logic
│   └── analyzer.py            # Data analysis utilities
├── requirements.txt           # Python dependencies  
├── .gitignore
└── README.md
```

---

## 🧠 AI Model Details

- The application uses **Google Gemini** via the `google-genai` SDK.
- CSV data is processed using **Pandas** and relevant context is dynamically constructed.
- The AI model is used to:
  - Answer natural language questions about the dataset
  - Generate concise summaries of CSV files
  - Extract insights, trends, and observations from structured data

> Note: All outputs are **AI-assisted interpretations** and should be reviewed for accuracy before making decisions.

---

## 🧪 Requirements

- Python 3.9+
- Streamlit
- Pandas
- google-genai
- FAISS
- Sentence Transformers
- python-dotenv

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application Locally

### Clone the repository
```bash
git clone https://github.com/your-username/CSVision.git
cd CSVision
```
### Create and activate a virtual environment
```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
```
### Configure environment variables

Create a `.env` file in the project root and add:

```bash
GOOGLE_API_KEY=your_gemini_api_key
```
### Start the Streamlit application
```bash
streamlit run app.py
```

---

## ⚠️ Notes and Limitations

- This project is intended for **educational and demonstration purposes**
- Performance may vary with large CSV files
- API usage is subject to **Google Gemini quota limits**
- Avoid exposing the application publicly without authentication or rate limiting

---

## Authors and Contact

- **Chirag Chauhan**  
  📧 chiragchauhan1401@gmail.com
