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
import webapp2, json, urllib, time

class MainHandler(webapp2.RequestHandler):
    def get(self):
        furl = urllib.urlopen("http://api.openweathermap.org/data/2.5/forecast/daily?q=Hyderabad&units=metric&cnt=7&APPID=cbf65e03a91e42aebd4ebba2d136c270")
        parsed = json.loads(furl.read())
        #print beautify_json(parsed['list'])
        wlist = parsed['list']
        for i in range(len(wlist)):
            self.response.write([str(wlist[i]['weather'][0]['description']), wlist[i]['temp']['max'], wlist[i]['temp']['min'], time.strftime("%d/%m/%y", time.localtime(int(wlist[i]['dt'])))])



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
