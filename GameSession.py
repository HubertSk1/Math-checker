import streamlit as st
from SesssionClock import Clock
from random import randint
from Task import Task

class Session():
    def __init__(self, task, answer, game):
        #Settings
        self.task = task
        self.answer = answer
        self.game = game
         
        #Tasks  
        self.total_tasks = 1
        self.solved_tasks = 0 
        self.current_task_number = 0
        self.inserted_answer = None
        self.current_task = Task(self.task)

        #Clock
        self.seconds_counter = 0 
        self.clock = Clock(self)
        self.clock.start()
        self.create_next_task()

        #Message
        self.message = None

    def create_next_task(self):
        self.current_task_number += 1
        if self.current_task_number <= self.total_tasks:
            self.current_task = Task(self.task)
            self.generate_task_layout()
        else :
            self.generate_summary_layout()

    def show_the_answer(self):
        answer = st.session_state["answer"]
        try:
            answer_converted=int(answer)
        except:
            st.write("twoja odpowiedź ma zły format, wprowadź liczbę")
            self.generate_task_layout()
            return
        
        if answer_converted == self.current_task.result and  self.current_task_number <= self.total_tasks :
            if self.current_task_number != self.total_tasks:
                st.write("super , twoja odpowiedź była poprawna")
            self.create_next_task()
        else:
            st.write("twoja odpowiedź była błędna, spróbuj ponownie")
            self.generate_task_layout()

    def generate_task_layout(self):
        st.markdown(f'<p style="text-align: center;font-size:40px">ZADANIE {self.current_task_number}</p>',unsafe_allow_html = True)
        form = st.form("my_form", clear_on_submit = True)
        form.markdown(f'<p style="text-align: center;font-size:40px">{self.current_task.equation}</p>',unsafe_allow_html = True)
        form.text_input("title", value="", label_visibility = "hidden",key="answer")
        form.columns(5)[4].form_submit_button("Sprawdź", on_click = self.show_the_answer)


    def generate_summary_layout(self):
        st.markdown(f'<p style="text-align: center;font-size:35px">Gratulacje, udało ci się ukończyć serię zadań! !</p>', unsafe_allow_html= True)
        st.write(f'ilość poprawnie wykonanych zadań: {self.total_tasks}')
        st.write(f'czas :  {self.seconds_counter} sekund')

