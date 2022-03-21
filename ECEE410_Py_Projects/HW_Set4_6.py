# School pick-up program - design 4 classes

class Dad:
    def __init__(self, dfname, dlname, dphone):
        self.dfname = dfname
        self.dlname = dlname
        self.dphone = dphone

    def getdadfname(self):
        self.dfname = input("Enter your dad's first name: ")

class Mom:
    def __init__(self, mfname, mlname, mphone):
        self.mfname = mfname
        self.mlname = mlname
        self.mphone = mphone

class EmergencyContact:
    def __init__(self, fname, lname, phone, allow):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.allow = allow

class Child(Dad, Mom, EmergencyContact):
    def __init__(self, cname, grade):
        self.cname = cname
        self.grade = grade
    def print_child_pickup_info(self):
        print(f"Summary of child's pickup information is as follows: \ "
        f"Father: {dfname} {dlname}, {dphone} \ "
        f"Mother: {mfname} {mlname}, {mphone} \ "
        f"EmergencyContact: {fname} {lname}, {phone}, {allow}")

# Please review the last function.
# I am not sure I referenced the names correctly.

d1 =