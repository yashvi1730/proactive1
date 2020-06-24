from django.shortcuts import render
from main.models import Patient,Medical_History,Schedule,Pcos_History,Purpose_of_visit,Test,Mensis
from main.forms import PatientForm,MedicalHistoryForm,ScheduleForm,Pcos_HistoryForm,Purpose_of_visitForm,TestForm,MensisForm
from django.shortcuts import redirect



# Create your views here.

def form_view(request):
    form = PatientForm()
    if request.method == 'POST':
        form =PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/pcos_history')

    context={
        "form":form,
    }

    return render(request,'main/home.html',context)

def medical_history_form(request):
    form1 = MedicalHistoryForm()
    if request.method == 'POST':
        form1 =MedicalHistoryForm(request.POST)
        if form1.is_valid():
            form1.save()
        return redirect('/mensis')

    context={
        "form1":form1,
    }

    return render(request,'main/medical_history.html',context)

def schedule_form(request):
    form2 = ScheduleForm()
    if request.method == 'POST':
        form2 =ScheduleForm(request.POST)
        if form2.is_valid():
            form2.save()
        return redirect('/lastpage')

    context={
        "form2":form2,
    }

    return render(request,'main/schedule.html',context)

def pcos_history_form(request):
   form3 = Pcos_HistoryForm()
   if request.method == 'POST':
        form3 =Pcos_HistoryForm(request.POST)
        
        if form3.is_valid():
            form3.save()
            print('valid')
            return redirect('/medical_history')
        else:
            print('not valid')
   context={
        "form3":form3,
    }

   return render(request,'main/pcos_history.html',context)

    
def purpose_form(request):
    form4 = Purpose_of_visitForm()
    if request.method == 'POST':
        form4 =Purpose_of_visitForm(request.POST)
        if form4.is_valid():
            form4.save()
        return redirect('/schedule')

    context={
        "form4":form4,
    }

    return render(request,'main/purpose.html',context)



def test(request):
    form6 = TestForm()
    if request.method == 'POST':
        form6 =TestForm(request.POST)
        if form6.is_valid():
            form6.save()
        return redirect('/test')

    context={
        "form6":form6,
    }

    return render(request,'main/test.html',context)


def mensis(request):
    form7 = MensisForm()
    if request.method == 'POST':
        form7 =MensisForm(request.POST)
        if form7.is_valid():
            form7.save()
        return redirect('/purpose')

   
    context={
        "form7":form7,
    }

    return render(request,'main/mensis.html',context)

def lastpage(request):
    appoint=Schedule.objects.all().last()
    print(appoint)
    context={
      "appoint":appoint
    }

    return render(request,'main/lastpage.html',context)