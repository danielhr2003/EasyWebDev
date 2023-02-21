<?php

# SELECTION CONTROL

// IF, ELSE, ELSEIF

$age = 19;

if ($age > 18) {
   echo $age . " is greater than 18";
}
elseif ($age < 18) {
    echo $age . " is less than 18";
}
else {
    echo "Age is " . $age;
}

// SWITCH

$favcolor = "red";

switch ($favcolor) {
  case "red":
    echo "Your favorite color is red!";
    break;
  case "blue":
    echo "Your favorite color is blue!";
    break;
  case "green":
    echo "Your favorite color is green!";
    break;
  default:
    echo "Your favorite color is neither red, blue, nor green!";
}

# REPETITION CONTROL 

// WHILE

$x = 1;

while($x <= 5) {
  echo "The number is: $x <br>";
  $x++;
}

// DO..WHILE

$x = 1;

do {
  echo "The number is: $x <br>";
  $x++;
} while ($x <= 5);

// FOR

for ($x = 0; $x <= 10; $x++) {
    echo "The number is: $x <br>";
  }

// init counter: Initialize the loop counter value
// est counter: Evaluated for each loop iteration. 
// If it evaluates to TRUE, the loop continues. If it evaluates to FALSE, the loop ends.
// increment counter: Increases the loop counter value

// FOR EACH

// The following example will output the values of the given array ($colors):
$colors = array("red", "green", "blue", "yellow");

foreach ($colors as $value) {
  echo "$value <br>";
}

// The following example will output both the keys and the values of the given array ($age):
$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");

foreach($age as $x => $val) {
  echo "$x = $val<br>";
}

// BREAK AND CONTINUE

// The break statement can also be used to jump out of a loop.

for ($x = 0; $x < 10; $x++) {
  if ($x == 4) {
    break;
  }
  echo "The number is: $x <br>";
}

// The continue statement breaks one iteration (in the loop), if a specified condition occurs,
// and continues with the next iteration in the loop.

for ($x = 0; $x < 10; $x++) {
    if ($x == 4) {
      continue;
    }
    echo "The number is: $x <br>";
  }

?>