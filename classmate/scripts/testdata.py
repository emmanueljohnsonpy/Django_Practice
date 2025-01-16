from student.models import department, studentData
from django.db import connection

def run():
    # std=studentData.objects.all()
    # for i in std:
    #     print(i.id)
    #     print(i.name)
    #     print(i.rollno)
    #     print(i.gender)
    #     print(i.place)
    #     print(i.fees_amt)
    #     print(i.department)
    std=studentData.objects.first()
    print(std)
    print(std.rollno)

    print()
    print(connection.queries)