# 🎬 AI-Powered Movie Recommender System
Developed by: **Darshan Kotadiya** | Full Stack Developer

## 🚀 Live Demo
Check out the live application here: [darshan-movie.streamlit.app](https://darshan-movie.streamlit.app)

## 📌 Project Overview
This project is a Content-Based Movie Recommendation Engine built for my **Codsoft Internship (Task 4)**. It analyzes movie metadata—including genres, keywords, cast, and crew—to suggest the top 5 most similar movies based on a user's selection.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Streamlit, Pandas, Scikit-learn, NLTK, Pickle
* **Dataset:** TMDB 5000 Movies Dataset

## 🧠 How It Works (Algorithm)
1. **Data Preprocessing:** Merged movie and credit datasets, cleaned metadata, and handled missing values.
2. **Text Vectorization:** Converted text tags into mathematical vectors using **CountVectorizer**.
3. **Similarity Engine:** Calculated the "distance" between movie vectors using **Cosine Similarity** to find the most relevant matches.
4. **Cloud Deployment:** Implemented a "Live Calculation" fallback to handle the 25MB GitHub upload limit for large data models.


## 💻 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/darshankotadiya/CODSOFT.git](https://github.com/darshankotadiya/CODSOFT.git)

   Navigate to the folder:

Bash
cd Task-4-Recommendation-System
2.Install dependencies:

Bash
pip install -r requirements.txt

3. Run the application:

Bash
streamlit run app.py

---

### **Project Final Explanation (For your Interview/Portfolio)**
* **The "Live Calculation" Logic:** Because GitHub prevents browser uploads of files over 25MB (like your `similarity.pkl`), you successfully updated the code to calculate the similarity matrix directly on the Streamlit server. This is a great example of **Production Problem Solving**.
* **Vectorization:** Your app uses the top 5,000 features from your movie "tags" to create a high-dimensional space where similar movies sit closer together.


**Darshan, you've mastered Task 4! Should we now prepare the professional English README for Task 5 (Face Intelligence) so you can submit your final internship report?**
