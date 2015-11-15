""" GUI interface for showing prosess list""" 

import pygtk
pygtk.require("2.0")

from back import view_controler
from back.prosessSchedular import Scheduler
from back.ignoreList import Ignore_list

from gi.repository import Gtk,GObject


import threading

class HellowWorldGTK:
    """Interface of window class """

    def __init__(self):
        self.gladefile = "prosessList.glade" 
        self.glade = Gtk.Builder()
        self.glade.add_from_file(self.gladefile)
        self.glade.connect_signals(self)   
        self.glade.get_object("MainWindow").show_all()
        self.dialog = self.glade.get_object("ignore_popup")
        self.glade.get_object("MainWindow").set_title("adams cool thing")

        self.ignoreList = Ignore_list() #instance ignore list app  

        self.sch = Scheduler()  #instance of Scheduler
                                #NOTE: its best to create new instances of this to 
                                #      prevent crossover of the scheduler 

                                #TODO: prevent multiple schedule jobs from being ran  


    def on_MainWindow_delete_event(self, widget, event):
        Gtk.main_quit()


    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)



    def on_ignore_list_delete(self,widget):
        #TODO: get the delete event to only close the ignore list window and not quit out of all windows
        print "did this happen ?"


    def refresh_button_clicked(self,widget):
         self.set_app_data()


    #unknown when this function is ran or anything about what connects from/to it 
    def shedual_toggeld(self,widget): 
        onOffSwitch = widget.get_active()

        """ After main GTK has logicly finished all GUI work run thread on togged button """
        thread = threading.Thread(target=self.call_schedual, args=(onOffSwitch,))
        thread.daemon = True
        thread.start()


    def call_schedual(self, onOffSwitch):
        if onOffSwitch == True:
            self.sch.start_background_checker()
        else:
            self.sch.stop_background_checker() 


    def click_ignore_app(self,widget):
        """ opens ignore dialogue and populates the fields """ 

        app_num = widget.get_property("name")   #gets the name form glades unique id
        app_num = int(app_num[-1:])     #name is only the last part of the word

        iter_app = viewControler.gen_top_6()
        
        while (app_num != 0): #runs through the top 6 apps to find the right 1
            app = iter_app.next( )
            app_num -= 1

        #gets then sets the values for the app chosen
        self.ignore_name = self.glade.get_object("ignore_app_name")
        self.ignore_hour = self.glade.get_object("ignore_app_hours")
        self.ignore_min = self.glade.get_object("ignore_app_mins")

        self.ignore_name.set_text(app[0])
        self.ignore_hour.set_text(app[1])
        self.ignore_min.set_text(app[2])

        #runs the dialog TODO check why it cannot be opened more then once 
        self.dialog.run() 


    def clicked_show_ignore_list(self,widget):
        self.glade.get_object("IgnoredAppWindow").show_all()
        self.glade.get_object("IgnoredAppWindow").set_title("Ignored Apps List")
        self.ignore_lable_initializer()
        self.set_ignore_data()


    def clicked_unignore_app(self,widget):
        print "hello" 


    def ignore_app_button_clicked(self,widget):
        """Gets the applications name and then sends to ignore handler to be 
           Added to the list of ignored apps 
        """

        ignore_app_name = self.glade.get_object("ignore_app_name")
        ignore_app_name = ignore_app_name.get_text()
        
        self.ignoreList.add_app(ignore_app_name)


    def lable_initalizer(self):
        #gets label vars 
        self.name_1 = self.glade.get_object("name_data_1")
        self.hour_1 = self.glade.get_object("hour_data_1")
        self.min_1 = self.glade.get_object("min_data_1")
        
        self.name_2 = self.glade.get_object("name_data_2")
        self.hour_2 = self.glade.get_object("hour_data_2")
        self.min_2 = self.glade.get_object("min_data_2")
        
        self.name_3 = self.glade.get_object("name_data_3")
        self.hour_3 = self.glade.get_object("hour_data_3")
        self.min_3 = self.glade.get_object("min_data_3")

        self.name_4 = self.glade.get_object("name_data_4")
        self.hour_4 = self.glade.get_object("hour_data_4")
        self.min_4 = self.glade.get_object("min_data_4")

        self.name_5 = self.glade.get_object("name_data_5")
        self.hour_5 = self.glade.get_object("hour_data_5")
        self.min_5 = self.glade.get_object("min_data_5")

        self.name_6 = self.glade.get_object("name_data_6")
        self.hour_6 = self.glade.get_object("hour_data_6")
        self.min_6 = self.glade.get_object("min_data_6")
 

    def ignore_lable_initializer(self):
        """is used to get the ignored labels of ignore app window """ 
 
        self.ign_name_1 = self.glade.get_object("ignored_name_1")
        self.ing_date_1 = self.glade.get_object("ignored_date_1")
        
        self.ign_name_2 = self.glade.get_object("ignored_name_2")
        self.ing_date_2 = self.glade.get_object("ignored_date_2")
        
        self.ign_name_3 = self.glade.get_object("ignored_name_3")
        self.ing_date_3 = self.glade.get_object("ignored_date_3")

        self.ign_name_4 = self.glade.get_object("ignored_name_4")
        self.ing_date_4 = self.glade.get_object("ignored_date_4")

        self.ign_name_5 = self.glade.get_object("ignored_name_5")
        self.ing_date_5 = self.glade.get_object("ignored_date_5")

        self.ign_name_6 = self.glade.get_object("ignored_name_6")
        self.ing_date_6 = self.glade.get_object("ignored_date_6")
 
        self.ign_name_7 = self.glade.get_object("ignored_name_7")
        self.ing_date_7 = self.glade.get_object("ignored_date_7")

        self.ign_name_8 = self.glade.get_object("ignored_name_8")
        self.ing_date_8 = self.glade.get_object("ignored_date_8")


    def set_ignore_data(self):
        listOfIgnored = self.ignoreList.get_ignored_apps



    def set_app_data(self):
         #gets top 6 apps and inserts there name and time running into labes
        self.lable_initalizer() 
        iter_app = viewControler.gen_top_6()    #bad name for the generator 

        current_app = iter_app.next()
        self.name_1.set_text(current_app[0])
        self.hour_1.set_text(current_app[1])
        self.min_1.set_text(current_app[2])
            
        current_app = iter_app.next()
        self.name_2.set_text(current_app[0])
        self.hour_2.set_text(current_app[1])
        self.min_2.set_text(current_app[2])
         
        current_app = iter_app.next()
        self.name_3.set_text(current_app[0])
        self.hour_3.set_text(current_app[1])
        self.min_3.set_text(current_app[2])
         
        current_app = iter_app.next()
        self.name_4.set_text(current_app[0])
        self.hour_4.set_text(current_app[1])
        self.min_4.set_text(current_app[2])
         
        current_app = iter_app.next()
        self.name_5.set_text(current_app[0])
        self.hour_5.set_text(current_app[1])
        self.min_5.set_text(current_app[2])
         
        current_app = iter_app.next()
        self.name_6.set_text(current_app[0])
        self.hour_6.set_text(current_app[1])
        self.min_6.set_text(current_app[2])
         


if __name__ == "__main__":
    try:
        GObject.threads_init()#sets up thread
        gtkInstince = HellowWorldGTK()
        Gtk.main()
    except KeyboardInterrupt:
        pass 
