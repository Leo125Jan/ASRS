<?php
	include('templates/header.php');
?>

<section class="container black-text">
	<form class="white" action="includes/signup.inc.php" method="post">
		<h4 class="center">Sign Up</h4>
		<input type="text" name="name" placeholder="Full name...">
		<input type="text" name="email" placeholder="Email...">
		<input type="text" name="uid" placeholder="Username...">
		<input type="password" name="pwd" placeholder="Password...">
		<input type="password" name="pwdrepeat" placeholder="Repeat password...">
		<div class="center">
			<input type="submit" name="submit" value="Sign Up" class="btn brand z-depth-0">
		</div>

		<?php
		if(isset($_GET["error"]))
		{
			if($_GET["error"] == "emptyinput")
		{
			echo "<h5><center>Fill in all fields!</h5>";
		}
		else if($_GET["error"] == "invaliduid")
		{
			echo "<h5><center>Choose a proper username!</h5>";
		}
		else if($_GET["error"] == "invalidemail")
		{
			echo "<h5><center>Choose a proper email!</h5>";
		}
		else if($_GET["error"] == "passwordsdontmatch")
		{
			echo "<h5><center>Password doesn't match!</h5>";
		}
		else if($_GET["error"] == "stmtfailed")
		{
			echo "<h5><center>Something went wrong, try again!</h5>";
		}
		else if($_GET["error"] == "usernametaken")
		{
			echo "<h5><center>Username already taken!</h5>";
		}
		else if($_GET["error"] == "none")
		{
			echo "<h5><center>You have signed up!</h5>";
		}
	}
	?>

	</form>
</section>

<?php
	include('templates/footer.php');
?>