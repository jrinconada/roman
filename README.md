# Roman Numeral Translator
Trying different algorithms to translate modern **decimal system** numbers to **roman numerals** and viceversa.
## Explanation of the algorithms
### Algorithm A
This is the **simple** and **efficient** way to do it. Defining four tuples of all combinations of numbers:
- **To 10**: *1,2,3,4...10*
- **To 100**: *10, 20, 30, 40...100*
- **To 1000**: *100, 200, 300, 400...1000*
- **The last 3**: *1000, 2000, 3000*

Getting the proper combination for every digit. For example, for the number *437*:
- For the first digit, access the third tuple with *4* and get `CD`
- For the second digit, access the second tuple with *3* and get `XXX`
- For the third digit, access the first tuple with *8* and get `VII`
- Finally, Concatenate the all results to get `CDXXXVII`

### Algorithm B
This a more **complex** and less efficient algorithm but also more **interesting**... See code and try to understand it for yourself.

### Getting the nth digit
To resolve the problem of getting a digit from a number I explored three different solutions: 
- The pure **mathematical** one: Get the module with 10 to the power of the digit and divide by *10* to power of the digit minus one.
- The **programmer** way: Convert from int to string get, access to the proper index and convert from string to int.
- The **mix**: Similar to the first one but with a loop involved, not very elegant but maybe a little easier for programmers to understand.

## Validation
### Simple validation
- An input number must be between *1* and *3999* to be expressed as a roman numeral.
- A roman numeral must be composed of a combination of these letters: `I`, `V`, `X`, `L`, `C`, `D` or `M`.

### Strict validation
If **algorithm B** is used for translation of roman numerals to decimal number system adding and subtraction rules are applied without any validation, this means that numbers like `IIII`, `IC`, `VV` or even `MMMMMMM` are translated and produce a logical result given the rules (so *4*, *99*, *10* and *70000*).

The translation of invalid numbers is made but with a comment pointing it out and providing the proper roman numeral. The rules checked to consider a roman numeral fully valid are:
- No more than three consecutive numerals
- No more than one consecutive *5* based numeral
- No invalid subtractions (ex: IL, XM, VX)
- No invalid ordering (smaller numbers before bigger ones) if it is not a valid subtraction (ex: IC, IIV, VC, XDM)

## Usage
This program is compose of several Python 3 scripts with no dependencies on external libraries. 
Given that you have Python 3 installed, run it as any Python script:
```
python main.py
```
