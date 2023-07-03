def validate_email(email):
    if not email[0].isalpha():
        raise ValueError("Username should starts with a letter")

    i = 0
    while email[i] != "@":
        if (
            not email[i].isalpha()
            and not email[i].isdigit()
            and email[i] not in ("_", "-")
        ):
            raise ValueError(
                "Username contain only letters,digits, dashes or underscores"
            )
        i += 1
    i += 1

    while email[i] != ".":
        if not email[i].isalpha() and not email[i].isdigit():
            raise ValueError("Website should contain only letters, and digits")
        i += 1
    i += 1

    counter = 0
    while i < len(email):
        counter += 1
        i += 1
    if counter > 3:
        raise ValueError("Extension maximum length is 3")

    return None
