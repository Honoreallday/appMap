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
from google.appengine.api import ndb

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'));

class Applicant(webapp2.RequestHandler):
    name = ndb.StringProperty()
    checkbox = {"name": name, "grade": grade, "profile": profile,
                "activities": activities, "essay": essay,
                "supplements": supplements,"recommendations": recommendations,
                "interviews": interviews,"fafsa": fafsa, "css": css,
                "idoc": idoc, "scores": scores, "scholarship": scholarship,
                "program": program, "other": other}

class Login(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email_address = user.nickname()
            applicant = Applicant.get_by_id(user.user_id())
            signout_link_html = '<a href="%s">sign out</a>' % (
                users.create_logout_url('/'))
            if applicant:
                self.redirect('/track')
            else:
                self.redirect('/registration')
        else:
            self.redirect('/')
    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect('/registration')
            return
        applicant.put()
        template = env.get_template('login.html')
        self.response.write(template.render())

class Registration(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('registration.html')
        template_vars = {"name": self.request.get('name'),
                         "email": self.request.get('email')}
        self.response.write(template.render(template_vars))

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

class Track(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('track.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', Login),
    ('/application', Application),
    ('/finaid', FinancialAid),
    ('/testing', Testing),
    ('/programs', Programs),
    ('/timeline', TimeLine),
    ('/track', Track),
    ('/about', About),
    ('/registration', Registration)
], debug=True)
