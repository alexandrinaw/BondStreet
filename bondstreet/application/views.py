from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

from .models import Application


class ApplicationWizard(SessionWizardView):
    instance = Application()

    def get_form_instance(self, step):
        return self.instance

    def done(self, form_list, **kwargs):
        """When all the forms have been submitted."""
        self.instance.save()
        return render(self.request, 'application/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get(self, request, *args, **kwargs):
        """This method handles GET requests.

        Overwrote SessionWizardView/WizardView's get method in order to prevent
        the form data from being cleared upon GET requests.
        """
        return self.render(self.get_form())

    def get_template_names(self):
        """This could be used for different templates per page. I'm using it to
        return my own template instead of the default one that comes with formtools.
        """
        return 'application/step.html'

    def get_form_initial(self, step):
        """The initial data for the given `step`.

        This looks up already-submitted form data from the Session storage backend,
        and constucts a dict out of the step's questions and answers.

        This data is used both to populate form answers if a user e.g. goes back
        to a previous step, and also in calculating what the furthest step the user
        made it to is.
        """
        data = self.storage.data['step_data'].get(step, {})
        initial_data = {}
        for key, value in data.iteritems():
            if key[0] == step:
                initial_data[key[2:]] = value[0]
        return initial_data

    def get_next_step(self, step=None):
        """The next step is always the first incomplete step, or the furthest the
        user has made it without submitting that step/form."""
        num_forms = len(self.form_list)
        for form_id in range(num_forms):
            form_id_str = str(form_id)
            data = self.get_form_initial(form_id_str)
            form = self.form_list[form_id_str]
            if not form(data).is_valid():
                return form_id_str
        return str(num_forms)
