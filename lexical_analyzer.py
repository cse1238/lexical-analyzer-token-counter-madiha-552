import re
import sys

# C/C++/Java-style keywords
KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue", "default",
    "do", "double", "else", "enum", "extern", "float", "for", "goto",
    "if", "int", "long", "register", "return", "short", "signed",
    "sizeof", "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while", "class", "public",
    "private", "protected", "new", "delete", "try", "catch", "throw",
    "this", "true", "false", "boolean", "package", "import"
}

# Operators are checked longest-first
OPERATORS = [
    ">>=", "<<=", "++", "--", "==", "!=", ">=", "<=",
    "&&", "||", "+=", "-=", "*=", "/=", "%=", "&=", "|=",
    "^=", "->", "<<", ">>",
    "+", "-", "*", "/", "%", "=", ">", "<", "!", "&", "|", "^"
]

SEPARATORS = {
    "(", ")", "{", "}", "[", "]", ";", ",", ":"
}

SPECIAL_SYMBOLS = {
    ".", "#", "@", "$", "?"
}


def lexical_analyzer(source):
    tokens = []

    # Remove and record comments
    comment_pattern = re.compile(
        r'//[^\n]*|/\*[\s\S]*?\*/'
    )

    # Strings and character literals
    token_pattern = re.compile(
        r'"(?:\\.|[^"\\])*"'       # String literal
        r"|'(?:\\.|[^'\\])*'"      # Character literal
        r'|(?:\d+\.\d*|\.\d+|\d+)' # Number
        r'|[A-Za-z_][A-Za-z0-9_]*' # Identifier/keyword
        r'|>>=|<<=|\+\+|--|==|!=|>=|<=|&&|\|\||'
        r'|\+=|-=|\*=|/=|%=|&=|\|=|\^=|->|<<|>>'
        r'|[+\-*/%=><!&|^]'
        r'|[()[\]{};,:\.]'
        r'|[#@$?]'
    )

    pos = 0

    while pos < len(source):
        comment_match = comment_pattern.match(source, pos)

        if comment_match:
            comment = comment_match.group()
            tokens.append((comment, "Comment"))
            pos = comment_match.end()
            continue

        match = token_pattern.match(source, pos)

        if match:
            token = match.group()

            if token.startswith('"'):
                token_type = "String Literal"

            elif token.startswith("'"):
                token_type = "Constant"

            elif re.fullmatch(r'(?:\d+\.\d*|\.\d+|\d+)', token):
                token_type = "Constant"

            elif token in KEYWORDS:
                token_type = "Keyword"

            elif re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', token):
                token_type = "Identifier"

            elif token in OPERATORS:
                token_type = "Operator"

            elif token in SEPARATORS:
                token_type = "Separator"

            elif token in SPECIAL_SYMBOLS:
                token_type = "Special Symbol"

            else:
                token_type = "Unknown"

            tokens.append((token, token_type))
            pos = match.end()

        else:
            pos += 1

    return tokens


def print_tokens(tokens):
    print("\nTOKEN TYPE")
    print("-" * 48)

    counts = {
        "Keyword": 0,
        "Identifier": 0,
        "Operator": 0,
        "Constant": 0,
        "String Literal": 0,
        "Separator": 0,
        "Special Symbol": 0,
        "Comment": 0
    }

    for token, token_type in tokens:
        # Comments are identified but not displayed in the sample output.
        # They are still counted.
        if token_type == "Comment":
            counts["Comment"] += 1
            continue

        print(f"{token:<25} {token_type}")
        counts[token_type] = counts.get(token_type, 0) + 1

    print("\n" + "-" * 48)
    print("Token Count")

    print(f"Keywords        : {counts['Keyword']}")
    print(f"Identifiers     : {counts['Identifier']}")
    print(f"Operators       : {counts['Operator']}")
    print(f"Constants       : {counts['Constant']}")
    print(f"String Literals : {counts['String Literal']}")
    print(f"Separators      : {counts['Separator']}")
    print(f"Special Symbols : {counts['Special Symbol']}")
    print(f"Comments        : {counts['Comment']}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python lexical_analyzer.py <source_file>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, "r", encoding="utf-8") as file:
            source = file.read()

        tokens = lexical_analyzer(source)
        print_tokens(tokens)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
