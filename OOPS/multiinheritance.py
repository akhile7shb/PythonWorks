class Hospital:
    def __init__(self):
        self.hname=input('enter hospital name')
        self.location=input('enter the location')
    def showdetails(self):
        print('hospital name:',self.hname)
        print('location:',self.location)
class Department:
    def __init__(self):
        self.dname=input('department name:')
        self.docname=input('docter name:')
    def showdepdetails(self):
        print('department is:',self.dname)
        print('doctor name is:',self.docname)
class Patient(Hospital,Department):
    def __init__(self):
      Hospital().__init__()
      Department().__init__()
      self.id=input('enter id')
      self.name=input('enter name')
      self.gender=input('enter gender')
      self.place=input('enter place')
      self.admitdate=int(input('enter admit date'))
      self.dischargedate=int(input('enter discharge date'))
    def fullsummary(self):
#        print('patient id:',self.id)
#        print('patient name:',self.name)
#        print('gender:',self.gender)
#        print('place:',self.place)
#        print('admitdate:',self.admitdate)
#        print('dischargedate:',self.dischargedate)
# p=Patient()
# p.fullsummary()
        Hospital().showdetails()
        Department().showdepdetails()
        print(f"Patient id:{self.id}")
        print(f"Patient name:{self.name}")
        print(f"Gender={self.gender}")
        print(f"Place:{self.place}")
        print(f"Admission date:{self.admitdate}")
        print(f"Discharge date:{self.dischargedate}")

    def dischargeDetails(self):
            Hospital().showdetails()
            Department().showdepdetails()
            print(f"Patient id:{self.id}")
            print(f"Admission date:{self.admitdate}")
            print(f"Discharge date:{self.dischargedate}")
p=Patient()



