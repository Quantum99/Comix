#!/usr/bin/env python
 
import gtk, webkit, urllib2
 
x=100
 
def update_buttons(view, frame, resource, request, response):
   global x
   url=request.get_uri()
   if "jpg?" in url:
     print url
     u = urllib2.urlopen(url)
     file = open( str(x) + '.jpg','w')
     file.write(u.read())
     file.close()
     x+=1
 
win = gtk.Window()
win.connect('destroy', lambda w: gtk.main_quit())
win.show()
 
box1 = gtk.HBox()
win.add(box1)
 
web = webkit.WebView()
web.connect("resource-request-starting", update_buttons)
box1.pack_start(web)
 
web.open("http://www.mangahere.co/manga/itsuwaribito_utsuho/c001/")
 
box1.show_all()
 
gtk.main()
