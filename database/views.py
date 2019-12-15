from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import personal_information
from .models import internship_history
from .models import qualifications_on_entry
from .models import past_employees
from .models import employment_history
from .models import employee_degrees
from .models import countries

@csrf_exempt
def new(request):
   
    if request.method == 'POST':
        new=personal_information()
        new.First_Name = request.POST.get('First_Name')
        new.Last_Name = request.POST.get('Last_Name')
        new.Other_Name = request.POST.get('Other_Name')
        new.save()

        context = {
            'First_Name': new.First_Name,
            'Last_Name': new.Last_Name,
            'Other_Name': new.Other_Name
        }
        

        return render(request, 'database/new.html', {})
    

    else:
        return render(request, 'database/new.html', {})
        

def home(request):
    return render(request, 'database/home.html', {})


def homex(request):
    return render(request, 'database/homex.html', {})



def login(request):
    return render(request, 'database/login.html', {})


def search(request):
    Personal_Information = personal_information.objects.all()
    if request.method == 'POST':
      search_query = request.POST.get('search_item', '')      
      Personal_Information = personal_information.objects.filter(First_Name__icontains= search_query).order_by('InternID') | personal_information.objects.filter(Last_Name__icontains= search_query).order_by('InternID')
      return render(request, 'database/search.html', {'Personal_Information': Personal_Information})

    else:
         # return render(request, 'database/home.html', {})
         return HttpResponse('Nothing to display')



def searchx(request):
    Personal_Information = past_employees.objects.all()
    if request.method == 'POST':
      search_query = request.POST.get('search_item', '')       
      Past_Employees = past_employees.objects.filter(First_Name__icontains= search_query).order_by('PastEmployeeID') | past_employees.objects.filter(Last_Name__icontains= search_query).order_by('PastEmployeeID')
      return render(request, 'database/searchx.html', {'Past_Employees': Past_Employees})

    else:
         # return render(request, 'database/homex.html', {})
         return HttpResponse('Nothing to display')


def view(request, key):
    detail = personal_information.objects.get(InternID=key)
    result = internship_history.objects.filter(InternID=key)
    query_set = qualifications_on_entry.objects.filter(InternID=key)
    return render(request, 'database/view.html', {'personal_information': detail, 'internship_history': result, 'qualifications_on_entry': query_set})


def viewx(request, keyx):
    detail = past_employees.objects.get(PastEmployeeID=keyx)
    result = employment_history.objects.filter(PastEmployeeID=keyx)
    query_set = employee_degrees.objects.filter(PastEmployeeID=keyx)
    query_setx = countries.objects.filter(PastEmployeeID=keyx)
    return render(request, 'database/viewx.html', {'past_employees': detail, 'employment_history': result, 'employee_degrees': query_set, 'countries': query_setx})


   
def edit_record(request, key): 
    detail = personal_information.objects.get(InternID=key)
    result = internship_history.objects.filter(InternID=key)
    query_set = qualifications_on_entry.objects.filter(InternID=key)
    return render(request, 'database/edit.html', {'personal_information': detail, 'internship_history': result, 'qualifications_on_entry': query_set})


def edit_intern_history(request, key, keyy):
    detail = personal_information.objects.get(InternID=keyy)
    result = internship_history.objects.get(HistoryID=key)
    return render(request, 'database/edit_internhistoryform.html', {'internship_history': result, 'personal_information': detail})



def edit_intern_qualification(request, key, keyy):
    detail = personal_information.objects.get(InternID=keyy)
    query_set = qualifications_on_entry.objects.get(QualificationID=key)
    return render(request, 'database/edit_internqualificationform.html', {'qualifications_on_entry': query_set, 'personal_information': detail})



def edit_recordx(request, keyx): 
    detail = past_employees.objects.get(PastEmployeeID=keyx)
    result = employment_history.objects.filter(PastEmployeeID=keyx)
    query_set = employee_degrees.objects.filter(PastEmployeeID=keyx)
    query_setx = countries.objects.filter(PastEmployeeID=keyx)
    return render(request, 'database/editx.html', {'past_employees': detail, 'employment_history': result, 'employee_degrees': query_set, 'countries': query_setx})




def edit_xemployee_history(request, keyx, keyyx):
    detail = past_employees.objects.get(PastEmployeeID=keyyx)
    result = employment_history.objects.get(EmploymentHistoryID=keyx)
    return render(request, 'database/edit_xemployeehistoryform.html', {'employment_history': result, 'past_employees': detail})



def edit_xemployee_degrees(request, keyx, keyyx):
    detail = past_employees.objects.get(PastEmployeeID=keyyx)
    query_set = employee_degrees.objects.get(DegreeID=keyx)
    return render(request, 'database/edit_xemployeedegreesform.html', {'employment_degrees': query_set, 'past_employees': detail})



def edit_xemployee_countries(request, keyx, keyyx):
    detail = past_employees.objects.get(PastEmployeeID=keyyx)
    result_set = countries.objects.get(CountriesID=keyx)
    return render(request, 'database/edit_xemployeecountriesform.html', {'employment_countries': result_set, 'past_employees': detail})




def update_record(request, key):
    det = personal_information.objects.get(InternID=key)
    res = internship_history.objects.filter(InternID=key)
    sett = qualifications_on_entry.objects.filter(InternID=key)
    if request.method == 'POST':
        det.First_Name = request.POST.get('two')  
        det.Last_Name = request.POST.get('four') 
        det.Other_Name = request.POST.get('six')  
        #det.Date_of_Birth = request.POST.get('ten') 
        det.Gender = request.POST.get('eight')
        det.Nationality = request.POST.get('twelve')
        det.Email = request.POST.get('fourteen')
        det.Home_Telephone = request.POST.get('one')
        det.Mobile_Telephone = request.POST.get('three')
        det.Permanent_Address_Line1 = request.POST.get('five')
        det.Permanent_Address_Line2 = request.POST.get('seven')
        det.City = request.POST.get('nine')
        det.Country = request.POST.get('eleven')
        det.Current_Address_Line1 = request.POST.get('thirteen')
        det.Current_Address_Line2 = request.POST.get('fifteen')
        det.Documents = request.POST.get('sixteen')
        det.save()
        return HttpResponseRedirect('/database/edit_record/%s/' % key)



def update_intern_history(request, key, keyy):
    res = internship_history.objects.get(HistoryID=key)
    if request.method == 'POST':
        res.Type_of_Internship = request.POST.get('TypeofInternship')
        res.Area_Assigned = request.POST.get('Area') 
        res.Location = request.POST.get('Location') 
        res.Supervisor_name = request.POST.get('Supervisor') 
        #res.Start_date = request.POST.get('Start') 
        #res.Stop_date = request.POST.get('Stop') 
        res.Paid_Period = request.POST.get('PaidPeriod') 
        res.Stipend_cost_per_month = request.POST.get('Stipend') 
        res.Accomodation_cost_per_month = request.POST.get('Accomodation') 
        res.Air_Fare = request.POST.get('AirFare') 
        res. Comments = request.POST.get('Comments')
        res.save() 
        
        return HttpResponseRedirect('/database/edit_record/%s/' % keyy)





def update_intern_qualification(request, key, keyy):
    sett = qualifications_on_entry.objects.get(QualificationID=key)
    if request.method == 'POST':
        sett.Name_of_Institution = request.POST.get('NameofInstitution') 
        sett.Type_of_Institution = request.POST.get('TypeofInstitution') 
        sett.Level_Attained = request.POST.get('Level') 
        #sett.Year_Attained = request.POST.get('Year') 
        sett.Grade = request.POST.get('Grade') 
        sett.Experience = request.POST.get('Experience')
        sett.save()

        return HttpResponseRedirect('/database/edit_record/%s/' % keyy)






def update_recordx(request, keyx):
    det = past_employees.objects.get(PastEmployeeID=keyx)
    res = employment_history.objects.filter(PastEmployeeID=keyx)
    sett = employee_degrees.objects.filter(PastEmployeeID=keyx)
    output = countries.objects.filter(PastEmployeeID=keyx)
    if request.method == 'POST':
        det.File_Number = request.POST.get('two')
        det.Title = request.POST.get('four')
        det.First_Name = request.POST.get('six')
        det.Middle_Name = request.POST.get('ten') 
        det.Last_Name = request.POST.get('eight')  
        det.Gender = request.POST.get('twelve')
        #det.Date_of_Birth = request.POST.get('fourteen') 
        det.Nationality = request.POST.get('sixteen')
        #det.Date_of_Employment = request.POST.get('three')
        det.Place_of_Recruitment = request.POST.get('five')
        det.Qualifications_on_Entry = request.POST.get('twenty')
        det.Highest_Level_of_Education = request.POST.get('eighteen')
        #det.Date_of_Departure = request.POST.get('seven')
        det.Reason_for_Departure = request.POST.get('nine')
        det.Summary_of_Performance = request.POST.get('fifteen')
        det.Summary_of_Performance1 = request.POST.get('seventeen')
        det.Summary_of_Performance2 = request.POST.get('nineteen')
        det.Summary_of_Performance3 = request.POST.get('twentyone')
        det.Summary_of_Performance4 = request.POST.get('twentythree')
        det.Special_Comments_Disciplinary_or_Commendation = request.POST.get('twentyfive')
        det.Final_Salary = request.POST.get('eleven')
        det.Final_Allowance = request.POST.get('thirteen')
        det.Job_Status = request.POST.get('one')
        det.Verified = request.POST.get('twentysix')
        det.Verified_By = request.POST.get('twentyseven')
        #det.Verified_Date = request.POST.get('twentynine')
        det.Created_By = request.POST.get('twentytwo')
        #det.Created_Date = request.POST.get('twentyfour')
        det.Remarks = request.POST.get('twentyeight')
        det.save()
        return HttpResponseRedirect('/database/edit_recordx/%s/' % keyx)





def update_xemployee_history(request, keyx, keyyx):
    res = employment_history.objects.get(EmploymentHistoryID=keyx)
    if request.method == 'POST':
        res.Job_Title = request.POST.get('JobTitle')
        res.Job_Period = request.POST.get('JobPeriod')
        res.Job_Description = request.POST.get('JobDescription')
        res.Achievements = request.POST.get('Achievement')
        res.Salary = request.POST.get('salary')
        res.Job_Level = request.POST.get('JobLevel')
        res.Job_Step = request.POST.get('JobStep')
        #res.Start_date = request.POST.get('Start')
        #res.End_date = request.POST.get('End')
        res.save()
        return HttpResponseRedirect('/database/edit_recordx/%s/' % keyyx)





def update_xemployee_degrees(request, keyx, keyyx):
    sett = employee_degrees.objects.get(DegreeID=keyx)
    if request.method == 'POST':
        sett.Degree_Acronym = request.POST.get('DegreeAcronym')
        sett.Degree_Name = request.POST.get('DegreeName')
        sett.Institution_Name = request.POST.get('InstitutionName')
        sett.Country = request.POST.get('country')
        #sett.Start_date = request.POST.get('Start')
        #sett.End_date = request.POST.get('End')
        sett.save()
        return HttpResponseRedirect('/database/edit_recordx/%s/' % keyyx)





def update_xemployee_countries(request, keyx, keyyx):
    output = countries.objects.get(CountriesID=keyx)
    if request.method == 'POST':
        output.Country_Name = request.POST.get('Countries')
        output.save()
        return HttpResponseRedirect('/database/edit_recordx/%s/' % keyyx)
