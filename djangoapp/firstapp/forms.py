"""forms"""
from django import forms
from .models import request_info

class reg_info(forms.ModelForm):
    """Create your models here."""
    # firstname=forms.CharField(max_length=50)
    # middlename=forms.CharField(max_length=50)
    # lastname=forms.CharField(max_length=50)
    # dob=forms.DateField()
    # gender=forms.CharField(max_length=50)
    # nationality=forms.CharField(max_length=50)
    # city=forms.CharField(max_length=50)
    # state=forms.CharField(max_length=50)
    # pincode=forms.IntegerField()
    # qualification=forms.CharField(max_length=50)
    # salary=forms.IntegerField()
    # panid=forms.CharField(max_length=50)
    # #request_date=forms.DateField(default=timezone.now())
    class Meta:
        model = request_info
        fields = '__all__'
        # fields = ['firstname', 'middlename', 'lastname', 'dob', 'gender',
        # 'nationality', 'city', 'state', 'pin', 'qualification', 'salary', 'panid']
