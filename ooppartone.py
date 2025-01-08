class Leave:

    #constructor is a method that is called when an object is created
    def __init__(self, message):
        print("Leave constructor", message)
        self.name = ""
        self.fromdate = ""
        self.todate = ""
        self.reason = ""
        self.email = ""


    #methods
    def doApply(self):
        print("Apply leave: ", self.name)
        print("From date: ", self.fromdate)
        print("To date: ", self.todate)
        print("Reason: ", self.reason)
    def doApprove(self):
        print("Approve leave")
        self.doEmail()
    def doReject(self):
        print("Reject leave: ", self.reason)
    def doUpdate(self):
        print("Update leave")
    def doEmail(self):
        print("Email the status: ", self.email)


#instance
myleave = Leave("Suck ma")
#give values
myleave.name = "John"
myleave.email = "John@hmail.com"
myleave.fromdate = "2022-01-01"
myleave.todate = "2022-01-10"
myleave.reason = "ill"
#call methods
myleave.doApply()
myleave.doApprove()
myleave.doReject()
myleave.doUpdate()