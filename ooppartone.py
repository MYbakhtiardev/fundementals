class Leave:

    #constructor is a method that is called when an object is created
    def __init__(self, message):
        print("Leave constructor", message)
        self.name = ""
        self.fromdate = ""
        self.todate = ""
        self.reason = ""


    #methods
    def doApply(self):
        print("Apply leave: ", self.name)
    def doApprove(self):
        print("Approve leave")
    def doReject(self):
        print("Reject leave: ", self.reason)
    def doUpdate(self):
        print("Update leave")


#instance
myleave = Leave("Suck ma")
#give values
myleave.name = "John"
myleave.fromdate = "2022-01-01"
myleave.todate = "2022-01-10"
myleave.reason = "ill"
#call methods
myleave.doApply()
myleave.doApprove()
myleave.doReject()
myleave.doUpdate()