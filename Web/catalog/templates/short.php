<head>
	<title>ASRS CONTROL</title>
  	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  	<style type="text/css">
	 .brand
	{
	  	background: #cbb09c !important;
	}
  	.brand-text
  	{
  		color: #cbb09c !important;
  	}
  	form
  	{
  		max-width: 500px;
  		margin: 20px auto;
  		padding: 20px;
  	}
    table
    {
      width: 900px;
      border: 10px;
      align-items: center;
      margin: 20px auto;
    }
  	</style>
</head>
<body class="grey lighten-4">
	<nav class="white z-depth-0">
    <div class="container">
      <a href="cover.php" class="brand-logo brand-text">ASRS CONTROL CENTER</a>
      <ul id="nav-mobile" class="right hide-on-small-and-down">
      	
        <?php
          if(isset($_SESSION["useruid"]))
          {
            echo "<li><a href='includes/logout.inc.php'><h7 style='color:black'>Log out</h7></a></li>";
          }
          else
          {
            echo "<li><a href='signup.php'><h7 style='color:black'>Sign up</h7></a></li>";
            echo "<li><a href='login.php'><h7 style='color:black'>Log in</h7></a></li>";
          }
        ?>

      </ul>
    </div>
  </nav>

        <li><a href="add.php" class="btn brand z-depth-0">New Data</a></li>
        <li><a href="alldata.php" class="btn brand z-depth-0">All Data</a></li>
        <li><a href="index_Scan.php" class="btn brand z-depth-0">Scan</a></li>
        <li><a href="index_Search.php" class="btn brand z-depth-0">Search</a></li>


                    echo "<li><a href='signup.php'><h5 style='color:black'>Sign up</h5></a></li>";
            echo "<li><a href='login.php'><h5 style='color:black'>Log in</h5></a></li>";