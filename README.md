# lexical-analyzer-token-counter-madiha-552
 ## 1. TITLE 
 ## Lexical Analyzer & Token Counter
 ## 2. Objective
The objective of this project is to develop a lexical analyzer that reads a source-code file and identifies and counts different types of tokens.
The program identifies:
* Keywords
* Identifiers
* Operators
* Constants/Literals
* String Literals
* Separators/Delimiters
* Special Symbols
* Comments
## 3. Problem Statement
Develop a program in Python that reads a source-code file and performs lexical analysis by identifying different types of tokens.
The program should:
1. Read source code from a file.
2. Identify keywords.
3. Identify identifiers.
4. Identify operators.
5. Identify constants/literals.
6. Identify string literals.
7. Identify separators/delimiters.
8. Identify special symbols.
9. Identify comments.
10. Count the number of tokens in each category.
11. Display each token along with its token type.
## 4. Algorithm
1. Start the program.
2. Read the source-code file.
3. Define the set of programming-language keywords.
4. Scan the source code from left to right.
5. Check whether the current text is a comment.
6. Check whether it is a string or character literal.
7. Check whether it is a numeric constant.
8. Check whether it is a keyword.
9. Check whether it is an identifier.
10. Check whether it is an operator.
11. Check whether it is a separator.
12. Check whether it is a special symbol.
13. Store the token and its corresponding token type.
14. Increment the appropriate token counter.
15. Display all identified tokens.
16. Display the total count of each token type.
17. Stop the program.
## 5. Source Code
The source code is available in:
`lexical_analyzer.py`
The program can be executed using:
bash
python lexical_analyzer.py sample.c
## 6. Sample Input
int sum = a + b;
float average = sum / 2.0;
if (average > 50)
printf("Pass");
## 7. Sample Output
TOKEN TYPE
------------------------------------------------
int                       Keyword
sum                       Identifier
=                         Operator
a                         Identifier
+                         Operator
b                         Identifier
;                         Separator
float                     Keyword
average                   Identifier
=                         Operator
sum                       Identifier
/                         Operator
2.0                       Constant
;                         Separator
if                        Keyword
(                         Separator
average                   Identifier
>                         Operator
50                        Constant
)                         Separator
printf                    Identifier
(                         Separator
"Pass"                    String Literal
)                         Separator
;                         Separator
------------------------------------------------
Token Count
Keywords        : 3
Identifiers     : 7
Operators       : 5
Constants       : 2
String Literals : 1
Separators      : 8
Special Symbols : 0
Comments        : 1
## 8. Token Classification
| Token Type     | Description                                        | Examples                   |
| -------------- | -------------------------------------------------- | -------------------------- |
| Keyword        | Reserved words in a programming language           | `int`, `float`, `if`       |
| Identifier     | Names of variables, functions, etc.                | `sum`, `average`, `printf` |
| Operator       | Symbols used to perform operations                 | `=`, `+`, `/`, `>`         |
| Constant       | Numeric or character values                        | `50`, `2.0`, `'A'`         |
| String Literal | Text enclosed in double quotes                     | `"Pass"`                   |
| Separator      | Symbols used to separate or group program elements | `(`, `)`, `;`              |
| Special Symbol | Other special characters                           | `#`, `@`, `?`              |
| Comment        | Text ignored during program execution              | `// Calculate average`     |
## 9. Test Cases
### Test Case 1: Arithmetic Operations
**Input:**
int a = 10;
int b = 20;
int result = a + b;
**Expected Token Types:**
* Keywords: `int`
* Identifiers: `a`, `b`, `result`, `a`, `b`
* Constants: `10`, `20`
* Operators: `=`, `+`
* Separators: `;`
### Test Case 2: Conditional Statement
**Input:**
if (x >= 10)
{
    printf("Valid");
}
**Expected Token Types:**
* Keyword: `if`
* Identifiers: `x`, `printf`
* Constant: `10`
* Operator: `>=`
* String Literal: `"Valid"`
* Separators: `(`, `)`, `{`, `}`, `(`, `)`, `;`
### Test Case 3: Floating-Point Constant and Comment
**Input:**
float price = 25.50;
// Display price
printf("Price");
**Expected Token Types:**
* Keyword: `float`
* Identifiers: `price`, `printf`
* Constant: `25.50`
* String Literal: `"Price"`
* Operator: `=`
* Comment: `// Display price`
* Separators: `;`, `(`, `)`, `;`
### Test Case 4: Multiple Operators
**Input:**
int x = a * b + c / d;
**Expected Token Types:**
* Keyword: `int`
* Identifiers: `x`, `a`, `b`, `c`, `d`
* Operators: `=`, `*`, `+`, `/`
* Separator: `;`
## 10. Conclusion
The Lexical Analyzer & Token Counter successfully reads source code and breaks it into meaningful lexical tokens.
Each token is classified as a keyword, identifier, operator, constant, string literal, separator, special symbol, or comment.
The program also counts the number of tokens in each category. This project demonstrates the basic working principle of the lexical analysis phase of a compiler and provides a foundation for understanding further compiler phases such as syntax analysis and semantic analysis.
