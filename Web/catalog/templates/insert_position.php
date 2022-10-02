<?php
session_start();
$server="localhost";
$username="To";
$password="SQL123";
$databasename="qrcode";

$conn = mysqli_connect($server, $username, $password, $databasename);

if(!$conn)
{
	die("Connection failed" .mysqli_connect_erroe());
}
if(isset($_POST['text']))
{
	$text = $_POST['text'];
	$Ro = rand(1,3);
	$Co = rand(1,4);

	$sql =" SELECT * FROM ps ";
	$query = $conn->query($sql);

	$sql = " INSERT INTO ps(Code,Ro,Co) VALUES('$text','$Ro','$Co') ";
	if($conn->query($sql) === TRUE)
	{
		$_SESSION['success'] = 'Successfully set';
	}
	else
	{
		$_SESSION['error'] = $conn->error;
	}
	
}
else
{
	$_SESSION['error'] = 'Please scan your QRcode';
}


header("location: index.php");
$conn->close();
?>
