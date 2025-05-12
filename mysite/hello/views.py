from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from .models import UploadedFile

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_file')  # Redirect to upload
        else:
            return render(request, 'hello/login.html', {'error': 'Invalid credentials'})
    return render(request, 'hello/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'hello/upload.html', {'form': form})

@login_required
def file_list(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'hello/file_list.html', {'files': files})

@login_required
def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    file.file.delete()  # Deletes the actual file from media folder
    file.delete()
    return redirect('file_list')
