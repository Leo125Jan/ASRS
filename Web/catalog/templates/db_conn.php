<?php
	//connect to database
	$conn=mysqli_connect('localhost','To','SQL123','qrcode');

	// check connection
	if(!$conn)
	{
		echo 'Connection error: '. mysqli_connect_error();
	}
?>