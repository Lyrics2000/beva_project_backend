from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import EmailInput

class ComplainForm(forms.Form):
    profile_pic = forms.FileField(widget=forms.FileInput(
        attrs={
            "id":"files","type":'file' , "onchange":"readURL(this);", "style":"display: none;"

        }
    ))

    name = forms.CharField(
        widget=forms.TextInput(
           attrs={ 

            "type":"text", "name":"name"
           }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
           attrs={ 

            "type":"email"
           }
        )
    )
    is_university = forms.CharField(
        widget=forms.TextInput(
           attrs={ 

              "type":"radio", "checked":"checked" , "name":"student_type", "value":"University Student"
           }
        )
    )