from django.shortcuts import render, get_object_or_404, redirect
from .models import Code
from .form import CodeForm
from django.urls import reverse
def code_list(request):
    codes = Code.objects.all()
    return render(request, 'code_app/code_list.html', {'codes': codes})

def code_detail(request, code_id):
    code = get_object_or_404(Code, id=code_id)
    return render(request, 'code_app/code_detail.html', {'code': code})

def code_draw(request, code_id):
    code = get_object_or_404(Code, id=code_id)
    return render(request, 'code_app/code_draw.html', {'code': code})

def code_submit(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('code_list')
    else:
        form = CodeForm()
    return render(request, 'code_app/code_submit.html', {'form': form})

def code_delete(request, code_id):
    code = get_object_or_404(Code, id=code_id)
    code.delete()
    return redirect(reverse('code_list'))
