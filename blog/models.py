from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Post(models.Model):
    sno= models.AutoField(primary_key=True)
    title= models.CharField(max_length=130,default="")
    # content= models.TextField()  #yaha text liya hain ek dabba type ban jayega 
    content=RichTextField(blank=True, null=True)
    author= models.CharField(max_length=100, default="")
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
   
  

    def __str__(self):
        return "Title is " + self.title + ' by' + self.author
    objects = models.Manager()
    

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    # objects = models.Manager()