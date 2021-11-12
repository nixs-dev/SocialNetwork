import os

class Session:
    mainPath = os.getcwd()
    key = 'TheAdmin'

    def saveSession(data):
        encyptedData = os.popen(Session.mainPath + '/external/encryptor.exe' + ' -enc "'+ data +'" "' + Session.key +'"').read().replace('\n', '')

        with open(Session.mainPath + '/data.bin', 'w') as f:
            f.write(encyptedData)

    def readSession():
        data = ''

        with open(Session.mainPath + '/data.bin', 'r') as f:
            data = f.readline()

        decyptedData = os.popen(Session.mainPath + '/external/encryptor.exe' + ' -dec "'+ data +'" "' + Session.key +'"').read().replace('\n', '')
        return decyptedData

    def closeSession():
        with open(Session.mainPath + '/data.bin', 'w') as f:
            f.write('')