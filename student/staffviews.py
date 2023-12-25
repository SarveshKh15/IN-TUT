from django.shortcuts import render,redirect,HttpResponse
from stuapp.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def home(request):
    staffID=Staff.objects.get(admin=request.user.id)

    subject=Subject.objects.filter(staff=staffID)
    leave=StaffLeave.objects.filter(staffID=staffID)


    l1=leave.filter(status=0)
    l2=leave.filter(status=1)
    l3=leave.filter(status=2)


    return render(request,'staff/home.html',{'s':subject ,'l':leave,'l1':l1,'l2':l2,'l3':l3})

@login_required(login_url='/')
def notification(request):
    staff=Staff.objects.filter(admin=request.user.id)
    print(staff)
    for i in staff:
        staffID=i.id
        notification=StaffNotifcation.objects.filter(staffID=staffID)
        
    return render(request,'staff/notification.html',{'notification':notification})

@login_required(login_url='/')
def status(request,st):
    notification=StaffNotifcation.objects.get(id=st)
    notification.status=1
    notification.save()
    return redirect('notification')


@login_required(login_url='/')
def staffleave(request):
        return render(request,'staff/applyleave.html')    

@login_required(login_url='/')
def leavelist(request):
    staff=Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staffID=i.id
        list=StaffLeave.objects.filter(staffID=staffID)

        
    return render(request,'staff/leavelist.html',{'list':list})

@login_required(login_url='/')
def submitstaffleave(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        staff=Staff.objects.get(admin=request.user.id)
        
        leave=StaffLeave(
            staffID=staff,
            fromdate=fromdate,
            todate=todate,
            message=reason
        )
        leave.save()
        messages.success(request,'Leave Applicattion submitted successfully')
        return redirect('staffleave')
        
    return render(request,'staff/leavelist.html')

@login_required(login_url='/')
def stafffeedback(request):
    return render(request,'staff/feedback.html')


@login_required(login_url='/')
def submitstafffeedback(request):
    if request.method=="POST":
        feedback=request.POST.get('feedback')
        staff=Staff.objects.get(admin=request.user.id)
        feedbacks=StaffFeedback(staffID=staff,feedback=feedback)
        feedbacks.save()
        
        messages.success(request,'feedback submitted successfully')
        return redirect('stafffeedback')
    return render(request,'staff/feedback.html')


@login_required(login_url='/')
def stafffeedbacklist(request):
    staff=Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staffID=i.id
        list=StaffFeedback.objects.filter(staffID=staffID)

        
    return render(request,'staff/feedbacklist.html',{'list':list})


@login_required(login_url='/')
def takeattendance(request):
    staffID=Staff.objects.get(admin=request.user.id)
    
    subject=Subject.objects.filter(staff=staffID)
    acad_year=Acad_year.objects.all()
    action=request.GET.get('action')
    get_subject=None
    get_acad_year=None
    students=None
    if action is not None:
        if request.method=="POST":
            print(action)
            subject_id=request.POST.get('subject_id')
            acad_year_id=request.POST.get('acad_year_id')
            get_subject=Subject.objects.get(id=subject_id)
            get_acad_year=Acad_year.objects.get(id=acad_year_id)
            
            subject=Subject.objects.filter(id=subject_id)
            
            for i in subject:
                studentID=i.branch.id
                students=Student.objects.filter(branch_id=studentID)
        
    
    dict={
        'subject':subject,'y':acad_year,'get_subject':get_subject,'get_acad_year':get_acad_year,'action':action,'students':students
    }
    return render(request,'staff/attendance.html',dict)

def saveattendance(request):
    if request.method=="POST":
        subject_id=request.POST.get('subject_id')
        acad_year_id=request.POST.get('acad_year_id')
        date=request.POST.get('date')
        studentID=request.POST.getlist('studentID')
        
        get_subject=Subject.objects.get(id=subject_id)
        get_acad_year=Acad_year.objects.get(id=acad_year_id)
        
        attendance=Attendance(subject_id=get_subject,attendance_date=date,acad_year_id=get_acad_year)
        attendance.save()
        
        for i in studentID:
            studID=i
            int_stud=int(studID)
            
            pstudent=Student.objects.get(id=int_stud)
            
            attendance_report=Attendance_report(studentID=pstudent,
                                                attendance_id=attendance)
            attendance_report.save()
            
            
    return redirect('takeattendance')


def viewattendance(request):
    staffID=Staff.objects.get(admin=request.user.id)
    subject=Subject.objects.filter(staff_id=staffID)
    acad_year=Acad_year.objects.all()
    
    action=request.GET.get('action')
    get_subject=None
    date=None
    get_acad_year=None
    attendance_report=None
    if action is not None:
        if request.method=="POST":
            subject_id=request.POST.get('subject_id')
            acad_year_id=request.POST.get('acad_year_id')
            date=request.POST.get('date')
        
            get_subject=Subject.objects.get(id=subject_id)
            get_acad_year=Acad_year.objects.get(id=acad_year_id)
            attendance=Attendance.objects.filter(subject_id=get_subject,attendance_date=date )
            
            
            for i in attendance:
                attendance_id=i.id
                attendance_report=Attendance_report.objects.filter(attendance_id=attendance_id)
                print(i,attendance_report)
                
    
    
    return render(request,'staff/viewattendance.html',{'subject':subject,'yy':acad_year,'action':action,'get_subject':get_subject,'y': get_acad_year,'date':date,'attendance_report':attendance_report})
 