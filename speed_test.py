from timer import Timer

from back.application_mgmt import Application,Data_saver,View_control 

view_control = View_control()
data_saver = Data_saver()

with Timer() as t:
    view_control.top_6_background_today()
print "=> elasped top 6 today: %s s" % t.secs


with Timer() as t:
    view_control.new_top_6_background_today()
print "=> elasped new top 6 today: %s s" % t.secs



with Timer() as t:
    view_control.all_active_today()
print "=> elasped all active today: %s s" % t.secs

with Timer() as t:
    view_control.get_all_ignored()
print "=> elasped get_all_ignored: %s s" % t.secs

with Timer() as t:
    data_saver.get_file("saved_active_data")
print "=> elasped get_file (active): %s s" % t.secs

with Timer() as t:
    data_saver.get_file("saved_meta_data")
print "=> elasped get_file (meata): %s s" % t.secs

with Timer() as t:
    data_saver.get_file("saved_background_data")
print "=> elasped get_file (background): %s s" % t.secs

with Timer() as t:
    data_saver.get_file("saved_ignore_data")
print "=> elasped get_file (ignore): %s s" % t.secs

