from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,Employee

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all
    employees = Employee.objects.all
    if(restaurants and employees):
        return render(request, 'index.html', {'restaurants' : restaurants, 'employees':employees})
    else: return HttpResponse('<h1>404 - Something went wrong</h1>')
    

def results(request):
    if request.method == 'GET':
        emp_id = request.GET['employee_id']
        try: employee = Employee.objects.get(id=int(emp_id))
        except: employee = None
        if(employee):
            data = {
                'employee_name' : employee.emp_name,
                'restaurant_name' : employee.emp_restaurant.restaurant_name,
                'location' : employee.emp_restaurant.location,
                'contact' : employee.contact_no,
            }
            return render(request, 'result.html', data)
        else: return HttpResponse('<h3>Employee not found.</h3>')
    else: return HttpResponse('<h2>Something went wrong.</h2>')
