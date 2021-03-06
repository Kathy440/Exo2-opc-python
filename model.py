import json
import math
import matplotlib as mil
mil.use('TkAgg') # add it before launching matplotlib
import matplotlib.pyplot as plt

class Agent:
    
    def say_hello(self, first_name):
        return "Bien le Bonjour " + first_name 

    def __init__(self,position, **agent_attributes): #constructeur -> Insatnce est représenter par le parametre self
        # pour y associer un attribut self.agreeableness
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            # set attribute
            setattr(self, attr_name, attr_value)
     #   self.agreeableness = agent_attributes['agreeableness']

class Position:
    def __init__(self, longitude_degrees, latitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees

    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 100    
    
    @property
    def latitude(self):
        return self.latitude_degrees * math.pi / 180

class Zone:

    ZONES = []
    MIN_LONGITUDE_DEGREES = -180 # Pour y acceder nom de la classe plus la method print(Zone. MIN_LONGITUDE_DEGREES)
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1 # degrees of longitude
    HEIGHT_DEGREES = 1 # degrees of latitude
    EARTH_RADIUS_KILOMETERS = 6371

    def __init__(self, corner1, corner2):
        self.corner1 = corner1 #initialise le corner
        self.corner2 = corner2
        self.inhabitants = []

    @property
    def population(self):
        return len(self.inhabitants)

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    @property
    def width(self):
        return abs(self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILOMETERS
        # valeur absolue grace a la methde abs (tjrs supeireur a zero ou egal a 0)

    @property
    def height(self):
        return abs(self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def area(self):
        return self.height * self.width

    def population_density(self):
        return self.population / self.area

    @classmethod
    def _initialize_zones(cls):
        for latitude in range (cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)
        print(len(cls.ZONES))


    def contains(self, position):
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
            position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
            position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
            position.latitude < max(self.corner1.latitude, self.corner2.latitude)


    @classmethod
    def find_zone_that_contains(cls, position):
        if not cls.ZONES:
            cls._initialize_zones()
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES) / cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)

        zone_index = latitude_index * longitude_bins + longitude_index

        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone

    def average_agreeableness(self):
        if not self.inhabitants:
            return 0
        """ agreeableness = []
        for inhabitant in self.inhabitants:
            agreeableness.append(inhabitant.agreeableness)
        return sum(agreeableness) / self.population """
        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants]) / self.population


class BaseGraph:
    
    def __init__(self):
        self.title = "Your graph title"
        self.x_label = "X-axis label"
        self.y_label = "X-axis label"
        self.show_grid = True

    def show(self, zones):
        # x_values = gather only x_values from our zones
        # y_values = gather only y_values from our zones
        x_values, y_values = self.xy_values(zones)
        plt.plot(x_values, y_values, '.')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()

    def xy_values(self, zones):
        raise NotImplementedError


class AgreeablenessGraph(BaseGraph):

    def __init__(self):
        super().__init__() # appel la classe parent et execute une method de la class parent
        self.title = "Nice people live in the countryside"
        self.x_label = "population density"
        self.y_label = "agreeableness"

    def xy_values(self, zones):
        x_values = [zone.population_density() for zone in zones]
        y_values = [zone.average_agreeableness() for zone in zones]
        return x_values, y_values



def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)
        agent = Agent(position,**agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
    
    agreeableness_graph = AgreeablenessGraph()
    agreeableness_graph.show(Zone.ZONES)


       # print(zone.average_agreeableness())
       # print("Zone population:", zone.population)
       # print(agent.language)
       # print(agent.position.longitude)
       # print(agent.position.latitude)     




main()

#agent_attributes = {"neuroticism": -0.0739192627121713, "language": "Shona", "latitude": -19.922097800281783, "country_tld": "zw", "age": 12, "income": 333, "longitude": 29.798455535838603, "sex": "Male", "religion": "syncretic", "extraversion": 1.051833688742943, "date_of_birth": "2005-01-10", "agreeableness": 0.1441229877537559, "id_str": "LB3-3Cl", "conscientiousness": 0.2419104411765549, "internet": "false", "country_name": "Zimbabwe", "openness": -0.024607605122172617, "id": 6636726630}


# agent = Agent(0) Ex 2
# agent.say_hello("Kathy") Ex 1
# print(agent.say_hello("Kathy")) Ex 1

# agent = Agent(agent_attributes) # Ex 3
# print(agent.language) #Mtn grâce à cette methode on choisi la clé qu'on veux afficher)