<?php
session_start();
$OUTPUT = NULL;

$server="localhost";
$username="To";
$password="SQL123";
$databasename="qrcode";

//PROCESS SEARCH WHEN FORM SUBMITTED
if (isset($_POST['search'])) 
{
  //SEARCH FOR Wines
  $conn = mysqli_connect($server, $username, $password, $databasename);
  $search = $conn->real_escape_string($_POST['search']);
  $resultSet = $conn->query("SELECT * FROM wine WHERE Code='$search' ");
  //DISPLAY RESULTS
  if ($resultSet->num_rows>0)
  {
    while($rows = $resultSet->fetch_assoc())
    {
      $Code = $rows['Code'];
      $Name = $rows['Name'];
      $Firm = $rows['Firm'];
      $OUTPUT = "Code: $Code <br /> Name: $Name <br /> Firm: $Firm <br /> ";
    }
  }
  else
    {
      $OUTPUT = "No results found";
    }
  }
$conn->close();
?>

<?php
echo $OUTPUT;
?>

