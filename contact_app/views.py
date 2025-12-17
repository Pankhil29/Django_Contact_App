from django.shortcuts import redirect, render,get_object_or_404
from .models import Contact
from login.models import Registration
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

# Create your views here.

def home(req):
    return render(req,'contact.html')

def logout(req):
    req.session.flush()
    messages.success(req,"Logout Success")
    return redirect("login")

@never_cache
def add_contact(req):
    user_id = req.session.get("user_id")
    if not user_id:
        return redirect("login")
    
    if req.method == 'POST':
        # print(req.POST)
        # user =  Registration.objects.get(id=user_id)
        
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        address = req.POST['address']
        Contact.objects.create(name=name,email=email,phone=phone,address=address,user_id=user_id)
        # user_id is fixed text b'cause request.session["user_id"] = user.id in this we write user_id
        # print(name)
        messages.success(req,"contact added successfully")
        return redirect('show_contact')    
    return render(req,'contact.html')
    
@never_cache
def show_contact(req):
    user_id = req.session.get("user_id")
    # req -> httprequest object
    # req.session -> Django session object
    # print(user_id)
    if not user_id:
        return redirect('login')
    
    user = Registration.objects.get(id =user_id)

    keyword = req.GET.get('keyword') 
    # print(keyword)
    if keyword:
        contacts = Contact.objects.filter(Q(name__icontains=keyword) | Q(phone__icontains=keyword) | Q(email__icontains=keyword) | Q(address__icontains=keyword))
        paginator = Paginator(contacts, 3)
        page_number = req.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # print("sfdfdsf",page_obj)
        # print(paginator)
        context = {
        "keyword": keyword,
        "data" : page_obj,
    }
    
        return render(req, 'show_contact.html',context)
    else:
        contacts = Contact.objects.filter(user=user)
        paginator = Paginator(contacts, 3)
        page_number = req.GET.get('page')
        page_obj = paginator.get_page(page_number)
        #    print("sfdfdsf",page_obj)
        # print(paginator)
        context = {
        "keyword": keyword,
        "data" : page_obj,
    }
    
        return render(req, 'show_contact.html',context)
        
      
    

@never_cache
def edit_contact(req,pk):
    user_id = req.session.get("user_id")
    if not user_id:
        return redirect("login")
    get_contact = get_object_or_404(Contact,pk=pk,user_id=user_id)
    # get_contact = Contact.objects.get(pk=pk)
    # print(get_contact)
    # print(get_contact.email)
    # print(model_to_dict(get_contact))
    if req.method == 'POST' :    # jyare update button click thay tyare post req.
        # print(req.POST)
        get_contact.name = req.POST['name']      
        get_contact.phone = req.POST['phone']
        get_contact.email = req.POST['email']
        get_contact.address = req.POST['address']
        get_contact.save()
        messages.success(req,"Contact edited successfully")
        return redirect('show_contact')
    else:   # edit button click thay tyare get req. avse
        context = {
            'get_contact':get_contact
        }
       
        return render(req,'edit_contact.html',context)
    
@never_cache
def delete_contact(req,pk):
    
    user_id = req.session.get("user_id")
    if not user_id:
        return redirect("login")
    get_contact = get_object_or_404(Contact,pk=pk,user_id=user_id)
    get_contact.delete()
    return redirect('show_contact')


# def search(req):
    
#     keyword = req.GET.get('keyword')
#     print(keyword)
#     contact = Contact.objects.filter(Q(name__icontains=keyword) | Q(phone__icontains=keyword) | Q(email__icontains=keyword) | Q(address__icontains=keyword))
#     print(contact)
#     context = {
#         'contact': contact,
#     }
#     return render(req,'show_contact',context)