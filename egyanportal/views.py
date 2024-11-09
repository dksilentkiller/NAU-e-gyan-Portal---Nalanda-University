from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.cache import cache_control
from .models import registration, Login, Complaints, Usm, assignment, lecture, Feedbacks, Enquiry,Adbranch,program
from .models import noti
from django.contrib import messages
from datetime import date, datetime
from . import smssender
from django.core.mail import send_mail

# Create your views here.
#======================================== All Method For Templates ============================================ 

def layout(request):
    return render(request, 'layout.html')

def home(request):
    return render(request, 'home.html')

def homelogin(request):
    return render(request, 'homelogin.html')

def courses(request):
    return render(request, 'courses.html')

def aboutportal(request):
    return render(request, 'aboutportal.html')

def courselayout(request):
    return render(request, 'courselayout.html')

def ugcourse(request):
    return render(request, 'ugcourse.html')

def pgcourse(request):
    return render(request, 'pgcourse.html')

def dpcourse(request):
    return render(request, 'dpcourse.html')

def cfcourse(request):
    return render(request, 'cfcourse.html')


def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def viewstudy(request):
    if 'userid' in request.session:
        branch = request.session.get('branch')

        if branch:
            # Fetch material specific to the branch
            papa = Usm.objects.filter(branch=branch)

            # Render the template with the filtered materials
            return render(request, 'viewstudy.html', {'papa': papa})
        else:
            # If no branch information is found in the session, redirect to login
            messages.error(request, 'Branch information is missing.')
            return render(request,'viewstudy.html')
    else:
        # If 'userid' is not in session, redirect to login
        return redirect('homelogin')

def Registration(request):
     jv1=program.objects.all()
     fg=Adbranch.objects.all()
     return render(request, 'registration.html',{'jv':jv1,'fg':fg})

def login(request):
    return render(request, 'homelogin.html')

def adminpanel(request):
    if 'userid' in request.session:
        return render(request, 'adminpanel.html')
    else:
        return redirect('homelogin')

def logcode(request):
    if request.method == "POST":
        userid = request.POST['userid']
        password = request.POST['password']
        usertype = request.POST['usertype']
        ad = Login.objects.filter(userid=userid, password=password).first()
        if ad:
            if ad.usertype == "student" and usertype == "student":
                request.session['userid']=userid
                return redirect('adminpanel')
            elif ad.usertype=="admin" and usertype=="admin":
                request.session['adminid']=userid
                return redirect('adminzone')
            else:
                messages.success(request, 'Ivalid User')
                return redirect('login')
        else:
            messages.success(request, 'Invalid User')
            return render(request, 'homelogin.html')
        
def showdata(request):
    if 'adminid' in request.session:
        show = registration.objects.all()
        return render(request, 'showdata.html', {'Show':show})
    else:
        return redirect('homelogin')

def doubt(request):
    return render(request, 'doubt.html')

def complain(request):
    if 'userid' in request.session:
        sh = registration.objects.all()
        return render(request, 'complain.html',{'S':sh})
    else:
        return redirect('homelogin')


def feedback(request):
    if 'userid' in request.session:
        f = registration.objects.all()
        return render(request, 'feedback.html',{'f':f})
    else:
        return redirect('homelogin')

def assignments(request):
    if 'userid' in request.session:
        assg = assignment.objects.all()
        return render(request, 'assignments.html', {'assg':assg})
    else:
        return redirect('homelogin')

def lectures(request):
    if 'userid' in request.session:
        lec = lecture.objects.all()
        return render(request, 'lectures.html', {'lec':lec})
    else:
        return redirect('homelogin')

def maintenance(request):
    return render(request, 'maintenance.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminzone(request):
    return render(request, 'adminzone.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    allstudent = registration.objects.count()
    alllec = lecture.objects.count()
    allass = assignment.objects.count()
    allfeed = Feedbacks.objects.count()
    allcomp = Complaints.objects.count()
    allenq = Enquiry.objects.count()
    return render(request, 'adminhome.html',{'allstudent':allstudent, 'alllec':alllec, 'allass':allass, 'allfeed':allfeed, 'allcomp':allcomp, 'allenq':allenq})

'''def manageuser(request):
    ab = registration.objects.all()
    return render(request, 'showdata.html', {'Show':ab})'''

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def uploadstudy(request):
    if 'adminid' in request.session:
        ups = Usm.objects.all()
        return render(request, 'uploadstudy.html',{'ups':ups})
    else:
        return redirect('homelogin')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def uploadlecture(request):
    if 'adminid' in request.session:
        uls = lecture.objects.all()
        return render(request, 'uploadlecture.html',{'uls':uls})
    else:
        return redirect('homelogin')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def uploadassignment(request):
    if 'adminid' in request.session:
        uas = assignment.objects.all()
        return render(request, 'uploadassignment.html',{'uas':uas})
    else:
        return redirect('homelogin')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def updateprofile(request):
    if 'userid' in request.session:
        #stud = registration.objects.all()
        user_email = request.session.get('userid')
        user = registration.objects.filter(email=user_email).first()
        co = {
            'uee':user
            }
        return render(request, 'updateprofile.html',co)
    else:
        return redirect('homelogin')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studenthome(request):
    if 'userid' in request.session:
        nt = noti.objects.all()
        allassg = assignment.objects.count()
        alllt = lecture.objects.count()
        allsm = Usm.objects.count()
        allnoti = noti.objects.count()
        return render(request, 'studenthome.html',{'nt':nt, 'allassg':allassg, 'alllt':alllt, 'allsm':allsm, 'allnoti':allnoti})
    else:
        return redirect('homelogin')

def viewenquiry(request):
    if 'adminid' in request.session:
        enqs = Enquiry.objects.all()
        return render(request, 'viewenquiry.html',{'enqs':enqs})
    else:
        return redirect('homelogin')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def feedbackshow(request):
    if 'adminid' in request.session:
        fbs = Feedbacks.objects.all()
        return render(request, 'feedbackshow.html',{'fbs':fbs})
    else:
        return redirect('homelogin')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def complainshow(request):
    if 'adminid' in request.session:
        cps = Complaints.objects.all()
        return render(request, 'complainshow.html',{'cps':cps})
    else:
        return redirect('homelogin')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addnotification(request):
    if 'adminid' in request.session:
        return render(request, 'addnotification.html')
    else:
        return redirect('homelogin')

def uploaddata(request,id):
    qw = registration.objects.get(pk=id)
    return render(request, 'uploaddata.html',{'qw':qw})

def logout(request):
    request.session.flush()
    return redirect('home')

#======================================== All Method For Templates ============================================


#======================================== All Method For Save =================================================

def save(request):
    enrollment = request.POST['enrollment']
    name = request.POST['name']
    fname = request.POST['fname']
    mname = request.POST['mname']
    gender = request.POST['gender']
    address = request.POST['address']
    course = request.POST['course']
    branch = request.POST['branch']
    year = request.POST['year']
    mobile = request.POST['mobile']
    email = request.POST['email']
    password = request.POST['password']
    usertype = 'student'
    status = 'N'
    a = registration(enrollment=enrollment, name=name, fname=fname, mname=mname, gender=gender, address=address, course=course, branch=branch, year=year, mobile=mobile, email=email, password=password)
    b = Login(userid=email, password=password, usertype=usertype, status=status)
    a.save()
    b.save()
    messages.success(request, 'Your data has successfully submitted')
    return render(request, 'registration.html')

def save_view(request):
    if request.method == 'POST':
        # Extract form data
        enrollment = request.POST.get('enrollment')
        name = request.POST.get('name')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usertype = 'student'
        status = 'N'
        a = registration(enrollment=enrollment, name=name, fname=fname, mname=mname, gender=gender, address=address, course=course, branch=branch, year=year, mobile=mobile, email=email, password=password)
        b = Login(userid=email, password=password, usertype=usertype, status=status)
        a.save()
        b.save()

        # Prepare email content
        subject = 'Registration Confirmation'
        message = f'''
        Welcome to Nou Egyan!
        We’re excited to have you as a part of our community. 
        Below, you’ll find your login details for accessing the Nou Egyan portal.

        Your Userid And Password is:
        Userid: {email}
        Password: {password}

        Please keep this information secure and do not share it with anyone.
        '''
        from_email = 'rashmivartika5@gmail.com'
        recipient_list = [email]

        # Send email
        send_mail(subject, message, from_email, recipient_list)

        # Add success message and redirect
        messages.success(request, 'Registration successful! Please check your email for confirmation.')
        return render(request, 'registration.html') # Replace with your success URL

    return render(request, 'registration.html')

def complaintsave(request, id):
    sg = registration.objects.get(pk=id)
    Subject = request.POST['Subject']
    comp = request.POST['comp']
    status = 'Pending'
    reqdate = datetime.now()
    v = Complaints(name=sg.name, program=sg.course, branch=sg.branch, contactno=sg.mobile, email=sg.email, Subject=Subject, comp=comp,status=status, reqdate=reqdate)
    v.save()
    messages.success(request, 'Complain successfully registered')
    return redirect('complain')

def feedbacksave(request, id):
    fb = registration.objects.get(pk=id)
    Subject = request.POST['Subject']
    feed = request.POST['feed']
    status = 'Pending'
    reqdate = datetime.now()
    ak = Feedbacks(name=fb.name, program=fb.course, branch=fb.branch, contactno=fb.mobile, email=fb.email, Subject=Subject, feed=feed,status=status, reqdate=reqdate)
    ak.save()
    messages.success(request, 'Feedback submitted successfully!')
    return redirect('feedback')

def usmsave(request):
    program = request.POST['program']
    Branch = request.POST['Branch']
    Year = request.POST['Year']
    subject = request.POST['subject']
    file_name = request.POST['file_name']
    new_file = request.FILES['new_file']
    sv = Usm(program=program, Branch=Branch, Year=Year, subject=subject, file_name=file_name, new_file=new_file)
    sv.save()
    messages.success(request, 'Study Material successfully saved')
    return redirect('uploadstudy')

def assignmentsave(request):
    program = request.POST['program']
    Branch = request.POST['Branch']
    Year = request.POST['Year']
    subject = request.POST['subject']
    file_name = request.POST['file_name']
    new_file = request.FILES['new_file']
    ass = assignment(program=program, Branch=Branch, Year=Year, subject=subject, file_name=file_name, new_file=new_file)
    ass.save()
    messages.success(request, 'Assignment Uploaded successfully')
    return redirect('uploadassignment')

def lecturesave(request):
    program = request.POST['program']
    Branch = request.POST['Branch']
    Year = request.POST['Year']
    subject = request.POST['subject']
    file_name = request.POST['file_name']
    link = request.POST['link']
    ass = lecture(program=program, Branch=Branch, Year=Year, subject=subject, file_name=file_name, link=link)
    ass.save()
    messages.success(request, 'Lecture Uploaded successfully')
    return redirect('uploadlecture')

def enqsave(request):
    name = request.POST['name']
    contactno = request.POST['contactno']
    email = request.POST['email']
    enq = request.POST['enq']
    enqdate = datetime.now()
    ens = Enquiry(name=name, contactno=contactno, email=email, enq=enq, enqdate=enqdate)
    ens.save()
    smssender.sendsms(contactno)
    messages.success(request, 'Enquiry Uploaded successfully!')
    return redirect('contact')

def notisave(request):
    notm = request.POST['notm']
    notdate = date.today()
    ns = noti(notm=notm, notdate=notdate)
    ns.save()
    messages.success(request,'Notificaion added successfully!')
    return redirect('addnotification')

def updateform(request):
    if request.method=='POST':
        enrollment = request.POST['enrollment']
        name = request.POST['name']
        fname = request.POST['fname']
        mname = request.POST['mname']
        gender = request.POST['gender']
        address = request.POST['address']
        course = request.POST['course']
        branch = request.POST['branch']
        year = request.POST['year']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        up = registration(enrollment=enrollment, name=name, fname=fname, mname=mname, gender=gender, address=address, course=course, branch=branch, year=year, mobile=mobile, email=email, password=password)
        up.save()
        return redirect('showdata')

#======================================== All Method For Save =================================================
#======================================== All Method For Delete ================================================
def deleteusm(request, id):
    usd = Usm.objects.get(pk=id)
    usd.delete()
    return redirect('uploadstudy')

def deleteuser(request, id):
    duser = registration.objects.get(pk=id)
    duser.delete()
    return redirect('showdata')

def deleteass(request, id):
    asd = assignment.objects.get(pk=id)
    asd.delete()
    return redirect('uploadassignment')

def deletelect(request, id):
    lecd = lecture.objects.get(pk=id)
    lecd.delete()
    return redirect('uploadlecture')

def deletecomps(request,id):
    cpd = Complaints.objects.get(pk=id)
    cpd.delete()
    return redirect('complainshow')

def deletefeeds(request,id):
    fdd = Feedbacks.objects.get(pk=id)
    fdd.delete()
    return redirect('feedbackshow')

def deleteenq(request,id):
    eqd = Enquiry.objects.get(pk=id)
    eqd.delete()
    return redirect('viewenquiry')

#======================================== All Method For Delete ================================================

def proupdate(request):
    user_email = request.session.get('userid')
    user = registration.objects.filter(email=user_email).first()
    con = {
        'ue':user
    }
    return render(request, 'proupdate.html', con)

def upsave(request):
    if request.method == 'POST':
        user_email = request.session.get('userid')
        user = registration.objects.filter(email=user_email).first()

        if user:
            user.enrollment = request.POST['enrollment']
            user.name = request.POST['name']
            user.fname = request.POST['fname']
            user.mname = request.POST['mname']
            user.gender = request.POST['gender']
            user.address = request.POST['address']
            user.course = request.POST['course']
            user.branch = request.POST['branch']
            user.year = request.POST['year']
            user.mobile = request.POST['mobile']
            user.email = request.POST['email']
            user.password = request.POST['password']

            if 'new_file' in request.FILES:
                user.new_file = request.FILES['new_file']

            user.save()
            return redirect('updateprofile')
        else:
           
             return redirect('updateprofile')
        
def addcourse(request):
    jv1=program.objects.all()
    return render(request,'addcourse.html',{'av':jv1})


def coursave(request):
    course=request.POST['course']
    addate=datetime.now()
    av=program(course=course,addate=addate)
    av.save()
    return redirect('addcourse')

def addbranch(request):
     fg=Adbranch.objects.all()
     return render(request,'addbranch.html',{'fg':fg})

def branchsave(request):
    branch=request.POST['branch']
    adddate=datetime.now()
    mg=Adbranch(branch=branch,adddate=adddate)
    mg.save()
    return redirect('addbranch')

    