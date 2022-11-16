import unittest, lexer


input_code = """
function count_even_numbers(A: List): Number => {
    let even_count: Number = 0;

    for (i, v of A) {
        if (v % 2 == 0) {
            even_count = even_count + 1;
        }
    }

    return even_count;
}
"""

output = """
function
count_even_numbers
(
A
:
List
)
:
Number
=>
{
let
even_count
:
Number
=
0
;
for
(
i
,
v
of
A
)
{
if
(
v
%
2
==
0
)
{
even_count
=
even_count
+
1
;
}
}
return
even_count
;
}
"""


class TestLexer(unittest.TestCase):
    def runTest(self):
        self.maxDiff = None
        self.assertEqual(lexer.getTokens(input_code), output, "wrong output!")


unittest.main()