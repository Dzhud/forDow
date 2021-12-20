from django.shortcuts import render, redirect
from .forms import UserForm, UserLoginForm, ImageLoginForm
from django.http import HttpResponse
import requests
#from django.contrib.auth import authenticate, login, logout
#from requests.auth import HTTPBasicAuth
#from requests.structures import CaseInsensitiveDict


def index(request):
    form = UserLoginForm(request.POST)  
    
    return render(request, 'accounts/index.html', {'form': form}) 


def signup(request):
    form = UserForm(request.POST)
    form = UserForm(use_required_attribute=False)   
    return render(request, 'accounts/signup1.html', {'form': form})

def signup_success(request):
    form = UserForm(request.POST)
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    password2 = request.POST.get("password2")
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    roles = request.POST.get("role")
    country_code = request.POST.get("country_code")
    phone_number = request.POST.get("phone_number")  
        
    jsonify = {'user_name': user_name, 'password': password, 'password2': password2, 'email': email, 'first_name': first_name, 'last_name': last_name, 'role': roles, 'country_code': country_code, 'phone_number': phone_number}
        
    req = requests.post('https://100014.pythonanywhere.com/accounts/register/', json= jsonify)
    txt = req.text
    #getRole = req.json()['role']
    greet = None
    
    if req.status_code == 201:
        get_role = requests.post('https://100014.pythonanywhere.com/accounts/user_roles/').json()
        greet = f'Welcome onboard {user_name}\n Your selected role is {roles}'
        
        '''
        if getRole == 4:
            HttpResponse(f'<h2>Welcome {user_name} We Know Your role is a Vendor</h2>')
        
        else:
            return render(request, 'accounts/signup_success.html', {'txt': txt, 'req': req.status_code, 'js': req.json(), 'greet': greet, 'form': form})
            print('\n', req.status_code, '\n', req.text)
        '''
        return render(request, 'accounts/signup_success.html', {'txt': txt, 'req': req.status_code, 'js': req.json(), 'greet': greet, 'form': form})
    
    if req.status_code == 400:
        print(req.text, '\n', req.json().values())
       
        jso = req.json().values()
        return HttpResponse(f"Error: <h3>{jso}</h3>")
    
    
    return render(request, 'accounts/signup.html')            
    #return redirect('index')
    
        
    


'''
def login(request):
    if request.method == 'POST':
        req = requests.post('https://100014.pythonanywhere.com/api/password_token/', params=request.POST)
     
    else:
        req = requests.get('https://100014.pythonanywhere.com/api/password_token/', params=request.GET)
        
    if req.status_code == 200:
        return HttpResponse('API Request Submitted')

    #return render(request, 'accounts/login.html', {'response':response})
    return HttpResponse('API Request Fail')
'''
    

# Dashboard works
def dashboard(request):
    form = UserLoginForm(request.POST)
    #if req.status_code == 200: 
    if form.is_valid():
        username = form.cleaned_data.get("user_name")
        password = form.cleaned_data.get("password")
        req = requests.post('https://100014.pythonanywhere.com/api/password_token/', json={'user_name': username, 'password': password})
        if req.status_code == 200:
            showTxt = req.text
            greet = f'Welcome {username}'
            ty = req.json()
            print('\n', req.status_code,'\n', req.text, '\n', req.json())
            return render(request, 'accounts/dashboard.html', {'req': req, 'showTxt': showTxt, 'ty': ty, 'user_name': username, 'greet': greet})
        else:
            form = UserLoginForm()
            return HttpResponse("Oops! Your password is not correct")
       
        
    return HttpResponse('<strong><h2 style="display:grid; place-items:center; margin-top:20%; margin-down:20%; color:black; background-color:pink">Please Ensure your <br>login credentials are correct</h2></strong>')
    
'''
def face_login(request):
    if request.method == 'POST':
        form = ImageLoginForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            
            return HttpResponseRedirect('<int>/dashboard')
        else:
            form = ImageLoginForm()
    req = request.post("https://100014.pythonanywhere.com/api/face_id_token/")
    
    return HttpResponse('Face Login')
    
    
    
'''    
def select_role(request):
    return render(request, 'accounts/select-role.html')
