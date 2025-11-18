class employee:
    def set_id(self , eid):
        self.eid=eid
    def set_name(self , ename):
        self.ename=ename
    def set_salary(self , esalary):
        self.esalary=esalary

    
    def get_id(self):
        print("empoyee id = ",self.eid)
    def get_name(self):
        print("empoyee name = ",self.ename)
    def get_salary(self):
        print("empoyee salary = ",self.esalary)

object = employee()

object.set_id(101)
object.get_id()

object.set_name("jack")
object.get_name()

object.set_salary(50000)
object.get_salary()  
