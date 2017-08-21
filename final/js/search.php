<?php
//database configuration
$dbHost = 'localhost';
$dbUsername = 'jmacach1';
$dbPassword = 'Milkshake11';
$dbName = 'jmacach1';
    
//connect with the database
$db = new mysqli($dbHost,$dbUsername,$dbPassword,$dbName) or die('Error connecting to MySQL server.');
    
//get search term
$searchTerm = $_GET['term'];
    
//get matched data from featureprop table
$query = $db->query("SELECT Title FROM faaSeq") or die('Error querying database.');
while ($row = $query->fetch_assoc()) {
  $data[] = $row['value'];
}
    
//return json data
echo json_encode($data);
    
//close mysql
mysqli_close($db);
?>