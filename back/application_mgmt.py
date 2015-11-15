"""
module for getting and storing active / background application. 
all applications will be stored as application objects 

"""
import datetime 
import subprocess
import cPickle as pickle
import sys

from collections import OrderedDict


class Application():
    """ Class for creating and managing the application obj aka meta_info objects 
        these objects are used by mostly by the GUI extra information about applications 
        colour,prod score and display name. 

        The "name" must remain the same as its the referince to the saved applications and 
        snap shots
    """

    def __init__(self,name,focus=False):
        self.name = name
        self.focus = focus

        self.prod_score = 5
        self.display_name = name
        self.color = "none"
   
    def print_app(self):
        """simple print function for debugging
        """

        print "name", self.name 
        print "first time", self.first_time 
        print "focus ? ", self.focus 

        print "time list", self.time_list 

        print "prod score", self.prod_score 
        print "display name", self.display_name 
        print "color" , self.color

     

class Process_checker():
    """ Class for running checks on the applications running and cleaning that data up to be used.
        Also this class will package the data and send it to data saver to be saved to disk
    """
   
    def call_fouce_bash(self):
        """ Calls focus bash saves as focus_app
            
        """
        try:
            self.raw_foucs_app = subprocess.check_output(
                                    ['sh','back/bash/get_active_window.sh'])

            self.focus_app = self.raw_foucs_app[1:-2]
            self.create_and_save(True)

        except subprocess.CalledProcessError as e:
            print "Error with Scripts \n return code = %s " %(e.returncode) 
            return False


    def call_background_bash(self):
        """function for calling background apps creates raw_background_app
        """
        try:
            self.raw_background_app = subprocess.check_output(
                                            ['sh','back/bash/prosessScript.sh'])

            self.create_background_list()
            self.create_and_save()

        except subprocess.CalledProcessError as e:
            print "Error with Scripts \n return code = %s " %(e.returncode) 
            return False


    def create_background_list(self):
        """
        cleans result from bash script creates self.clean_list

        NOTE: due to shell retuning '/n' between app names 
              A flag will del every second value 
        """


        clean_list = []
        raw_list = self.raw_background_app.split(',')
        raw_list = self.raw_background_app.split('"')
        
        flag = True
        for string in raw_list:  
            string = string.strip() 
            string = string.split(',')

            if flag is True:
                del string
                flag = False
            else:
                if string[0] not in clean_list: #will not append if already in
                    clean_list.append(string[0])
                flag = True


        self.background_list = clean_list


    def create_and_save(self,active=False):
        """  function creates a application obj 
        """

        data_saver = Data_saver()   #ref to data_saver class

        time_stamp = datetime.datetime.now()
        time_stamp = time_stamp.replace(second=0,microsecond = 0)

        if active is True:
            time_stamp = time_stamp - datetime.timedelta(minutes=time_stamp.minute % 1)
            
            self.active_obj = {time_stamp: self.focus_app}
            data_saver.add_active(self.active_obj) 

        else:
            obj_dict = {} 
            time_stamp = time_stamp - datetime.timedelta(minutes=time_stamp.minute % 10)
            time_stamp_list = [time_stamp]
            
            for app in  self.background_list:
                obj_dict[app] = time_stamp_list

            data_saver.add_passive(obj_dict) 



class View_control():
    """ Class for GUI to get useful data to display
        Some functions are place holders for later version features 
    """ 

    def __init__(self):
        """ sets up commonly used vars for all the functions
        """
        self.saved_files = Data_saver()
 

    def top_6_background_today(self):
        """ Function returns the 6 most popular apps of today.
        """

        all_background = self.saved_files.get_file("saved_background_data")
        ignored_apps = self.saved_files.get_file("saved_ignore_data")


        user_background = {}    #all applications not in ignore file
        for name in all_background:
            if name not in ignored_apps:
                user_background[name] = all_background[name]

       
        
        #filters all time stamps not ran today
        today_date = datetime.date.today()
        today_background = {}

        for name, time_list in user_background.iteritems():

            time_list = filter(lambda time_stamp: time_stamp.date() == today_date, time_list)

            if len(time_list) != 0:
                today_background[name] = time_list


        #gets the 6 most recorded apps 
        return_background = {} 
        lowest = 9999999 #first finds lowest score

        for name,time_list in today_background.iteritems():
            if len(return_background) < 6:
                return_background[name] = time_list

            else:
                for old_name,old_time_list in return_background.iteritems():
                    if lowest > len(old_time_list):
                        lowest = len(old_time_list)
                
                #print lowest        

                if len(time_list) > lowest:
                    del(return_background[old_name])
                    return_background[name] = time_list

        #TODO check if this really returns the 6 highest used apps
        return return_background

    
    def all_active_today(self):
        """ gen a dict of all un-ignored active apps ran today 
        """

        all_active = self.saved_files.get_file("saved_active_data")

        #removes apps not ran today
        today_date = datetime.date.today()
        today_active = {} 

        #Left off need to send out data as orderd dict orderd by the KEY witch is a time stamp
        #appart from that this function works like a dream

        for time in all_active:
            if time.date() == today_date:
                today_active[time] =  all_active[time]


        #removes ignored apps 
        ignored_apps = self.saved_files.get_file("saved_ignore_data")

        unsorted = {} 

        for time, name in today_active.iteritems():
            if name not in ignored_apps:
                unsorted[time] = name



        #sorts the values by first date_time to lateist date time
        return_dict = OrderedDict()

        while len(unsorted) > 0:
            min_time = min(unsorted, key=lambda time_stamp: time_stamp.time() ) 
            return_dict[min_time] = name
            del(unsorted[min_time])


        return return_dict


    def check_meta_info(self, app_name):
        """ returns a copy of a Application obj or else returns False
        """
        saved_metas = self.saved_files.get_file("saved_meta_data")

        for metas in saved_metas:
            if metas.name == app_name:
                return metas 


    def change_meta_info(self,new_meta):
        """ function for permanently changing the properties of a meta obj
        """

        saved_metas = self.saved_files.get_file("saved_meta_data")
        
        for old_meta in saved_metas:

            if new_meta.name == old_meta.name:
                print old_meta.name
                print new_meta.display_name
                old_meta.color = new_meta.color
                old_meta.display_name = new_meta.display_name
        
        self.saved_files.save_file(saved_metas,"saved_meta_data")


    def get_all_ignored(self):
        """ Returns a list of the names of all the ingnored apps and there display names
        """
        saved_ignore = self.saved_files.get_file("saved_ignore_data")
         
        return saved_ignore

    
    def add_ignore(self,app_name):
        """ Adds app to ingore list
        """

        print app_name
        saved_ignores = self.saved_files.get_file("saved_ignore_data")
        
        if app_name in saved_ignores:
            print "duplicate entry for adding ignore file" 
        else:
            saved_ignores.append(app_name)

        self.saved_files.save_file(saved_ignores, "saved_ignore_data")


    def remove_ignore(self,app_name):
        """ Removes a app from the ignored_list
        """

        saved_ignores = self.saved_files.get_file("saved_ignore_data")

        for ignored in saved_ignores:
            
            if app_name == ignored:
                saved_ignores.remove(ignored)
                self.saved_files.save_file(saved_ignores, "saved_ignore_data")
                return True 


        print "no such app as %s in ingored list" % (app_name)
        return False



class Data_saver():
    """ Class for File I/O manages the active,passive applications also the ignore file and the        
        meta info. Save_file and get_file are the actual file handling functions 
    """

    def add_active(self, new_active):
        """ function for adding new active entry's to file function will get the old file 
            and update it with the new data it will also check the ignore file and will
            not add ignored applications in the first place
        """
        name =  new_active.values()[0]
        time_stamp = new_active.keys()[0]

        self.check_ignore(name)
        self.add_meta_info(name)

        saved_data = OrderedDict()
        saved_data = self.get_file("saved_active_data")

        if time_stamp not in saved_data:
            saved_data[time_stamp] = name
            self.save_file(saved_data, "saved_active_data") 
          
    def remove_active(self, name):
        """ removes a active out right
        """
        saved_data = self.get_file("saved_active_data")

        if name in saved_data:
            print "removing ", name 
            del(saved_data[name])
        else:
            print "no such app as ", name

        self.save_file(saved_data, "saved_active_data")

    

    def add_passive(self, new_passives):
        """ function for adding a dict of new passives to the saved dict of passives.
            the function will check the ignore file also
        """
        saved_data = self.get_file("saved_background_data")
        
        for app in new_passives:    #checks each app for ignore/meta
            if self.check_ignore(app) == True:
                del app     #stops ignored apps from being added
            else:
                self.add_meta_info(app)

          
        #adds new time stamps to app already in saved background file        
        for app in saved_data:
            if app in new_passives:
                if saved_data[app][-1] != new_passives[app][0]:  #stops duplicate time stamps
                    saved_data[app].append(new_passives[app][0]) 

                del new_passives[app]   

        for passive in new_passives:    #add left over passives to saved_data
            saved_data[passive] = new_passives[passive] 

        self.save_file(saved_data, "saved_background_data")


    def remove_passive(self,name):
        """ removes a passive out right
        """
        saved_data = self.get_file("saved_background_data")

        if name in saved_data:
            print "removing ", name 
            del(saved_data[name])
        else:
            print "no such app as ", name

        self.save_file(saved_data, "saved_background_data")


    def add_meta_info(self, new_application):
        """ Function for checking and adding data to meta info. Returns false if duplicate 
            Saves to file other wise.
        """

        new_meta = Application(new_application)  # creates obj

        saved_meta_info = self.get_file("saved_meta_data")
        #print saved_meta_info
            
        for metas in saved_meta_info:
            if new_meta.name == metas.name:
                return False


        saved_meta_info.append(new_meta)
        self.save_file(saved_meta_info,"saved_meta_data")
        del new_meta


    def check_ignore(self, app_name):
        """ Returns True if in ingnore file and false if not
        """

        saved_ignores = self.get_file("saved_ignore_data")
        
        if app_name in saved_ignores:
            return True
        else:
            return False


    def get_file(self, file_name):
        """ Function for safely getting a files contents. Requires the name of the file 
            .Returns the contents of the file not a ref to the file its self.

            File names:
                saved_active_data
                saved_background_data
                saved_ignore_data
                saved_meta_data
        """

        sys.path.append('/home/adam/Dropbox/Personal/hours/back')
        #sys.path.append('/home/adam/Dropbox/Personal/hours')
        #print sys.path 


        path = "back/saved_data/%s" % (file_name)

        try:
            with open(path,'rb') as saved_file:
                saved_list = pickle.load(saved_file)
                saved_file.close()
                
                return saved_list

        except IOError:
            print "I/O error could not find %s" % (file_name)
            print "In %s" % (path)
            return False


        except EOFError:
            print "EOF Error" 
            return False


    def save_file(self, new_data, file_name):
        """ Function for saveing new data to a file. requres the file name and the new data
            will return false and try to print error if something fails
        """

        path = "back/saved_data/%s" % (file_name)

        try:
            with open(path,'wb') as old_file:
                pickle.dump(new_data, old_file) 
                old_file.close()

        except IOError:
            print "I/O error could not find %s" % (file_name)

            print "In %s" % (path)
            return False

        except EOFError:
            print "EOF Error" 
            return False   



         

#test_view =  View_control()
#test_view.check_meta_info("Gvim")



#val = test_view.top_6_background_today()
#test_view.all_active_today()



#test_background = Process_checker()

#test_background.call_background_bash()
#test_background.call_fouce_bash()


#   test_application = Application("Blank") 
#   test_time = datetime.datetime.now()

#   test_app_dict = {test_time: test_application}


#test_saver = Data_saver()
#test_saver.remove_active("time_stamp")
#test_saver.add_ignore("File-roller")
#test_saver.remove_ignore("File-roller")


