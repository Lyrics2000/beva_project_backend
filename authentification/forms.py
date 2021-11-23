from django import forms

class SignINForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
           "type":"text", "class":"form-control" , "placeholder":"Enter Your Email","required":""

        }
    ))

    password = forms.CharField(
        widget=forms.PasswordInput(
           attrs={ "type":"password", "class":"form-control pe-5" , "placeholder":"Enter Password",
            "required":""}
        )
    )




class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "type":"text", "class":"form-control", "placeholder":"Enter Username",  "required":""
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
             "type":"text", "class":"form-control", "placeholder":"Enter First Name",  "required":""

        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
           "type":"text", "class":"form-control", "placeholder":"Enter Last Name",  "required":""

        }
    ))

    phone = forms.CharField(widget=forms.TextInput(
        attrs={
             "type":"text", "class":"form-control", "placeholder":"Enter Phone Number",  "required":""

        }
    ))

    type = forms.CharField(widget=forms.TextInput(
        attrs={
             "type":"text", "class":"form-control", "placeholder":"Enter User Type",  "required":""

        }
    ))

    department = forms.CharField(widget=forms.TextInput(
        attrs={
             "type":"text", "class":"form-control", "placeholder":"Enter User Type",  "required":""

        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
             "type":"email", "class":"form-control", "placeholder":"Enter Email",  "required":""

        }
    ))

    password = forms.CharField(
        widget=forms.PasswordInput(
           attrs={ 
                "type":"password", "class":"form-control", "placeholder":"Enter Password",  "required":""
            }
        )
    )

