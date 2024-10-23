from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .models import Course,Enrollment,Section,Lecture
from .forms import CourseForm, AssociateEmailForm,SectionForm,LectureForm
from django.contrib.auth import get_user_model
from django.forms import formset_factory,inlineformset_factory



@login_required
def create_course_step1(request):
    AssociateFormSet = formset_factory(AssociateEmailForm, extra=1)
    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        associate_formset = AssociateFormSet(request.POST, prefix='associates')

        if course_form.is_valid() and associate_formset.is_valid():
            course = course_form.save(commit=False)
            course.instructor = request.user
            course.save()
            for form in associate_formset:
                if form.cleaned_data:
                    email = form.cleaned_data['email']
                    try:
                        user = get_user_model().objects.get(email=email)
                        course.associates.add(user)
                    except get_user_model().DoesNotExist:
                        print('User is not registered')

            return redirect('add_sections_lectures', course_id=course.id)  
    else:
        course_form = CourseForm()
        associate_formset = AssociateFormSet(prefix='associates')

    return render(request, 'courses/course_creation1.html', {
        'course_form': course_form,
        'associate_formset': associate_formset,
    })
    
    

def add_sections_lectures(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    SectionFormSet = inlineformset_factory(Course, Section, form=SectionForm, extra=1)
    LectureFormSet = inlineformset_factory(Section, Lecture, form=LectureForm, extra=1)

    if request.method == 'POST':
        print(request.POST)
        
        section_formset = SectionFormSet(request.POST, request.FILES, instance=course)
        
        if section_formset.is_valid():
            sections = section_formset.save(commit=False)
            for section in sections:
                section.course = course  # Associate section with the course
                section.save()

                # Process the lecture formset for this specific section
                lecture_formset = LectureFormSet(request.POST, request.FILES, instance=section, prefix=f'section-{section.pk}')
                if lecture_formset.is_valid():
                    lecture_formset.save()
                else:
                    print(f"Lecture formset errors for section ID {section.pk}:", lecture_formset.errors)
            
            section_formset.save_m2m()  # Save any M2M relations if they exist
            return redirect('instructor_home')
        else:
            print("Section formset errors:", section_formset.errors)

    else:
        section_formset = SectionFormSet(instance=course)
        lecture_formsets = []
        
        for section_form in section_formset:
            section_instance = section_form.instance
            lecture_formsets.append(LectureFormSet(instance=section_instance, prefix=f'section-{section_instance.pk}'))

    return render(request, 'courses/add_sections_lectures.html', {
        'course': course,
        'section_formset': section_formset,
        'lecture_formsets': lecture_formsets,
    })
    
    
def add_section(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    total_forms = int(request.GET.get('total_forms', 0))  # get current form count
    section_form = SectionForm(prefix=f'section_{total_forms}')
    return render(request, 'courses/section_form.html', {'section_form': section_form})

def add_lecture(request, section_prefix):
    lecture_form = LectureForm(prefix=f'lecture_{section_prefix}')
    return render(request, 'courses/lecture_form.html', {'lecture_form': lecture_form})







def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {"courses": courses})


@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    # Check if the user is already enrolled
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)

    if created:
        return redirect(f'/courses/?status=enrolled')  # Adjust the URL to your page
    else:
        return redirect(f'/courses/?status=already_enrolled')

def display_course(request, id): #for the user
    course = get_object_or_404(Course, id=id)
    return render(request, 'courses/course_display.html', {'course': course})



@login_required
def course_list(request): #for the instructor
    qs=Course.objects.filter(user=request.user)
    context={'course_list':qs}
    return render(request, courses/course_list.html,context)









