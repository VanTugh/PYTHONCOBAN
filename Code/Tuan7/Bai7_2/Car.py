from Vehicle import Verhicle
class Car(Verhicle):
    def __init__(self, make, model):
        super().__init__(make) 
        self.model = model
    def description(self):
        return super().description() +  f" Model : {self.model}|"
    