import cPickle as pickle


class Application():
    
    def __init__(self):
        self.name = "place holder" 
        self.focus = "blank"

        self.prod_score = 5
        self.display_name = "place holder" 
        self.color = "none"


def meta_fixer():
    print 123
    place_list = []
    place = Application()

    place_list.append(place)

    pickle.dump(place_list, open("saved_meta_data","wb"))

    del place
    del place_list
    


meta_fixer()

