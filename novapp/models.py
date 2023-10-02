from django.db import models
from django.contrib.auth.models import User
from datetime import date
User._meta.get_field('email')._unique = True

# Create your models here.
 
class Department(models.Model):
    name= models.CharField(max_length=20)
    description = models.TextField(max_length=100,default='')
    department_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name




class Doctor(models.Model):
    user =models.OneToOneField(User,  on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    profile_pic = models.ImageField(upload_to='doctorprofile/', null=True)
    mobileno = models.CharField(max_length=13,null=True)
    dob = models.DateField(max_length=14,null=True)
    gender = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=30,null=True)
    status = models.BooleanField(default=False)

    @property
    def fname(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    @property
    def age(self):
        today = date.today()
        dob = self.dob
        if dob:
            age = today.year - dob.year
            return age
        return None
 
    
    def __str__(self):
         return self.user.username

class Patient(models.Model):
        user =models.OneToOneField(User, verbose_name=("Patient"), on_delete=models.CASCADE)
        profile_pic = models.ImageField(upload_to='patientprofile/')
        dob = models.DateField(max_length=14,null=True)
        address = models.CharField(max_length=30)
        gender = models.CharField(max_length=10,null=True,blank=True)
        symptoms = models.CharField(max_length=100, null=False,blank=True)
        assignedDoctorId = models.PositiveIntegerField(null=True)
        admitDate = models.DateField(auto_now_add=True)
        status = models.BooleanField(default=False)
        mobileno = models.CharField(max_length=13)
        email = models.EmailField(max_length=50,default='',null=True)
        

        @property
        def fname(self):
            return f'{self.user.first_name} {self.user.last_name}'
        
        @property
        def age(self):
            today = date.today()
            dob = self.dob
            if dob:
                age = today.year - dob.year
                return age
            return None
        
        def __str__(self):
         return self.user.username



class Appointment(models.Model):
    patientName = models.CharField(max_length=50)
    doctorName = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=False)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    appointmentBookDate = models.DateField(auto_now_add=True)
    appointmentDate = models.DateField()
    # address = models.CharField(max_length=100,null=True)
    status = models.BooleanField(default=False)
    mobileno = models.CharField(max_length=13,null=True)
    email = models.EmailField(max_length=50,default='')



    def  __str__(self):
        return self.patientName



class AdminDetails(models.Model):
    user =models.OneToOneField(User,  on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='adminprofile/', null=True)
    mobileno = models.CharField(max_length=13,null=True)
    dob = models.DateField(max_length=14,null=True)
    gender = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=30,null=True)
    state =models.CharField(max_length=30,null=True)
    country= models.CharField(max_length=30,null=True)
    institution=models.CharField(max_length=30,null=True)
    subject =models.CharField(max_length=30,null=True)
    start_date=models.DateField(max_length=14,null=True)
    complete_date=models.DateField(max_length=14,null=True)
    degree =models.CharField(max_length=14,null=True)
    percentage=models.FloatField(max_length=10,null=True)
    company_name= models.CharField(max_length=20,null=True)
    location=models.CharField(max_length=20,null=True)
    job_position=models.CharField(max_length=20,null=True)
    Period_from=models.DateField()
    Period_to=models.DateField()

    status = models.BooleanField(default=False)
      
    def  __str__(self):
        return self.user
