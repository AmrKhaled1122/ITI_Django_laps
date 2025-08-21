

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm

def register_student(request):
    saved_student = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            saved_student = form.save()  # save to database
            messages.success(request, 'Student registered successfully!')
            # Option A: redirect to avoid re-POST on refresh:
            # return redirect('courses:register_student_success', pk=saved_student.pk)
            # Option B (we'll show entered data on same page): do not redirect,
            # pass saved_student to template (so form stays empty or you can re-init)
            form = StudentForm()  # reset form after saving
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = StudentForm()

    return render(request, 'courses/register_student.html', {
        'form': form,
        'saved_student': saved_student,
    })
