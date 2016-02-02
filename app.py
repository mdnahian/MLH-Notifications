#!/usr/bin/python
from main import Main
from daemon import runner
import urllib, urllib2
import time
import os

app = Main()

def deletePYCFiles():
    directory = os.listdir('.')
    for filename in directory:
        if filename[-3:] == 'pyc':
            os.remove(filename)

def sendEmail(body, to_email="mdnahian@outlook.com", from_email="do_not_repy@mlh-notifications.com", subject="MLH: New Hackathons Posted"):
    print("Sending Email to: "+to_email)
    emailer_url = "http://mdislam.com/static/projects/emailer/send.php"
    data = urllib.urlencode({'to' : to_email, 'from' : from_email, 'subject' : subject, 'body' : body})
    req = urllib2.Request(emailer_url, data)
    response = urllib2.urlopen(req)
    d = response.read()
    print(d)



class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5
        
    def run(self):
        while True:
            new_events = app.parse()
        
            if len(new_events) > 0:
                body = "The following hackathons have been recently posted:<br><br><ul>"
                for event in new_events:
                    body = body + "<li><a href='" + event[3] + "'><b>" + event[0] + "</b></a> in " + event[2] + " on " + event[1] + "</li>"
                body = body + "</ul>"
        
                sendEmail(body)
            # else:
                # print("Everything is Up to Date")
            
            deletePYCFiles()
            time.sleep(3600)


application = App()
daemon_runner = runner.DaemonRunner(application)
daemon_runner.do_action()
