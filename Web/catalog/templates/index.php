<?php 

    include('db_conn.php');
	// write query for wine
	$sql = 'SELECT Code, Name, Firm FROM wine ';

	// get the result set (set of rows)
	$result = mysqli_query($conn, $sql);

	// fetch the resulting rows as an array
	$wine = mysqli_fetch_all($result, MYSQLI_ASSOC);

	// free the $result from memory (good practise)
	mysqli_free_result($result);

	//close connection
	mysqli_close($conn);
?>

<!DOCTYPE html>
<html>
	{% include 'header.php' %}


	{% include 'footer.html' %}

</html>
