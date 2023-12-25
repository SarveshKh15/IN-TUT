from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from stuapp.models import CustomUser
from stuapp.models import *

@login_required(login_url='/')
def home(request):
    tstudent=Student.objects.all().count()
    tstaff=Staff.objects.all().count()
    tsubject=Subject.objects.all().count()
    tbranch=Branch.objects.all().count()
    
    tboys=Student.objects.filter(gender='Male').count()
    tgirls=Student.objects.filter(gender='Female').count()
    
    
    
    dict={'student':tstudent,'staff':tstaff,'subject':tsubject,'branch':tbranch,'boys':tboys,'girls':tgirls}
    return render(request,'hod/home.html',dict)

@login_required(login_url='/')
def addstudent(request):
    branch=Branch.objects.all()
    acad_year=Acad_year.objects.all()
    
    if request.method=="POST":
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        branch_id=request.POST.get('branch_id')
        acad_year_id=request.POST.get('acad_year_id')
        
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        parentmob=request.POST.get('parentmob')
        studentmob=request.POST.get('studentmob')
        gender=request.POST.get('gender')
       
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"Email Already exists")
            return redirect('addstudent')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exists')
            return redirect('addstudent')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()   
            branch=Branch.objects.get(id=branch_id)
            acad_year=Acad_year.objects.get(id=acad_year_id)
            
            student= Student(
                admin=user,
                address=address,
                branch_id=branch,
                acad_year_id=acad_year,
                gender=gender,
                parentmob=parentmob,
                studentmob=studentmob,
                dob=dob
                )          
            student.save()
            messages.success(request,'Student Saved Succesffully')
            return redirect('studentlist')

                
            

    dict={
        'branch':branch,'year':acad_year
    }
    return render(request,'hod/addstudent.html',dict)

@login_required(login_url='/')
def studentlist(request):
    student =Student.objects.all()
    dict={
        'student':student
    }
    
    return render(request,'hod/studentlist.html',dict)

@login_required(login_url='/')
def studentedit(request,id):
    branch=Branch.objects.all()
    acad_year=Acad_year.objects.all()
    student=Student.objects.filter(id=id)
    dict={'branch':branch,
          'year':acad_year,
        'student':student,
    }
     
    return render(request,'hod/studentedit.html',dict)

@login_required(login_url='/')
def studentupdate(request):
    
    if request.method=="POST":
        
        student_id=request.POST.get('student_id')
        
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        
        branch_id=request.POST.get('branch_id')
        acad_year_id=request.POST.get('acad_year_id')
      
        
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        parentmob=request.POST.get('parentmob')
        studentmob=request.POST.get('studentmob')
        gender=request.POST.get('gender')
        
        
        
        userr=CustomUser.objects.get(id=student_id)
       
        userr.first_name=first_name
        userr.last_name=last_name
        userr.email=email
        userr.username=username
        if password!=None and password!="":
            userr.set_password(password)
        if profile_pic!=None and profile_pic!= "":
            userr.profile_pic = profile_pic
            
        
        userr.save()
        
        student=Student.objects.get(admin=student_id)
        
        student.address=address
        student.gender=gender
        
        student.studentmob=studentmob
        student.parentmob=parentmob
        if dob!=None and dob!="":
            student.dob=dob
        
       
        branch=Branch.objects.get(id=branch_id)
        student.branch_id=branch
        acad_year=Acad_year.objects.get(id=acad_year_id)
        student.acad_year_id=acad_year
        
        student.save()
        messages.success(request,'records are successfully updated')
        
        return redirect('studentlist')
    return render(request,'hod/studentedit.html')

@login_required(login_url='/')
def deletestudent(request,admin):
    student=CustomUser.objects.get(id=admin)
    
    student.delete()
    messages.success(request,"Record is successfully deleted")
    return redirect('studentlist')


@login_required(login_url='/')
def viewstudent(request,id):
    
    student=Student.objects.get(id=id)
    return render(request,'hod/viewstudent.html',{'student':student})


















@login_required(login_url='/')
def addbranch(request):
    
    if request.method=="POST":
        branch_name=request.POST.get('branch_name')
        
        branch=Branch(
            name=branch_name
        )
        branch.save()
        messages.success(request,'Branch Added Successfully')
        
        
    return render(request,'hod/addbranch.html')

@login_required(login_url='/')
def branchlist(request):

    branch=Branch.objects.all()

    return render(request,'hod/branchlist.html',{'branch':branch})

@login_required(login_url='/')
def editbranch(request,id):
    branch=Branch.objects.get(id=id)
    
    return render(request,'hod/editbranch.html',{'branch':branch})
    


@login_required(login_url='/')
def updatebranch(request):
    if request.method=="POST":
        branch_id=request.POST.get('branch_id')
        branch_name=request.POST.get('branch_name')
        branch=Branch.objects.get(id=branch_id)
        branch.name=branch_name
        branch.save()
        messages.success(request,'Branch edited successfully')
        return redirect('branchlist')
        
    return redirect('editbranch')

@login_required(login_url='/')
def deletebranch(request,id):
    branch=Branch.objects.get(id=id)
    branch.delete()
    messages.success(request,'Branch deleted successfully')
    return redirect('branchlist')












@login_required(login_url='/')
def addstaff(request):
    if request.method=="POST":
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        mobile=request.POST.get('mobile')
        altmobile=request.POST.get('altmobile')
        gender=request.POST.get('gender')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"Email Already exists")
            return redirect('addstaff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exists')
            return redirect('addstaff')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2
            )
            user.set_password(password)
            user.save() 
            
            staff=Staff(
                admin=user,
                address=address,
                gender=gender,
                mobile=mobile,
                altmobile=altmobile,
                dob=dob
                
            )
            staff.save()
            messages.success(request,'Staff added successfully')
            return redirect('addstaff')
    return render(request,'hod/addstaff.html')

@login_required(login_url='/')
def stafflist(request):
    staff=Staff.objects.all()
    return render(request,'hod/stafflist.html',{'staff':staff})


@login_required(login_url='/')
def editstaff(request,id):
    staff=Staff.objects.filter(id=id)
    return render(request,'hod/editstaff.html',{'staff':staff})

@login_required(login_url='/')
def staffupdate(request):
    if request.method=="POST":
        
        staff_id=request.POST.get('staff_id')
        
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        mobile=request.POST.get('mobile')
        altmobile=request.POST.get('altmobile')
        gender=request.POST.get('gender')
        
        
        
        userr=CustomUser.objects.get(id=staff_id)
       
        userr.first_name=first_name
        userr.last_name=last_name
        userr.email=email
        userr.username=username
        if password!=None and password!="":
            userr.set_password(password)
        if profile_pic!=None and profile_pic!= "":
            userr.profile_pic = profile_pic
            
        
        userr.save()
        
        staff=Staff.objects.get(admin=staff_id)
        
        staff.address=address
        staff.gender=gender
        
        staff.mobile=mobile
        staff.altmobile=altmobile
        if dob!=None and dob!="":
            staff.dob=dob
        
       
        
        
        staff.save()
        messages.success(request,'Staff Records are successfully updated')
        
        return redirect('stafflist')
    return render(request,'editstaff')

@login_required(login_url='/')
def deletestaff(request,admin):
    staff=CustomUser.objects.get(id=admin)
    
    staff.delete()
    messages.success(request,"Staff Record is successfully deleted")
    return redirect('stafflist')
@login_required(login_url='/')
def viewstaff(request,id):
    staff=Staff.objects.get(id=id)
    return render(request,'hod/viewstaff.html',{'staff':staff})





@login_required(login_url='/')
def studentnotification(request):
    student=Student.objects.all()
    viewnotification=StudentNotification.objects.all()
    return render(request,'hod/studentnotification.html',{'student':student,'v':viewnotification})

@login_required(login_url='/')
def staffnotification(request):
    staff=Staff.objects.all()
    viewnotification=StaffNotifcation.objects.all()
    
    return render(request,'hod/staffnotification.html',{'staff':staff,'v':viewnotification},)


@login_required(login_url='/')
def savestudentnotification(request):
    if request.method=="POST":
        student_ID=request.POST.get('student_ID')
        message=request.POST.get('message')
        student=Student.objects.get(admin=student_ID)
        notification=StudentNotification(
            studentID=student,message=message
        )
        notification.save()
        messages.success(request,'Notification send successfully')
        return redirect('studentnotification')


@login_required(login_url='/')
def savestaffnotification(request):
    if request.method=="POST":
        staff_ID=request.POST.get('staff_ID')
        message=request.POST.get('message')
        staff=Staff.objects.get(admin=staff_ID)
        
        notification=StaffNotifcation(
            staffID=staff,message=message
        )
        notification.save()
        messages.success(request,'Notification send  successfully')
        return redirect('staffnotification')
    
    return render(request,'hod/staffnotification.html')

@login_required(login_url='/')
def hodstaffleave(request):
    staff=StaffLeave.objects.all()

    return render(request,'hod/staffleave.html',{'list':staff})


@login_required(login_url='/')
def approvestaffleave(request,id):
    status=StaffLeave.objects.get(id=id)
    status.status=1
    status.save()
    return redirect('hodstaffleave')

@login_required(login_url='/')
def disapprovestaffleave(request,id):
    status=StaffLeave.objects.get(id=id)
    status.status=2
    status.save()
    return redirect('hodstaffleave')



@login_required(login_url='/')
def hodstudentleave(request):
    student=StudentLeave.objects.all()

    return render(request,'hod/studentleave.html',{'list':student})


@login_required(login_url='/')
def approvestudentleave(request,id):
    status=StudentLeave.objects.get(id=id)
    status.status=1
    status.save()
    return redirect('hodstudentleave')

@login_required(login_url='/')
def disapprovestudentleave(request,id):
    status=StudentLeave.objects.get(id=id)
    status.status=2
    status.save()
    return redirect('hodstudentleave')


@login_required(login_url='/')
def sfeedback(request):
    list=StaffFeedback.objects.all()
    return render(request,'hod/sfeedback.html',{'list':list})

@login_required
def givesreply(request,id):
    reply=StaffFeedback.objects.get(id=id)
    return render(request,'hod/givesreply.html',{'reply':reply})

def submitsreply(request):
    if request.method=="POST":
        reply=request.POST.get('givesreply')
        replyID=request.POST.get('id')
        f=StaffFeedback.objects.get(id=replyID)
        f.feedbackreply=reply
        f.save()
        messages.success(request,'Replied On feedback successfully')
        return redirect('studentfeedback')

        
    return redirect('studentfeedback')


@login_required(login_url='/')
def stfeedback(request):
    list=StudentFeedback.objects.all()
    return render(request,'hod/stfeedback.html',{'list':list})

@login_required
def givestreply(request,id):
    reply=StudentFeedback.objects.get(id=id)
    return render(request,'hod/givestreply.html',{'reply':reply})

def submitstreply(request):
    if request.method=="POST":
        reply=request.POST.get('givestreply')
        replyID=request.POST.get('id')
        f=StudentFeedback.objects.get(id=replyID)
        f.feedbackreply=reply
        f.save()
        messages.success(request,'Replied On feedback successfully')
        return redirect('studentfeedback')

        
    return redirect('studentfeedback')









    











@login_required(login_url='/')
def addsubject(request):
    staff=Staff.objects.all()
    branch=Branch.objects.all()
    dict={
        'staff':staff,'branch':branch,
    }
    
    if request.method=="POST":
        subject_name=request.POST.get('name')
        branch_id=request.POST.get('branch_id')
        staff_id=request.POST.get('staff_id')
        branch=Branch.objects.get(id=branch_id)
        staff=Staff.objects.get(id=staff_id)
        subject= Subject(name=subject_name,branch=branch,staff=staff)
        
        subject.save()
        messages.success(request,'Subject Added Successfully')
        return redirect('addsubject')
        
    return render(request,'hod/addsubject.html',dict)

@login_required(login_url='/')
def subjectlist(request):
    subject=Subject.objects.all()
    return render(request,'hod/subjectlist.html',{'subject':subject})

@login_required(login_url='/')
def editsubject(request,id):
    subject=Subject.objects.get(id=id)
    staff=Staff.objects.all()
    branch=Branch.objects.all()
    return render(request,'hod/editsubject.html',{'subject':subject,'staff':staff,'branch':branch})

@login_required(login_url='/')
def updatesubject(request):
    if request.method=="POST":
        subject_id=request.POST.get('subject_id')
        subject_name=request.POST.get('name')
        branch_id=request.POST.get('branch_id')
        staff_id=request.POST.get('staff_id')
        
        branch=Branch.objects.get(id=branch_id)
        staff=Staff.objects.get(id=staff_id)
        
        subject=Subject.objects.get(id=subject_id)
        subject.name=subject_name
        subject.branch=branch
        subject.staff=staff
        subject.save()
        
        messages.success(request,'Subject Records are successfully updated')
        
        return redirect('subjectlist')
    return render(request,'editsubject')

@login_required(login_url='/')
def deletesubject(request,id):
    subject=Subject.objects.get(id=id)
    subject.delete()
    messages.success(request,'Subject deleted successfully')
    return redirect('subjectlist')
    
    
    
   






@login_required(login_url='/')
def addacademic(request):
    
    if request.method=="POST":
        startt=request.POST.get('start')
        endd=request.POST.get('end')
        acad=Acad_year(start=startt,end=endd)
        acad.save()
        messages.success(request,'Academic Year added successfully')
        return redirect('addacademic')
        
    return render (request,'hod/addacademic.html') 

@login_required(login_url='/')
def academiclist(request):
    acad=Acad_year.objects.all()
    return render (request,'hod/academiclist.html',{'acad':acad})

@login_required(login_url='/')
def editacademic(request,id):
    acad=Acad_year.objects.get(id=id)
    
    return render(request,'hod/editacademic.html',{'acad':acad})

@login_required(login_url='/')
def updateacademic(request):
    if request.method=="POST":
        acad_id=request.POST.get('acad_id')
        start=request.POST.get('start')
        end=request.POST.get('end')

        acad=Acad_year(id=acad_id,
        start=start,
        end=end)

        acad.save()
        messages.success(request,'Academic Year edited successfully')
        return redirect('academiclist')
        
    return redirect('academiclist')

@login_required(login_url='/')
def deleteacademic(request,id):
    acad=Acad_year.objects.get(id=id)
    acad.delete()
    messages.success(request,'Academic Year deleted successfully')
    return redirect('academiclist')
    
@login_required(login_url='/')
def viewattendance(request):
    subject=Subject.objects.all()
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
                
    
    
    return render(request,'hod/attendance.html',{'subject':subject,'yy':acad_year,'action':action,'get_subject':get_subject,'y': get_acad_year,'date':date,'attendance_report':attendance_report})