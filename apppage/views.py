from typing import Any
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from apppage import models
from apppage import forms


class PortfolioView(FormMixin, ListView):
    template_name = 'index.html'
    model = models.PortfolioModel
    context_object_name = 'posts'
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse_lazy('pages:home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()

            return self.form_valid(form)
        else:

            return self.form_invalid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tech_skills'] = models.TechnicalSkillsModel.objects.all()
        context['pro_skills'] = models.ProfessionalSkillsModel.objects.all()
        context['tags'] = models.PortfolioTagModel.objects.all()
        context['clients'] = models.ClientModel.objects.all()
        context['educations'] = models.EducationModel.objects.all()
        context['works'] = models.WorkExperienceModel.objects.all()
        context['languages'] = models.WorkLanguageModel.objects.all()

        return context
