Rock n roll wagtail
====================

![No Wagtail playing](https://github.com/heymonkeyriot/rocknroll-wagtail-cookiecutter/blob/master/wagtail%20rock%20n%20roll.jpg)

**Status**: Currently very much a work in progress. Models are working, but there aren't any templates!

### A Wagtail project for cut 'n' paste pulling apart

Why
---

For those who are bad at reading documentation. At a code sprint for Wagtail in Philadelphia, in March 2016, there was a request for something showing different aspects of Wagtail to help you get set-up with understanding how Wagtail CMS works.

What's here at the moment
-------------------------

 - A Django project with Wagtail preinstalled
 - A number of apps
   - **Home**
   - **Reviews**
   - **Author**
   - **Artist**
   - **Album**
   - **Feature content page**
   - **Standard page**
 - Vagrant configuration (using the [torchbox/wagtail](https://github.com/torchbox/vagrant-wagtail-base) base box)
 - Heroku configuration
 - Sphinx docs

Installation locally
--------------------
```
Git clone git@github.com:heymonkeyriot/rocknroll-wagtail.git
Cd rocknrollwagtail
Vagrant up
Vagrant ssh
pip install -r requirements.txt
cd rocknrollwagtail/static
npm install
bower install
gulp watch
cd ../../
dj makemigrations
dj migrate
dj createsuperuser --username username
djrun
```

You should now be able to visit localhost:1234 and see the site

TODO 
----------------------------

 -[ ] Put `cd rocknrollwagtail/static && npm install && bower install` within vagrant provision file
 -[ ] Fully inline comments the different models and templates
 -[ ] Creating categorisation around bands
 -[ ] Creating categorisation around genres / sub-genres