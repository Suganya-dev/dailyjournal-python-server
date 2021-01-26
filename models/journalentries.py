class JournalEntries():

    def __init__(self,id,date,concept,entry,moodsId):
        self.id = id
        self.date = date
        self.concept=concept
        self.entry=entry
        self.moodsId=moodsId
        self.moods = None