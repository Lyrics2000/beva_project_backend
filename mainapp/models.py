from django.db import models
import random
import os
from authentification.models import User

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






# Create your models here.
