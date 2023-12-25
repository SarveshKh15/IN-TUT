from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.timezone import now
# Create your models here.



class CustomUser(AbstractUser):
    USER={
        (1,'HOD'),(2,'STAFF'),(3,'STUDENT')
        
    }
    user_type=models.CharField(choices=USER,max_length=100,default=1)
    profile_pic=models.ImageField(upload_to='media/profile_pic')
    
    
    
class Branch(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name
    
class Acad_year(models.Model):
    start=models.CharField(default=datetime.now().date(),blank=True,max_length=100)
    end=models.CharField(default=datetime.now().date(),blank=True,max_length=100)
    created_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)
    
    
    def __str__(self):
        return self.start+" to "+self.end
    
    
    

    

class Student(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=100)
    branch_id=models.ForeignKey(Branch,on_delete=models.DO_NOTHING)
    acad_year_id=models.ForeignKey(Acad_year,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    studentmob=models.CharField(max_length=100,default="0")
    parentmob=models.CharField(max_length=100,default="0")
    dob=models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.admin.first_name+" "+self.admin.last_name
    
    
class Staff(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender=models.CharField(max_length=10)
    address=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    dob=models.DateField(default=datetime.now)
    mobile=models.CharField(max_length=100,default="0")
    altmobile=models.CharField(max_length=100,default="0")
    
    
    
    def __str__(self):
        return self.admin.first_name
    
class Subject(models.Model):
    name=models.CharField(max_length=100)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
    
class StudentNotification(models.Model):
    message=models.TextField()
    studentID=models.ForeignKey(Student,on_delete=models.CASCADE)
    created_At=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(default=0)
    
    def __str__(self):
        return self.studentID.admin.first_name + " "+self.studentID.admin.last_name +" (ID "+str(self.id) +")" 
    

    
class StaffNotifcation(models.Model):
    message=models.TextField()
    staffID=models.ForeignKey(Staff,on_delete=models.CASCADE)
    created_At=models.DateTimeField(auto_now_add=True)
    status =models.IntegerField(null=True,default=0)
    def __str__(self):
        return self.staffID.admin.first_name + " "+self.staffID.admin.last_name +" (ID "+str(self.id) +")" 
    

class StaffLeave(models.Model):
    staffID=models.ForeignKey(Staff,on_delete=models.CASCADE)
    fromdate=models.CharField(max_length=20)
    todate=models.CharField(max_length=20)
    status=models.IntegerField(default=0)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.staffID.admin.first_name + " "+self.staffID.admin.last_name +" (ID "+str(self.id) +")" 
    
class StudentLeave(models.Model):
    studentID=models.ForeignKey(Student,on_delete=models.CASCADE)
    fromdate=models.CharField(max_length=20)
    todate=models.CharField(max_length=20)
    status=models.IntegerField(default=0)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.studentID.admin.first_name + " "+self.studentID.admin.last_name +" (ID "+str(self.id) +")" 

class StaffFeedback(models.Model):
    staffID=models.ForeignKey(Staff,on_delete=models.CASCADE)
    
    feedback=models.TextField()
    feedbackreply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.staffID.admin.first_name + " "+self.staffID.admin.last_name +" (ID "+str(self.id) +")" 
    
class StudentFeedback(models.Model):
    studentID=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    feedback=models.TextField()
    feedbackreply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.studentID.admin.first_name + " "+self.studentID.admin.last_name +" (ID "+str(self.id) +")" 
  

class Attendance(models.Model):
    subject_id=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    
    attendance_date=models.DateField()
    
    acad_year_id=models.ForeignKey(Acad_year,on_delete=models.DO_NOTHING)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.subject_id.name
    
    
class Attendance_report(models.Model):
    studentID=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
   
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.studentID.admin.first_name 
    
      
# class Result(models.Model):
#     studentID=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
#     subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
#     emarks=models.IntegerField()
#     amarks=models.IntegerField()
#     created_at=models.DateField(auto_now_add=True)
#     updated_at=models.DateField(auto_now_add=True)
    
#     def __str__(self):
#         return self.studentID.admin.first_name
    
    
    
    
    
    
    
    
