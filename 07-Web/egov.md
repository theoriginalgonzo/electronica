# EGOV
- Open the egov login page
- Enter any username and password into the login form and submit it. Submitting the login form creates a cookie that tracks whether the user is an admin. Once the cookie is created it can be modified from false to true
- Right click and select inspect
- Go to the console tab  
- enter this command: document.cookie = "admin=true" 
- add /admin to the end of the url and load the page
- when it loads, the flag will be displayed