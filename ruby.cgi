#!/usr/local/bin/ruby
puts "Content-type: text/html\n\n";
require "cgi"
cgi = CGI.new

city = cgi['name'].capitalize # Getting all the Data from the form
province =  cgi['province'].capitalize
country = cgi['country'].capitalize
pop = cgi['population']
url = cgi['url']

puts "<html><body>";
puts "<div style='text-align: center; color: pink; background-color: teal; font-size: 76px'>"; # Header
puts city + ", " + province + ", " + country;
puts "</div>";
puts "<div style='text-align: center; color: lightblue; background-color: teal; font-size: 50px; padding: 10px'>" # Population Header
puts "Population: " + pop;
puts "</div>";
puts "<img src='" + url + "' alt='Picture of City' width=100%>"; # Picture
puts "</body></html>";

