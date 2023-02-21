<?php

# OUTPUT

echo "Hello World";

print "Hello World";

#  The differences are small: 
#  echo has no return value while print has a return value of 1 so it can be used in expressions. 
#  echo can take multiple parameters (although such usage is rare) while print can take one argument. 
#  echo is marginally faster than print.

# DATA TYPES

$string = "This is a string";

$integer = 22;

$float = 22.2;

$boolean = true;

$boolean = false;

$empty = null;

# MATH AND OPERATIONS

// CHECK DATA TYPE AND VALUE

var_dump($variable) 

// CHECK INFINITY 

is_finite($variable);
is_infinite($variable);

// NAN NOT A NUMBER

is_nan($variable)

// CHECK NUMERIC 

var_dump(is_numeric($variable));

// CASTING 

// Cast float to int
$x = 23465.768;
$int_cast = (int)$x;
echo $int_cast;

// Cast string to int
$x = "23465.768";
$int_cast = (int)$x;
echo $int_cast;

// PI

pi(); // declares 3.1415926535898

// MIN AND MAX

echo(min(0, 150, 30, 20, -8, -200));  // returns -200
echo(max(0, 150, 30, 20, -8, -200));  // returns 150

// ABSOLUTE VALUE

echo(abs(-6.7));  // returns 6.7

// SQUARE ROOT

echo(sqrt(64));  // returns 8

// ROUND

echo(round(0.60));  // returns 1
echo(round(0.49));  // returns 0

// RANDOM NUMBERS

echo(rand());

echo(rand(10, 100)); // with min and and max parameters

# OPERATORS

// ARITHMETICS

$addition = 2 + 2;

$substraction = 5 - 2;

$multiplication = 2 * 2;

$division = 8 / 2;

$modulus = 8 % 2;

$exponent = 8**2;

// ASSIGNMENTS

x = y	x = y       //	The left operand gets set to the value of the expression on the right	
x += y	x = x + y	//  Addition	
x -= y	x = x - y   // 	Subtraction	
x *= y	x = x * y	//  Multiplication	
x /= y	x = x / y	//  Division	
x %= y	x = x % y	//  Modulus

// COMPARISON 

$x == $y  // equal
$x === $y // identical
$x != $y  // not equal
$x <> $y  // not equal
$x !== $y // not identical
$x > $y	 // greater than
$x < $y	// less than
$x >= $y // greater than or equal
$x <= $y // less than or equal
$x <=> $y // Returns an integer less than, equal to, or greater than zero, depending on if $x is less than, equal to, or greater than $y.

// INCREMENT/DECREMENT

++$x //	Increments $x by one, then returns $x	
$x++ //	Returns $x, then increments $x by one	
--$x // Decrements $x by one, then returns $x	
$x-- //	Returns $x, then decrements $x by one

// LOGICAL OPERATORS

$x and $y // True if both $x and $y are true	
$x or $y //	True if either $x or $y is true	
$x xor $y // True if either $x or $y is true, but not both	
$x && $y //	True if both $x and $y are true	
$x || $y //	True if either $x or $y is true	
!$x // True if $x is not true

// STRING OPERATORS

$txt1 . $txt2 // Concatenation of $txt1 and $txt2	
$txt1 .= $txt2 // Appends $txt2 to $txt1	


// ARRAY OPERATORS

$x + $y // Union of $x and $y	
$x == $y //	Returns true if $x and $y have the same key/value pairs	
$x === $y // Returns true if $x and $y have the same key/value pairs in the same order and of the same types	
$x != $y //	Returns true if $x is not equal to $y	
$x <> $y //	Returns true if $x is not equal to $y	
$x !== $y // Returns true if $x is not identical to $y

// CONDITIONAL ASSIGMENT OPERATORS

// Ternary	
$x = expr1 ? expr2 : expr3	
// Returns the value of $x.
// The value of $x is expr2 if expr1 = TRUE.
// he value of $x is expr3 if expr1 = FALSE	

// Null coalescing
$x = expr1 ?? expr2	
// Returns the value of $x.
// The value of $x is expr1 if expr1 exists, and is not NULL.
// If expr1 does not exist, or is NULL, the value of $x is expr2.



?>









