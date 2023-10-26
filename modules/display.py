from threading import Thread
from time import sleep

class DisplayModule:
    def __init__(self):
        self.top_text = ""
        self.bottom_text = ""

        self.top_display_text = ""
        self.bottom_display_text = ""

        self.top_pos = 0
        self.top_pos_max = 0

        self.bottom_pos = 0
        self.bottom_pos_max = 0

        self.running = False

    def display(self, line, text):

        if self.running:
            self.running = False
            self.update_thread.join()

        self.top_pos = 0
        self.bottom_pos = 0

        if line == 0:
            self.top_pos = 0
            if len(text) <= 16:
                self.top_text = text
                self.top_pos_max = 0
            else:
                self.top_text = "   " + text + "   " #pad the text with spaces
                self.top_pos_max = 16 - len(self.top_text) 
        else:
            self.bottom_pos = 0
            if len(text) <= 16:
                self.bottom_text = text
                self.bottom_pos_max = 0
            else:
                self.bottom_text = "   " + text + "   " #pad the text with spaces
                self.bottom_pos_max = 16 - len(self.bottom_text)

        self.update_thread = Thread(target = self.update, args = ( ))
        self.update_thread.start()
        
         
    
    def update(self):

        while self.running:
            if self.top_pos == self.top_pos_max:
                self.top_pos = 0
            else:
                self.top_pos += 1

            if self.bottom_pos == self.bottom_pos_max:
                self.bottom_pos = 0
            else:
                self.bottom_pos += 1

            lcdstring = self.top_text[self.top_pos : self.top_pos_max + 16] + '\n' + self.bottom_text[self.bottom_pos : self.bottom_pos_max + 16]
            #lcd display lcdstring

            sleep(0.3)
