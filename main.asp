<%
color = Request.QueryString("color") ' Getting information from URL
texture = Request.QueryString("texture")

' Displaying the image and background color
response.write("<body style='background: " & color & " url(""" & texture & """)'>")

' Creating a cookie if this is the user's first ever visit. Displays a greeting message.
if Request.Cookies("lastVisit") = "" then
	Response.Cookies("lastVisit") = DateAdd("h",3,Now()) ' Server is located on the west coast. This adds 3 hours to display east coast time.
	response.write("Welcome to our Website. Enjoy your First Visit.")
else ' Updating the cookie if this is not the user's first ever visit. Displays last visit time and date prior to updating cookie.
	response.write("Your last visit occured at: " & Request.Cookies("lastVisit"))
	Response.Cookies("lastVisit") = DateAdd("h",3,Now())
end if
%>
