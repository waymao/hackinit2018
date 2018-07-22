from django.shortcuts import render
from .models import Color
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FileFieldForm
from django.views.decorators.csrf import csrf_exempt
from . import UselessNeuralNetwork


@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = FileFieldForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            result = handle_uploaded_file(request.POST['title'], request.FILES['file'])
            return HttpResponse('{"result": ' + str(result) + '}')
    else:
        form = FileFieldForm()
    return render(request, 'upload.html', {'form': form})


def handle_uploaded_file(name,f):
    with open('uploaded_files/' + name + '.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    result = UselessNeuralNetwork.getIndex('uploaded_files/' + name + '.jpg')
    return result



# Create your views here.
