📩 Spam SMS Detection 🔍

🚀 Overview SMS Spam Predictor is a machine learning-based classifier that predicts whether a given message is Spam or Not Spam using Natural Language Processing (NLP) techniques. It is built with Flask for the web interface and trained using TF-IDF Vectorization and Naïve Bayes.

🛠️ Features ✅ Preprocesses text (lowercasing, tokenization, stopword removal, stemming). ✅ Uses TF-IDF vectorization for feature extraction. ✅ Trained on Naïve Bayes & other ML models. ✅ Provides a web-based interface for predictions.

📂 Project Structure

📁 Spam SMS Detection
│── 📄 app.ipynb # Jupyter Notebook with Flask App
│── 📄 model_training.ipynb # Notebook for Training & Saving Model
│── 📄 vectorizer.pkl # Saved TF-IDF Vectorizer
│── 📄 model.pkl # Saved ML Model
│── 📄 README.md # Project Documentation
│── 📄 requirements.txt # Python Dependencies
🏗️ Setup Instructions 🔹 1. Clone the Repository git clone https://github.com/yourusername/SMS-Spam-Predictor.git cd SMS-Spam-Predictor

🔹 2. Install Dependencies pip install -r requirements.txt

🔹 3. Train & Save the Model If model.pkl and vectorizer.pkl are missing, run:

jupyter notebook Open model_training.ipynb, run all cells, and save the model.

🔹 4. Run the Flask App Since you're using Jupyter Notebook, run the following command inside it: from threading import Thread Thread(target=run_flask).start() Now, open http://127.0.0.1:5000/ in your browser.

⚡ Tech Stack Python 🐍 Flask 🌐 NLTK 📚 Scikit-Learn 🤖 Pandas & NumPy 📊 📌 To-Do ✅ Train with more datasets ✅ Improve accuracy with advanced NLP techniques ⬜ Deploy to a cloud service

💡 Contributing Feel free to fork this repository and submit a pull request if you find any improvements! 🚀
