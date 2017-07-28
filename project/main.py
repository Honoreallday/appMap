#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import time
from google.appengine.api import users
from google.appengine.ext import ndb

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'));

class Applicant(ndb.Model):
    name = ndb.StringProperty()
    class_year = ndb.StringProperty()
    profile = ndb.BooleanProperty()
    activities = ndb.BooleanProperty()
    essay = ndb.BooleanProperty()
    supplements = ndb.BooleanProperty()
    recommendations = ndb.BooleanProperty()
    interviews = ndb.BooleanProperty()
    fafsa = ndb.BooleanProperty()
    css = ndb.BooleanProperty()
    idoc = ndb.BooleanProperty()
    scores = ndb.BooleanProperty()
    scholarship = ndb.BooleanProperty()
    program = ndb.BooleanProperty()

class Event(ndb.Model):
    title = ndb.StringProperty()
    due_date = ndb.StringProperty()
    due_time = ndb.StringProperty()
    description = ndb.StringProperty()
    key = ndb.KeyProperty(Applicant)

class Home(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('home.html')
        self.response.write(template.render())

class Login(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user: # if user is logged into Google
            email_address = user.nickname()
            applicant = Applicant.get_by_id(user.user_id())
            signout_link_html = '<a href="%s">Sign out</a>' % (
                users.create_logout_url('/'))
            if applicant:
                self.redirect('/track')
            else:
                self.redirect('/registration')
        else:
            # template = env.get_template('login.html')
            # self.response.write(template.render())
            self.response.write('''
            Please log in to use our site! <br>
            <a href="%s">Sign in</a>''' % (
            users.create_login_url('/login')))


class Registration(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('registration.html')
        template_vars = {"name": self.request.get('name'),
                         "class_year": self.request.get('class_year'),
                         "profile": self.request.get('profile'),
                         "activities": self.request.get('activities'),
                         "essay": self.request.get('essay'),
                         "supplements": self.request.get('supplements'),
                         "recommendations": self.request.get('recommendations'),
                         "interviews": self.request.get("interviews"),
                         "fafsa": self.request.get('fafsa'),
                         "css": self.request.get('css'),
                         "idoc": self.request.get('idoc'),
                         "scores": self.request.get('scores'),
                         "scholarship": self.request.get('scholarship'),
                         "program": self.request.get('program')}
        self.response.write(template.render(template_vars))


class Track(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        query = Event.query()
        query = query.order(Event.due_date)
        events = query.fetch()
        template = env.get_template('track.html')
        applicant = Applicant.get_by_id(user.user_id())
        template_vars = {"name": applicant.name,
                         "class_year": applicant.class_year,
                         "profile": applicant.profile,
                         "activities": applicant.activities,
                         "essay": applicant.essay,
                         "supplements": applicant.supplements,
                         "recommendations": applicant.recommendations,
                         "interviews": applicant.interviews,
                         "fafsa": applicant.fafsa,
                         "css": applicant.css,
                         "idoc": applicant.idoc,
                         "scores": applicant.scores,
                         "scholarship": applicant.scholarship,
                         "program": applicant.program,
                         "events": events}
        self.response.write(template.render(template_vars))
        signout_link_html = '<a href="%s">Sign out</a>' % (
            users.create_logout_url('/'))
        self.response.write(signout_link_html)

    def post(self):
        user = users.get_current_user()
        if not user:
            # You shouldn't be able to get here without being logged in
            self.error(500)
            return
        applicant = Applicant(
        name= self.request.get('name'),
        class_year= self.request.get('class_year'),
        profile= bool(self.request.get('profile')),
        activities= bool(self.request.get('activities')),
        essay= bool(self.request.get('essay')),
        supplements= bool(self.request.get('supplements')),
        recommendations= bool(self.request.get('recommendations')),
        interviews= bool(self.request.get("interviews")),
        fafsa= bool(self.request.get('fafsa')),
        css= bool(self.request.get('css')),
        idoc= bool(self.request.get('idoc')),
        scores= bool(self.request.get('scores')),
        scholarship= bool(self.request.get('scholarship')),
        program= bool(self.request.get('program')),
        id=user.user_id()
        )
        applicant.put()
        time.sleep(1)
        self.get()

class EventHandler(webapp2.RequestHandler):
    def post(self):
        event = Event (
        title = self.request.get('title'),
        due_date = self.request.get('due_date'),
        due_time = self.request.get('due_time'),
        description = self.request.get('description')
        )
        event.put()
        time.sleep(1)
        self.redirect('/track')

class About(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('about.html')
        self.response.write(template.render())

class Application(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('application.html')
        self.response.write(template.render())

class FinancialAid(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('finaid.html')
        self.response.write(template.render())

class Testing(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('testing.html')
        self.response.write(template.render())

class Programs(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('programs.html')
        self.response.write(template.render())
#
# class TimeLine(webapp2.RequestHandler):
#     def get(self):
#         template = env.get_template('timeline.html')
#         self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', Home),
    ('/login', Login),
    ('/application', Application),
    ('/finaid', FinancialAid),
    ('/testing', Testing),
    ('/programs', Programs),
    #('/timeline', TimeLine),
    ('/track', Track),
    ('/event', EventHandler),
    ('/about', About),
    ('/registration', Registration)
], debug=True)
