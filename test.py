from lexer import Lexer



txt = """function count_even_numbers(A: List): Number => { // salam
    let even_count: Number = 0;

    for (i, v of A) {
        if (v % 2 == 0) {
            even_count = even_count + 1;
        }
    }

    return even_count;
}"""

l = Lexer().get_lexer()
tokens = l.lex(txt)


for token in tokens:
    print(token)