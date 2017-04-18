#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import MySQLdb

form = cgi.FieldStorage() 

# Get data from fields
emp_no = form.getvalue('emp_no')
department = form.getvalue('department')
flag = form.getvalue('flag')

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
        <title>Enigma - Leave Requests
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
            background-color: #212F3C;
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
            color: #212F3C;
            font-size: 50px;
        }
        .logo {
            color: #212F3C;
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
            color: #212F3C;
        }
        .carousel-indicators li {
            border-color: #212F3C;
        }
        .carousel-indicators li.active {
            background-color: #212F3C;
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
            border: 1px solid #212F3C; 
            border-radius:0 !important;
            transition: box-shadow 0.5s;
        }
        .panel:hover {
            box-shadow: 5px 0px 40px rgba(0,0,0, .2);
        }
        .panel-footer .btn:hover {
            border: 1px solid #212F3C;
            background-color: #fff !important;
            color: #212F3C;
        }
        .panel-heading {
            color: #fff !important;
            background-color: #212F3C !important;
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
            background-color: #212F3C;
            color: #fff;
        }
        .navbar {
            margin-bottom: 0;
            background-color: #212F3C;
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
            color: #212F3C !important;
            background-color: #fff !important;
        }
        .navbar-default .navbar-toggle {
            border-color: transparent;
            color: #fff !important;
        }
        footer .glyphicon {
            font-size: 20px;
            margin-bottom: 20px;
            color: #212F3C;
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

    <body id="myPage" data-spy="scroll" data-target=".navbar" data-offset="60">'''

str1 = str(emp_no)

sql = "select count(*) from passwords where emp_no='"+(str1)+"';"

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

if count>0 :

        print'''<nav class="navbar navbar-default navbar-fixed-top">
            <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>                        
                </button>
                <a class="navbar-brand" href="/cgi-bin/Employees_Project/index.py"><i class="fa fa-play-circle"></i> <span class="light">Enigma Corporation</a>
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav navbar-right">'''

        str99 = str(emp_no)
        str999 = "/cgi-bin/Employees_Project/requests.py?emp_no=" + str99 + "&flag=1"
        str997 = "/cgi-bin/Employees_Project/requests.py?emp_no=" + str99 + "&flag=1"
        str998 = "/cgi-bin/Employees_Project/employee.py?emp_no=" + str99
        print   "<li><a href='"+(str999)+"'>REQUESTS</a></li>"
        print   "<li><a href='"+(str998)+"'>EMPLOYEE DIRECTORY</a></li>"

        print '''
                    <li><a href="/cgi-bin/Employees_Project/loginpage.py">LOGOUT</a></li>
                </ul>
                </div>
                </div>
            </nav>'''

	str1 = str(emp_no);
 	sql = "select distinct(first_name),last_name,dept_name from departments NATURAL JOIN dept_emp NATURAL JOIN employees where employees.emp_no='"+(str1)+"';"

  	try:
	    # Execute the SQL command
	    		cursor.execute(sql)
	    # Fetch all the rows in a list of lists.
	    		results = cursor.fetchall()

	    		for row in results:

		            empid = row[0]
		            birth = row[1]
		            first = row[2]
		            break

	except:
    		print "Error: unable to fetch data"

  	print '''
	    <div class="jumbotron text-center">
	        <h1>Your Requests</h1> '''
	print '''<p>'''
	print empid + " " + birth
	print '''<p>'''
        print '''<h5>'''
        print first
        print '''</h5>
	    </div>
    	<div class="container-fluid text-center">'''

        print '''
<div id="services" class="container-fluid">
    <h2 align="center">Your Leave Requests</h2><br><br>'''

        str121 = str(emp_no)
        #print str1
        sql = "select days,approval,dated from absentapp where absentapp.emp_no = '"+(str121)+"';"

        if str121!="None":

            try:
            # Execute the SQL command
                cursor.execute(sql)
            # Fetch all the rows in a list of lists.
                results = cursor.fetchall()

                print '''<div class="container">

                <table class="table table-striped">
                    <thead>
                    <tr>
                        <th>Number of Days</th>
                        <th>Status</th>
                        <th>Dated</th>
                    </tr>
                    </thead>
                    <tbody>'''

                for row in results:

                    name = row[0]
                    type1 = row[1]
                    type2 = str(row[2])

                    type2.split(' ')
                    # Now print fetched result
                    #print "name=%s,type1=%s,type2=%s <br>" % \
                            #(name, type1, type2)
                    print "<tr>"
                    print "<td align='left'>"
                    print str(name) + " days"
                    print "</td>"
                    print "<td align='left'>"
                    print type1
                    print "</td>"
                    print "<td align='left'>"
                    print type2[0]+type2[1]+type2[2]+type2[3]+type2[4]+type2[5]+type2[6]+type2[7]+type2[8]+type2[9]
                    print "</td>"
                    print "</tr>"
                print '''</tbody>
                </table>
                </div>'''

            except:
                print "Error: unable to fetch data"

        print'''
        </div>'''

else :

    print '''

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
            <h1>Access Denied</h1> 
            <p><a href = "/cgi-bin/Employees_Project/loginpage.py">Try Again</a></p> 
        </div>'''

# disconnect from server
db.close()

#print emp_no

print '''

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
</html>'''
