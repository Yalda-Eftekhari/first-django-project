from django.forms import ModelForm
from . models import Project

class ProjectForm(ModelForm):
    class Meta: # Meta class is used to specify various options for this model form.
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']