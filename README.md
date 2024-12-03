BigInt: Arbitrary-Precision Integer Calculator

This project implements a custom 'BigInt' class to handle large integers with arbitrary precision. It also includes a command-line calculator (REPL) to perform various arithmetic operations and factorials.

---

## Key Features

- **Handles Extremely Large Integers**: Supports numbers much larger than Python's built-in types can natively handle.
- **Basic Arithmetic Operations**:
  - Addition ('add')
  - Subtraction ('sub)
  - Multiplication ('mul')
  - Division ('div')
  - Modulo ('mod')
  - Exponentiation ('pow')
- **Factorial Calculation**: Computes factorials of very large numbers.
- **Custom REPL Interface**: A user-friendly command-line environment to interact with the calculator.

---

*How to Run

1. Clone the repository:
   
2. Run the calculator:
   python big_int_calculator.py
   
3. Follow the prompts in the REPL to perform calculations.
   REPL Command Syntax
   Use the following commands in the REPL:

 add [a] [b]: Add two integers.
 sub [a] [b]: Subtract the second integer from the first.
 mul [a] [b]: Multiply two integers.
 div [a] [b]: Divide the first integer by the second (integer division).
 mod [a] [b]: Find the modulo (remainder) of the first integer divided by the second.
 pow [a] [b]: Raise the first integer to the power of the second.
 fact [a]: Calculate the factorial of a number.
 exit: Exit the calculator.

   

*Implementation details
The BigInt class uses lists to store digits of numbers in reverse order for efficient computation.
Operations such as addition, subtraction, multiplication, and division are implemented digit by digit, mimicking how manual calculations are performed.
Special care is taken to handle:
Different signs (positive/negative numbers).
Carry-over in addition and borrowing in subtraction.
Edge cases like division by zero or invalid inputs.

