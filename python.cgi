#!/usr/bin/python
import cgi, cgitb

form = cgi.FieldStorage() # Getting all the Data from the form
city = form.getvalue("name").upper()
province =  form.getvalue("province")
country = form.getvalue("country").upper()
pop = form.getvalue("population")
url = form.getvalue("url")
print "Content-type:text/html\n\n"

print "<html>"
print "<head><style>img {border: 50px solid #39648f;}</style></head>" # Styling for the image border
print "<body>"
print "<div style='text-align: center; color: pink; background-color: teal; font-size: 76px'>"; # Header
print city + ", " + province + ", " + country
print "</div>"
print "<div style='text-align: center; color: lightblue; background-color: teal; font-size: 50px; padding: 10px'>" # Population Header
print "Population: " + pop;
print "</div>";
print "<div style='background-color:teal; text-align:center'><img src='" + url + "' alt='Picture of City' width=80%></div>"; # Picture
print "</body></html>"