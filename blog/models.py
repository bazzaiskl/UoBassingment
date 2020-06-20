from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class CV(models.Model):
    #personal deeeeets
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    phone_number= models.CharField(max_length= 20)
    email = models.EmailField() #change not tested

    #professional deets
    objective = models.TextField()
    skills = models.TextField()
    interests  = models.TextField()
    awards = models.TextField()
    involvement = models.TextField()

    #class holders
    experience_list =[]
    education_list =[]
    reference_list =[]

    #expereince
    class experience(models.Model):
        job_title = models.CharField(max_length= 100)
        company = models.CharField(max_length= 100)
        start_year = models.DateField()
        end_year = models.DateField()
        job_description = models.TextField()

    class education(models.Model):
        program = models.CharField(max_length= 200)
        insitution = models.CharField(max_length= 100)
        start_year_ed = models.DateField()
        end_year_ed = models.DateField()
        education_description = models.TextField()

    class references(models.Model):
        ref_name = models.CharField(max_length=100)
        ref_position = models.CharField(max_length=100)
        ref_company = models.CharField(max_length=100)
        ref_contact = models.CharField(max_length=100)

    
    def new_experience(self):
        CV.experience_list.append(CV.experience)
        return CV.experience_list[0]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

