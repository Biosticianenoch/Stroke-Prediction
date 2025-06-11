
<h1 align="center">🧠 Stroke Risk Prediction App</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Model-RandomForest-success?style=flat-square" />
</p>

> 🏥 **Predict your stroke risk instantly using a machine learning-powered Streamlit web app.**  
> Empowering preventive healthcare through AI and data science.

---

## 📸 App Preview

![App Screenshot](https://github.com/your-repo/stroke-predictor-app/assets/demo-gif.gif)  
<sup><i>Live prediction, personalized recommendations, and educational health resources.</i></sup>

[Live url](https://stroke-prediction-phurginmqmv3exp8uv9pxz.streamlit.app)
---

## 📚 Table of Contents

- [✨ Features](#-features)
- [🧠 Motivation](#-motivation)
- [📊 Dataset & EDA](#-dataset--eda)
- [🚀 Model Pipeline](#-model-pipeline)
- [🛠 Technologies Used](#-technologies-used)
- [💻 How to Run](#-how-to-run)
- [📈 Model Performance](#-model-performance)
- [📁 Project Structure](#-project-structure)
- [📌 Author](#-author)

---

## ✨ Features

✅ Predict stroke risk using demographic and clinical inputs  
✅ Modern, intuitive UI built with Streamlit  
✅ Real-time result and visual alerts  
✅ Personalized health advice  
✅ Interactive sidebar navigation  
✅ FAQ section for awareness & education  
✅ Fast & accurate ML models  

---

## 🧠 Motivation

Stroke is the **second leading cause of death** globally and a major contributor to disability.  
With machine learning, we can make early prediction **accessible, fast, and personalized**.

> "Prevention is better than cure – and prediction is the first step to prevention."

---

## 📊 Dataset & EDA

<details>
<summary><strong>Click to expand</strong> 🔍</summary>

- 4909 entries, 12 features
- No missing or duplicate values
- Columns include:
  - `gender`, `age`, `hypertension`, `heart_disease`, `work_type`, `smoking_status`, etc.
- **Outliers handled** using IQR
- **Label encoding** applied on categorical features
- **Class imbalance** fixed using `RandomOverSampler`

</details>

---

## 🚀 Model Pipeline

```python
1️⃣ Data Cleaning & Preprocessing
2️⃣ Exploratory Data Analysis (EDA)
3️⃣ Feature Engineering & Label Encoding
4️⃣ Oversampling for class balance
5️⃣ Model Training (8 models tested)
6️⃣ Evaluation & Selection (Random Forest chosen)
7️⃣ Deployment via Streamlit + Pickle
```

---

## 🛠 Technologies Used

| Category       | Tools |
|----------------|-------|
| Language       | Python 3.10 |
| Framework      | Streamlit |
| ML Libraries   | Scikit-learn, XGBoost, imbalanced-learn |
| Data Viz       | Seaborn, Matplotlib |
| Deployment     | Pickle, Streamlit Cloud or Vercel |

---

## 💻 How to Run

```bash
# 1. Clone this repo
git clone https://github.com/your-username/stroke-predictor-app.git

# 2. Navigate to folder
cd stroke-predictor-app

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

> ⚠ Ensure `stroke.sav` is in the same directory as `app.py`

---

## 📈 Model Performance Comparison

| Model                     | Accuracy (%) | F1 Score |
|--------------------------|--------------|----------|
| 🏆 Random Forest          | 99.8         | 0.998    |
| Gradient Boosting        | 98.2         | 0.982    |
| XGBoost                  | 98.0         | 0.980    |
| Support Vector Machine   | 93.9         | 0.940    |
| K-Nearest Neighbors      | 89.9         | 0.908    |
| Voting Classifier        | 88.5         | 0.892    |
| AdaBoost                 | 84.9         | 0.860    |
| Logistic Regression      | 76.5         | 0.774    |

> ✅ Best Model: **Random Forest Classifier** — High accuracy and balanced recall/precision.

---

## 📁 Project Structure

```bash
├── app.py                 # Streamlit frontend
├── stroke.sav             # Saved ML model
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── Stroke Prediction.pdf  # Detailed project report
```

---

## 📌 Author

**🧑‍💻 DataQuest Solutions**  
_Data science, AI, and health innovation_  
🌐 [www.dataquestsolutions.tech](https://dqs-git-main-enocks-projects-27f604c8.vercel.app/) • 📧 [info@dataquestsolutions.tech](dataquestsolutions2@gmail.com)

---

## 🌍 Let's Connect

<a href="https://www.linkedin.com/in/enock-bereka"><img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white"></a>
<a href="mailto:enochosenwafulah@gmail.com"><img src="https://img.shields.io/badge/Gmail-red?logo=gmail&logoColor=white"></a>
<a href="https://github.com/Biosticianenoch"><img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white"></a>

---

### ⭐ If you find this project useful, don't forget to give it a star!
