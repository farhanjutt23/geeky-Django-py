from django.shortcuts import render

# Create your views here.
def django_learing(self):

    stu={'stu1':{'name': 'Rahul', 'roll': 109},
         'stu2': {'name':'sonam', 'roll':2990},
         'stu3': {'name':'farhan', 'roll':899},
         'stu4': {'name': 'sajjad', 'roll':5654},     
         }
    student={'fani':stu}
    return render(self,'course/course_one.html',student)
