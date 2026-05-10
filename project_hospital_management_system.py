class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.__age}")

class Staff(Person):
    total_staff = 0

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        Staff.total_staff += 1
    def display_info(self):
         print(f"name:{self.name} age:{self.get_age()} salary:{self.salary}")   
           
    @staticmethod
    def check_working_hours(hours):
        if hours <= 8:
            print(f"Hours: {hours} → ✅ Working hours valid!")
        else:
            print(f"Hours: {hours} → ❌ Overtime!")
class Patient(Person):
    total_patients = 0           
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.__disease = disease
        Patient.total_patients += 1
    def get_disease(self):
        return self.__disease    
    def display_info(self):
        print(f"Patient: {self.name} | Age: {self.get_age()} | Disease: {self.__disease}")    
        
        
class Doctor(Staff):
    def __init__(self, name, age, salary, department, fees):
        super().__init__(name, age, salary)   # pehle super
        self.department = department
        self.fees = fees
    def display_info(self):
        print(f"Doctor: {self.name} | Department: {self.department} | Fees: {self.fees}")    
        
class Nurse(Staff):
    def __init__(self , name , age , salary, shift , ward) :
        super().__init__(name , age , salary) 
        self.name=name
        self.shift=shift
        self.ward=ward
        
    def display_info(self):
        print(f"Nurse: {self.name} | Shift: {self.shift} | Ward: {self.ward}")
            
class Operator:
    def __init__(self , operation_type):
        self.operation_type=operation_type
    def display_info(self):
        print(self.operation_type)
               
class Surgeon(Doctor , Operator):
    def __init__(self , name , age , salary, department , fees , speciality , operation_type):
        self.name=name
        self.speciality=speciality
        Doctor.__init__(self, name, age, salary, department, fees)
        Operator.__init__(self, operation_type)
    def display_info(self):
        print(f"Surgeon: {self.name} | Speciality: {self.speciality} | Operation: {self.operation_type}")
            
        
        
p1=Patient("Ali" , 25 , "Diabetic")
d1=Doctor("Dr . Ahmed" , 25 , 2000 , "Cardiology" , 500)
n1=Nurse("Ayesha" , 30 , 800 , "Morning" , "ICU")
s1=Surgeon("Dr . Bilal" , 50 , 5000 , "Neuro", 3000 , "Brain Expert" , "Brain Surgery")

p2 = Patient("Sara", 30, "Fever")
p3 = Patient("Ahmed", 45, "BP")
d2 = Doctor("Dr. Ali", 40, 3000, "Neurology", 800)
n2 = Nurse("Fatima", 25, 700, "Night", "General")
s2 = Surgeon("Dr. Usman", 55, 8000, "Cardio", 5000, "Heart Expert", "Heart Surgery")


print("=" * 55)
print("        🏥 HOSPITAL MANAGEMENT SYSTEM")
print("          Built with Python OOP Concepts")
print("=" * 55)

print("\n📋 PATIENTS RECORD:")
print("-" * 55)
for person in [p1, p2, p3]:
    person.display_info()

print("\n👨‍⚕️ DOCTORS & STAFF RECORD:")
print("-" * 55)
for person in [d1, d2, n1, n2, s1, s2]:
    person.display_info()

print("\n📊 HOSPITAL STATISTICS:")
print("-" * 55)
print(f"  🤒 Total Patients Admitted : {Patient.total_patients}")
print(f"  👨‍💼 Total Staff Members     : {Staff.total_staff}")

print("\n⏰ WORKING HOURS CHECK:")
print("-" * 55)
Staff.check_working_hours(6)
Staff.check_working_hours(10)

print("\n🔍 STAFF VERIFICATION (isinstance):")
print("-" * 55)
print(f"  Is Dr. Ahmed a Doctor? → {isinstance(d1, Doctor)}")
print(f"  Is Ayesha a Doctor?    → {isinstance(n1, Doctor)}")
print(f"  Is Dr. Bilal a Staff?  → {isinstance(s1, Staff)}")

print("\n✅ OOP CONCEPTS USED:")
print("-" * 55)
print("  ✔ Classes & Objects")
print("  ✔ Inheritance")
print("  ✔ Encapsulation")
print("  ✔ Polymorphism")
print("  ✔ Class Variables")
print("  ✔ Static Methods")
print("  ✔ Property Decorators")
print("  ✔ isinstance() Function")
print("  ✔ Multiple Inheritance")
print("=" * 55)
print("        Developed by: Danish Ali")
print("=" * 55)
