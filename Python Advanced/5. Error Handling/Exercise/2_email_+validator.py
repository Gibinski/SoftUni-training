from re import findall

class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

pattern_name = r"[\w+\.]+"
pattern_domain = r"\.[a-z]+"

email = input()
valid_domain = [".com", ".bg", ".org", ".net"]

while email:
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(findall(pattern_name, email.split("@")[0])[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif findall(pattern_domain, email.split("@")[1])[0] not in valid_domain:
        raise InvalidDomainError(f"Domain must be one of the folowing: {', '.join(valid_domain)}")

    email = input()

