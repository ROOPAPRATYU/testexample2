from django.urls import path
from .views import DoctorRegisterView,PatientRegisterView,DoctorLoginView,PatientLoginView,register_doctor,CategorySelectView, Mental_Health,Heart_Disease,Covid19,Immunization

urlpatterns=[
    path("doctor_register/",DoctorRegisterView.as_view(),name="doctor_register"),
    path("patient_register/",PatientRegisterView.as_view(),name="patient_register"),
    path("doctor_login/",DoctorLoginView.as_view(),name="doctor_login"),
    path("patient_login/",PatientLoginView.as_view(),name="patient_login"),

    path("",register_doctor,name="doc_reg"),
    path("categoryselect/",CategorySelectView.as_view(),name="categoryselect"),
    path("Mental_Health/", Mental_Health,name="Mental_Health"),
    path("Heart_Disease/",Heart_Disease,name="Heart_Disease"),
    path("Covid19/",Covid19,name="Covid19"),
    path("Immunization/",Immunization,name="Immunization")

]