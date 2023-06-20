from rest_framework import serializers
from .models import Doctor,Petient,Category
from .models import Post

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=["First_Name","Last_Name","Profile_Pic","Username","Email_Id","Password","Confirm_Password","Address_line1","City","State","Pincode"]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Petient
        fields=["First_Name","Last_Name","Profile_Pic","Username","Email_Id","Password","Confirm_Password","Address_line1","City","State","Pincode"]
    
class LoginDoctorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = Doctor
        fields =['email', 'password']

class LoginPatientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = Petient
        fields =['email', 'password']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["Category"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["Title",'post_image','Category', 'Summury', 'post_content',"posted_by","Draft" ]