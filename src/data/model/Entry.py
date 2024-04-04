import datetime


class Entry:
    def __init__(self, id, title, body, ownerName):
        self.id = id
        self.title = title
        self.body = body
        self.ownerName = ownerName
        self.timeAndDate = datetime.datetime.now()

    # def add_entry(self, entry):
    #     self.entries.append(entry)

    def lock_diary(self):
        self.isLock = True

    def unlock_diary(self):
        self.isLock = False




