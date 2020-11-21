class Detector:
    class DEFAULT_DHCP_DETECTOR:
            def __init__(self):
                import subprocess
            
            def run(self):
                self.resultBytes = subprocess.run(["nmap","--script","broadcast-dhcp-discover"], stdout=subprocess.PIPE)
                self.result = str(self.resultBytes.stdout)
                self.dhcp_server = self.result.split('  ')[7].split(' ')[3].split('\\n')[0]
            
            def getResults(self):
                return self.dhcp_server