from scapy.all import *
import configparser
import datetime
import time

class DefaultTracer:
    def __init__(self):
        self.file_date = datetime.datetime.fromtimestamp(time.time()).isoformat()
        self.config = configparser.ConfigParser()
        self.config.read('/vagrant/network.ini')
        self.devconfig = self.config['default']
        self.target = "/app/"+self.graphFileName
    def __run(self):
        self.tr_answer, self.tr_unanswered = traceroute([self.devconfig['HOST_MTR_1'], self.devconfig['HOST_MTR_2']])
        self.graphFileName  = "tracerouteGraph-All-" + self.file_date + ".svg"
        self.graph = self.tr_answer.graph(target)

    def getLocation(self):
        return self.target
