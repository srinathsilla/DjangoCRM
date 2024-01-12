from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="",max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
    last_name = forms.CharField(label="",max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    '''
    In the context of Django forms, a Meta class inside a Form or ModelForm subclass is used to specify metadata about the form. This can include things like the model the form is associated with (model = User), the fields to include in the form (fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')), and other options.
    '''
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

        #username, password1, password are customizable through class instance by passing keyword arguments whereas email, firstname, lastname are not
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     username_placeholder = kwargs.get('username_placeholder', 'User Name')
        #     self.fields['username'].widget.attrs['placeholder'] = username_placeholder

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True,label="",widget=forms.widgets.TextInput(attrs={'placeholder':"First Name", 'class':'form-control'}))
    last_name = forms.CharField(required=True,label="",widget=forms.widgets.TextInput(attrs={'placeholder':"Last Name", 'class':'form-control'}))
    email = forms.CharField(required=True,label="",widget=forms.widgets.TextInput(attrs={'placeholder':"Email", 'class':'form-control'}))
    phone = forms.CharField(required=True,label="",widget=forms.widgets.TextInput(attrs={'placeholder':"Phone", 'class':'form-control'}))
    address = forms.CharField(required=True,label="",widget=forms.widgets.TextInput(attrs={'placeholder':"Address", 'class':'form-control'}))
    city = forms.CharField(required=True,label="",widget=forms.widgets.TextInput(attrs={'placeholder':"City", 'class':'form-control'}))
    state = forms.CharField(required=True,label="",widget=forms.widgets.TextInput(attrs={'placeholder':"State", 'class':'form-control'}))
    zipcode = forms.CharField(required=True,label="",widget=forms.widgets.TextInput(attrs={'placeholder':"Zipcode", 'class':'form-control'}))

    class Meta:
        model = Record
        exclude = ("user",)