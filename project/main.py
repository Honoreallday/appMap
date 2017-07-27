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

# class Login(webapp2.RequestHandler):
#     def get(self):
#         user = users.get_current_user()
#         if user: #if user is logged into their Google account
#             email_address = user.nickname()
#             applicant = Applicant.get_by_id(user.user_id())
#             signout_link_html = '<a href="%s">sign out</a>' % (
#                 users.create_logout_url('/'))
#             if applicant:
#                 self.redirect('/track')
#             else: #if they are a new user
#                 self.redirect('/registration')
#         else:
#             self.error(500)
#         template = env.get_template('login.html')
#         self.response.write(template.render())
#
#     def post(self):
#         user = users.get_current_user()
#         if not user:
#             self.error(500)
#             return
#         applicant = Applicant(
#         name= self.request.get('name'),
#         class_year= self.request.get('class_year'),
#         profile= self.request.get('profile'),
#         activities= self.request.get('activities'),
#         essay= self.request.get('essay'),
#         supplements= self.request.get('supplements'),
#         recommendations= self.request.get('recommendations'),
#         interviews= self.request.get("interviews"),
#         fafsa= self.request.get('fafsa'),
#         css= self.request.get('css'),
#         idoc= self.request.get('idoc'),
#         scores= self.request.get('scores'),
#         scholarship= self.request.get('scholarship'),
#         program= self.request.get('program'),
#         id=user.user_id()
#         )
#         applicant.put()
#         self.redirect('/track')

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
        template = env.get_template('track.html')
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
        profile= self.request.get('profile'),
        activities= self.request.get('activities'),
        essay= self.request.get('essay'),
        supplements= self.request.get('supplements'),
        recommendations= self.request.get('recommendations'),
        interviews= self.request.get("interviews"),
        fafsa= self.request.get('fafsa'),
        css= self.request.get('css'),
        idoc= self.request.get('idoc'),
        scores= self.request.get('scores'),
        scholarship= self.request.get('scholarship'),
        program= self.request.get('program'),
        id=user.user_id()
        )
        print applicant
        applicant.put()

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

class TimeLine(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('timeline.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', Home),
    ('/login', Login),
    ('/application', Application),
    ('/finaid', FinancialAid),
    ('/testing', Testing),
    ('/programs', Programs),
    ('/timeline', TimeLine),
    ('/track', Track),
    ('/about', About),
    ('/registration', Registration)
], debug=True)
