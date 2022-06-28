q1 = """1.Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom
"""

q2 = """2.Which type of Programming does Python support?
a) object-oriented programming
b) structured programming
c) functional programming
d) all of the mentioned
"""

q3 = """3.Is Python case sensitive when dealing with identifiers?
a) no
b) yes
c) machine dependent
d) none of the mentioned
"""

q4 = """4.Which of the following is the correct extension of the Python file?
a) .python
b) .pl
c) .py
d) .p
"""

q5 = """Is Python code compiled or interpreted?
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted
"""
name = input("Enter Your Name: ").title()

question = {q1: "c", q2: "d", q3: "b", q4: "c", q5: "b"}
score = 0

for i in question:
    print(i)
    skip_question = input("Do you want skip this Question? 'yes' or 'no: ").lower()
    if skip_question == 'yes':
        print()
        continue

    answer = input("Enter Correct Answer: ")

    if answer == question[i]:
        print("Correct Answer!\n")
        score += 1

    else:
        print("Wrong Answer!\n")
        score -= 1

print(f"Congrates! {name}, Your Total Score: ", score, "\n")
