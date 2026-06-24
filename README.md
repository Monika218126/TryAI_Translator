# TryAI_Translator
# 🌐 Linguify – AI Language Translation & Speech Assistant

Linguify is a full-stack web application that enables real-time language translation, speech-to-text conversion, and text-to-speech output using AI and NLP libraries. It supports multilingual communication using machine learning and speech processing tools.

---

## 🚀 Features

- 🌍 Automatic language detection
- 🔤 Real-time text translation
- 🎤 Speech-to-text (voice input)
- 🔊 Text-to-speech (audio output)
- 🤖 AI-based NLP processing using Transformers
- 💬 Simple and responsive web interface

---

## 🛠️ Tech Stack

### Frontend:
- HTML
- CSS
- JavaScript

### Backend:
- Python (Flask)

### Libraries Used:
- googletrans (translation)
- langdetect (language detection)
- SpeechRecognition (voice to text)
- gTTS (text to speech)
- transformers (AI/NLP models)

---

## 📁 Project Structure

linguify/

│

├── static/

│   ├── style.css

│   └── script.js

│

├── templates/

│   └── index.html

│
├── app.py

├── requirements.txt

└── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/your-username/linguify.git
cd linguify

---

### 2. Create virtual environment (recommended)
python -m venv venv

Activate virtual environment:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 3. Install dependencies
pip install flask googletrans==4.0.0-rc1 langdetect SpeechRecognition gTTS transformers

---

### 4. Run the application
python app.py

---

### 5. Open in browser
http://127.0.0.1:5000/

---

## 🎤 How It Works

1. User enters text or speaks using microphone  
2. Backend detects language automatically  
3. Text is translated into target language  
4. Output is displayed in browser  
5. Audio output is generated using gTTS  

---

## 📦 requirements.txt

flask
googletrans==4.0.0-rc1
langdetect
SpeechRecognition
gTTS
transformers

---

## 🔮 Future Improvements

- Real-time conversation translation  
- Mobile app version  
- Offline translation support  
- Better transformer models for accuracy  
- Voice cloning feature  
- More language support  

---

## 🤝 Contributing

- Fork the repository  
- Create a new branch  
- Make changes  
- Submit Pull Request  

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by Monika M

---

⭐ If you like this project, give it a star on GitHub!
