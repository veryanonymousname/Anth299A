## Week 6

## Pandas filters
import pandas as pd

file = '/users/nick/desktop/anth299a/Data Sets/Historic Global Temperatures.csv'
df = pd.read_csv(file)


df["Date"]
type(df["Date"])
boolean = df["Date"] > 198001
type(boolean)
filter1 = df[df["Date"] > 198001]
type(filter1)


## Regular Expressions

# Regular expressions are a method for pattern matching in strings. There are many variations and uses of regular
# expressions across computer languages, like grep in the command line. Python has the re module built in:

import re
help(re)

sample = "This is just a sample of text, with the word sample showing up twice"
pattern = "This"

# match
# only matches beginnings of strings, and only returns the matched pattern
match = re.match(pattern, sample)
if match:
    print(match.group())
    print(match.string)
    print(match.span())


# findall
# matches every instance anywhere in the data and returns a list
pattern = "sample"
match = re.findall(pattern, sample)
if match:
    print(match)  # findall doesn't use the group method


# search
# searches the whole string and returns the first match
pattern = "sample"
match = re.search(pattern, sample)
if match:
    print(match.group())


# split
# works like the string.split() method, but with regex's more powerful matching
pattern = " "
match = re.split(pattern, sample)
if match:
    print(match) # similar to findall, returns a list instead of group


# sub
# works like .replace()
print(sample)
pattern = "T"
new = re.sub(pattern, 't', sample)
if new:
    print(new)

# Patterns
# These functions are pretty easy to do with string methods, but the important part of the re module is it's pattern matching
r""" 
   The special characters are:
        "."      Matches any character except a newline.
        "^"      Matches the start of the string.
        "$"      Matches the end of the string or just before the newline at
                 the end of the string.
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
        "?"      Matches 0 or 1 (greedy) of the preceding RE.
        *?,+?,?? Non-greedy versions of the previous three special characters.
        {m,n}    Matches from m to n repetitions of the preceding RE.
        {m,n}?   Non-greedy version of the above.
        "\\"     Either escapes special characters or signals a special sequence.
        []       Indicates a set of characters.
                 A "^" as the first character indicates a complementing set.
        "|"      A|B, creates an RE that will match either A or B.
        (...)    Matches the RE inside the parentheses.

    The special sequences consist of "\\" and a character from the list
    below.  If the ordinary character is not on the list, then the
    resulting RE will match the second character.
        \number  Matches the contents of the group of the same number.
        \A       Matches only at the start of the string.
        \Z       Matches only at the end of the string.
        \b       Matches the empty string, but only at the start or end of a word.
        \B       Matches the empty string, but not at the start or end of a word.
        \d       Matches any decimal digit; equivalent to the set [0-9] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode digits.
        \D       Matches any non-digit character; equivalent to [^\d].
        \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode whitespace characters.
        \S       Matches any non-whitespace character; equivalent to [^\s].
        \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
                 in bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the
                 range of Unicode alphanumeric characters (letters plus digits
                 plus underscore).
                 With LOCALE, it will match the set [0-9_] plus characters defined
                 as letters for the current locale.
        \W       Matches the complement of \w.
        \\       Matches a literal backslash.

"""
# side note, r"string" forces the string to be read as plain text, with no escape characters

sample = """
John Doe: johndoe@example.com, Phone: 555-1234-567, Birthday: 1985-10-25
Jane Smith: jane.smith@anotherexample.org, Phone: 555-9876-543, Website: http://janedoe.com
Company XYZ: contact@companyxyz.com, Support: 800-555-0001, Address: 1234 Market St, San Francisco, CA 94105
Project Alpha: Version 1.2.5, Release Date: 2023-07-15, Documentation: https://projectalpha.net/docs
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.
Email: random.person@example.net, Mobile: +1-202-555-0182, LinkedIn: https://www.linkedin.com/in/randomperson
Special Dates: 2024-02-29, 2025-12-31, 2023-01-01
AlphaNumeric: A7B3C9, XYZ123, 789xyz
IPv4 Addresses: 192.168.1.1, 10.0.0.1, 172.16.254.1
IPv6 Address: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
Credit Card Numbers: 1234-5678-9012-3456, 9876-5432-1098-7654 (Note: These are not real credit card numbers)
Patterns: #hashtag, @username, $price, %percentage, ^caret, &ampersand, *asterisk, (parentheses)
"""

email_pattern = "\s[a-z.]+[@][a-z]+[.com|.org|.net]+"
re.findall(email_pattern, sample)

# \s looks for whitespace character " "
# [a-z.] looks for both a-z string characters, or .
    # you could also do [a-zA-Z] or [a-m]
    # [a-zA-Z0-9] == \w
# + matches 1 or more instances of the preceding pattern
# [@] is looking for the '@' charcter specifically
# [a-z]+ matches one or more lowercase letter
# [.com|.org|.net] the vertical line in re is used as an OR statement, so this matches either '.com' or '.org' or '.net'
# + at the end specifies that there must be at least 1 instance of [.com|.org|.net]

email_pattern = "\s[a-z.]+[@][a-z]+[.com|.org|.net]"
re.findall(email_pattern, sample)

file = open('/users/nick/documents/mtdna_alignment.txt', 'r')
lines = file.readlines()
print(lines)
for line in lines:
    match = re.match(r'^target.*?([ACGT]+)', line)
    if match:
        sequence = match.group(1)
        print(sequence)
