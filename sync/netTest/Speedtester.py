class Speedtester:
    def __init__(self):
        import speedtest
        self.speedtest = speedtest.Speedtest()
        self.speedtest.get_best_server()

        def getResults(self):
            return self.speedtst.results().dict()
        
        def runTest(self):
            self.speedtest.download()
            self.speedtest.upload()
            self.speedtest.results.share()
