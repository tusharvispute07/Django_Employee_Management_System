from django import forms
from .models import Employee, Role, Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['dept'].widget = forms.Select(choices=[(dept.id, dept.name) for dept in Department.objects.all()])
        self.fields['role'].widget = forms.Select(choices=[(role.id, role.name) for role in Role.objects.all()])

class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'first_name', 'last_name', 'dept', 'role', 'salary', 'phone']