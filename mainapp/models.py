from django.db import models
import random
import os
from authentification.models import User
from django.shortcuts import reverse

# # Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "inqury/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Inqury(BaseModel):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    commitee_id = models.CharField(max_length=255)
    inqury_details =  models.TextField()
    inqury_image =  models.ImageField(upload_to=upload_image_path,blank=True,null=True)

    def __str__(self):
        return str(self.user_id)


class Feedback(BaseModel):
    inqury_id =  models.ForeignKey(Inqury,on_delete=models.CASCADE)
    feeback_details =  models.TextField()

    def __str__(self):
        return str(self.inqury_id)


class Response(BaseModel):
    feedback_id = models.ForeignKey(Feedback,on_delete=models.CASCADE)
    response_details =  models.TextField()

    def __str__(self):
        return str(self.feedback_id)



class ComplaintsDetails(models.Model):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    name =  models.CharField(max_length=255,blank=True,null=True)
    profile_image = models.ImageField(upload_to=upload_image_path,blank=True,null = True)
    email =  models.EmailField(blank=True,null=True)
    university =  models.CharField(max_length=255,blank=True,null=True)
    course =  models.CharField(max_length=255,blank=True,null=True)
    reg_no =  models.CharField(max_length=255,blank=True,null=True)
    department =  models.CharField(max_length=255,blank=True,null=True)
    complaint =  models.TextField(blank=True,null=True)
    file =  models.FileField(upload_to = upload_image_path,blank=True,null=True)
    send_sms =  models.BooleanField(default=False,blank=True,null=True)
    send_email =  models.BooleanField(default=False,blank=True,null=True)
    submitted = models.BooleanField(default=False)
    reviewed =  models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("mainapp:post_detailed", kwargs={
            'id': self.id
        })
        
    def get_absolute_url_edit(self):
        return reverse("mainapp:post_edit", kwargs={
            'id': self.id
        })









# Create your models here.
