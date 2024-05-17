# ========= Question 2 =============

class Event:
    def __init__(self, name, date, count):
        self.name = name
        self.date = date
        self.count = count

    def event_name(name):
        print("dimmesdale dimmedome basketball game")

    def event_date(date):
        print("june 3rd")

    def add_participant(self):
        print("We just sold a ticket!")
        self.count += 1
        print(f"Now we have {self.count} people coming!")

    def get_participant_count(self):
        print(f"{self.count} tickets have been sold!")

dimmesdale_basketball_game = Event("dimmesdale dimmedome basketball game", "june 3rd", 230)
dimmesdale_basketball_game.add_participant()
dimmesdale_basketball_game.add_participant()
dimmesdale_basketball_game.add_participant()
dimmesdale_basketball_game.add_participant()
dimmesdale_basketball_game.add_participant()
dimmesdale_basketball_game.add_participant()
dimmesdale_basketball_game.get_participant_count()