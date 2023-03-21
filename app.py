import streamlit as st
import pandas as pd
from htbuilder import div, big, h2, styles
from htbuilder.units import rem
import pickle

# load saved model
with open('rfc_model_pkl' , 'rb') as f:
   rfc_pretrained = pickle.load(f)

st.markdown('# ANÁLISE DE CANDIDATO')

st.markdown('Esta aplicação permite que você escolha as características do candidato e automaticamente aparecerá na tela a decisão a ser tomada baseada no perfil desejado. Aproveite!')

# Getting heat exchanger data

def get_manager_data():

    st.markdown("# Dados do candidato:")
    analitico = st.selectbox('É analítico?', ('Sim', 'Não'))
    proativo = st.selectbox('É proativo?', ('Sim', 'Não'))
    resiliente = st.selectbox('É resiliente?', ('Sim', 'Não'))
    comunicador = st.selectbox('É comunicador?', ('Sim', 'Não'))
    pensamento_critico = st.selectbox('Tem pensamento crítico?', ('Sim', 'Não'))
    flexivel = st.selectbox('É flexível?', ('Sim', 'Não'))

    if analitico == 'Sim':
        analitico = 1
    else:
        analitico = 0

    if proativo == 'Sim':
        proativo = 1
    else:
        proativo = 0

    if resiliente == 'Sim':
        resiliente = 1
    else:
        resiliente = 0

    if comunicador == 'Sim':
        comunicador = 1
    else:
        comunicador = 0

    if pensamento_critico == 'Sim':
        pensamento_critico = 1
    else:
        pensamento_critico = 0

    if flexivel == 'Sim':
        flexivel = 1
    else:
        flexivel = 0

    manager_data = {'Analítico' : analitico,
                    'Proativo' : proativo,
                    'Resiliente' : resiliente,
                    'Comunicador' : comunicador,
                    'Pensamento crítico' : pensamento_critico,
                    'Flexível' : flexivel}
                        
    features = pd.DataFrame(manager_data, index = [0])

    return features

manager_input = get_manager_data()

# Making predictions
prediction = rfc_pretrained.predict(manager_input)
if prediction == 0:
    prediction = "NÃO"
else:
    prediction = "SIM"

# Creating parameters to use after
color = '#FF4D4C'
title = 'EU CONTRATARIA?'
value = prediction + '!'

st.markdown(
        div(
            style=styles(
                text_align="left",
                color = color,
                padding=(rem(1), 0, rem(1), 0),
            )
        )(
            h2(style=styles(font_size=rem(2), font_weight=800, padding=0))(title),
            big(style=styles(font_size=rem(4), font_weight=800, line_height=1.5))(
                value
            ),
        ),
        unsafe_allow_html=True,
    )