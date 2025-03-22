import textwrap

input_string = input()
width = int(input())

wrapped_text = textwrap.wrap(input_string, width)

for line in wrapped_text:
    print(line)
