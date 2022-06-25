from .models import Employee
from django import forms


class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name','mobile','employee_id','email_id','position']

        labels={
            'full_name': 'FULL NAME',
            'mobile' : 'MOBILE',
            'employee_id' : 'EMPLOYEE-ID',
            'email_id' : 'EMAIL-ID',
            'position' : 'POSITION' }



        widgets = {
            'full_name' : forms.TextInput(attrs = {'placeholder': 'full name'}),
            'mobile' : forms.TextInput(attrs = {'placeholder': 'mobile no.'}),
            'employee_id' : forms.TextInput(attrs = {'placeholder': 'employee id'}),
            'email_id' : forms.EmailInput(attrs = {'placeholder': 'email id'}),
        }

    def __init__(self,*args,**kwargs):
        super(Employee_form,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['full_name'].required = True
        self.fields['mobile'].required = True
        self.fields['employee_id'].required = True
        self.fields['email_id'].reqiured = True
        self.fields['position'].required = True
