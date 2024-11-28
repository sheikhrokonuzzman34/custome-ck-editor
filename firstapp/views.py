from django.shortcuts import render

# Create your views here.


def hello_view(request):
    message = "Hello World Django"
    return render(request, 'firstapp/hello.html', {'message': message})


from django.shortcuts import render, redirect
from .models import MyModel

def my_model_list(request):
    my_models = MyModel.objects.all()
    return render(request, 'my_model_list.html', {'my_models': my_models})

def my_model_create(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        MyModel.objects.create(content=content)
        return redirect('my_model_list')
    return render(request, 'my_model_create.html')
