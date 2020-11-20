import logging
import speedtest
import testDirectives
import datetime
import subprocess
from scapy.all import *

logging.getLogger("speedtestLog")
now = datetime.now()
file_date = now.strftime("%Y-%m-%d@%H:%m")

logging.basicConfig(filename="speedtestAuto-" + file_date + ".log", level=logging.DEBUG)

speedtest = speedtest.Speedtest()
speedtest.get_best_server()
speedtest.download(threads=3)
speedtest.upload(threads=3)
speedtest.results.share()
speedResults = speedtest.results.dict()

srURL = speedResults['share']
srPingMS = speedResults['ping']
srDownloadSpeed = speedResults['download']
srUploadSpeed = speedResults['upload']
srDownloadSpeed = srDownloadSpeed / 1024/1024
srUploadSpeed = srUploadSpeed / 1024/1024

logging.info("Speedtest completed. Pic URL: " + srURL)
logging.info("Download Speed: " + str(srDownloadSpeed) + "mbps")
logging.info("Upload Speed: " + str(srUploadSpeed) + "mbps")

tr_answer, tr_unanswered = traceroute(testDirectives.HOST_MTR_1)
graphFileName = "traceroute-"+file_date+".svg"
graph = tr_answer.graph(target="/app/"+graphFileName)

logging.info("Saved traceroute to " + graphFileName)

resultBytes = subprocess.run(["nmap","--script","broadcast-dhcp-discover"], stdout=subprocess.PIPE)
result = str(resultBytes)
dhcp_server = result.split('  ')[7].split(' ')[3].split('\\n')[0]

logging.critical("Found DHCP server at " + dhcp_server)






