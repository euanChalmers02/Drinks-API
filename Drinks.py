from urllib.request import urlopen
import random

class Drinks:
    def __init__(self):
        url = "https://webpagebucket77.s3.eu-west-1.amazonaws.com/All_Drinks"
        operUrl = urlopen(url)
        self.loaded_file = json.loads(operUrl.read())
        
    def RANDOM(self):
        return self.loaded_file[(random.randint(0,len(self.loaded_file)))]
    
    def ALL(self):
        return self.loaded_file
    
    def RANDOMTYPE(self,drink_type):
        output_dict = [x for x in self.loaded_file if drink_type.lower() in (x["properties"]['Type']).lower()]
        return output_dict[(random.randint(0,len(output_dict)))]
    
    def Get(self,drink_name):
        output = [x for x in self.loaded_file if drink_name.strip() in x['name'].strip()]
        return output
    
    def SEETYPES(self):
        typey = []
        
        for dt in self.loaded_file:
            if dt["properties"]["Type"] not in typey:
                typey.append(dt["properties"]["Type"])

        output_dict = []
        for each in typey:
            dict_temp = {"Type":str(each)}
            print(dict_temp)
            output_dict.append(dict_temp)
            
        return output_dict 