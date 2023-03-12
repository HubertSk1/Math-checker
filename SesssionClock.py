import threading
import time
import streamlit as st

class Clock(threading.Thread):
    def __init__(self, Session):
        threading.Thread.__init__(self)
        self.clock_runing = True
        self.session = Session
    def run(self, *args, **kwargs):
        while self.clock_runing:
            self.session.seconds_counter += 1
            time.sleep(1)
        self.seconds_counter = 0

    def end_the_clock(self):
        self.clock_runing=False

