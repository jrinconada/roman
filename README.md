# Roman Numeral Translator
Trying different algorithms to translate modern **decimal** numbers to **roman numerals**
## Explanation of the algorithms
### Algorithm A
This is the **simple** and **efficient** way to do it. Defining four tuples of all combinations of numbers:
- **To 10**: 1,2,3,4...10
- **To 100**: 10, 20, 30, 40...100 
- **To 1000**: 100, 200, 300, 400...1000
- **The last 3**: 1000, 2000, 3000

Getting the proper combination for every digit. For example, for the number `437`:
- For the first digit, access the third tuple with `4` and get `CD`
- For the second digit, access the second tuple with `3` and get `XXX`
- For the third digit, access the first tuple with `8` and get `VII`
- Finally, Concatenate the all results to get `CDXXXVII`

### Algorithm B
This a more **complex** and less efficient algorithm but also more **interesting**... See code and try to understand it for yourself.
 
## Usage
This program is compose of several Python 3 scripts with no dependencies on external libraries. 
Given that you have Python 3 installed, run it as any Python script:
```
python main.py
```
## Further improvements
Add translation from roman numeral to modern decimal number system