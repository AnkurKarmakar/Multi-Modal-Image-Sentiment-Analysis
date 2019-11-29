# Import modules
from PIL import Image
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pytesseract
# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Create an image object of PIL library
image = Image.open('ecc.jpg')
# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')
# Print the text
print(image_to_text)

analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

sentiment_analyzer_scores(image_to_text) #image_to_text contains extracted text

