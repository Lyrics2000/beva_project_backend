from django.shortcuts import redirect, render
from authentification.models import User
from django.contrib.auth.decorators import login_required
from .forms import ComplainForm
from .models import ComplaintsDetails
from django.db import IntegrityError
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
@login_required(login_url="authentification:login")
def index(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user_id = request.user.id
            user_obj =  User.objects.get(id= user_id)
            name =  request.POST.get('name')
            email = request.POST.get('email')
            student_type = request.POST.get('student_type')
            university = request.POST.get('university')
            course =  request.POST.get('course')
            reg_no =  request.POST.get('reg_no')
            if str(student_type) == "University Student":
                try:
                    obj=  ComplaintsDetails.objects.create(user_id = user_obj,
                    name = name,
                    email  =  email,
                    university =  university,
                    course = course,
                     reg_no= reg_no
                    )
                  

                    request.session['complaint_id'] = obj.id
                    messages.success(request, "submitted detailed successfully!" )
                    return redirect("mainapp:student_department")
                except IntegrityError as e:
                    print("error")
            elif str(student_type) == "Professional":
                try:
                    obj = ComplaintsDetails.objects.create(user_id = user_obj,name = name,email  =  email)
                  
                    request.session['complaint_id'] = obj.id
                    messages.success(request, "submitted detailed successfully!" )
                    return redirect("mainapp:student_department")
                except IntegrityError as e:
                    print("error")

    return render(request,'index.html')


@login_required(login_url="authentification:login")
def student_department(request):
    if request.method == "POST":
        complain_id =  request.session.get('complaint_id')
        department = request.POST.get('select_department')
        complaints =  request.POST.get('complaints')
        try:
             obj = ComplaintsDetails.objects.get(id=complain_id)
             obj.department =  department
             obj.complaint =  complaints
             obj.save()
             messages.success(request, "submitted detailed successfully!" )
             return redirect("mainapp:document_upload")
        except IntegrityError as e:
                    print("error")

    return render(request,'student_department.html')


@login_required(login_url="authentification:login")
def doc_upload(request):
    if request.method == "POST":
        complain_id =  request.session.get('complaint_id')
        browse_file = request.FILES['browse_files']
        try:
             obj = ComplaintsDetails.objects.get(id=complain_id)
             obj.file =  browse_file
             obj.save()
             messages.success(request, "submitted detailed successfully!" )
             return redirect("mainapp:choose_custome")
        except IntegrityError as e:
                    print("error")
        
    return render(request,'document_upload.html')



@login_required(login_url="authentification:login")
def choose_custome(request):
    if request.method == "POST":
        complain_id =  request.session.get('complaint_id')
        send_sms =  request.POST.get('send_sms')
        send_email = request.POST.get('send_email')
        if send_sms == 'on':
            try:
                obj = ComplaintsDetails.objects.get(id=complain_id)
                obj.send_sms =  True
                obj.save()
                messages.success(request, "submitted detailed successfully!" )
                
            except IntegrityError as e:
                    print("error")

        if send_email == 'on':
            try:
                obj = ComplaintsDetails.objects.get(id=complain_id)
                obj.send_email =  True
                obj.save()
                messages.success(request, "submitted detailed successfully!" )
                
            except IntegrityError as e:
                    print("error")
        return redirect("mainapp:thankyou")

        
    return render(request,'choose_custome.html')

@login_required(login_url="authentification:login")
def success(request):
    complain_id =  request.session.get('complaint_id')
    try:
        obj = ComplaintsDetails.objects.get(id=complain_id)
        obj.submitted =  True
        obj.save()
        current_site = get_current_site(request)
        messages.success(request, "submitted detailed successfully!" )
        del request.session['complaint_id']
        user_mail = request.user.email
        user = request.user
        email_subject = 'Submission of Complain'
        message = render_to_string('complain_submitted.html', {
        'user': user,
        'domain': current_site.domain,
 
        })
        to_email = user_mail
        email = EmailMessage(email_subject, message, to=[to_email])
        email.send()
    except IntegrityError as e:
            print("error")
        

    return render(request,'thankyou.html')

@login_required(login_url="authentification:login")
def confirmer(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_obj =  User.objects.get(id= user_id)
        if user_obj.type == "Student":
            return redirect("mainapp:student")
        elif user_obj.type == "Committee":
            return redirect("mainapp:committee")
    return redirect("authentification:login")

@login_required(login_url="authentification:login")
def home_student(request):
    user_id =  request.user.id
    user_obj = User.objects.get(id=user_id)
    total_complaints = ComplaintsDetails.objects.filter(user_id= user_obj).count()
    total_responded = ComplaintsDetails.objects.filter(user_id= user_obj,reviewed=True).count()
    total_unresponded =  total_complaints - total_responded
    context = {
        'total_complaints':total_complaints,
        'total_responded' : total_responded,
        'total_unresponded' :total_unresponded
    }
    return render(request,'home_student.html',context)

@login_required(login_url="authentification:login")
def home_committee(request):
    return render(request,'home_commitee.html')


@login_required(login_url="authentification:login")
def previous_complaints(request):
    all_complaints = ComplaintsDetails.objects.all()
    context = {
       'all_complaints':all_complaints
    }
    return render(request,'previous_complains.html',context)

@login_required(login_url="authentification:login")
def complaints_detailed(request,id):
    prop =  ComplaintsDetails.objects.get(id= id)

    context = {
        'props':prop
    }
    
    return render(request,'complaints_detailed.html',context)


@login_required(login_url="authentification:login")
def complaints_edit(request,id):
    prop =  ComplaintsDetails.objects.get(id= id)
    context = {
        'props':prop
    }
    if request.method == "POST":
        prop2 =  ComplaintsDetails.objects.get(id= id)
        name =  request.POST.get('name')
        email = request.POST.get('email')
        university =  request.POST.get('university')
        course  =  request.POST.get('course')
        reg_no =  request.POST.get('reg_no')
        department =  request.POST.get('department')
        complaint =  request.POST.get('complaint')
        file_upload =  request.FILES['file_upload']
        prop2.name =  name
        prop2.email =  email
        prop2.university =  university
        prop2.course =  course
        prop2.reg_no =  reg_no
        prop2.department = department
        prop2.complaint =  complaint
        prop2.file =  file_upload
        prop2.save()
        return redirect('mainapp:previous')

    return render(request,'edit_complaint.html',context)



@login_required(login_url="authentification:login")
def delete_complaint(request):
    if request.method == "POST":
        print(request.POST)
        complaint_id =  request.POST.get('complain_id')
        print(complaint_id,"complaint it")
        ComplaintsDetails.objects.get(id = complaint_id).delete()
        return redirect('mainapp:previous')

@login_required(login_url="authentification:login")
def follow_ups(request):
    return render(request,'follow_up.html')





