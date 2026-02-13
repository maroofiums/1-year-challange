from django.shortcuts import render, redirect, get_object_or_404
from .utils import calculate_grade
from .models import Student


def student_list(request):
    query = request.GET.get('query', '')
    grade_filter = request.GET.get('grade', '')
    sort = request.GET.get('sort', 'grade')

    students = Student.objects.all()

    if query:
        students = students.filter(name__icontains=query)

    if grade_filter:
        students = students.filter(grade__iexact=grade_filter)

    if sort == 'grade_desc':
        students = students.order_by('-grade')
    else:
        students = students.order_by('grade')

    return render(request, 'student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        marks = request.POST.get('marks')

        grade = calculate_grade(float(marks))

        Student.objects.create(
            name=name,
            age=age,
            marks=marks,
            grade=grade
        )

        return redirect('student_list')

    return render(request, 'add_student.html')




def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.marks = request.POST.get("marks")

        # Important: convert to float/int
        student.grade = calculate_grade(float(student.marks))

        student.save()
        return redirect("student_list")

    return render(request, "update_student.html", {"student": student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')
