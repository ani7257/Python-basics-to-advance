#Problem1
class Employee:
    def __init__(self, name, basic_salary, qualification):
        self.name = name
        self.basic_salary = basic_salary
        self.qualification = qualification
    
    def validate_basic_salary(self):
        if self.basic_salary > 3000:
            return True
        else:
            return False
    
    def validate_qualification(self):
        if self.qualification == "Bachelors" or self.qualification == "Masters":
            return True
        else:
            return False

class Graduate(Employee):
    def __init__(self, name, basic_salary, qualification, job_band, cgpa):
        super().__init__(name, basic_salary, qualification)
        self.job_band = job_band
        self.cgpa = cgpa
    
    def validate_job_band(self):
        if self.job_band == "A" or self.job_band == "B" or self.job_band == "C":
            return True
        else:
            return False
    
    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
            
            if 4 <= self.cgpa <= 4.25:
                tpi = 1000
            elif 4.26 <= self.cgpa <= 4.5:
                tpi = 1700
            elif 4.51 <= self.cgpa <= 4.75:
                tpi = 3200
            elif 4.76 <= self.cgpa <= 5:
                tpi = 5000
            
            if self.job_band == "A":
                incentive = 0.04 * self.basic_salary
            elif self.job_band == "B":
                incentive = 0.06 * self.basic_salary
            elif self.job_band == "C":
                incentive = 0.1 * self.basic_salary
            
            gross_salary = self.basic_salary + pf + tpi + incentive
            return gross_salary
        else:
            return -1

class Lateral(Employee):
    def __init__(self, name, basic_salary, qualification, job_band, skill_set):
        super().__init__(name, basic_salary, qualification)
        self.job_band = job_band
        self.skill_set = skill_set
    
    def validate_job_band(self):
        if self.job_band == "D" or self.job_band == "E" or self.job_band == "F":
            return True
        else:
            return False
    
    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
            
            if self.skill_set == "AGP":
                sme_bonus = 6500
            elif self.skill_set == "AGPT":
                sme_bonus = 8200
            elif self.skill_set == "AGDEV":
                sme_bonus = 11500
            
            if self.job_band == "D":
                incentive = 0.13 * self.basic_salary
            elif self.job_band == "E":
                incentive = 0.16 * self.basic_salary
            elif self.job_band == "F":
                incentive = 0.2 * self.basic_salary
            
            gross_salary = self.basic_salary + pf + sme_bonus + incentive
            return gross_salary
        else:
            return -1

g1 = Graduate("Aniket", 4000, "Masters", "A", 4.5)
print("Graduate Details:")
print("Name-", g1.name)
print("Basic Salary-", g1.basic_salary)
print("Specializations-", g1.qualification)
print("Job Band-", g1.job_band)
print("CGPA-",g1.cgpa)
