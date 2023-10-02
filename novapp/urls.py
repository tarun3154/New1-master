from django.urls import path
from .views import *
urlpatterns = [
    path('',ViewHome,name='home'),
    path('login/',ViewLogin,name='login'),
    path('logout/',ViewLogout,name='logout'),
    path('admin-register/',ViewAdminRegister,name='adminRegister'),
    path('patient-register/',ViewPatientRegister,name='patientRegister'),
    path('doctor-register/',ViewDoctorRegister,name='doctorRegister'),
    path('forget-password/',ViewForgetPassword.as_view(),name='forgetPassword'),
    path('setpass/<userId>/<token>',Viewsetpassword.as_view(),name='setpass'),


    # ADMIN DASHBOARD


    path('admin-dash/',viewAdminDashboardMain,name='adminMain'),
    path('admin-doctor-dash/',viewAdminDoctorDashboard,name='adminDoctor'),
    path('admin-doc-schedule/',viewAdminDoctorSchedule,name='adminDoctorSchedule'),
    path('admin-department/',viewAdminDepartment,name='adminDepartment'),
    path('admin-edit-department/<int:id>/',viewAdminEditDepartment,name='adminEditDepartment'),
    path('admin-edit-department/',viewAdminAddDepartment,name='adminAddDepartment'),

    path('admin-add-doctor/',viewAdminAddDoctor,name='adminAddDoctor'),

    path('admin-update-doctor/<int:id>/',viewAdminUpdateDoctor,name='adminUpdateDoctor'),
    path('admin-delete-doctor/<int:id>/',viewAdminDeleteDoctor,name='adminDeleteDoctor'),
    path('admin-edit-profile/',viewAdminEditProfile,name='editAdminProfile'),






    path('admin-patient-dash/',viewAdminPatientDashboard,name='adminPatient'),
    path('add-patient/',viewAddPatient,name='addPatient'),
    path('delete-patient/<int:id>/',viewDeletePatient,name='deletePatient'),
    path('edit-patient/<int:id>/',viewEditPatient,name='editPatient'),






    path('admin-appointment-dash/',viewAdminAppointmentDashboard,name='adminAppointment'),
    path('take_appointment/<int:id>/',viewTakeAppointment,name='takeAppointment'),
    path('add-appointment/',viewAddAppointment,name='addAppointment'),
    path('edit-appointment/<int:id>/',viewEditAppointment,name='editAppointment'),
    path('delete-appointment/<int:id>/',viewDeleteAppointment,name='deleteAppointment'),


    

]
