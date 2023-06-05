import streamlit as st
import pandas as pd
import pickle
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import string
from nltk.corpus import stopwords

def process_description(description):
    # Tokenização
    tokens = nltk.word_tokenize(description.lower())

    # Remoção de stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Remoção de pontuações
    tokens = [token for token in tokens if token not in string.punctuation]

    # Unir tokens em uma única string
    processed_description = ' '.join(tokens)

    return processed_description


st.title("Project: Natural Language Processing")
model_path = 'modelo_lgb.pkl'
tfidf_path = 'tfidf.pkl'

# Carregar o modelo treinado a partir do arquivo .pkl
model = None

with open(model_path, 'rb') as file:
    model = pickle.load(file)

loaded_tfidf = None
with open(tfidf_path, 'rb') as file:
    loaded_tfidf = pickle.load(file)


user_description = st.text_input("Digite a frase de descrição do produto (em inglês):", key="user_description")
if user_description:


    # Pré-processar a descrição do usuário
    processed_user_description = process_description(user_description)

    # Aplicar a transformação TF-IDF na descrição do usuário
    user_description_tfidf = loaded_tfidf.transform([processed_user_description])

    # Fazer a previsão usando o modelo carregado
    user_score = model.predict(user_description_tfidf)[0]


    st.write("Score previsto do produto: ", user_score)

