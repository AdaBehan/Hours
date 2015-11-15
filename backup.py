#SL imports
import sys
import datetime 
from collections import OrderedDict
import threading

#GTK imports
import pygtk
pygtk.require("2.0")
from gi.repository import Gtk,GObject,Gdk


# Own Imports
from back.application_mgmt import Application,Data_saver,View_control 
from back.scheduler import Scheduler



class new_display():

    def __init__(self):

        #GTK and Main Display 
        self.gladefile = "new_display.glade"
        self.glade = Gtk.Builder()
        self.glade.add_from_file(self.gladefile)
        self.glade.connect_signals(self)

        self.glade.get_object("main_display").show_all()
        self.glade.get_object("main_display").set_title("Hours")

        #Dialogues
        self.edit_dialogue = self.glade.get_object("Edit_dialog")
        self.color_dialogue = self.glade.get_object("color_changer_dialog")
        self.ignore_dialogue = self.glade.get_object("ignore_dialog")



        self.sch = Scheduler()    #instance of Scheduler
        
                                #NOTE: its best to create new instances of this to 
                                #      prevent crossover of the scheduler 

                                #TODO: prevent multiple schedule jobs from being ran 

        self.view_control = View_control()


    def on_close_window(self, *args):
        Gtk.main_quit(*args) 

   

#Main Stuff [2 thing left]

    def toggle_recording(self,toggle_button):
        if toggle_button.get_active() == True:
           self.sch.start_scheduler()
        else:
           self.sch.stop_scheduler() 


    def call_schedual(self, toggle_button):
        """ This function puts toggle_recording into its own thread witch allows the scheduler module 
            To run independently of GTK`s main loop. 
        """

        thread = threading.Thread(target=self.toggle_recording, args=(toggle_button,))
        thread.daemon = True
        thread.start()


    def get_grey(self):
        """ Gives back 36 different shades of grey as strings in hex
        """
        color_list = ["#B9B9B9", "#403E3A", "#9E9BAE", "#2D2A21", "#B3B0AA", "#63A582",
                      "#BFB8BB", "#19191B", "#797882", "#A89BA1", "#817C7C", "#5E5757",
                      "#867074", "#B0B1C6", "#B0C6BC", "#C6C3B0", "#C6B0BB", "#7F7B72",
                      "#798670", "#868270", "#8A857A", "#7D7086", "#ECE3F3", "#E3E4F3",
                      "#8A8E7F", "#E7F3E3", "#F3EEE3", "#F3E3E8", "#A8B1E4"]


        for color in color_list:
            yield color

        raise StopIteration

    def set_top_6(self):
        """sets the info for the background top 6 
            The function uses 3 generator functions for simplicity and flexibility
        """
        #TODO this function is waaaaaaaaaaaaaay 2 long it needs to be split into sup functions


        def gen_name_place():
            """ Generator for the background name place
            """
            index = 0

            while index != 6:
                index = index + 1
                path = "name_app_%s" % (index) 
                name_place = self.glade.get_object(path) 
                yield name_place 


        def gen_time_place():
            """ Generator for the background time place
            """
            index = 0

            while index != 6:
                index = index + 1
                path = "hours_today_app_%s" % (index) 
                time_place = self.glade.get_object(path) 
                yield time_place 


        def gen_color_place():
            """ genator for the color place holder
            """
            index = 0

            while index != 6:
                index = index + 1
                path = "color_app_%s" % (index) 
                color_place = self.glade.get_object(path) 
                yield color_place 


        top_6_today = self.view_control.top_6_background_today()
        name_list = top_6_today.keys()
        self.top_6_ref_dict = {}
        ref_index = 1

        for name in name_list:
            self.top_6_ref_dict[ref_index] = name 
            ref_index = ref_index + 1 


        iter_name = gen_name_place()
        iter_time = gen_time_place()
        iter_color = gen_color_place()
        iter_grey = self.get_grey() 

        counter = 6     #used to catch less then 6 top apps given 
        for apps in top_6_today:
            counter = counter - 1
            name = apps
            time_in_10 = len(top_6_today[apps])

            if time_in_10 >= 6:     #Deals with more then 60 mins of background
                time = time_in_10 / 6 
                time = round(time, 4)
                time = str(time)

            else:   #deals with less then 60 mins 
                time = time_in_10
                time = time / 10.00
                time = str(time)
                time = "%s0" % (time)   #adds the last 0 to the time


            meta = self.view_control.check_meta_info(apps)
            if meta == False:
                print "Error in set background" 
                print "No Known meta for app"

            else:
                if meta.color == "none":
                    meta.color = iter_grey.next() 
                    self.view_control.change_meta_info(meta)


                fixed_color = meta.color
                event_box  = iter_color.next()

                state = event_box.get_state()
                color = Gdk.RGBA()
                color.parse(fixed_color)
                color.to_string() 

                event_box.override_background_color(state, color) 


            iter_name.next().set_text(meta.display_name)
            iter_time.next().set_text(time)

        while counter != 0: #Handles when there is less then 6 top apps
            iter_name.next().set_text("None")
            iter_time.next().set_text("0")
            counter = counter -1



    #TODO rewrtie this so that it fills all unused boxes with grey and all future boxes w/ white or something
    def set_active(self):
        """ Sets the active color blocks (the color blocks at the top of the app
        """
        all_active = self.view_control.all_active_today()
        event_box_gen = self.gen_event_box()
        iter_grey = self.get_grey() 

        #Date time stuff
        first_user_time = all_active.iterkeys().next()
        first_possible_time = datetime.datetime.now()
        first_possible_time = first_possible_time.replace(hour=0,
                                                          minute=1,
                                                          second=0,
                                                          microsecond = 0)


        iter_time = self.gen_time(False,4)
        
        if first_user_time > first_possible_time:   #makes all time slots before first active grey
            grey = "#9E9BAE"
            color = Gdk.RGBA()
            color.parse(grey)
            color.to_string() 


            time_index = iter_time.next()
            while first_user_time > time_index:

                current_box = event_box_gen.next() 
                state = current_box.get_state()
                current_box.override_background_color(state, color) 
                time_index = iter_time.next()

        meta_list = [] 
        for time_stamp in all_active:
            name = all_active[time_stamp]
            meta = self.view_control.check_meta_info(name)
            

            if len(meta_list) < 4:
                meta_list.append(meta)
            else:
                meta = meta_list[0]
                meta_list = []

                if meta.color == "none":
                    meta.color = iter_grey.next() 
                    self.view_control.change_meta_info(meta)
                
                new_color = meta.color

                color = Gdk.RGBA()
                color.parse(new_color)
                color.to_string() 

                
                current_box = event_box_gen.next() 
                state = current_box.get_state()
                current_box.override_background_color(state, color) 


    def new_set_active(self):
        """ Sets the active part of the display
        """
        event_box_gen = self.gen_event_box()
        iter_time = self.gen_time()

        time_now = datetime.datetime.now()
        time_now = time_now.replace(second=0,microsecond = 0)


        end_of_day = datetime.datetime.now()
        end_of_day = end_of_day.replace(hour = 23, minute = 59, 
                                        second = 0, microsecond = 0)

        all_active = self.view_control.all_active_today()

        
        block_counter = 0 
        earlyest_time = False
        active_in_block = False 
        name_list = []
        current_time = iter_time.next() #passed to box filler

        while current_time > time_now:
            all_mins -= 1
            current_time = iter_time.next() #passed to box filler


            
            if earlyest_time == False :  #gets the earlyest entry from all_active
                if len(all_active) == 0:
                    earlyest_time = [0]
                else:
                    earlyest_time = all_active.popitem(0)
                 
            if current_time == earlyest_time[0]:    
                name_list.append(earlyest_time[1])
                earlyest_time = False
                active_in_block = True 


            if block_counter == 4:
                current_box = event_box_gen.next() 

                if active_in_block == False:
                    self.fill_box(current_box)
                else:
                    #do stuff
                    app_name =  max(name_list, key=name_list.count) #gets the most common element
                    self.fill_box(current_box,app_name)
                    current_time = False
                    name_list = []

                active_in_block = False
                block_counter = 0
            else:
                block_counter += 1

        block_counter = 0
        while current_time < end_of_day: 

            current_time = iter_time.next() #passed to box filler

            if block_counter == 4:
                current_box = event_box_gen.next() 
                self.fill_box(current_box,"end")
                block_counter = 0
            else:
                block_counter += 1
                 




    def fill_box(self,current_box, app_name=False):
        """ fills the event boxes with color if no app is given will fill with grey else
            will fill with apps meta.color value. 

            Note: current_box is made from a generator function and cannot be internally generated
        """

        iter_grey = self.get_grey() 

        if app_name == False:
            grey = "#9E9BAE"
            color = Gdk.RGBA()
            color.parse(grey)
            color.to_string() 

        elif app_name == "end":
            grey = "#E5E9F6"
            color = Gdk.RGBA()
            color.parse(grey)
            color.to_string() 

        else:
            meta = self.view_control.check_meta_info(app_name)
            
            if meta.color == "none": #if user does not pick a color gives it a color 
                    meta.color = iter_grey.next() 
                    self.view_control.change_meta_info(meta)
                
            new_color = meta.color

            color = Gdk.RGBA()
            color.parse(new_color)
            color.to_string() 

        
        state = current_box.get_state()
        current_box.override_background_color(state, color) 






    def gen_time(self, start_from=False,intervals=1):
        """ Yeilds back date time objects, by default starts at 00.01 and 
            counts in 1 min intervals but none defaults arguments can change this
        """

        if start_from == False:
            current_time = datetime.datetime.now()
            current_time = current_time.replace(hour=0, minute=0, second=0,microsecond = 0)

        else:
            current_time = start_from

        last_possible_time = datetime.datetime.now()
        last_possible_time = last_possible_time.replace(hour=23, minute=59, second=0,microsecond = 0)


        while current_time < last_possible_time:
            current_time = current_time + datetime.timedelta(minutes = intervals)
            yield current_time  


        raise StopIteration


    def gen_event_box(self):
        """ Generator function for getting references to the active color boxes 
        """
        index = 0

        while index != 359:   #AM gen
            current_box_string = "color_place_%s" % (index)
            current_box = self.glade.get_object(current_box_string)
            index = index + 1
            yield current_box
        
        print "end of iter"
        raise StopIteration


    def show_records(self,widget):
        """ Simple button to show the old records 
        """
        print "started up"
        #TODO build a no data mode for start up

        self.set_top_6()
        self.set_active()


#TODO: get display to show some grey when there is no data between 2 records
#TODO: display none when there is less then 6 background apps


#Edit Stuff [finished]

    def edit_button_clicked(self,widget):
        """ Starts edit dialog also grabs the right app_obj
        """
        place = widget.get_name()
        print place
        place = int(place[-1])    #gets the num of the app

        app_name = self.top_6_ref_dict[place]

        self.app_to_edit = self.view_control.check_meta_info(app_name)


        self.new_display_name = ""  # Sets up edit vars just in case
        self.new_color = "none"
        self.ignore = False

        self.start_edit_dialogue(self.app_to_edit)


    def start_edit_dialogue(self,edited_app):
        """ Sets the values for the edit dialog and also runs the dialog
        """

        name_holder = self.glade.get_object("name_lable")
        event_box = self.glade.get_object("edit_color_holder")

        state = event_box.get_state()
        color = Gdk.RGBA()
        color.parse(edited_app.color)
        color.to_string()  

        event_box.override_background_color(state, color) 
        name_holder.set_text(edited_app.name)


        self.edit_dialogue.run()

    def edit_dialog_close(self,widget,responce=False):
        print " edit diaglog close"

        self.edit_dialogue.hide()
        print responce


    def edits_dialogue_changes(self,widget):
        """runs changes after user has made edits in edit dialog and hits ok 
        """

        new_name_entry = self.glade.get_object("new_name_entry")
        new_name_entry = new_name_entry.get_text() 


        if new_name_entry != "":
            self.new_display_name = new_name_entry 


        self.send_edits_off()
        self.edit_dialog_close(widget)


    def start_color_changer_dialog(self,widget):
        """ Runs color changer dialogue
        """
        self.color_dialogue.run()


    def color_picked(self,widget,colors):
        """when user picks color set new_color and close color dialog
        """

        self.new_color = self.color_dialogue.get_rgba()
        self.color_picker_closed(widget)


    def color_picker_closed(self,widget,responce=False):
        """ Closes the color picker class
        """
        self.color_dialogue.hide()

    def send_edits_off(self):
        """ Function for applying user issued changes to the application object,
            and sending it off to the view controller for the changes to be saved
        """

        if self.new_display_name != "":
            self.app_to_edit.display_name = self.new_display_name 


        if self.new_color != "none":
            #Changes RGBA color to hex color
            red = int(self.new_color.red*255)
            green = int(self.new_color.green*255)
            blue = int(self.new_color.blue*255)
            hex_new_color = '#{r:02x}{g:02x}{b:02x}'.format(r=red,g=green,b=blue)

            self.app_to_edit.color = hex_new_color


        self.view_control.change_meta_info(self.app_to_edit)


    def ignore_button_clicked(self,widget):
        """ Handels the ignore button for edit window
        """
        name = self.app_to_edit.name

        print "added ignore", name
        self.view_control.add_ignore(name)




# Ignore List stuff [Finished]
    def open_ignore(self,widget):
        """ After user pressess on open ignore creates the ignore dialog 
        """
        container = self.glade.get_object("ignore_container") 
        self.ignore_grid = Gtk.Grid()
        container.add(self.ignore_grid)

        #TODO: make it so that the ingore data shows up when you open dialog first time

        self.ignore_dialogue.run()
        self.ignore_dialogue.show_all()
        
        self.display_ignore_data()


    def display_ignore_data(self):
        """ Adds the ingored app names to the dialog also adds the un-ignore button
        """
        ignore_gen = self.gen_ignored_data()

        left = 0    #These are for the attach method witch takes in places
        top = 0
        width = 1 
        height = 1 
        
        try:
            while True:  #for each value in ignore list loop once
                ignore_data =  ignore_gen.next()

                if type(ignore_data) is not str:
                    ignore_data = str(ignore_data) #Some of the old data is not 
                                                   #stored as a string
                name_lable = Gtk.Label(ignore_data)

                unignore_button = Gtk.Button("unignore")
                linked_name = ignore_data 
                unignore_button.connect("clicked", self.unignore_pressed, linked_name)
                
                self.ignore_grid.attach(name_lable,left,top,1,1)
                self.ignore_grid.attach_next_to(unignore_button,name_lable, 1,1,1)

                width = width + 4
                height = height + 4
                top = top + 1

        except StopIteration: 
            pass
      

    def gen_ignored_data(self):
        """ Yeilds ignore data until none left
        """
        saved_ignored = self.view_control.get_all_ignored()
        self.ref_saved_ignored = saved_ignored  #used for referring
        

        for ignored in saved_ignored:
            meta_ignore = self.view_control.check_meta_info(ignored)

            if meta_ignore != False and meta_ignore != None:
                yield meta_ignore.name

            else:
                yield ignored


    def unignore_pressed(self,button,linked_name):
        self.view_control.remove_ignore(linked_name)


    def ignore_dialog_close(self,arg):
        self.ignore_dialogue.hide()




test_class = new_display()
test_class.new_set_active()
#test_class.set_top_6()
#test_class.set_active()

if __name__ == "__main__":
    try:

        GObject.threads_init()  #sets up thread
        GtkInstince = new_display()
        Gtk.main()
    
    except KeyboardInterrupt:
        print "123"
