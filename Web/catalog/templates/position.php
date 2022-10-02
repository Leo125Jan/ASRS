<?php header("Refresh: 3")?>
<?php 
			$server="localhost";
                		$username="To";
                		$password="SQL123";
                		$databasename="qrcode";

                		$conn = mysqli_connect($server, $username, $password, $databasename);
                		if(!$conn)
                		{
                			die("Connection failed" .mysqli_connect_erroe());
                		} ?>
<!DOCTYPE html>
<head>
	<link rel="stylesheet" href="http://apps.bdimg.com/libs/jquerymobile/1.4.5/jquery.mobile-1.4.5.min.css">
</head>
<html>
{% include 'header.php' %}
<body>
	<center><h1
		class="container white-text"
		style="font-size:48px;" 
	> <font face ='Volkhov', serif> Product Position</h1> </font></center>


	<div class="box">

		<section class="ui-grid-c">

			<div class="ui-block-a"><h5>3-1</h5></div>
			<div class="ui-block-b"><h5>3-2</h5></div>
			<div class="ui-block-c"><h5>3-3</h5></div>
			<div class="ui-block-d"><h5>3-4</h5></div>			
			<div class="ui-block-a" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px;"><p>
            <?php
			$sql ="SELECT Code FROM ps WHERE Ro = '3' AND Co = '1'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}
			 ?>
			</p></div>

			<div class="ui-block-b" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px"><p>            
			<?php
			$sql ="SELECT Code FROM ps WHERE Ro = '3' AND Co = '2'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}
			 ?></p></div>

			<div class="ui-block-c" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px"><p>
			<?php
			$sql ="SELECT Code FROM ps WHERE Ro = '3' AND Co = '3'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}
			 ?>
			</p></div>

			<div class="ui-block-d" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px"><p>
			<?php
			$sql ="SELECT Code FROM ps WHERE Ro = '3' AND Co = '4'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}?>
			</p></div>

			<div class="ui-block-a"><h5>2-1</h5></div>
			<div class="ui-block-b"><h5>2-2</h5></div>
			<div class="ui-block-c"><h5>2-3</h5></div>
			<div class="ui-block-d"><h5>2-4</h5></div>			
			<div class="ui-block-a" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px;"><p>
            <?php
			$sql ="SELECT Code FROM ps WHERE Ro = '2' AND Co = '1'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}
			 ?>
			</p></div>
			
			<div class="ui-block-b" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px"><p>            
			<?php
			$sql ="SELECT Code FROM ps WHERE Ro = '2' AND Co = '2'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}
			 ?></p></div>

			<div class="ui-block-c" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px"><p>
			<?php
			$sql ="SELECT Code FROM ps WHERE Ro = '2' AND Co = '3'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}
			 ?>
			</p></div>

			<div class="ui-block-d" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px"><p>
			<?php
			$sql ="SELECT Code FROM ps WHERE Ro = '2' AND Co = '4'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}?>
			</p></div>

			<div class="ui-block-a"><h5>1-1</h5></div>
			<div class="ui-block-b"><h5>1-2</h5></div>
			<div class="ui-block-c"><h5>1-3</h5></div>
			<div class="ui-block-d"><h5>1-4</h5></div>			
			<div class="ui-block-a" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px;"><p>
            <?php
			$sql ="SELECT Code FROM ps WHERE Ro = '1' AND Co = '1'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}
			 ?>
			</p></div>
			
			<div class="ui-block-b" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px"><p>            
			<?php
			$sql ="SELECT Code FROM ps WHERE Ro = '1' AND Co = '2'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}
			 ?></p></div>

			<div class="ui-block-c" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px"><p>
			<?php
			$sql ="SELECT Code FROM ps WHERE Ro = '1' AND Co = '3'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}
			 ?>
			</p></div>

			<div class="ui-block-d" style="background:url('box.png') no-repeat;background-size: 310px 220px; width: 300px ;height:200px"><p>
			<?php
			$sql ="SELECT Code FROM ps WHERE Ro = '1' AND Co = '4'";
			$query = $conn->query($sql);
            $row = $query->fetch_assoc();
            if ($query->num_rows>0) {
            	echo $row['Code'];
            	// code...
            }
            else{
			 echo 'x';}?>
			</p></div>

			
 
		</section> 
	</div>



</body>
{% include 'footer.html' %}
</html>