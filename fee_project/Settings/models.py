


from django.db import models


# Create your models here.
class Companies(models.Model):
    Company=models.CharField(max_length=250)
    
    Address1=models.CharField(max_length=500)
    
    Phone=models.CharField(max_length=100)
   
    Email=models.EmailField(max_length=100)
    
    Website=models.CharField(max_length=100)
    Active=models.BooleanField(default=True)
    

    def __str__(self):
        return self.Company
    

    class Meta:
        verbose_name_plural = "A. Company"

class State(models.Model):
    state=models.CharField(max_length=250)
    Active=models.BooleanField(default=True)
    def __str__(self):
        return self.state
    
    class Meta:
        verbose_name_plural = "B. State"

class District(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    district=models.CharField(max_length=100)


    def __str__(self):
        return self.district
    
    class Meta:
        verbose_name_plural = "C. District"
 


class Qualification(models.Model):
    Qualificationname=models.CharField(max_length=250)
    Active=models.BooleanField(default=True)
    def __str__(self):
        return self.Qualificationname
    Active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "E. Qualification"

class Courses(models.Model):
    Course=models.CharField(max_length=250)
    Coursecode = models.CharField(max_length=250)
    Amount = models.DecimalField(max_digits=10, decimal_places=2) 
    Active=models.BooleanField(default=True) 



    def __str__(self):
        return self.Course
    class Meta:
        verbose_name_plural ="F.  Course" 

class MasterData(models.Model):
    Name=models.CharField(max_length=250)
    value=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Name}"
    
    class Meta:
        verbose_name_plural ="G.  Master Data"   