from flask import Flask, render_template, request
from googletrans import Translator
from langdetect import detect
from gtts import gTTS
import os

app = Flask(__name__)

translator = Translator()

languages = {
    "English":"en",
    "Tamil":"ta",
    "Hindi":"hi",
    "French":"fr",
    "German":"de",
    "Spanish":"es"
}

@app.route("/", methods=["GET","POST"])
def home():

    translated_text = ""
    detected_lang = ""

    if request.method == "POST":

        text = request.form["text"]
        target = request.form["target"]
        source = request.form["source"]

        detected_lang = detect(text)

        lang_names = {
              "en": "English",
    "ta": "Tamil",
    "hi": "Hindi",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "da": "Danish",
    "te": "Telugu",
    "ml": "Malayalam",
    "kn": "Kannada",
    "bn": "Bengali",
    "gu": "Gujarati",
    "mr": "Marathi",
    "pa": "Punjabi",
    "ur": "Urdu",
    "ar": "Arabic",
    "zh-cn": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "ru": "Russian"
        }
        detected_lang = lang_names.get(
             detected_lang,
             detected_lang
        )

        result = translator.translate(
            text,
            src=source,
            dest=languages[target]
        )

        translated_text = result.text

        tts = gTTS(translated_text)

        if not os.path.exists("static/audio"):
            os.makedirs("static/audio")

        tts.save("static/audio/output.mp3")

    return render_template(
        "index.html",
        translated_text=translated_text,
        detected_lang=detected_lang,
        languages=languages.keys()
    )

if __name__ == "__main__":
    app.run(debug=True)