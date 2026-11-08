def parse_input(user_input : str) -> tuple[str, list[str]]:
    inside_quote = False
    tokens = []
    temp = ""

    for c in user_input:
        if c == '"':
            inside_quote = not inside_quote

        if c == ' ' and not inside_quote:
            tokens.append(temp.replace('"', ''))
            temp = ""
        else:
            temp += c

    tokens.append(temp.replace('"', ''))

    command, *arguments = tokens

    return (command, arguments)
