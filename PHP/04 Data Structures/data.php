<?php
# ARRAYS

/* 
In PHP, there are three types of arrays:

Indexed arrays - Arrays with a numeric index
Associative arrays - Arrays with named keys
Multidimensional arrays - Arrays containing one or more arrays 
*/

# INDEXED ARRAYS

$cars = array("Volvo", "BMW", "Toyota");
echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";

// The count() function is used to return the length (the number of elements) of an array:

echo count($cars);

// To loop through and print all the values of an indexed array, you could use a for loop, like this:

$cars = array("Volvo", "BMW", "Toyota");
$arrlength = count($cars);

for($x = 0; $x < $arrlength; $x++) {
  echo $cars[$x];
  echo "<br>";
}

# ASSOCIATIVE ARRAY

// There are two ways to create an associative array: 

$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43"); // OR..

$age['Peter'] = "35";
$age['Ben'] = "37";
$age['Joe'] = "43";

// EXAMPLE

$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
echo "Peter is " . $age['Peter'] . " years old.";

// To loop through and print all the values of an associative array, you could use a foreach loop, like this:

 $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");

 foreach($age as $x => $x_value) {
      echo "Key=" . $x . ", Value=" . $x_value;
      echo "<br>";
    }

# MULTIDIMENSIONAL ARRAY

// A multidimensional array is an array containing one or more arrays. Check the following table:

// Name	        Stock	Sold
// Volvo	    22	    18
// BMW	        15	    13
// Saab	        5	    2
// Land Rover   17	    15

$cars = array (
    array("Volvo",22,18),
    array("BMW",15,13),
    array("Saab",5,2),
    array("Land Rover",17,15)
  );

// Now the two-dimensional $cars array contains four arrays, and it has two indices: row and column.

// To get access to the elements of the $cars array we must point to the two indices (row and column):

echo $cars[0][0].": In stock: ".$cars[0][1].", sold: ".$cars[0][2].".<br>";
echo $cars[1][0].": In stock: ".$cars[1][1].", sold: ".$cars[1][2].".<br>";
echo $cars[2][0].": In stock: ".$cars[2][1].", sold: ".$cars[2][2].".<br>";
echo $cars[3][0].": In stock: ".$cars[3][1].", sold: ".$cars[3][2].".<br>";

// We can also put a for loop inside another for loop to get the elements of the $cars array (we still have to point to the two indices):

for ($row = 0; $row < 4; $row++) {
    echo "<p><b>Row number $row</b></p>";
    echo "<ul>";
    for ($col = 0; $col < 3; $col++) {
        echo "<li>".$cars[$row][$col]."</li>";
    }
    echo "</ul>";
    }

# ARRAY SORTING

// ASCENDING ORDER

$cars = array("Volvo", "BMW", "Toyota");
sort($cars);

// DESCENDING ORDER

$cars = array("Volvo", "BMW", "Toyota");
rsort($cars);

// ASCENDING ORDER ACCORDING TO VALUE

$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
asort($age);

// ASCENDING ORDER ACCORDING TO KEY

$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
ksort($age);

// DESCENDING ORDER ACCORDING TO VALUE

$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
arsort($age);

// DESCENDING ORDER ACCORDING TO KEY

$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
krsort($age);

?>