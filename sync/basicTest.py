import logging
import speedtest
import testDirectives
import datetime
import time
import subprocess
from scapy.all import *

logging.getLogger("speedtestLog")
__TIME_FORMAT = "%Y-%m-%dT%H-%M-%S"
file_date = datetime.now().strftime(__TIME_FORMAT)

logging.basicConfig(filename="/app/autonetscript-" + file_date + ".log", level=logging.DEBUG, format='%(asctime)s %(message)s')

speedtest = speedtest.Speedtest()
speedtest.get_best_server()
speedtest.download()
speedtest.upload()
speedtest.results.share()
speedResults = speedtest.results.dict()
srPingMS = str(speedResults['ping'])
srURL = str(speedResults['share'])

dlSpeed = '{:05.2f}'.format(speedResults['download']/1024/1024)
upSpeed = '{:05.2f}'.format(speedResults['upload']/1024/1024)

logging.info("Speedtest.net speedtest completed. Pic URL: " + srURL)
logging.info("Speedtest.net Download Speed: " + str(dlSpeed) + "mbps")
logging.info("Speedtest.net Upload Speed: " + str(upSpeed) + "mbps")
logging.info("Ping: " + str(srPingMS) + "ms")

tr_answer, tr_unanswered = traceroute([testDirectives.HOST_MTR_1, testDirectives.HOST_MTR_2, testDirectives.HOST_PERFSONAR])
graphFileName = "tracerouteGraph-All-" + file_date + ".svg"
graph = tr_answer.graph(target="/app/"+graphFileName)

logging.info("Saved traceroute to " + graphFileName)

resultBytes = subprocess.run(["nmap","--script","broadcast-dhcp-discover"], stdout=subprocess.PIPE)
result = str(resultBytes.stdout)
dhcp_server = result.split('  ')[7].split(' ')[3].split('\\n')[0]

logging.critical("Found DHCP server at " + dhcp_server)





