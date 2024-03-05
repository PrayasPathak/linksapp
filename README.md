# Link Shortener App

It is a basic project that stores the name of link along with the slug and the number of clicks. The slug is computed on the basis of the name provided by the user. When a link is clicked the number of clicks is increased and the user is redirected to the site referenced by the link.

Link Model:

- name
- url
- slug
- clicks

# Run the project

Follow the following steps to run the project successfully:

1. Create a virtual environment:
   python -m venv env

2. Activate the virtual envrironment:
   On Windows: venv\scripts\activate

on Linux/Max: source venv/Scripts/activate

3. Install Necessary packages
   pip install -r requirements.txt

4. Run migrations
   python manage.py migrate

5. Run project
   python manage.py runserver
