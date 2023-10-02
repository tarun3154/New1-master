from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import *

class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class DoctorUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,label='Password')
   
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self,*args, **kwargs):

        super().__init__(*args, **kwargs)
        for frm in self.fields.values():
            frm.widget.attrs['class']='form-control'
            frm.widget.attrs['placeholder']=frm.label

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'],)
        if commit:
            user.save()
        return user
    
    
class DoctorForm(forms.ModelForm):
    CHOICES = [('Male','Male'),('Female','Female'),('Other','Other')]
    gender = forms.ChoiceField(widget=forms.RadioSelect(),choices=CHOICES)
    department = forms.ModelChoiceField(queryset=Department.objects.all(),empty_label='Select Department',)
    
    class Meta:
        model = Doctor
        fields = ['dob','address','profile_pic','mobileno','gender','dob']

    def __init__(self,*args, **kwargs):
        
        super().__init__(*args, **kwargs)
        for frm in self.fields.values():
            # frm.widget.attrs['class']='form-control'
            frm.widget.attrs['placeholder']=frm.label

class PatientUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,label='Password')
   
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self,*args, **kwargs):

        super().__init__(*args, **kwargs)
        for frm in self.fields.values():
            frm.widget.attrs['class']='form-control'
            frm.widget.attrs['placeholder']=frm.label

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'],)
        if commit:
            user.save()
        return user
    
    
class PatientForm(forms.ModelForm):
    CHOICES = [('Male','Male'),('Female','Female'),('Other','Other')]
    gender = forms.ChoiceField(widget=forms.RadioSelect(),choices=CHOICES)
    assignedDoctorId = forms.ModelChoiceField(queryset=Doctor.objects.all(),empty_label='Select Doctor')
    class Meta:
        model = Patient
        fields = ['dob','address','profile_pic','mobileno','symptoms','gender','email']

    def __init__(self,*args, **kwargs):
        
        super().__init__(*args, **kwargs)
        for frm in self.fields.values():
            # frm.widget.attrs['class']='form-control'
            frm.widget.attrs['placeholder']=frm.label

class AdminAppointmentForm(forms.ModelForm):
    appointment_id =forms.ModelChoiceField(queryset=Appointment.objects.all())
     
    class Meta:
        model = User
        fields='__all__'

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for frm in self.fields.values():
                frm.widget.attrs['class']='form-control'
                frm.widget.attrs['placeholder']=frm.label


class AppointmentForm(forms.ModelForm):
    doctorName= forms.ModelChoiceField(queryset= Doctor.objects.all(),empty_label='Select Doctor')
    department= forms.ModelChoiceField(queryset= Department.objects.all(),empty_label='Select Department')
    patientName= forms.ModelChoiceField(queryset= Patient.objects.all(),empty_label='Select Patient ')
    appointment_id =forms.ModelChoiceField(queryset=Appointment.objects.all())

    class Meta:
        model = Appointment
        fields= '__all__'


        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for frm in self.fields.values():
                frm.widget.attrs['placeholder']=frm.label
                    # frm.widget.attrs['class']='form-control'



class DepartmentForm(forms.ModelForm):
    CHOICES= [(True,'Active'),(False,'No active')]
    department_status = forms.ChoiceField(widget=forms.RadioSelect(),choices=CHOICES)
    
    class Meta:
        model = Department
        fields= ['name',]

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for frm in self.fields.values():
                frm.widget.attrs['class']='form-control'
                frm.widget.attrs['placeholder']=frm.label

class AdminDetailsForm(forms.ModelForm):
    class Meta:
        model= AdminDetails
        fields=['user','dob','address','state','country','mobileno','institution','subject','start_date','complete_date','degree','percentage','company_name','location','job_position','Period_from','Period_to']
        
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for frm in self.fields.values():
                frm.widget.attrs['class']='form-control'
                frm.widget.attrs['placeholder']=frm.label
