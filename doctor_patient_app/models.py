from django.db import models

# Create your models here.
class Doctor(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Profile_Pic=models.ImageField(upload_to="profile_pic_doc",null=True,default=None)
    Username=models.CharField(max_length=100)
    Email_Id=models.EmailField(max_length=100)
    Password=models.CharField(max_length=100)
    Confirm_Password=models.CharField(max_length=100)
    Address_line1=models.CharField(max_length=200)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Pincode=models.IntegerField()

    def _str__(self) -> str:
        return self.Username


# Create your models here.
class Petient(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Profile_Pic=models.ImageField(upload_to="profile_pic_doc")
    Username=models.CharField(max_length=100)
    Email_Id=models.EmailField(max_length=100)
    Password=models.CharField(max_length=100)
    Confirm_Password=models.CharField(max_length=100)
    Address_line1=models.CharField(max_length=200)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Pincode=models.IntegerField()

    def _str__(self)->str:
        return self.Email_Id
    
class Category(models.Model):
    category_choices=(("MentalHealth","MentalHealth"),("HeartDiasese","HeartDisease"),('Covid19',"Covid19"),("Immunization","Immunization"))
    Category=models.CharField(choices=category_choices,max_length=100)


    def __str__(self) -> str:
        return self.Category
    
class Post(models.Model):
    Title=models.CharField(max_length=100,default=None,null=True)
    post_image = models.ImageField(upload_to="Posts", null=True)
    category_choices=(("MentalHealth","MentalHealth"),("HeartDiasese","HeartDisease"),('Covid19',"Covid19"),("Immunization","Immunization"))
    Category=models.CharField(choices=category_choices,max_length=100)
    posted_by = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='Posts')
    Summury=models.CharField(max_length=200,default=None,null=True)
    post_content = models.TextField(null=True)
    Draft=models.BooleanField(default=False)
    
    post_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.posted_by.Username
