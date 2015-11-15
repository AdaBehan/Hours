import cPickle as pickle
from collections import OrderedDict

class Application():
    
    def __init__(self):
        self.name = "place holder" 
        self.focus = "blank"

        self.prod_score = 5
        self.display_name = "place holder" 
        self.color = "none"


def first_time_builder():
    active_place_holder = OrderedDict({"time_stamp" : "name"})
    passive_place_holder = {"name": ["time"], "name_2":["time", "time2", "time3"] }
    ignore_place_holder = ["place"]
    
    yolk = []
    some_app = Application()
    yolk.append(some_app)
    meta_place_holder = yolk 



    pickle.dump(active_place_holder, open("saved_active_data","wb"))
    pickle.dump(passive_place_holder, open("saved_background_data","wb"))
    pickle.dump(ignore_place_holder, open("saved_ignore_data","wb"))
    pickle.dump(meta_place_holder, open("saved_meta_data","wb"))


    del yolk
    del meta_place_holder


if __name__ == '__main__':
    print "new saved file created "
    first_time_builder()
    
