from apscheduler.schedulers.background import BackgroundScheduler
import time
from application_mgmt import Process_checker,Application,Data_saver 
import logging

logging.basicConfig()

class Scheduler:
    """ Class for scheduling the bash checks. Check will be ran every 10 mins for background 
        and 1 min for active. The checker is toggleable via start/stop check but should be ran 
        out side of any main threads like the GTK. 

        The Bash scripts are located in the bash folder and the function this checker will call are 
        in application_mgmt.Proses_checker . For bash related error check there.

        Also a infinite loop with a sleep is attached to this file in start_scheduler to keep this tread
        alive. Its a little hack-ey but its the simplest solution.
    """

    def __init__(self):
        self.backSh = BackgroundScheduler()
        self.backSh.start()

        self.prosess_checker = Process_checker()    #ref to application mgmt


    def background_check(self):
        """ calls background checker from application mgmt
        """
        check = self.prosess_checker.call_background_bash()

        if check == False:
            print "Error in background check"
        else:
            print "Back ground check ran"


    def active_check(self):
        """ Calls fouces function in application mgmt
        """
        check = self.prosess_checker.call_fouce_bash()

        if check == False:
            print "Error in background check"
        else:
            print "Active check ran"


    def start_scheduler(self):
        """ Starts the scheduler. Will run indefinitely or until the stop function is ran 
        """
        print "Scheduler started"
        self.background_check()
        self.backSh.add_job(self.background_check,
                            'interval',
                            minutes = 10,
                            id='background_checker')

        self.backSh.add_job(self.active_check,
                            'interval',
                            minutes = 1,
                            id='active_checker')

        while True:
            time.sleep(2)   #keeps the thread alive


    def stop_scheduler(self):
        """ Stop the schedule checking
        """
        self.backSH.remove_job('background_checker')
        self.backSH.remove_job('background_checker')

if __name__ == '__main__':
    auto_scheduler = Scheduler() 
    auto_scheduler.start_scheduler()




