# Isotheric languages interpreter

## Thue

Thue rules:
* Every line is a new instruction
* '::=' indicates the end of the code and the start of the data
* 'a::=b' will replace a random 'a' in the data with a 'b'
* 'a::=~b' will delete a random 'a' in the data and print a 'b'
* The data is a line of characters
* Instructions are read in a random order
* 'a::=:::' replaces a with an input from the user

```bash
python3 thue.py
```
Typing this command will ask for a file name to read containing the thue program. Once entered, it will run the thue program and show the steps and instructions it is following.

There is a sample programm '**adder**' to test thue.py which adds 2 integers.
