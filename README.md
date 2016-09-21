# To run
* `cd bondstreet`
* Install requirements: `pip install -r requirements.txt` (you might want to do this in a virtualenv)
* Start server: `python manage.py runserver`
* Go to http://localhost:8000/application/ in your browser

# Decisions
I had to make a lot of assumptions about what was expected because the task
description was pretty brief.
* I assumed you didn't want me to make it pretty, because you asked for the GET
and POST handlers, and I thought the inclusion of screenshots was there to make
it easier for me to understand the task, rather than wanting me to make something
that looks like the screenshots.
* I decided that this application was an application to join a website or something,
rather than an application that a user who is already logged in might be completing.
Therefore, my app has no User model, because it wasn't needed.
* I figured the fastest way for me to get up and running with a database and models
to interact with would be using Django, since that's what I'm familiar with. By using
django, a lot of things become easy, like migrations and forms and csrf protection.
* I found a library called [django-formtools](https://github.com/django/django-formtools),
which used to be a part of core django before it was separated out to keep the core
library cleaner. This allowed me to use Django forms, but not save a new `Application`
model instance to the database until the entire process is completed.

# The meat
The files that will be most interesting to you are:
* [bondstreet/application/models.py](/bondstreet/application/models.py): Where the Application model is defined
* [bondstreet/application/forms.py](/bondstreet/application/forms.py): Where the Application model is split into 5 different forms.
* [bondstreet/application/views.py](/bondstreet/application/views.py): Where the view layer that manages the application state & progress lives. Here, I overwrote some of the default behavior of the FormWizard in order to customize the behavior to the specifications.

One thing that isn't yet perfect is the fact that the input fields in the forms on the frontend are still `required`, so there's some annoying validation that pops up when you try to go backwards to a previous step. To get around this, you can type any value into this field -- it won't be saved. I think that in order to fix this, I'd need to not use `{{ form }}` in the templates, and instead construct the form & fields from the data nested within `form`, leaving out the fact that the field is `required`. They'd still be required on the backend, so validation and feedback should still work, but it would allow the user to go back without those pesky error messages popping up.
