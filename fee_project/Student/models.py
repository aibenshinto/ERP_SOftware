
from django.db import models
from Settings.models import Companies, State, District, Qualification, Courses,MasterData

class StudentForm(models.Model):
    name = models.CharField(max_length=250)
    # Add ForeignKey fields from Settings app
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    PAYMENT_CHOICES = [
        ( 'One Time','One Time '),
        ( 'Two Time','Two Time '),
        ( 'Three Time','Three Time')
        
    ]
    payment_type = models.CharField(max_length=20, verbose_name="Installment Type",choices=PAYMENT_CHOICES)
   
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "A.Student Forms"

    


class Receipts(models.Model):
    student_form = models.ForeignKey(StudentForm, on_delete=models.CASCADE)
   
    amount = models.CharField(max_length=100)
    # Add other fields specific to Receipts

    def __str__(self):
        return f'Receipt for {self.student_form.name}'




    









