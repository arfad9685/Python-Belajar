#Registration form in HTML using python

import webbrowser
# open form.html file in write-only mode
# it will automatically create the file
# if it is not exist
file = open("form.html", "w")
# write the html code for registration form 
html_code = """<!DOCTYPE html>
<html>
<head>
<title>Registration Form</title>
</head>
<body>
<h1>Registration Form</h1>
<form action="/action_page.php">
<label for="name"> <b>Enter your Name:</b> </label>
<input type="text" id="name" name="name"> <br><br>
<label for="email"> <b>Enter your Email:</b> </label> 
<input type="email" id="email" name="email"> <br>
<h3>Select Course:</h3>
<input type="radio" id="Course1" name="Course" value="C++">
<label for="Course1"> <b> C++ </b> </label> <br>
<input type="radio" id="Course2" name="Course" value="Java">
<label for="Course2"> <b> Java </b> </label> <br>
<input type="radio" id="Course3" name="Course" value="Python">
<label for="Course3"> <b> Python </b> </label> <br><br>
<input type="submit" value="Submit">
</form>
</body>
</html>"""
# write the html code in form.html file
file.write(html_code)
# close the file
file.close()
#open the form in new tab of browser
webbrowser.open_new_tab("form.html")