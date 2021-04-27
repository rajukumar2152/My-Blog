from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255 ,default="")
     phone= models.CharField(max_length=13,default="")
     email= models.CharField(max_length=100, default="")
     # content=models.TextField()
     content=RichTextField(blank=True, null=True)
     slug=models.CharField(max_length=130)



     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email
    