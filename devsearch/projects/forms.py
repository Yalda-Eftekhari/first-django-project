from django.forms import ModelForm
from . models import Project

class ProjectForm(ModelForm):
    class Meta: # Meta class is used to specify various options for this model form.
        model = Project
        fields = '__all__' # This will include all the fields in the model.