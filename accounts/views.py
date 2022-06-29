from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from listings.models import Listing
from realtors.models import Realtor
from realtors.validators import validate_file_size

from .forms import RealtorForm, UserEditForm, ListingForm

# Regiter Endpoint
def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

# Login
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

# Logot Endpoint
def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

# Dasboard EndPoint
def dashboard(request):
  if request.user.is_authenticated:
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)

# Inquiries List EndPoint
def inquiryList(request):
  if request.user.is_authenticated and request.user.is_staff:
    user_contacts = Contact.objects.all().order_by('-contact_date')
  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/inquiries.html', context)

# Delete User Inquiry Endpoint
def deleteInquiry(request, inquiry_id):
  if request.user.is_authenticated:
    obj = get_object_or_404(Contact, id=inquiry_id)
    obj.delete()
    return redirect('dashboard')
  else:
    return redirect('login')

# Delete User Inquiry Admin EndPoint
def adminDeleteInquiry(request, admin_inquiry_id):
  if request.user.is_authenticated  and request.user.is_staff:
    obj = get_object_or_404(Contact, id=admin_inquiry_id)
    obj.delete()
    return redirect('inquiries-list')
  else:
    return redirect('login')

# Create Realtor Endpoint
def createRealtor(request):
  if request.user.is_authenticated and request.user.is_staff:
    if request.method == 'POST':
      form = RealtorForm(request.POST, request.FILES)
      if form.is_valid():
        email = form.cleaned_data["email"]
        if Realtor.objects.filter(email=email).exists():
          messages.error(request, "Email Already Exists")
          return redirect('create-realtor')
        else:
          realtor_object = form.save(commit=False)
          realtor_object.save()
          messages.success(request, "Realtor Created Successfully")
          return redirect('create-realtor')
      else:
        return render(request, 'accounts/create_realtor.html', {'form': form})      
    else:
      form = RealtorForm()
      return render(request, 'accounts/create_realtor.html', {'form': form})
  else:
    return redirect('login')

# Realtor Edit Endpoint
def realtorEdit(request, realtor_id=None):
  if request.user.is_authenticated: 
    if realtor_id:
      realtor = get_object_or_404(Realtor, id=realtor_id)
    else:
      realtor = Realtor(pk=realtor_id)

    form = RealtorForm(request.POST or None, request.FILES or None, instance=realtor)
    if request.POST and form.is_valid():
      form.save()
      messages.success(request, "Realtor Updated Successfully")
      # Save was successful, so redirect to another page
      return redirect('realtors-list')

    return render(request, 'accounts/realtor_edit.html', {'form': form})      
  else:
      return redirect('login')

# List Realtors Endpoint
def realtorsList(request):
  if request.user.is_authenticated and request.user.is_staff:
    realtors_list = Realtor.objects.all()
  context = {
    'realtors': realtors_list
  }
  return render(request, 'accounts/realtors_list.html', context)

# Delete Realtor Endpoint
def deleteRealtor(request, id):
  if request.user.is_authenticated and request.user.is_staff:
    obj = get_object_or_404(Realtor, id=id)
    obj.delete()
  return redirect('realtors-list')

# Create Listing Endpoint
def createListing(request):
  if request.user.is_authenticated and request.user.is_staff:
    if request.method == 'POST':
      form = ListingForm(request.POST, request.FILES)
      if form.is_valid():
        title = request.POST['title']
        if Listing.objects.filter(title=title).exists():
          messages.error(request, "Listing Already Exists")
          return redirect('create-listing')
        else:
          listing_object = form.save(commit=False)
          listing_object.save()
          messages.success(request, "Listing Created Successfully") 
          return redirect('create-listing')
      else:
        return render(request, 'accounts/create_listing.html', {'form': form})    
    else:
      form = ListingForm()
      return render(request, 'accounts/create_listing.html', {'form': form})
  else:
    return redirect('login')

# Listing Edit Endpoint
def listingEdit(request, listing_id=None):
  if request.user.is_authenticated: 
    if listing_id:
      listing = get_object_or_404(Listing, id=listing_id)
    else:
      listing = Listing(pk=listing_id)

    form = ListingForm(request.POST or None, request.FILES or None, instance=listing)
    if request.POST and form.is_valid():
      form.save()
      messages.success(request, "Listing Updated Successfully")
      # Save was successful, so redirect to another page
      return redirect('list_listings')

    return render(request, 'accounts/listing_edit.html', {'form': form})      
  else:
    return redirect('login')


# List Listings Endpoint
def listingsList(request):
  if request.user.is_authenticated and request.user.is_staff:
    list_listings = Listing.objects.all()
  context = {
    'listings_all': list_listings
  }
  return render(request, 'accounts/listings_list.html', context)

# Delete listing Endpoint
def deleteListing(request, listing_id):
  if request.user.is_authenticated and request.user.is_staff:
    obj = get_object_or_404(Listing, id=listing_id)
    obj.delete()
  return redirect('listings-list')

# List Users Endpoint
def usersList(request):
  if request.user.is_authenticated and request.user.is_staff:
    users_list = User.objects.all()
  context = {
    'users': users_list
  }
  return render(request, 'accounts/users_list.html', context)

# Edit User Endpoint
def userEdit(request, user_id=None):
  if request.user.is_authenticated and request.user.is_staff:
    if user_id:
      user = get_object_or_404(User, id=user_id)
    else:
      user = User(pk=user_id)

    form = UserEditForm(request.POST or None, instance=user)
    if request.POST and form.is_valid():
      form.save()
      messages.success(request, "User Updated Successfully")
      # Save was successful, so redirect to another page
      return redirect('users-list')
    else:
      return render(request, 'accounts/user_edit.html', {'form': form})
  else:
    return redirect('login')

# Delete User Endpoint
def deleteUser(request, id):
  if request.user.is_authenticated and request.user.is_staff:
    obj = get_object_or_404(User, id=id)
    obj.delete()
  return redirect('users-list')

# Profile EndPoint
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['user']
            password = request.POST['password']
            password2 = request.POST['password2']
            #check if password match
            if password == password2:
                user =  User.objects.get(email=email)
                user.set_password(password2)
                user.save()
                auth.login(request, user)
                messages.success(request, 'Your password has been changed successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'Passwords donot match!!!')
                return redirect('dashboard')
        else:
            return render(request, 'accounts/dashboard.html')

    else:
        return redirect('login')
