<?php
	include('templates/header.php');
?>

<section class="container black-text">
	<form class="white" action="includes/login.inc.php" method="post">
		<h4 class="center">Log In</h4>
		<input type="text" name="uid" placeholder="Username...">
		<input type="password" name="pwd" placeholder="Password...">
		<div class="center">
			<input type="submit" name="submit" value="Log in" class="btn brand z-depth-0"style="background-image: linear-gradient(to right, #434343 0%, black 100%);">
		</div>

		<?php
		if(isset($_GET["error"]))
		{
				if($_GET["error"] == "emptyinput")
			{
				echo "<h5><center>Fill in all fields!</h5>";
			}
			else if($_GET["error"] == "wronglogin")
			{
				echo "<h5><center>Incorrect login information!</h5>";
			}
		}
		?>

	</form>
</section>

<?php
	include('templates/footer.php');
?>