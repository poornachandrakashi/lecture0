class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]
        
    
    def add_passengers(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
     
    def open_seats(self):
        return self.capacity-len(self.passengers)   
    
    
fli=Flight(10)

people=['poorna','pankaj','navya','naveen','neha']
for person in people:
    # success=
    if fli.add_passengers(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")