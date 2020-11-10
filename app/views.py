from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import JobPost, Cv


#classbased 
class HomePageView(ListView):
	template_name = 'index.html'
	model = JobPost	
	context_object_name = 'jobposts'

class JobDetailView(DetailView):
	template_name = 'detail.html'
	model = JobPost
	context_object_name = 'jobposts'


def search(request):
	if request.GET:
		search_term = request.GET['search_term']
		search_results = JobPost.objects.filter(
			Q(job_name__icontains=search_term)|
			Q(company_name__icontains=search_term)|
			Q(experiance_req__icontains=search_term)
			)
		context = {
			'search_term': search_term,
			'jobposts': search_results
		}
		return render(request, 'search.html', context)
	else:
		return redirect('home')



class SignUpView(CreateView):
	form_class = UserCreationForm
	template_name = 'registration/signup.html'
	success_url = '/login/'

class CvCreateView(LoginRequiredMixin, CreateView):
	model = Cv
	template_name = 'create_cv.html'
	fields = ['name', 'mobile', 'email', 'present_address', 'career_objective', 'ssc_result', 'hsc_result', 'bsc_result', 'msc_result', 'phd', 'no_of_work_experiance', 'language_skill', 'interest']
	
	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.manager = self.request.user
		instance.save()
		return redirect('cv-list-view')


class CvListView(LoginRequiredMixin,ListView):
	model = Cv
	template_name = 'cv_list_view.html'
	paginate_by = 5


	def get_queryset(self):
		object_list = super().get_queryset()
		return object_list.filter(manager = self.request.user)