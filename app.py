import pickle
import nltk
from flask import Flask, request, jsonify, render_template
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# Ensure correct nltk path
nltk.data.path.append("D:/nltk_data")

# Ensure NLTK dependencies are installed
nltk.download('punkt')
nltk.download('stopwords')

# Load Model & Vectorizer
try:
    with open('vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)  # Ensure this is a TfidfVectorizer
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)  # Ensure this is a trained model
    print("✅ Model and Vectorizer loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")

ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    # Ensure stopwords list exists
    stop_words = set(stopwords.words('english'))
    
    text = [i for i in text if i not in stop_words]
    text = [ps.stem(i) for i in text if i.isalnum()]
    return " ".join(text)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        message = data.get("message", "")

        if not message:
            return jsonify({"error": "No message provided"}), 400

        transformed_msg = transform_text(message)
        vector_input = tfidf.transform([transformed_msg])
        
        # Convert sparse matrix to dense array before passing to SVC
        prediction = model.predict(vector_input.toarray())[0]  

        result = "Spam" if prediction == 1 else "Not Spam"
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
