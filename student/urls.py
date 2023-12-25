"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views, hodviews,staffviews,studentviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name='base'),
    path('',views.loginn,name='loginn'),
    
     
    # login
    path('dologin',views.dologin,name='dologin'),
    
    #logout
    path('dologout',views.dologout,name='dologout'),
    
    #profile
    path('profile',views.profile,name='profile'),
    
    path('profile/update',views.profileUpdate,name='profileUpdate'),
    
    
     
    # hod
    path('Hod',hodviews.home,name='hodhome'),
    path('Hod/student/Add',hodviews.addstudent,name='addstudent'),
    path('Hod/student',hodviews.studentlist,name='studentlist'),
    path('Hod/student/edit/<str:id>',hodviews.studentedit,name='studentedit'),
    path('Hod/student/update',hodviews.studentupdate,name='studentupdate'),
    path('Hod/student/delete/<str:admin>',hodviews.deletestudent,name='deletestudent'),
    path('Hod/student/view/<str:id>',hodviews.viewstudent,name='viewstudent'),
    path('Hod/student/notification',hodviews.studentnotification,name="studentnotification"),
    path('Hod/student/savestaffnotification',hodviews.savestudentnotification,name='savestudentnotification'),
    # path('Hod/student/leave',hodviews.hodstudentleave,name='hodstudentleave'),

    
    
    
    path('Hod/staff/add',hodviews.addstaff,name='addstaff'),
    path('Hod/staff',hodviews.stafflist,name='stafflist'),
    path('Hod/staff/edit/<str:id>',hodviews.editstaff,name='editstaff'),
    path('Hod/staff/update',hodviews.staffupdate,name='staffupdate'),
    path('Hod/staff/delete/<str:admin>',hodviews.deletestaff,name='deletestaff'),
    path('Hod/staff/view/<str:id>',hodviews.viewstaff,name='viewstaff'),
    path('Hod/staff/notification',hodviews.staffnotification,name='staffnotification'),
    path('Hod/staff/savestaffnotification',hodviews.savestaffnotification,name='savestaffnotification'),
    path('Hod/staff/leave',hodviews.hodstaffleave,name='hodstaffleave'),
    path('Hod/staff/approvestaffleave/<str:id>',hodviews.approvestaffleave,name='approvestaffleave'),
    path('Hod/staff/disapprovestaffleave/<str:id>',hodviews.disapprovestaffleave,name='disapprovestaffleave'),
    
    path('Hod/student/leave',hodviews.hodstudentleave,name='hodstudentleave'),
    path('Hod/student/approvestudentleave/<str:id>',hodviews.approvestudentleave,name='approvestudentleave'),
    path('Hod/student/disapprovestudentleave/<str:id>',hodviews.disapprovestudentleave,name='disapprovestudentleave'),
    
    path('Hod/staff/feedback',hodviews.sfeedback,name='sfeedback'),
    path('Hod/sreply/<str:id>',hodviews.givesreply,name='givesreply'),
    path('Hod/staff/sreply',hodviews.submitsreply,name='submitsreply'),
    
    path('Hod/student/feedback',hodviews.stfeedback,name='stfeedback'),
    path('Hod/streply/<str:id>',hodviews.givestreply,name='givestreply'),
    path('Hod/student/streply',hodviews.submitstreply,name='submitstreply'), 
    
    
    path('Hod/branch/add',hodviews.addbranch,name='addbranch'),
    path('Hod/branch',hodviews.branchlist,name='branchlist'),
    path('Hod/branch/edit/<str:id>',hodviews.editbranch,name='editbranch'),
    path('Hod/branch/update',hodviews.updatebranch,name='updatebranch'),
    path('Hod/branch/delete/<str:id>',hodviews.deletebranch,name='deletebranch'),
    
    

    
    path('Hod/subject/add',hodviews.addsubject,name='addsubject'),
    path('Hod/subject',hodviews.subjectlist,name='subjectlist'),
    path('Hod/subject/edit/<str:id>',hodviews.editsubject,name='editsubject'),
    path('Hod/subject/update',hodviews.updatesubject,name='updatesubject'),
    path('Hod/subject/delete/<str:id>',hodviews.deletesubject,name='deletesubject'),
    
    path('Hod/academic/add',hodviews.addacademic,name='addacademic'),
    path('Hod/academic',hodviews.academiclist,name='academiclist'),
    path('Hod/academic/edit/<str:id>',hodviews.editacademic,name='editacademic'),
    path('Hod/academic/update',hodviews.updateacademic,name='updateacademic'),
    path('Hod/academic/delete/<str:id>',hodviews.deleteacademic,name='deleteacademic'),
    
    path('Hod/attendance/view',hodviews.viewattendance,name='hodattendance'),
    
    
    
    
    
    
    #staff
    path('Staff',staffviews.home,name='staffhome'),
    path('Staff/notification',staffviews.notification,name='notification'),
    path('Staff/status/<str:st>',staffviews.status,name='stfstatus'),
    
    path('Staff/applyleave',staffviews.staffleave,name='staffleave'),
    path('Staff/submitstaffleave',staffviews.submitstaffleave,name='submitstaffleave'),
    path('Staff/leavelist',staffviews.leavelist,name='stfleavelist'),
    path('Staff/feedback',staffviews.stafffeedback,name='stafffeedback'),
    path('Staff/submitfeedback',staffviews.submitstafffeedback,name='submitstafffeedback'),
    path('Staff/feedbacklist',staffviews.stafffeedbacklist,name='stafffeedbacklist'),
    path('Staff/TakeAttendance',staffviews.takeattendance,name='takeattendance'),
    path('Staff/saveattendance',staffviews.saveattendance,name='saveattendance'),
    path('Staff/viewattendance',staffviews.viewattendance,name='viewattendance'),

   
   
   #student
    path('Student',studentviews.home,name='studenthome'),
    path('Student/notification',studentviews.notification,name='stnotification'),
    path('Student/status/<str:st>',studentviews.status,name='status'),
    path('Student/applyleave',studentviews.studentleave,name='studentleave'),
    path('Student/submitstudentleave',studentviews.submitstudentleave,name='submitstudentleave'),
    path('Student/leavelist',studentviews.leavelist,name='leavelist'),
    path('Student/feedback',studentviews.studentfeedback,name='studentfeedback'),
    path('Student/submitfeedback',studentviews.submitstudentfeedback,name='submitstudentfeedback'),
    path('Student/feedbacklist',studentviews.studentfeedbacklist,name='studentfeedbacklist'),
    path('Student/viewattendance',studentviews.viewattendance,name='stviewattendance'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
