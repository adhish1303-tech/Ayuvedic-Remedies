from django.shortcuts import render
from django.shortcuts import redirect
from ayurvedic_app.models import Register, admin, remedies
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
# Create your views here.


def indexpage(request):
    return render(request, "index.html")

def aboutpage(request):
    return render(request, "about.html")

def servicespage(request):
    return render(request, "services.html")

def blogpage(request):
    return render(request, "blog.html")

def contactpage(request):
    return render(request, "contact.html")

def loginpage(request):
    return render(request, "login.html")

def login(request):
    Email = request.POST.get('email')
    Password = request.POST.get('password')

    if request.method == "POST":
        try:
            user_login = Register.objects.get(Email = Email)
            if user_login.Password == Password:
                request.session['Email'] = Email
                return redirect("mydashboardpage") 
            else:
                messages.success(request, "Invalid Password")
                return redirect("loginpage")

        except Register.DoesNotExist :
            messages.error(request, "Email does not exists")
            return redirect("loginpage")

def resgistration(request):
    return render(request, "registration.html")

def registrationpage(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    password = request.POST.get('password')

    if Register.objects.filter(Email = email).exists():
        messages.success(request, "Email already exisits")
        return redirect("loginpage")
    else:
        con = Register(Name = name, Email = email, Contact = contact, Password = password)
        con.save()
        messages.success(request, "Account Created Successfully")
        return redirect("loginpage")

def mydashboardpage(request):
    if 'Email' not in request.session:
        return redirect("loginpage")
    else:
        Email = request.session.get('Email')
        users = Register.objects.get(Email=Email)
        return render(request, "mydashboard.html",{'users':users}) #{"Users" : users})

def updatepage(request):
    if 'Email' not in request.session:
        return redirect("loginpage")
    else:
        Email = request.session.get('Email')
        users = Register.objects.get(Email=Email)
        return render(request, "updateinfo.html",{'users':users}) 

def updateinfo_code(request):
        Email = request.session.get('Email')
        users = Register.objects.get(Email = Email)
        if request.method == "POST":
            users.Name = request.POST.get('name')
            users.Email = request.POST.get('email')
            users.Conatct = request.POST.get('phone')
            users.Password = request.POST.get('password')
            users.save()
            messages.success(request, "Account Information Updated")
            return redirect("mydashboardpage")

def logout_view(request):
    logout(request)
    # The session data for the current request is completely cleaned out.
    return redirect('loginpage')  # Redirect to your login or home page

def adminloginpage(request):
    return render(request, 'adminlogin.html')

def admindashboardpage(request):
    if 'Email' not in request.session:
        return redirect("loginpage")
    else:
        #Email = request.session.get('Email')
        users = Register.objects.all()
        remedy = remedies.objects.filter(status = "PENDING")
        approved_remedies = remedies.objects.filter(status = "Approved")
        return render(request, "admindashboard.html",{'users':users, 'remedy' : remedy, 'approved_remedies' : approved_remedies}) #{"Users" : users})
    
    #return render(request, 'admindashboard.html')

def adminlogin(request):
    Email = request.POST.get('email')
    Password = request.POST.get('password')

    if request.method == "POST":
        try:
            admin_login = admin.objects.get(email = Email)
            if admin_login.password == Password:
                request.session['Email'] = Email
                return redirect("admindashboardpage") 
            else:
                messages.success(request, "Invalid Password")
                return redirect("loginpage")

        except admin.DoesNotExist :
            messages.error(request, "Email does not exists")
            return redirect("loginpage")

def logout_admin(request):
    logout(request)
    # The session data for the current request is completely cleaned out.
    return redirect('adminloginpage')  # Redirect to your login or home page

def search_users(request):
    query = request.GET.get('name')

    if query :
        users = Register.objects.filter(Name__icontains = query) # this will give you all the names that you are trying to search
                                                                    # ex : vijay sawar then if we search "vijay" it matches and also if we search "sawar" it matches
    else:
        users = Register.objects.none()
    return render(request, "search_users.html",{'users':users}) #{"Users" : users})

def admin_remedies(request):
    return render(request, "adminremedies.html")

def admin_upload(request, id):
    admins = admin.objects.get(id = id)
    user_name = request.POST.get("")
    user_email = request.POST.get(admins.email) 
    name = request.POST.get('remedy_name')
    issues = request.POST.get('issues')
    solution = request.POST.get('solutions')
    img = request.FILES.get('remedy_image')
    video = request.FILES.get('remedy_video')
    benefits = request.POST.get('benefits')

    con = remedies( user_name = user_name, user_email = user_email, Name = name, Issues = issues, Solution = solution, img = img, video = video, Benefits = benefits)
    con.save()
    messages.success(request, "Remedy Added Successfully")
    return redirect("admindashboardpage")

# def remedieslist(request):
#         #Email = request.session.get('Email')
#         remedy = remedies.objects.filter(status='PENDING')
#         return render(request, "admindashboard.html",{'remedies' : remedy}) #{"Users" : users})

def useremediespage(request):
    if 'Email' not in request.session:
            return redirect("loginpage")
    else:
        Email = request.session.get('Email')
        users = Register.objects.get(Email=Email)

    return render(request, "useremedies.html", {'users': users })

def user_upload(request):
    user_name = request.POST.get('name')
    user_email = request.POST.get('email')
    name = request.POST.get('remedy_name')
    issues = request.POST.get('issues')
    solution = request.POST.get('solutions')
    img = request.FILES.get('remedy_image')
    video = request.FILES.get('remedy_video')
    benefits = request.POST.get('benefits')

    con = remedies( user_name = user_name, user_email = user_email, Name = name, Issues = issues, Solution = solution, img = img, video = video, Benefits = benefits)
    con.save()
    messages.success(request, "Remedy will be reviwed")
    return redirect("useremediespage")

def pending_remedies(request):
    remedy = remedies.objects.filter(status = "PENDING")
    return render(request, "peding_remedies.html", {'remedy' : remedy})

def approve_remedy(request,id):
    remedy= remedies.objects.get(id=id)
    remedy.status='Approved'
    remedy.save()
    return redirect("admindashboardpage")

def disapprove_remedy(request,id):
    remedy= remedies.objects.get(id=id)
    remedy.status='Declined'
    remedy.save()
    return redirect("admindashboardpage")

def approved_remedies(request):
    remedy = remedies.objects.filter(status = "Approved")
    return render(request, "approved_remedy.html", {'remedy' : remedy})

def decline_remedies(request):
    remedy = remedies.objects.filter(status = "Declined")
    return render(request, "declined_remedy.html", {'remedy' : remedy})

def pending_remedies(request):
    remedy = remedies.objects.filter(status = "PENDING")
    return render(request, "pending_remedies.html", {'remedy' : remedy})

def approved_remedy(request):
    remedy = remedies.objects.filter(status = "Approved")
    return render(request, "approved_remedy.html",{'remedy' : remedy})

def allremedies(request):
    remedy = remedies.objects.all()
    return render(request, "all_remedy.html", {'remedy' : remedy})

def email(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        sender_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        from_email = f"{full_name}  <{sender_email}>"
        to_email = ["adhish.1303@gmail.com"]
        text_content = f"From {full_name}, \n\n {message} \n\n Thank You"
        html_content = f"""
                    <p> Dear <strong> { full_name } </strong> </p>
                    <p> { message } </p>
                    <br>
                    <p>Thank You, <br> <strong> {full_name} </strong> </p>
        """
        email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        email.attach_alternative(html_content, "text/html")

        try:
            email.send()
            messages.success(request,"Email sent successfully to the user !!")
            return redirect('email')
        except Exception as e:
            return HttpResponse(f"Failed to send email : {e}")