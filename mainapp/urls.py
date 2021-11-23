from django.urls import path

from .views import (delete_complaint, index,success,confirmer,home_student,home_committee,student_department,
doc_upload,
choose_custome,
previous_complaints,
complaints_detailed,
delete_complaint,
complaints_edit,
follow_ups)
app_name = "mainapp"
urlpatterns = [
    path('', index,name="index"),
    path('thankyou/',success,name="thankyou"),
    path("confirmer/",confirmer,name="confirmer"),
    path("home_student/",home_student,name="student"),
    path('home_committee',home_committee,name="committee"),
    path('student_department/',student_department,name="student_department"),
    path('doc_upload/',doc_upload,name="document_upload"),
    path('choose_custome/',choose_custome,name="choose_custome"),
    path('previous_complaints/',previous_complaints,name="previous"),
    path('complaints_detailed/<id>',complaints_detailed,name="post_detailed"),
    path('delete_complaint/',delete_complaint,name="delete_complain"),
    path('complaints_edit/<id>',complaints_edit,name="post_edit"),
    path('follow_up/',follow_ups,name="follow_up")
    
]