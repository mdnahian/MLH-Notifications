from bs4 import BeautifulSoup
import urllib2

class MLH_NOTIFICATIONS():

    BASE_URL = "https://mlh.io/seasons/s2016/events"

    def __init__(self, *args, **kwargs):
        self.appName = "MLH-Notifications"
        self.version = 1.0
        self.author = "MD ISLAM"

    def getHTML(self, inputURL):
        return urllib2.urlopen(inputURL)

    def match_class(self, target):
        def do_match(tag):
            classes = tag.get('class', [])
            return all(c in classes for c in target)
        return do_match

    def execute(self):
        # get raw html from mlh website
        rawHTML = self.getHTML(self.BASE_URL)
        html = BeautifulSoup(rawHTML, "html.parser")

        # get all events
        rawEvents = html.findAll(self.match_class(["event"]))

        # somewhere to store all parsed events
        events = []

        # start parsing events
        for rawEvent in rawEvents:
            # somewhere to store current event
            event = []
            
            # get event title, date, location, and link
            event.append(rawEvent.find("h3").text)
            event.append(rawEvent.findAll("p")[0].text)
            event.append(rawEvent.findAll("p")[1].text)
            event.append(rawEvent.find("a")['href'])
            
            # store event info
            events.append(event)

        return events

        


            

        
        
    
