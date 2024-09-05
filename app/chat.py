from app.models import 
class Message:
    def __init__(self, event, data):
        self.event = event
        self.data = data
        
    def analysis(self):
        events = [
            "new_message",
            "close_chat",
            "transfer_chat",
            "rating"
        ]
        if self.event in events:
            if self.event == "new_message":
                self.new_message()
            elif self.event == "close_chat":
                self.close_chat()
            elif self.event == "transfer_chat":
                self.transfer_chat()
            elif self.event == "rating":
                self.rating()
    
    def new_message(self):
        if self.data['sender']['from'] == 'user':
            

    def close_chat(self):
        pass
    
    def transfer_chat(self):
        pass
    
    def rating(self):
        pass
