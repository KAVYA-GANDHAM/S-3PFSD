class train_ticket():
    def booking(self, name, age, start, desti):
        self.name=name
        return name
        self.age = age
        return age
        self.start = start
        return start
        self.desti = desti
        return desti
        seats=60
        print("available seats:", seats)
        num_of_tic=int(input("enter number of tickets"))
        if(num_of_tic<=seats):
            print("Ticket booked")
        else:
            print("seats not available")

obj=train_ticket()
obj = booking("kavya")