class Module:
    def __init__(self):
        #Initialize the 3 dictionaries needed to store data.
        self.refs = {}
        self.uses = {}
        self.rems = {}
    def onattach(self,name):
        pass
    def attach(self,module,name):
        #Initialize the module under the given name.
        self.refs[name] = module
        self.uses[name] = 0
        self.rems[name] = False
        self.onattach(name)
    def checkout(self,name):
        #Check to see if the module even exists.
        if name not in self.rems:
            #If it doesn't, return False
            return False
        #Check to see if the module is about to be removed.
        if self.rems[name] == True:
            #If so, return False.
            return False
        #Increment the "uses" counter. 
        self.uses[name] += 1
        return self.refs[name]
    def checkin(self,name):
        #Decrement the "uses" counter.
        self.uses[name] -= 1
    def ondetach(self,name):
        pass
    def detach(self,name):
        #Let others know that the module is about to be removed.
        self.rems[name] = True
        #Wait until the module is no longer in use.
        while self.uses[name] != 0:
            pass
        #Delete the references to the module.
        del self.refs[name]
        del self.uses[name]
        del self.rems[name]
        self.ondetach(name)
    def run(self):
        while True:
            pass