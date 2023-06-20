from django import forms
from rest_framework import serializers
from .models import Category,Post,Doctor
from .serializer import PostSerializer,DoctorSerializer,PatientSerializer,LoginDoctorSerializer,LoginPatientSerializer,CategorySerializer

class DoctorForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = DoctorSerializer()
        self.fields = {
            field_name: self.get_form_field(field_data)
            for field_name, field_data in self.serializer.fields.items()
        }

    def get_form_field(self, field_data):

        if isinstance(field_data, serializers.ImageField):
            return forms.ImageField(label=field_data.label)
        elif isinstance(field_data, serializers.IntegerField):
            return forms.IntegerField(label=field_data.label)
        elif isinstance(field_data,serializers.BooleanField):
            return forms.BooleanField(label=field_data.label)
        elif isinstance(field_data,serializers.BooleanField):
            return forms.EmailField(label=field_data.label)
    
        else:
            return forms.CharField(label=field_data.label)

    

    def save(self):
        data = self.cleaned_data

        # Create an instance of the serializer with the form data
        serializer = DoctorSerializer(data=data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data and return the doctor object
            return serializer.save()

        # If data is not valid, raise an exception or handle the error as desired
        raise forms.ValidationError(serializer.errors)

class PatientForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = PatientSerializer()
        self.fields = {
            field_name: self.get_form_field(field_data)
            for field_name, field_data in self.serializer.fields.items()
        }

    def get_form_field(self, field_data):

        if isinstance(field_data, serializers.ImageField):
            return forms.ImageField(label=field_data.label)
        elif isinstance(field_data, serializers.IntegerField):
            return forms.IntegerField(label=field_data.label)
        elif isinstance(field_data,serializers.BooleanField):
            return forms.BooleanField(label=field_data.label)
        elif isinstance(field_data,serializers.BooleanField):
            return forms.EmailField(label=field_data.label)
    
        else:
            return forms.CharField(label=field_data.label)

    

    def save(self):
        data = self.cleaned_data

        # Create an instance of the serializer with the form data
        serializer = PatientSerializer(data=data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data and return the doctor object
            return serializer.save()

        # If data is not valid, raise an exception or handle the error as desired
        raise forms.ValidationError(serializer.errors)
#create form for Doctor Login  
class DoctorLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = LoginDoctorSerializer()
        self.fields = {
            field_name: self.get_form_field(field_data)
            for field_name, field_data in self.serializer.fields.items()
        }

    def get_form_field(self, field_data): 
        if isinstance(field_data,serializers.BooleanField):
            return forms.EmailField(label=field_data.label)
        else:
            return forms.CharField(label=field_data.label)
    def save(self):
        data = self.cleaned_data
        # Create an instance of the serializer with the form data
        serializer = DoctorSerializer(data=data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data and return the doctor object
            return serializer.save()

        # If data is not valid, raise an exception or handle the error as desired
        raise forms.ValidationError(serializer.errors)
    
#create form for Doctor Login  
class PatientLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = LoginPatientSerializer()
        self.fields = {
            field_name: self.get_form_field(field_data)
            for field_name, field_data in self.serializer.fields.items()
        }

    def get_form_field(self, field_data): 
        if isinstance(field_data,serializers.BooleanField):
            return forms.EmailField(label=field_data.label)
        else:
            return forms.CharField(label=field_data.label)
    def save(self):
        data = self.cleaned_data
        # Create an instance of the serializer with the form data
        serializer = PatientSerializer(data=data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data and return the doctor object
            return serializer.save()

        # If data is not valid, raise an exception or handle the error as desired
        raise forms.ValidationError(serializer.errors)

class PostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = PostSerializer()
        for field_name, field in self.serializer.fields.items():
            if field_name == 'Category':
                self.fields[field_name] = forms.ChoiceField(
                    choices=Post.category_choices,
                    label=field.label
                )
            else:
                self.fields[field_name] = self.get_form_field(field)

    def get_form_field(self, field):
        if isinstance(field, serializers.ImageField):
            return forms.ImageField(label=field.label)
        elif isinstance(field, serializers.IntegerField):
            return forms.IntegerField(label=field.label)
        elif isinstance(field, serializers.BooleanField,):
            return forms.BooleanField(label=field.label,required=False)
        elif isinstance(field, serializers.EmailField):
            return forms.EmailField(label=field.label)
        else:
            return forms.CharField(label=field.label)

    def save(self):
        data = self.cleaned_data
        posted_by = data.get("posted_by")
        if posted_by:
            data["posted_by"] = posted_by
        # Create an instance of the serializer with the form data
        serializer = PostSerializer(data=data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data and return the post object
            return serializer.save()

        # If data is not valid, raise an exception or handle the error as desired
        raise forms.ValidationError(serializer.errors)