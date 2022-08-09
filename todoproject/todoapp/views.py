from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.forms import todoform
from todoapp.models import tasks

from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
class tasklistview(ListView):
    model = tasks
    template_name = 'home.html'
    context_object_name = 'task1'
class taskdetailview(DetailView):
    model=tasks
    template_name = 'detail.html'
    context_object_name = 'tas'
class taskupdateview(UpdateView):
    model = tasks
    template_name = 'update.html'
    context_object_name = 't'
    fields = ['name','priority','date']
    def get_success_url(self):
        return reverse_lazy('update',kwargs={'pk':self.object.id})
class taskdeleteview(DetailView):
    model = tasks
    template_name = 'delete.html'
    success_url=reverse_lazy('hhome')







def add(request):
    task1 = tasks.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','' )
        priority = request.POST.get('prio','' )
        date=request.POST.get('date','')
        task = tasks(name=name, priority=priority,date=date)
        task.save()
    return render(request, 'home.html',{'task1':task1})
# def details(request):

    # return render(request,'detail.html',{'task1':task1})
def delete(request,taskid):
    task=tasks.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    t=tasks.objects.get(id=id)
    form=todoform(request.POST or None, instance=t)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'t':t})
