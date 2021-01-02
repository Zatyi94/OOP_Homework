class SpaceShip:
    Fuel = 400
    Passengers = ['John', 'Steve', 'Sam', 'Danielle']
    Shields = True
    Speedometer = 0

    def list_passengers(self):
        for name in self.Passengers:
            print('Passenger: {}'.format(name))

    def add_passenger(self, new_passenger):
        self.Passengers.append(new_passenger)
        print('{} was added to the ship.'.format(new_passenger))

    def travel(self, distance):
        print('trying to travel: {}'.format(distance))

        if self.Fuel == 0:
            print('cant go further, tank is empty')
        else:
            self.Fuel = self.Fuel - distance // 2
            if self.Fuel < 0:
                distance = distance - (self.Fuel * -2)
                print('can only travel: {}'.format(distance))
                self.Fuel = 0
            self.Speedometer = self.Speedometer + distance
            if self.Fuel < 30:
                self.Shields = False
                print('fuel is low, turning off shields...')
            print('the SpaceShip is at: {}'.format(self.Speedometer))
            print('the SpaceShip has: {} fuel'.format(self.Fuel))


mySpaceShip = SpaceShip()

mySpaceShip.list_passengers()
mySpaceShip.add_passenger('Lindsay')
mySpaceShip.list_passengers()
mySpaceShip.travel(750)
mySpaceShip.travel(200)
mySpaceShip.travel(100)
