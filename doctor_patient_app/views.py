from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import mixins,generics,status
from rest_framework.request import Request
from .models import Doctor,Petient,Category,Post
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializer import PostSerializer,DoctorSerializer,PatientSerializer,LoginPatientSerializer,LoginDoctorSerializer,CategorySerializer
from .form import DoctorForm,PatientForm,PatientLoginForm,DoctorLoginForm,PostForm

# Create your views here.
#Create Sign up view for Doctor
class DoctorRegisterView(generics.CreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    def get(self, request:Request, *args, **kwargs):
        form = DoctorForm()
        return render(request, 'Doctor_signup.html', {'form': form})
    
    def post(self, request:Request,*args,**kwargs):
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            password = form.data.get('Password')
            confirm_password = form.data.get('Confirm_Password')
        
            if password != confirm_password:
                error_message = "Password and Confirm Password do not match"
                return render(request, 'Doctor_signup.html', {'form': form, 'error_message': error_message})
            else:
                patient = form.save()
                message="Registered Successufylly!!!"
  
                return render(request, 'Doctor_signup.html', {'form': form,"message":message})
        else:
            response = {"message": "Invalid data or registration failed"}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        
#create Patient Sign Up View
class PatientRegisterView(generics.CreateAPIView):
    serializer_class = PatientSerializer
    queryset = Petient.objects.all()

    def get(self, request:Request, *args, **kwargs):
        form = PatientForm()
        return render(request, 'Patient_signup.html', {'form': form})
    
    def post(self, request:Request,*args,**kwargs):
        form = PatientForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            password = form.data.get('Password')
            confirm_password = form.data.get('Confirm_Password')
        
            if password != confirm_password:
                error_message = "Password and Confirm Password do not match"
                return render(request, 'Patient_signup.html', {'form': form, 'error_message': error_message})
            else:
                patient = form.save()
                message="Registered Successufylly!!!"
                return render(request, 'Patient_signup.html', {'form': form,"message":message})
        else:
            response = {"message": "Invalid data or registration failed"}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

#create Login View for Doctor 
class DoctorLoginView(generics.CreateAPIView):
    serializer_class=LoginDoctorSerializer
    queryset=Doctor.objects.all()
    def get(self, request:Request, *args, **kwargs):
        form = DoctorLoginForm()
        return render(request, 'Doctor_login.html', {'form': form})
    
    def post(self, request:Request,format=None):
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            data=request.data
            email=data.get("email",None)
            password=data.get("password",None)
            user=Doctor.objects.filter(Email_Id=email,Password=password)
            
            if user:
                form=PostForm()
                user2=Doctor.objects.get(Email_Id=email,Password=password)
                data_for_user=Post.objects.filter(posted_by=user2.id)
                user_data=user2.id
                return render(request,"ctegory.html",{"form":form,"data_for_user":data_for_user,"user_data":user_data})
            else:
                form1=DoctorLoginForm()
                message="User Does Not Exist Or Check Email id and Password"
                return render(request,"Doctor_login.html",{"form":form1,"message":message})
            
        else: 
            response={
                "message":"Not Valid User Information",
               
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)
        
#create login view for patient   
class PatientLoginView(generics.CreateAPIView):
    serializer_class=LoginPatientSerializer
    queryset=Petient.objects.all()
    def get(self, request:Request, *args, **kwargs):
        form = PatientLoginForm()
        return render(request, 'Patient_login.html', {'form': form})
    
    def post(self, request:Request,format=None):
        form = PatientLoginForm(request.POST)
        
        if form.is_valid():
            
            data=request.data
            email=data.get("email",None)
            password=data.get("password",None)
            #check wether the data present in the database
            user=Petient.objects.filter(Email_Id=email,Password=password)
            if user:
                message="login succcessfully,Select Option To View Post By Category Wise"
                
                return render(request,"select_category_patient.html",{"message":message})
            else:
                form=PatientLoginForm()
                message="User Does Not Exist Or Check Email id and Password"
                return render(request,"Patient_login.html",{"form":form,"message":message})
        else:
            
            response={
                "message":"Not Valid User Information",
               
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)
        
    
def register_doctor(request):
    form=DoctorForm()
    return render(request,'selectuser.html')




class CategorySelectView(generics.CreateAPIView):
    serializer_class = PostSerializer

    def get(self, request: Request, *args, **kwargs):
        form = PostForm()
        user_data = request.GET.get('user_data')  # Retrieve the user_data from the request parameters
        return render(request, 'ctegory.html', {'form': form, 'user_data': user_data})

    def post(self, request: Request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            id_value = form.cleaned_data.get('posted_by')
            data_for_user = Post.objects.filter(posted_by=id_value)
            return render(request, "extracted_data_post.html", {"data_for_user": data_for_user})
        else:
            return Response(data={"data": form.errors})
        
def Mental_Health(request):
    data_for_user=Post.objects.filter(Category="MentalHealth",Draft=False)
    return render(request,"category_data.html",{"data_for_user":data_for_user})

def Heart_Disease(request):
    data_for_user=Post.objects.filter(Category="HeartDiasese",Draft=False)
    return render(request,"category_data.html",{"data_for_user":data_for_user})

def Covid19(request):
    data_for_user=Post.objects.filter(Category="Covid19",Draft=False)
    return render(request,"category_data.html",{"data_for_user":data_for_user})

def Immunization(request):
    data_for_user=Post.objects.filter(Category="Immunization",Draft=False)
    return render(request,"category_data.html",{"data_for_user":data_for_user})