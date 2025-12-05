# rental/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import IndividualProfile, CorporateProfile, StudioProfile

class BaseRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class IndividualRegistrationForm(BaseRegistrationForm):
    full_name = forms.CharField(required=True, max_length=100)
    phone = forms.CharField(required=True, max_length=20)
    whatsapp = forms.CharField(required=True, max_length=20)
    date_of_birth = forms.DateField(required=True)
    profile_link = forms.URLField(required=True)
    camera_system = forms.CharField(required=False, max_length=100)
    hear_about = forms.ChoiceField(required=True, choices=[
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('friend', 'Friend'),
        ('other', 'Other')
    ])
    governorate = forms.ChoiceField(required=True, choices=[
        ('Cairo', 'Cairo'),
        ('Giza', 'Giza'),
        ('Alexandria', 'Alexandria')
    ])
    city = forms.CharField(required=True, max_length=100)
    street = forms.CharField(required=True, max_length=100)
    building = forms.CharField(required=True, max_length=100)
    floor = forms.CharField(required=True, max_length=50)
    apartment = forms.CharField(required=True, max_length=50)
    professional_category = forms.ChoiceField(required=True, choices=[
        ('Photographer', 'Photographer'),
        ('Videographer', 'Videographer'),
        ('Content Creator', 'Content Creator'),
        ('Filmmaker', 'Filmmaker'),
        ('Student', 'Student'),
        ('Other', 'Other')
    ])
    portfolio_link = forms.URLField(required=True)
    id_front = forms.FileField(required=True)
    id_rear = forms.FileField(required=True)
    other_id = forms.FileField(required=True)
    agree_terms = forms.BooleanField(required=True)

    def save(self, commit=True):
        user = super().save(commit)
        IndividualProfile.objects.create(
            user=user,
            full_name=self.cleaned_data['full_name'],
            phone=self.cleaned_data['phone'],
            whatsapp=self.cleaned_data['whatsapp'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            profile_link=self.cleaned_data['profile_link'],
            camera_system=self.cleaned_data['camera_system'],
            hear_about=self.cleaned_data['hear_about'],
            governorate=self.cleaned_data['governorate'],
            city=self.cleaned_data['city'],
            street=self.cleaned_data['street'],
            building=self.cleaned_data['building'],
            floor=self.cleaned_data['floor'],
            apartment=self.cleaned_data['apartment'],
            professional_category=self.cleaned_data['professional_category'],
            portfolio_link=self.cleaned_data['portfolio_link'],
            id_front=self.cleaned_data['id_front'],
            id_rear=self.cleaned_data['id_rear'],
            other_id=self.cleaned_data['other_id']
        )
        return user

class CorporateRegistrationForm(BaseRegistrationForm):
    company_name = forms.CharField(required=True, max_length=100)
    company_address = forms.CharField(required=True, max_length=200)
    company_phone = forms.CharField(required=True, max_length=20)
    company_website = forms.URLField(required=False)
    company_social = forms.URLField(required=True)
    ceo_name = forms.CharField(required=True, max_length=100)
    ceo_phone = forms.CharField(required=True, max_length=20)
    ceo_email = forms.EmailField(required=True)
    ceo_id_front = forms.FileField(required=True)
    ceo_id_rear = forms.FileField(required=True)
    auth_name = forms.CharField(required=True, max_length=100)
    auth_phone = forms.CharField(required=True, max_length=20)
    auth_email = forms.EmailField(required=True)
    auth_id_front = forms.FileField(required=True)
    auth_id_rear = forms.FileField(required=True)
    tax_card = forms.FileField(required=True)
    commercial_reg = forms.FileField(required=True)
    agree_terms = forms.BooleanField(required=True)

    def save(self, commit=True):
        user = super().save(commit)
        CorporateProfile.objects.create(
            user=user,
            company_name=self.cleaned_data['company_name'],
            company_address=self.cleaned_data['company_address'],
            company_phone=self.cleaned_data['company_phone'],
            company_website=self.cleaned_data['company_website'],
            company_social=self.cleaned_data['company_social'],
            ceo_name=self.cleaned_data['ceo_name'],
            ceo_phone=self.cleaned_data['ceo_phone'],
            ceo_email=self.cleaned_data['ceo_email'],
            ceo_id_front=self.cleaned_data['ceo_id_front'],
            ceo_id_rear=self.cleaned_data['ceo_id_rear'],
            auth_name=self.cleaned_data['auth_name'],
            auth_phone=self.cleaned_data['auth_phone'],
            auth_email=self.cleaned_data['auth_email'],
            auth_id_front=self.cleaned_data['auth_id_front'],
            auth_id_rear=self.cleaned_data['auth_id_rear'],
            tax_card=self.cleaned_data['tax_card'],
            commercial_reg=self.cleaned_data['commercial_reg']
        )
        return user

class StudioRegistrationForm(BaseRegistrationForm):
    studio_name = forms.CharField(required=True, max_length=100)
    phone = forms.CharField(required=True, max_length=20)
    whatsapp = forms.CharField(required=True, max_length=20)
    email = forms.EmailField(required=True)
    id_front = forms.FileField(required=True)
    id_rear = forms.FileField(required=True)
    profile_link = forms.URLField(required=True)
    hear_about = forms.ChoiceField(required=True, choices=[
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('friend', 'Friend'),
        ('other', 'Other')
    ])
    governorate = forms.ChoiceField(required=True, choices=[
        ('Cairo', 'Cairo'),
        ('Giza', 'Giza'),
        ('Alexandria', 'Alexandria')
    ])
    agree_terms = forms.BooleanField(required=True)

    def save(self, commit=True):
        user = super().save(commit)
        StudioProfile.objects.create(
            user=user,
            studio_name=self.cleaned_data['studio_name'],
            phone=self.cleaned_data['phone'],
            whatsapp=self.cleaned_data['whatsapp'],
            email=self.cleaned_data['email'],
            id_front=self.cleaned_data['id_front'],
            id_rear=self.cleaned_data['id_rear'],
            profile_link=self.cleaned_data['profile_link'],
            hear_about=self.cleaned_data['hear_about'],
            governorate=self.cleaned_data['governorate']
        )
        return user
