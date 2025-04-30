# Escreva a função aqui

def fix_search_value(string):
    return string.strip()


if __name__ == '__main__':
    # stripped_string deve conter o valor de 'A' (sem espaços)
    stripped_string = fix_search_value('     A     ')
    print(f"'{stripped_string}'")