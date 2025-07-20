from django.shortcuts import render
from .models import HomePage, skillbasedECprograms, PoliciesProcedures, contactusForm, registrationForm

def home(request):
    try:
        home_content = HomePage.objects.first()
    except HomePage.DoesNotExist:
        home_content = None
    
    context = {
        'home_content': home_content
    }
    return render(request, 'school/home.html', context)

def class9_10_SSC(request):
    return render(request, 'school/class9_10_ssc.html')

def contactUs(request):
    if request.method == 'POST':
        # Handle form submission
        contact_form = contactusForm(
            parent_name=request.POST.get('parent_name'),
            student_first_name=request.POST.get('student_first_name'),
            student_last_name=request.POST.get('student_last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            country=request.POST.get('country')
        )
        contact_form.save()
        return render(request, 'school/contact_us.html', {'success': True})
    
    return render(request, 'school/contact_us.html')

def enrollNow(request):
    if request.method == 'POST':
        # Handle registration form submission
        registration_form = registrationForm(
            parent_name=request.POST.get('parent_name'),
            student_first_name=request.POST.get('student_first_name'),
            student_last_name=request.POST.get('student_last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            country=request.POST.get('country'),
            gender=request.POST.get('gender'),
            grade=request.POST.get('grade'),
            age=request.POST.get('age'),
            subject=request.POST.get('subject')
        )
        registration_form.save()
        return render(request, 'school/enroll_now.html', {'success': True})
    
    return render(request, 'school/enroll_now.html')

def higherEducation_studyAbroad(request):
    return render(request, 'school/higher_education_study_abroad.html')

def onlineSchool(request):
    return render(request, 'school/online_school.html')

def policiesProcedures(request):
    try:
        policies_content = PoliciesProcedures.objects.first()
    except PoliciesProcedures.DoesNotExist:
        policies_content = None
    
    context = {
        'policies_content': policies_content
    }
    return render(request, 'school/policies_procedures.html', context)

def skillBasedECPrograms(request):
    try:
        programs_content = skillbasedECprograms.objects.first()
    except skillbasedECprograms.DoesNotExist:
        programs_content = None
    
    context = {
        'programs_content': programs_content
    }
    return render(request, 'school/skill_based_ec_programs.html', context)

def whyChooseSL(request):
    return render(request, 'school/why_choose_sl.html')

def free_education_view(request):
    return render(request, 'school/free_education.html')