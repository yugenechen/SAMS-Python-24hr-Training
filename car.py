class Car:
    def __init__(self,
                 make,
                 model,
                 color,
                 transmission,
                 doors,
                 features={}
                 ):
        self.color = "red",
        self.make = "Mitsubishi",
        self.transmission = "automatic",
        self.doors = 4,
        self.model = "Lancer"
        self.features = {"cup_holders": 2,
                         "cruise_control": False,
                         "automatic_windows": True}
        if features:
            self.features.update(features)
