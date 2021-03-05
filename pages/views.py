from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
	template_name = 'home.html'


class AboutPageView(TemplateView):
	template_name = 'about.html'


# 	@login_required
# def topics(request):
# 	"""Show all topics."""
# 	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
# 	#topics = Topic.objects.order_by('date_added')
# 	context = {'topics': topics}

# 	return render(request, 'learning_logs/topics.html', context)