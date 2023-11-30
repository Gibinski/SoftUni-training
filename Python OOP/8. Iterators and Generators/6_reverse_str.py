def reverse_text(text: str):
    text_to_list = list(text)

    while text_to_list:
        yield text_to_list.pop()


for char in reverse_text("step"):
    print(char, end='')