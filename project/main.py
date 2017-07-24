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

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'));

class Login(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('project.html')
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

class About(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('about.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', Login),
    ('/application', Application),
    ('/finaid', FinancialAid),
    ('/testing', Testing),
    ('/programs', Programs),
    ('/timeline', TimeLine),
    ('/track', Track),
    ('/about', About)
], debug=True)
