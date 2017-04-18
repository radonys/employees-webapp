#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import MySQLdb

form = cgi.FieldStorage() 

# Get data from fields
emp_no = form.getvalue('emp_no')
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
birth_date = form.getvalue('birth_date')
hire_date = form.getvalue('hire_date')
dept_no = form.getvalue('dept_no')
gender = form.getvalue('gender')

# Open database connection
db = MySQLdb.connect("localhost","l3","test123","Employees" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

print "Content-type:text/html\r\n\r\n"

print '''

<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Theme Made By www.w3schools.com - No Copyright -->
  <title>Enigma - Careers
  </title>
  <link rel="shortcut icon" type="image/x-icon" href="https://cdn0.iconfinder.com/data/icons/glyphpack/34/play-circle-128.png">
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
  <style>
  body {
      font: 400 15px Lato, sans-serif;
      line-height: 1.8;
      color: #818181;
  }
  h2 {
      font-size: 24px;
      text-transform: uppercase;
      color: #303030;
      font-weight: 600;
      margin-bottom: 30px;
  }
  h4 {
      font-size: 19px;
      line-height: 1.375em;
      color: #303030;
      font-weight: 400;
      margin-bottom: 30px;
  }  
  .jumbotron {
      background-color: #581845;
      color: #fff;
      padding: 100px 25px;
      font-family: Montserrat, sans-serif;
  }
  .container-fluid {
      padding: 60px 50px;
  }
  .bg-grey {
      background-color: #f6f6f6;
  }
  .logo-small {
      color: #581845;
      font-size: 50px;
  }
  .logo {
      color: #581845;
      font-size: 200px;
  }
  .thumbnail {
      padding: 0 0 15px 0;
      border: none;
      border-radius: 0;
  }
  .thumbnail img {
      width: 100%;
      height: 100%;
      margin-bottom: 10px;
  }
  .carousel-control.right, .carousel-control.left {
      background-image: none;
      color: #581845;
  }
  .carousel-indicators li {
      border-color: #581845;
  }
  .carousel-indicators li.active {
      background-color: #581845;
  }
  .item h4 {
      font-size: 19px;
      line-height: 1.375em;
      font-weight: 400;
      font-style: italic;
      margin: 70px 0;
  }
  .item span {
      font-style: normal;
  }
  .panel {
      border: 1px solid #581845; 
      border-radius:0 !important;
      transition: box-shadow 0.5s;
  }
  .panel:hover {
      box-shadow: 5px 0px 40px rgba(0,0,0, .2);
  }
  .panel-footer .btn:hover {
      border: 1px solid #581845;
      background-color: #fff !important;
      color: #581845;
  }
  .panel-heading {
      color: #fff !important;
      background-color: #581845 !important;
      padding: 25px;
      border-bottom: 1px solid transparent;
      border-top-left-radius: 0px;
      border-top-right-radius: 0px;
      border-bottom-left-radius: 0px;
      border-bottom-right-radius: 0px;
  }
  .panel-footer {
      background-color: white !important;
  }
  .panel-footer h3 {
      font-size: 32px;
  }
  .panel-footer h4 {
      color: #aaa;
      font-size: 14px;
  }
  .panel-footer .btn {
      margin: 15px 0;
      background-color: #581845;
      color: #fff;
  }
  .navbar {
      margin-bottom: 0;
      background-color: #581845;
      z-index: 9999;
      border: 0;
      font-size: 12px !important;
      line-height: 1.42857143 !important;
      letter-spacing: 4px;
      border-radius: 0;
      font-family: Montserrat, sans-serif;
  }
  .navbar li a, .navbar .navbar-brand {
      color: #fff !important;
  }
  .navbar-nav li a:hover, .navbar-nav li.active a {
      color: #581845 !important;
      background-color: #fff !important;
  }
  .navbar-default .navbar-toggle {
      border-color: transparent;
      color: #fff !important;
  }
  footer .glyphicon {
      font-size: 20px;
      margin-bottom: 20px;
      color: #581845;
  }
  .slideanim {visibility:hidden;}
  .slide {
      animation-name: slide;
      -webkit-animation-name: slide;
      animation-duration: 1s;
      -webkit-animation-duration: 1s;
      visibility: visible;
  }
  @keyframes slide {
    0% {
      opacity: 0;
      transform: translateY(70%);
    } 
    100% {
      opacity: 1;
      transform: translateY(0%);
    }
  }
  @-webkit-keyframes slide {
    0% {
      opacity: 0;
      -webkit-transform: translateY(70%);
    } 
    100% {
      opacity: 1;
      -webkit-transform: translateY(0%);
    }
  }
  @media screen and (max-width: 768px) {
    .col-sm-4 {
      text-align: center;
      margin: 25px 0;
    }
    .btn-lg {
        width: 100%;
        margin-bottom: 35px;
    }
  }
  @media screen and (max-width: 480px) {
    .logo {
        font-size: 150px;
    }
  }
  </style>
</head>
<body id="myPage" data-spy="scroll" data-target=".navbar" data-offset="60">

<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="/cgi-bin/Employees_Project/index.py"><i class="fa fa-play-circle"></i> <span class="light">Enigma Corporation</a>
    </div>
  </div>
</nav>

<div class="jumbotron text-center">
  <h1>Careers</h1> 
  <p>Join the company for a great and enjoyable career</p> 
</div>

<div class="container-fluid">
  <h2 align="center">Registration</h2><br>
  <form action="/cgi-bin/Employees_Project/career.py" method="post">
    <div class="form-group" align="center">
    <label for="emp_no">First 7 digits of Mobile Number (cum Employee ID)</label><br><br>
    <input type="number" class="form-control" id="emp_no" name="emp_no"><br><br>
    <label for="first_name">First Name</label><br><br>
    <input type="text" class="form-control" id="first_name" name="first_name"><br><br>
    <label for="last_name">Last Name</label><br><br>
    <input type="text" class="form-control" id="last_name" name="last_name"><br><br>
    <label for="birth_date">Date of Birth</label><br><br>
    <input type="date" class="form-control" id="birth_date" name="birth_date"><br><br>
    <label for="hire_date">Joining Date</label><br><br>
    <input type="date" class="form-control" id="hire_date" name="hire_date"><br><br>
    <label for="gender">Gender</label><br><br>
    <select class="selectpicker form-control show-tick" name="gender">
    <option value = "M">M</option>
    <option value = "F">F</option>
    </select><br><br>
    <label for="department">Department</label><br><br>
    <select class="selectpicker form-control show-tick" name="dept_no">
    '''

sql="select * from departments;"

try:
    # Execute the SQL command
        cursor.execute(sql)
    # Fetch all the rows in a list of lists.
        results = cursor.fetchall()

        for row in results:

            id1 = row[0] 
            name = row[1]
            
            print "<option value='"+(id1)+"'>"
            print name
            print "</option>"
 
except:
        print "Error: unable to fetch data"

print '''
  </select>
  </div><br>
  <div align="center">
  <button type="submit" class="btn btn-default">Submit</button>
  </div><br><br><br>'''

str1 = str(emp_no)
str2 = str(first_name)
str3 = str(last_name)
str4 = str(birth_date)
str5 = str(hire_date)
str6 = str(dept_no)
str7 = str(gender)

emp_no = "None"
first_name = "None"
last_name = "None"
birth_date = "None"
hire_date = "None"
dept_no = "None"
gender = "None"

#print str1 + " " + str2 + " " + str3 + " " + str4 + " " + str5 + " " + str6

sql = "select count(*) from applicants where emp_no='"+(str1)+"';"

cursor.execute('lock tables applicants write;')
cursor.execute('start transaction;')

try:
            # Execute the SQL command
        cursor.execute(sql)
            # Fetch all the rows in a list of lists.
        results = cursor.fetchall()

        for row in results:

            count = row[0]
            break

except:
        print "Error: unable to fetch data"

count = int(count)

if count==0 :

  sql = "INSERT into applicants (emp_no,first_name,last_name,birth_date,hire_date,gender,dept_no) values ('"+(str1)+"','"+(str2)+"','"+(str3)+"','"+(str4)+"','"+(str5)+"','"+(str7)+"','"+(str6)+"');"

  if str1!="None" and str2!="None" and str3!="None" and str4!="None" and str5!="None" and str6!="None":

      try:
      # Execute the SQL command
          cursor.execute(sql)
          db.commit()
      # Fetch all the rows in a list of lists.
          print "<h4 align='center' style='color:#FF0000';>Registered Sucessfully!</h4>"

      except:
          print "<h4 align='center' style='color:#FF0000';>Try Again!</h4>"

else :

    print "<h4 align='center' style='color:#FF0000';>Already Registered!</h4>"

cursor.execute('commit;')
cursor.execute('unlock tables;')
# disconnect from server
db.close()

print '''
</form><br><br>

<footer class="container-fluid text-center">
  <a href="#myPage" title="To Top">
    <span class="glyphicon glyphicon-chevron-up"></span>
  </a>
  <p>Enigma Corporation LLC</a></p>
</footer>

<script>
$(document).ready(function(){
  // Add smooth scrolling to all links in navbar + footer link
  $(".navbar a, footer a[href='#myPage']").on('click', function(event) {
    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
  
  $(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;

      var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
          $(this).addClass("slide");
        }
    });
  });
})
</script>

</body>
</html>

'''
