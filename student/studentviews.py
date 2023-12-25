from django.shortcuts import render,redirect,HttpResponse
from stuapp.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def home(request):
    
    studentID=Student.objects.get(admin=request.user.id)
    student=Student.objects.get(admin=request.user.id)
    subject=Subject.objects.filter(branch=student.branch_id)
    branch=Branch.objects.filter(name=student.branch_id)
    # subject=Subject.objects.filter(student=studentID)
    leave=StudentLeave.objects.filter(studentID=studentID)
    l1=leave.filter(status=0)
    l2=leave.filter(status=1)
    l3=leave.filter(status=2)


    return render(request,'student/home.html',{'s':subject,'l':leave,'l1':l1,'l2':l2,'l3':l3,'b':branch,})

@login_required(login_url='/')
def notification(request):
    student=Student.objects.filter(admin=request.user.id)
    print(student)
    for i in student:
        studentID=i.id
        notification=StudentNotification.objects.filter(studentID=studentID)
        
    return render(request,'student/notification.html',{'notification':notification})

@login_required(login_url='/')
def status(request,st):
    notification=StudentNotification.objects.get(id=st)
    notification.status=1
    notification.save()
    return redirect('stnotification')

@login_required(login_url='/')
def studentleave(request):
        return render(request,'student/applyleave.html')    

@login_required(login_url='/')
def leavelist(request):
    student=Student.objects.filter(admin=request.user.id)
    for i in student:
        studentID=i.id
        list=StudentLeave.objects.filter(studentID=studentID)

        
    return render(request,'student/leavelist.html',{'list':list})

@login_required(login_url='/')
def submitstudentleave(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        student=Student.objects.get(admin=request.user.id)
        
        leavee=StudentLeave(
            studentID=student,
            fromdate=fromdate,
            todate=todate,
            message=reason
        )
        leavee.save()
        messages.success(request,'Leave Applicattion submitted successfully')
        return redirect('studentleave')
        
    return render(request,'student/leavelist.html')

@login_required(login_url='/')
def studentfeedback(request):
    return render(request,'student/feedback.html')


@login_required(login_url='/')
def submitstudentfeedback(request):
    if request.method=="POST":
        feedback=request.POST.get('feedback')
        student=Student.objects.get(admin=request.user.id)
        feedbacks=StudentFeedback(studentID=student,feedback=feedback)
        feedbacks.save()
        
        messages.success(request,'feedback submitted successfully')
        return redirect('studentfeedback')
    return render(request,'student/feedback.html')


@login_required(login_url='/')
def studentfeedbacklist(request):
    student=Student.objects.filter(admin=request.user.id)
    for i in student:
        studentID=i.id
        list=StudentFeedback.objects.filter(studentID=studentID)

        
    return render(request,'student/feedbacklist.html',{'list':list})

def viewattendance(request):
    student=Student.objects.get(admin=request.user.id)
    subjects=Subject.objects.filter(branch=student.branch_id)
    action=request.GET.get('action')
    attendance_report=None
    get_subject=None
    if action is not None:
        if request.method=="POST":
            subject_id=request.POST.get('subject_id')
            get_subject=Subject.objects.get(id=subject_id)
            
            # attendance=Attendance.objects.get(subject_id=subject_id)
            attendance_report=Attendance_report.objects.filter(studentID=student,attendance_id__subject_id=subject_id)
        
    return render(request,'student/viewattendance.html',{'subjects':subjects,'get_subject':get_subject,'action':action,
                                                         'attendance_report':attendance_report})