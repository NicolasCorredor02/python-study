from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de la tarea", max_length=200)
    description = forms.CharField(label="Descripción de la tarea", max_length=200)
    # project = forms.ModelChoiceField(
    #     label="Proyecto", queryset=Project.objects.all(), required=False
    # )
    done = forms.BooleanField(label="Completada", required=False)
