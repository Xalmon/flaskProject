import datetime


class Diary:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        self.isLock = False
        self.entries = []
        self.timeAndDate = datetime.datetime.now()

    def add_entry(self, entry):
        self.entries.append(entry)

    def lock_diary(self):
        self.isLock = True

    def unlock_diary(self):
        self.isLock = False



