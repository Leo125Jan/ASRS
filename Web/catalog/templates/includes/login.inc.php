<?php

if(isset($_POST["submit"]))
{
	$username = $_POST["uid"];
	$pwd = $_POST["pwd"];

	require_once 'dbh.inc.php';
	require_once 'function.inc.php';

	if(emptyInputLogin($username,$pwd) !== false)
	{
		header("location: ../login.php?error=wronglogin");
		exit();
	}
	loginUser($conn,$username,$pwd);
}
else
{
	header("location: ../login.php");
	exit();
}