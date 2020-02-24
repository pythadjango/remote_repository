from django.shortcuts import render
from enquiryformapp.models import EnquieyData
from enquiryformapp.forms import EnquiryForm
from django.http.response import HttpResponse
def Enquieryview(request):
    if request.method=="POST":
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            name=request.POST.get('name')
            mobile=request.POST.get("mobile")
            email=request.POST.get("email")
            courses=eform.cleaned_data.get('courses')
            trainers=eform.cleaned_data.get('trainers')
            branches=eform.cleaned_data.get('branches')
            gender=eform.cleaned_data.get('gender')
            start_date=eform.cleaned_data.get('start_date')
            data=EnquieyData(
                name=name,
                mobile=mobile,
                email=email,
                courses=courses,
                trainers=trainers,
                branches=branches,
                gender=gender,
                start_date=start_date
            )
            data.save()
            eform=EnquiryForm()
            return render(request,'enquiery.html',{'eform':eform})
        else:
            return HttpResponse("User Missing value")
    else:
        eform=EnquiryForm()
        return render(request,'enquiery.html',{'eform':eform})