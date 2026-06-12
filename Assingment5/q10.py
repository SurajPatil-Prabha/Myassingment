class Vehicle:
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

v1 = Vehicle()
v2 = Vehicle()

print(Vehicle.vehicle_count)