import pygtk
pygtk.require("2.0")


from gi.repository import Gtk,GObject,Gdk


class focus_gui:

    def __init__(self):
        self.gladefile = "gui_fouces.glade" 
        self.glade = Gtk.Builder()
        self.glade.add_from_file(self.gladefile)
        self.glade.connect_signals(self)   

        self.glade.get_object("time_line_window").show_all()
        self.glade.get_object("time_line_window").set_title("focus test")

        self.color_dialogue = self.glade.get_object("color_picker")
    
    def on_close_window(self, *args):
        Gtk.main_quit(*args) 



    def tester_button_clicked(self,widget):
        self.set_cell()


    def set_cell(self):

        self.event_box_initalizer()


	state = self.box_1_am.get_state()

	color = Gdk.RGBA()
	color.parse('#2A660A')
	color.to_string() 

	self.box_0_am.override_background_color(state, color)
	self.box_1_am.override_background_color(state, color)
	self.box_2_am.override_background_color(state, color)
	self.box_3_am.override_background_color(state, color)
	self.box_4_am.override_background_color(state, color)
	self.box_5_am.override_background_color(state, color)


	color = Gdk.RGBA()
	color.parse('#FF0000')
	color.to_string() 

	self.box_6_am.override_background_color(state, color)
	self.box_7_am.override_background_color(state, color)
	self.box_8_am.override_background_color(state, color)
	self.box_9_am.override_background_color(state, color)
	self.box_10_am.override_background_color(state, color)
	self.box_11_am.override_background_color(state, color)


	color = Gdk.RGBA()
	color.parse('#FF66CC')
	color.to_string() 

	self.box_12_am.override_background_color(state, color)
	self.box_13_am.override_background_color(state, color)
	self.box_14_am.override_background_color(state, color)
	self.box_15_am.override_background_color(state, color)
	self.box_16_am.override_background_color(state, color)
	self.box_17_am.override_background_color(state, color)


	color = Gdk.RGBA()
	color.parse('#990099')
	color.to_string() 

	self.box_18_am.override_background_color(state, color)
	self.box_19_am.override_background_color(state, color)
	self.box_20_am.override_background_color(state, color)
	self.box_21_am.override_background_color(state, color)
	self.box_22_am.override_background_color(state, color)
	self.box_23_am.override_background_color(state, color)


	color = Gdk.RGBA()
	color.parse('#33CCCC')
	color.to_string() 

	self.box_24_am.override_background_color(state, color)
	self.box_25_am.override_background_color(state, color)
	self.box_26_am.override_background_color(state, color)
	self.box_27_am.override_background_color(state, color)
	self.box_28_am.override_background_color(state, color)
	self.box_29_am.override_background_color(state, color)

	color = Gdk.RGBA()
	color.parse('#FF99FF')
	color.to_string() 

	self.box_30_am.override_background_color(state, color)
	self.box_31_am.override_background_color(state, color)
	self.box_32_am.override_background_color(state, color)
	self.box_33_am.override_background_color(state, color)
	self.box_34_am.override_background_color(state, color)
	self.box_35_am.override_background_color(state, color)


	color = Gdk.RGBA()
	color.parse('#FF9900')
	color.to_string() 

	self.box_36_am.override_background_color(state, color)
	self.box_37_am.override_background_color(state, color)
	self.box_38_am.override_background_color(state, color)
	self.box_39_am.override_background_color(state, color)
	self.box_40_am.override_background_color(state, color)
	self.box_41_am.override_background_color(state, color)

	color = Gdk.RGBA()
	color.parse('#009933')
	color.to_string() 

	self.box_42_am.override_background_color(state, color)
	self.box_43_am.override_background_color(state, color)
	self.box_44_am.override_background_color(state, color)
	self.box_45_am.override_background_color(state, color)
	self.box_46_am.override_background_color(state, color)
	self.box_47_am.override_background_color(state, color)

        color = Gdk.RGBA()
	color.parse('#996633')
	color.to_string() 


	self.box_48_am.override_background_color(state, color)
	self.box_49_am.override_background_color(state, color)
	self.box_50_am.override_background_color(state, color)
	self.box_51_am.override_background_color(state, color)
	self.box_52_am.override_background_color(state, color)
	self.box_53_am.override_background_color(state, color)

        color = Gdk.RGBA()
	color.parse('#000066')
	color.to_string() 

	self.box_54_am.override_background_color(state, color)
	self.box_55_am.override_background_color(state, color)
	self.box_56_am.override_background_color(state, color)
	self.box_57_am.override_background_color(state, color)
	self.box_58_am.override_background_color(state, color)
	self.box_59_am.override_background_color(state, color)

        color = Gdk.RGBA()
	color.parse('#FF9900')
	color.to_string() 


	self.box_60_am.override_background_color(state, color)
	self.box_61_am.override_background_color(state, color)
	self.box_62_am.override_background_color(state, color)
	self.box_63_am.override_background_color(state, color)
	self.box_64_am.override_background_color(state, color)
	self.box_65_am.override_background_color(state, color)

        color = Gdk.RGBA()
	color.parse('#33CCCC')
	color.to_string() 


	self.box_66_am.override_background_color(state, color)
	self.box_67_am.override_background_color(state, color)
	self.box_68_am.override_background_color(state, color)
	self.box_69_am.override_background_color(state, color)
	self.box_70_am.override_background_color(state, color)
	self.box_71_am.override_background_color(state, color)





    def close_color_picker(self,widget,yolo):
        self.new_color = self.color_dialogue.get_rgba()
        self.color_dialogue.hide()

    def color_picker_button_clicked(self,widget):
        self.color_dialogue.run() 
    



    def event_box_initalizer(self):
        """function that gets the event_boxs and sets as self.values 
    
        """
        self.box_0_am = self.glade.get_object("am_color_place_0")
        self.box_1_am = self.glade.get_object("am_color_place_1")
        self.box_2_am = self.glade.get_object("am_color_place_2")
        self.box_3_am = self.glade.get_object("am_color_place_3")
        self.box_4_am = self.glade.get_object("am_color_place_4")
        self.box_5_am = self.glade.get_object("am_color_place_5")
        self.box_6_am = self.glade.get_object("am_color_place_6")
        self.box_7_am = self.glade.get_object("am_color_place_7")
        self.box_8_am = self.glade.get_object("am_color_place_8")
        self.box_9_am = self.glade.get_object("am_color_place_9")


        self.box_10_am = self.glade.get_object("am_color_place_10")
        self.box_11_am = self.glade.get_object("am_color_place_11")
        self.box_12_am = self.glade.get_object("am_color_place_12")
        self.box_13_am = self.glade.get_object("am_color_place_13")
        self.box_14_am = self.glade.get_object("am_color_place_14")
        self.box_15_am = self.glade.get_object("am_color_place_15")
        self.box_16_am = self.glade.get_object("am_color_place_16")
        self.box_17_am = self.glade.get_object("am_color_place_17")
        self.box_18_am = self.glade.get_object("am_color_place_18")
        self.box_19_am = self.glade.get_object("am_color_place_19")


        self.box_20_am = self.glade.get_object("am_color_place_20")
        self.box_21_am = self.glade.get_object("am_color_place_21")
        self.box_22_am = self.glade.get_object("am_color_place_22")
        self.box_23_am = self.glade.get_object("am_color_place_23")
        self.box_24_am = self.glade.get_object("am_color_place_24")
        self.box_25_am = self.glade.get_object("am_color_place_25")
        self.box_26_am = self.glade.get_object("am_color_place_26")
        self.box_27_am = self.glade.get_object("am_color_place_27")
        self.box_28_am = self.glade.get_object("am_color_place_28")
        self.box_29_am = self.glade.get_object("am_color_place_29")


        self.box_30_am = self.glade.get_object("am_color_place_30")
        self.box_31_am = self.glade.get_object("am_color_place_31")
        self.box_32_am = self.glade.get_object("am_color_place_32")
        self.box_33_am = self.glade.get_object("am_color_place_33")
        self.box_34_am = self.glade.get_object("am_color_place_34")

        self.box_35_am = self.glade.get_object("am_color_place_35")
        self.box_36_am = self.glade.get_object("am_color_place_36")
        self.box_37_am = self.glade.get_object("am_color_place_37")
        self.box_38_am = self.glade.get_object("am_color_place_38")
        self.box_39_am = self.glade.get_object("am_color_place_39")


        self.box_40_am = self.glade.get_object("am_color_place_40")
        self.box_41_am = self.glade.get_object("am_color_place_41")
        self.box_42_am = self.glade.get_object("am_color_place_42")
        self.box_43_am = self.glade.get_object("am_color_place_43")
        self.box_44_am = self.glade.get_object("am_color_place_44")
        self.box_45_am = self.glade.get_object("am_color_place_45")
        self.box_46_am = self.glade.get_object("am_color_place_46")
        self.box_47_am = self.glade.get_object("am_color_place_47")
        self.box_48_am = self.glade.get_object("am_color_place_48")
        self.box_49_am = self.glade.get_object("am_color_place_49")


        self.box_50_am = self.glade.get_object("am_color_place_50")
        self.box_51_am = self.glade.get_object("am_color_place_51")
        self.box_52_am = self.glade.get_object("am_color_place_52")
        self.box_53_am = self.glade.get_object("am_color_place_53")
        self.box_54_am = self.glade.get_object("am_color_place_54")
        self.box_55_am = self.glade.get_object("am_color_place_55")
        self.box_56_am = self.glade.get_object("am_color_place_56")
        self.box_57_am = self.glade.get_object("am_color_place_57")
        self.box_58_am = self.glade.get_object("am_color_place_58")
        self.box_59_am = self.glade.get_object("am_color_place_59")


        self.box_60_am = self.glade.get_object("am_color_place_60")
        self.box_61_am = self.glade.get_object("am_color_place_61")
        self.box_62_am = self.glade.get_object("am_color_place_62")
        self.box_63_am = self.glade.get_object("am_color_place_63")
        self.box_64_am = self.glade.get_object("am_color_place_64")
        self.box_65_am = self.glade.get_object("am_color_place_65")
        self.box_66_am = self.glade.get_object("am_color_place_66")
        self.box_67_am = self.glade.get_object("am_color_place_67")
        self.box_68_am = self.glade.get_object("am_color_place_68")
        self.box_69_am = self.glade.get_object("am_color_place_69")


        self.box_70_am = self.glade.get_object("am_color_place_70")
        self.box_71_am = self.glade.get_object("am_color_place_71")



        self.box_0_pm = self.glade.get_object("pm_color_place_0")
        self.box_1_pm = self.glade.get_object("pm_color_place_1")
        self.box_2_pm = self.glade.get_object("pm_color_place_2")
        self.box_3_pm = self.glade.get_object("pm_color_place_3")
        self.box_4_pm = self.glade.get_object("pm_color_place_4")
        self.box_5_pm = self.glade.get_object("pm_color_place_5")
        self.box_6_pm = self.glade.get_object("pm_color_place_6")
        self.box_7_pm = self.glade.get_object("pm_color_place_7")
        self.box_8_pm = self.glade.get_object("pm_color_place_8")
        self.box_9_pm = self.glade.get_object("pm_color_place_9")




if __name__ == "__main__":
    try:
        GtkInstince = focus_gui()
        Gtk.main()
    
    except KeyboardInterrupt:
        print "123"
 
