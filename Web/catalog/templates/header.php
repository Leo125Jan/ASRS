<!--upper links-->
<?php
  session_start();
?>

{% url 'cover' as cover %}
{% url 'NewData' as NewData %}
{% url 'AllData' as AllData %}
{% url 'ProductPosition' as ProductPosition %}
{% url 'Scan' as Scan %}
{% url 'Search' as Search %}
{% url 'LogOut' as LogOut %}

<head>
	<title>ASRS CONTROL</title>
	<!-- Compiled and minified CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Philosopher:ital,wght@1,700&family=Volkhov:wght@700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@600&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Lobster&family=Noto+Serif+TC:wght@600&display=swap" rel="stylesheet">

  <style type="text/css">



    .text-gradient {
  background: linear-gradient(to left, violet, #039be5 , green, yellow, orange, red);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
  }

  	form{
  		max-width: 700px;
  		margin: 80px auto;
  		padding: 50px;
      font-family: 'Philosopher', sans-serif;
      font-family: 'Volkhov', serif;
  	}
    table{
      width: 900px;
      border: 10px ;
      align-items: center;
      margin:10px auto;
      font-family: 'Gelasio', serif;
      color: white;
    }
    
    th{
      border: solid 2px #455a64;
      text-align: center;
      background-color: lightgrey;
      color: black;
      font-size: 20px;
    }
    td{
      border: solid 2px #455a64;
      text-align: center;
      color: black;
      background-color:white ;
      font-family: 'Noto Serif TC', serif;
    }
    .box{
          width: 1200px;
          margin: 10px auto;
          color: black;
          background-color:white ;
          font-family: 'Philosopher', sans-serif;
          font-family: 'Volkhov', serif;
    }
    .ui-block-a,.ui-block-b,.ui-block-c,.ui-block-d{
    background-color: lightgrey;
    border: 3px solid black;
    width: 50px;
    text-align: center;
    font-size: 40px;
    height
    }
    p{
     position: relative;
     top: 60px;
     right:25px; 
    }
    
  </style>
</head>
<body style="background-image: linear-gradient(to right, #434343 0%, black 100%);">
	<nav style="background-image: linear-gradient(to right, #434343 0%, black 100%);">
    <div class="container">
      <!--cover link-->
      <a  href="{% url 'cover' %}" class="brand-logo text-gradient">ASRS CONTROL CENTER</a>
      <ul id="nav-mobile" class="right hide-on-small-and-down">
       


<!--         <?php
          if(isset($_SESSION["useruid"]))
          {
            ?> -->

            <li><a href="{% url 'NewData' %}" >New Data</a></li>
            <li><a href="{% url 'AllData' %}">All Data</a></li>
            <li><a href="{% url 'ProductPosition' %}">Product position</a></li>
            <li><a href="{% url 'Scan' %}" >Scan</a></li>
            <li><a href="{% url 'Search' %}" >Search</a></li>
            <li><a href="{% url 'LogOut' %}" >Log out</a></li>

            <?php
          }
          else
          {
            ?>
            <li><a href="login.php" >Log in</a></li>
            <!-- li><a href="signup.php" class="btn brand z-depth-0">Sign up</a></li>; -->

      </ul>
    </div>
  </nav>
