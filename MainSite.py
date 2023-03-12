import streamlit as st
from GameSession import Session

from time import sleep
class MainPage():
    def __init__(self):
        #Rodzaj Zadania
        options_for_questions = ["Mnożenie", "Dzielenie", "Dodawanie", "Potęgowanie"]
        self.selected_task_type = st.sidebar.selectbox("Wybierz typ wyzwania", options_for_questions)

        # Rodzaj Odpowiedzi 
        options_for_answers = ["pytania otwarte", "pytania zamknięte" ]
        self.selected_answer_type = st.sidebar.selectbox("Wybierz rodzaj pytań", options_for_answers)

        # Tryb Aplikacji 
        options_for_mode = ["trening", "sprawdzian" ]
        self.selected_game_type = st.sidebar.selectbox("Wybierz rodzaj wyzwania", options_for_mode)
        
        # Przyciski Start i Stop
        col1, col2, col3, col4 = st.sidebar.columns(4)
        with col1:
            pass
        with col2:
            self.start_button = st.button('Start', on_click=self.create_session)
        with col3:
            self.stop_button = st.button('Stop')
        with col4 :
            pass
        self.session = None
        
    def create_session(self):
        self.session = Session(self.selected_task_type, self.selected_answer_type, self.selected_game_type) 


A = MainPage()