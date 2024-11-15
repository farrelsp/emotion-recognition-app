import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Inisialisasi stop words untuk bahasa Indonesia
stop_words = set(stopwords.words('indonesian'))

# Kamus emotikon ke emosi dalam bahasa Indonesia
emoticon_dict = {
    "😊": "ekspresi senang",
    "🤣": "ekspresi senang",
    "😃": "ekspresi senang",
    "😄": "ekspresi senang",
    "😂": "ekspresi senang",
    "😁": "ekspresi senang",
    "😆": "ekspresi senang",
    "😍": "ekspresi senang",
    "🤗": "ekspresi senang",
    "🤨": "ekspresi kaget",
    "😯": "ekspresi kaget",
    "😮": "ekspresi kaget",
    "🤢": "ekspresi jijik",
    "🤮": "ekspresi jijik",
    "😷": "ekspresi jijik",
    "😖": "ekspresi jijik",
    "😫": "ekspresi jijik",
    "😩": "ekspresi jijik",
    "😲": "ekspresi kaget",
    "🤯": "ekspresi kaget",
    "😢": "ekspresi sedih",
    "😭": "ekspresi sedih",
    "😞": "ekspresi sedih",
    "😔": "ekspresi sedih",
    "😟": "ekspresi sedih",
    "😕": "ekspresi sedih",
    "😦": "ekspresi sedih",
    "😿": "ekspresi sedih",
    "🤝": "ekspresi percaya",
    "👍": "ekspresi percaya",
    "🙏": "ekspresi percaya",
    "🤲": "ekspresi antisipasi",
    "😡": "ekspresi marah",
    "😠": "ekspresi marah",
    "🤬": "ekspresi sangat marah",
    "😤": "ekspresi marah",
    "😾": "ekspresi marah",
    "😨": "ekspresi takut",
    "😰": "ekspresi takut",
    "😥": "ekspresi takut",
    "😱": "ekspresi takut",
    ":')": "ekspresi senang",
    ":)": "ekspresi senang",
    ":D": "ekspresi senang",
    ":(": "ekspresi sedih",
    ":'(": "ekspresi sedih",
    ":-)": "ekspresi senang",
    ":-D": "ekspresi senang",
    ":-(": "ekspresi sedih",
    ":P": "ekspresi bahagia",
    ";)": "ekspresi senang",
    ":-O": "ekspresi kaget",
    ":O": "ekspresi kaget",
}

class Preprocessing:
    def init(__self__) -> None:
        pass

    def replace_emoticons(self, text):
        for emoticon, emotion in emoticon_dict.items():
            if emoticon in text:
                # Tambah koma sebelum deskripsi emosi jika ada teks sebelum emotikon
                text = re.sub(r'(\S)(' + re.escape(emoticon) + r')', r'\1, ' + emotion, text)
                # Ganti emotikon yang berdiri sendiri tanpa tambahan koma
                text = text.replace(emoticon, emotion)
        return text

    def clean_text(self, text):
        # Mengubah teks menjadi huruf kecil
        text = text.lower()
        # Menghapus URL
        text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
        # Menghapus mention (@username) dan hashtag
        text = re.sub(r'@\w+|#', '', text)
        # Menghapus angka
        text = re.sub(r'\d+', '', text)
        # Gantikan emotikon dengan deskripsi emosi terlebih dahulu
        text = self.replace_emoticons(text)
        # Menghapus tanda baca dan simbol kecuali yang ada dalam deskripsi emotikon
        allowed_punctuation = ''.join(re.escape(c) for c in emoticon_dict.values())
        text = re.sub(r'[^\w\s' + allowed_punctuation + r']', '', text)
        # Menghapus karakter non-ASCII
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        # Menghapus spasi berlebih
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
# # Example
# preprocessing = Preprocessing()
# text = "Ini adalah (contoh + :) tweet:') dengan emotikon 😊 dan URL https://example.com!"
# cleaned_text = preprocessing.clean_text(text)
# print(cleaned_text)