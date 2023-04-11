class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("")
        print("You're going {} mph.".format(self.speed))

    def accelerate(self):
        if self.speed >= 250:
            print("")
            print("The car can't go any faster!")
            self.speed += 0
        else:
            self.speed += 10

    def brake(self):
        if self.speed == 0:
            print("")
            print("You've already stopped.")
        elif self.speed < 10:
            self.speed = 0
        else:
            self.speed -= 10

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

    def hard_brake(self):
        if self.speed == 0:
            print("")
            print("You've already stopped!")
        elif self.speed < 60:
            self.speed = 0
        else: self.speed -= 60

    def end(self):
        print("")
        print("The drive is now over.")
        print("")
        print("When the drive ended:")
        print("You were going {} mph.".format(self.speed))
        print("You travelled {} miles.".format(self.odometer))
        print("Your average speed was {} mph.".format(self.odometer / self.time))
        self.odometer = 0
        self.time = 0



if __name__ == '__main__':

    my_car = Car()
    print("You're driving a car.")
    while True:
        action = input("What do you do? [A]ccelerate, [B]rake, "
                       "[H]ard brake, [E]nd drive, "
                 "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOSHE" or len(action) != 1:
            print("I don't know how to do that.")
            continue
        if action == 'E':
            my_car.end()
            quit()
        elif action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("")
            print("The car has driven {} miles".format(my_car.odometer))
        elif action == 'S':
            print("")
            print("The car's average speed is {} mph".format(my_car.average_speed()))
        elif action == 'H':
            my_car.hard_brake()
        my_car.step()
        my_car.say_state()