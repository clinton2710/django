from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm

# Create your views here.

# BASE VIEW CLASS = VIEW 

class CourseObjectMixin(object):
    model = Course
    lookup = 'id'
    def get_object(self):
        lookup = self.kwargs.get(self.lookup)
        obj = None
        if lookup is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


class CourseDeleteview(CourseObjectMixin, View): 
    template_name = "courses/course_delete.html" # DetailView
    def get(self, request, id=None, *arg, **kwargs):
        #GET METHOD 
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)
        
    def post(self, request, id=None, *arg, **kwargs):
        # POST METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)

class CourseUpdateview(View): 
    template_name = "courses/course_update.html" # DetailView
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *arg, **kwargs):
        #GET METHOD 
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
        
    def post(self, request, id=None, *arg, **kwargs):
        # POST METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
   
        return render(request, self.template_name, context) 

class CourseCreateview(View): 
    template_name = "courses/course_create.html" # DetailView
    def get(self, request, *arg, **kwargs):
        #GET METHOD 
        form = CourseModelForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)
        
    def post(self, request, *arg, **kwargs):
        # POST METHOD
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()

        context = {
            "form": form
        }
        return render(request, self.template_name, context)    

class CourseListview(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwaargs):
        context = {'object_list': self.get_queryset() }
        return render(request, self.template_name, context)


class Courseview(View): 
    template_name = "courses/course_detail.html" # DetailView
    def get(self, request, id=None, *arg, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

    # def post(request, *arg, **kwargs):
    #     return render(request, 'about.html', {})

# HTTP METHODS

def my_fbv(request, *arg, **kwargs):
    return render(request, 'about.html', {})