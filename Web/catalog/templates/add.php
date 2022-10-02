<?php

include('db_conn.php');
$code = $name = $firm ='';
$errors = array('code'=>'','name'=>'','firm'=>'');
if(isset($_POST['submit']))
{
	//check code
	if(empty($_POST['code']))
	{
		$errors['code'] = 'A code is required <br />';
	}
		//check name
	if(empty($_POST['name']))
	{
		$errors['name'] = 'A name is required <br /> ';
	}
		//check firm
	if(empty($_POST['firm']))
	{
		$errors['firm'] = 'A firm is required <br /> <h5><center>Errors in the form</h5>';
	}

	#if(array_filter($errors))
	#{
		#echo "<h5><center>Errors in the form</h5>";
	#}
	else
	{
		$code = mysqli_real_escape_string($conn,$_POST['code']);
		$name = mysqli_real_escape_string($conn,$_POST['name']);
		$firm = mysqli_real_escape_string($conn,$_POST['firm']);

		$sql = "INSERT INTO wine(Code,Name,Firm) VALUES('$code','$name','$firm')";


		if(mysqli_query($conn,$sql))
		{
			$errors['firm'] = '<br /> <h5><center>Form is vaild</h5>';
			sleep(2);
			header("Refresh:0");
			#echo "<h5><center>Form is vaild</h5>";
		}
		else
		{
			echo 'query error: ' . mysqli_error($conn);
		}
	}
}//end of POST check
?>

<!DOCTYPE html>
<html>
	
	{% include 'header.php' %}

	<section class="container black-text">
		<form class="white" action="add.php" method="POST">
			<h4 class="center">Add Wine Information</h4>
			<input type="text" name="code" placeholder="Wine Code..." value="<?php echo htmlspecialchars($code) ?>">
			<div class="red-text"><?php echo $errors['code'];?></div>
			<input type="text" name="name" placeholder="Name..." value="<?php echo htmlspecialchars($name) ?>">
			<div class="red-text"><?php echo $errors['name'];?></div>
			<input type="text" name="firm" placeholder="Firm..." value="<?php echo htmlspecialchars($firm) ?>">
			<div class="red-text"><?php echo $errors['firm'];?></div>
			<div class="center">
				<input type="submit" name="submit" value="submit" class="btn brand z-depth-0" style="background-image: linear-gradient(to right, #434343 0%, black 100%);">
			</div>
		</form>
	</section>

	{% include 'footer.html' %}

</html>