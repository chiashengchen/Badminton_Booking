from threading import activeCount


class PersonalInfo:
    account : str
    pwd :str
    
    def __init__(self, account, pwd):
        self.account = account
        self.pwd = pwd
     
    def getAccount(self):
        return self.account

    def getPassword(self):
        return self.pwd
    