import json

class Agent:
    def __init__(self, **agent_attributes):
        for attribut_name, attribut_value in agent_attributes.items():
            setattr(self, attribut_name, attribut_value)     

    def say_hello(self, first_name):
        return "Bien le Bonjour " + first_name    

def read_file():
    for agent_attributes in json.load(open("agents-100k.json")):
        agent = Agent(**agent_attributes)
        texte = "L'agent parle la langue suivant " + agent.language 
       # return "L'agent parle les langues suivantes " + agent.language + " !"
        print(texte)

read_file()

#agent = Agent()
#agent.say_hello("Kathy") 
#print(agent.say_hello("Kathy"))

#print(read_file())

agent_attributes = {"neuroticism": -0.0739192627121713, "language": "Shona", "latitude": -19.922097800281783, "country_tld": "zw", "age": 12, "income": 333, "longitude": 29.798455535838603, "sex": "Male", "religion": "syncretic", "extraversion": 1.051833688742943, "date_of_birth": "2005-01-10", "agreeableness": 0.1441229877537559, "id_str": "LB3-3Cl", "conscientiousness": 0.2419104411765549, "internet": "false", "country_name": "Zimbabwe", "openness": -0.024607605122172617, "id": 6636726630}

