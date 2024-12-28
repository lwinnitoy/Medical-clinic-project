from datetime import datetime

class Note:
    def __init__(self, code, text):
        self.code = code
        self.text = text
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Code: {self.code}\n\nText: {self.text}"
    
    def __eq__(self, other):
        return self.code == other.code and self.text == other.text