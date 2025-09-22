from random import randint

class Train:
    def __init__(self, TrainNo):
        self.TrainNO = TrainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.TrainNO} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.TrainNO} is running on time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.TrainNO} from {fro} to {to} is ₹{randint(200, 6000)}")


t = Train(12399)
t.book("delhi", "Kolkata")
t.getstatus()
t.getfare("delhi", "Kolkata")