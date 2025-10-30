from transformers import pipeline
from deep_translator import GoogleTranslator

# Inisialisasi pipeline deteksi emosi
emotion_pipeline = pipeline(
    "text-classification",
    model="bhadresh-savani/bert-base-uncased-emotion",
    top_k=None
)

# Fungsi penerjemahan otomatis ke bahasa Inggris
def translate_to_english(text):
    try:
        translator = GoogleTranslator(source='auto', target='en')
        return translator.translate(text)
    except Exception:
        return text

# Mapping label agar sesuai dengan format sistem
def map_emotion_to_supported(emotion):
    mapping = {
        "joy": "joy",
        "sadness": "sadness",
        "anger": "anger",
        "fear": "fear",
        "surprise": "surprise",
        "love": "love"
    }
    return mapping.get(emotion.lower(), emotion.lower())

# Fungsi utama: deteksi emosi dominan dari teks
def detect_emotion_from_text(text):
    english_text = translate_to_english(text)
    predictions = emotion_pipeline(english_text)[0]
    top = max(predictions, key=lambda x: x['score'])  
    return map_emotion_to_supported(top['label']), predictions

if __name__ == "__main__":
    text = input("Masukkan teks: ")
    detected_mood, predictions = detect_emotion_from_text(text)

    print(f"\nMood yang terdeteksi: {detected_mood}")
    print("\nSkor prediksi dari model:")
    for pred in predictions:
        print(f" - {pred['label']}: {pred['score']:.4f}")
