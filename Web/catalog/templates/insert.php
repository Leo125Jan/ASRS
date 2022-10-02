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
	$date = date('Y-m-d');

	$sql =" SELECT * FROM table_attendance WHERE Code='$text' AND LOGDATE='$date' AND STATUS='0' ";
	$query = $conn->query($sql);
	if($query->num_rows>0)
	{
		$sql = " UPDATE table_attendance SET TIMEOUT=NOW(), STATUS='1' WHERE Code='$text' AND LOGDATE='$date' ";
		$query = $conn->query($sql);
		$_SESSION['success'] = 'Successfully time out';
	}
	else
	{
		$sql = "INSERT INTO table_attendance(Code,TIMEIN,LOGDATE,STATUS) VALUES('$text',NOW(),'$date','0')";
		if($conn->query($sql) ===TRUE)
		{
			$_SESSION['success'] = 'Successfully time in';
		}
		else
		{
			$_SESSION['error'] = $conn->error;
		}
	}
	#指定位置的運算
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
header("location: index_Scan.php");
$conn->close();
?>
