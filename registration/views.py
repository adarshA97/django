
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from registration.models import *
from registration.forms import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "index.html"

class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "register_user.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = '/register/user/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)