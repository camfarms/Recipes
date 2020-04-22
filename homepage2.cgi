#! /usr/bin/awk -f
BEGIN{
	print "Content-type: text/html\n"
	print "<html>"
	print "<head>"
	print "<meta name="viewport" content="width=device-width, initial-scale=1">"
	print " <style>
	print "body {font-family: Arial, Helvetica, sans-serif;}
	print "form {border: 3px solid #f1f1f1;}
	print "
	print "input[type=text], input[type=password] {
	print "  width: 100%;
	print "  padding: 12px 20px;
	print "  margin: 8px 0;
	print "  display: inline-block;
	print "  border: 1px solid #ccc;
	print "  box-sizing: border-box;
	print "}
	print "
	print "button {
	print "  background-color: #4CAF50;
	print "  color: white;
	print "  padding: 14px 20px;
	print "  margin: 8px 0;
	print "  border: none;
	print "  cursor: pointer;
	print "  width: 100%;
	print "}
	print "
	print "button:hover {
	print "  opacity: 0.8;
	print "}
	print "
	print ".cancelbtn {
	print "  width: auto;
	print "  padding: 10px 18px;
	print "  background-color: #f44336;
	print "}
	print "
	print ".btn{
	print "  padding: 10px 18px;
	print "  background-color: #f44336;
	print "}
	print "
	print ".imgcontainer {
	print "  text-align: center;
	print "  margin: 24px 0 12px 0;
	print "}
	print "
	print "img.avatar {
	print "  width: 40%;
	print "  border-radius: 50%;
	print "}
	print "
	print ".container {
	print "  padding: 16px;
	print "}
	print "
	print "span.psw {
	print "  float: right;
	print "  padding-top: 16px;
	print "}
	print "
	print ".dropbtn {
	print "  background-color: #4CAF50;
	print "  color: white;
	print "  padding: 16px;
	print "  font-size: 16px;
	print "  border: none;
	print "  position: center;
	print "}
	print "
	print ".dropdown {
	print "  position: center;
	print "  display: inline-block;
	print "}
	print "
	print ".dropdown-content {
	print "  display: none;
	print "  position: center;
	print "  background-color: #f1f1f1;
	print "  min-width: 160px;
	print "  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
	print "  z-index: 1;
	print "}
	print "
	print ".dropdown-content a {
	print "  color: black;
	print "  padding: 12px 16px;
	print "  text-decoration: none;
	print "  display: block;
	print "}
	print "
	print ".dropdown-content a:hover {background-color: #ddd;}
	print "
	print ".dropdown:hover .dropdown-content {display: block;}
	print "
	print ".dropdown:hover .dropbtn {background-color: #3e8e41;}
	print "
	print "/* Change styles for span and cancel button on extra small screens */
	print "@media screen and (max-width: 300px) {
	print "  span.psw {
	print "     display: block;
	print "     float: none;
	print "  }
	print "  .cancelbtn {
	print "     width: 100%;
	print "  }
	print "}
	print "</style>
	print "</head>
	print "<body>
	print "
	print "<h2>Welcome!</h2>
	print "  <div class="container" style="background-color:#f1f1f1">
	print "    <button type="button" class="btn">Find New Recipe</button>
	print "    <button type="button" class="btn">Add Recipe</button>
	print "    <button type="button" class="btn">Get Recipe from Ingredits</button>
	print "    <button type="button" class="btn">Your Recipes</button>
	print "    <button type="button" class="btn">Random Recipe</button>
	print "
	print "    <div class="dropdown">
	print "    <button class="dropbtn">Cuisines</button>
	print "      <div class="dropdown-content">
	print "        <a href="#">African</a>
	print "        <a href="#">American</a>
	print "        <a href="#">British</a>
	print "        <a href="#">Cajun</a>
	print "        <a href="#">Caribbean</a>
	print "        <a href="#">Chinese</a>
	print "        <a href="#">Eastern</a>
	print "        <a href="#">European</a>
	print "        <a href="#">French</a>
	print "        <a href="#">German</a>
	print "        <a href="#">Greek</a>
	print "        <a href="#">Indian</a>
	print "        <a href="#">Irish</a>
	print "        <a href="#">Italian</a>
	print "        <a href="#">Japanese</a>
	print "        <a href="#">Jewish</a>
	print "        <a href="#">Korean</a>
	print "        <a href="#">Latin American</a>
	print "        <a href="#">Mediterranean</a>
	print "        <a href="#">Mexican</a>
	print "        <a href="#">Middle Eastern</a>
	print "        <a href="#">Nordic</a>
	print "        <a href="#">Southern</a>
	print "        <a href="#">Spanish</a>
	print "        <a href="#">Thai</a>
	print "        <a href="#">Vietnames</a>
	print "      </div>
	print "    </div>
	print "
	print "  </div>
	print "</body>
	print "</html>
	
}
