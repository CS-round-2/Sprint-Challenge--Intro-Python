# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#! BASE CLASS---------------------------------------------
class Vehicle():
    pass


#! AIR START---------------

class FlightVehicle(Vehicle):
    pass

# FlightVehicle group


class Starship(FlightVehicle):
    pass

# FlightVehicle group


class Airplane(FlightVehicle):
    pass


#! GROUND START----------

class GroundVehicle(Vehicle):
    pass

# GroundVehicle group


class Car(GroundVehicle):
    pass

# GroundVehicle group


class Motorcycle(GroundVehicle):
    pass
