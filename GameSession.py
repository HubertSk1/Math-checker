import datetime 
import streamlit as st
from SesssionClock import Clock
from time import sleep
class Session():
    def __init__(self, task, answer, game):
        #Settings
        self.task = task
        self.answer = answer
        self.game = game
         
        #Tasks  
        self.total_tasks = 25
        self.solved_tasks = 0 
        self.current_task_number = 0

        #Clock
        self.seconds_counter = 0 
        self.clock = Clock(self)
        self.clock.start()
        self.create_task()

        #Message
        self.message
    def create_task(self):
        self.current_task_number += 1
        self.message = self.seconds_counter
        self.generate_task_layout()

    def generate_task_layout(self):
        st.markdown(f'<p style="text-align: center;">ZADANIE {self.current_task_number}</p>',unsafe_allow_html = True)
        st.write("2+2")
        form = st.form("my_form", clear_on_submit=True)

        form.text_input("title", value="", label_visibility = "hidden")
        
        form.form_submit_button("Check", on_click = self.create_task )

class Task():
    def __init__(self):
        self.first_number = None
        self.secend_number = None
        self.Result = None
