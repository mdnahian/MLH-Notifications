from core import MLH_NOTIFICATIONS
import os.path

class Main():
    
    def __init__(self, *args, **kwargs):
        self.appName = "MLH-Notifications"
        self.version = 1.0
        self.author = "MD ISLAM"

    def readFromFile(self, filename):
        try:
            return open(filename, "r").read()
        except Exception as a:
            print("Failed: "+str(a))
            
    def writeToFile(self, filename, content, formatChar='a'):
        try:
            saveFile = open(filename, formatChar)
            saveFile.write(str(content))
            saveFile.close()
        except Exception as a:
            print("Failed: "+str(a))

    def saveNewEvents(self, output_file, events):
        for event in events:
            line = event[0] + " --- " + event[1] + " --- " + event[2] + " --- " + event[3]+"\n";
            self.writeToFile(output_file, line)

    def parse(self, username="test"):
        # parse mlh website
        mlh_notifier = MLH_NOTIFICATIONS()
        events = mlh_notifier.execute()

        output_file = username+".csv"
        
        # check if parse failed
        if len(events) == 0:
            print("Error: Failed to Parse Events")
            return []
        else:
            if os.path.isfile(output_file) == True:
                try:
                    # read saved output file to array
                    raw_saved_events = self.readFromFile(output_file).split("\n")

                    # somewhere to store saved events
                    saved_events = []
                    
                    # get each event 
                    for raw_saved_event in raw_saved_events:
                        # somewhere to store saved event
                        saved_event = []

                        # split each event and append info
                        raw_saved_event_array = raw_saved_event.split(" --- ")
                        for i in range(0, len(raw_saved_event_array)):
                            saved_event.append(raw_saved_event_array[i])

                        # store saved event
                        saved_events.append(saved_event)

                    # get new events by comparing with saved events
                    new_events = [i for i in events if i not in saved_events]

                    # check if there are new events
                    if len(new_events) > 0:
                        # delete old events
                        self.writeToFile(output_file, "", 'w')
                        # save new events
                        self.saveNewEvents(output_file, events)
                        
                    # return new events
                    return new_events
    
                except Exception as e:
                    print("Failed: "+str(e))
                    return []
            else:
                # there were no saved outputs. save them now
                self.saveNewEvents(output_file, events)
                return []
                    
