import random
import json
import pickle
import numpy as np
import speech_recognition as sr
import pyttsx3 as ttx
import googletrans
from googletrans import Translator
import nltk

from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

translator = Translator()

listener=sr.Recognizer()
engine=ttx.init()
voice=engine.getProperty('voices')
engine.setProperty('voice','french')

def parler(text):
    engine.say(text)
    engine.runAndWait()

def ecouter():
    try:
        with sr.Microphone() as source:
            print("parlez maintenant")
            voix=listener.listen(source)
            command=listener.recognize_google(voix,language='fr-FR')
            command.lower()
    except:
        pass
    return command




lemmatizer = WordNetLemmatizer()

intents = json.loads(open(r'C:\Users\HP\Desktop\bluetooth\hakkillo\wascalbot\backend\intents.json', encoding="utf8").read())

words = pickle.load(open(r'C:\Users\HP\Desktop\bluetooth\hakkillo\wascalbot\words.pkl', 'rb'))
classes = pickle.load(open(r'C:\Users\HP\Desktop\bluetooth\hakkillo\wascalbot\classes.pkl', 'rb'))
model = load_model(r'C:\Users\HP\Desktop\bluetooth\hakkillo\wascalbot\chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word)  for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words= clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1

    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda  x:x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list,intents_json):
    tag= intents_list[0]['intent']
    list_of_intents =intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

"""print("|============= Welcome to WASCAL =============|")
print("|============================== AI CHATBOT============================|")
print("|================================== To ===============================|")
print("|=============== Ask your any query about our entreprise ================|")"""
def chat(question):
    while True:
        # command = request.POST.get('input',False)
        Q=translator.translate(question, src="fr", dest="en")
        Qe= Q.text
        ints = predict_class(Qe)
        res = get_response(ints, intents)
        A=translator.translate(res, src='en', dest='fr')
        Ae= A.text
        
        #print("| wascalBot:", Ae)
        return Ae


