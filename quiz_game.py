from rich.console import Console


questions :list[tuple[str, list[str], str]] =[
    ("The best CMS in the world?", ["A:wordPress", "B: joomla", "C: Drupal","D: Squarespace"],"A"),
("what is the most popular CMS?",["A: wordpress","B: joomla","C: Drupal","D: Squarespa"],"A"),
("What CMS is known for its user-friendly interface?",["A: Wordpress","B: Joomla","C: Drupal","D: Squarespa"],"D")
]

console=Console()
score = 0
total_correct = 0
CORRECT_BUONS=10
PENALTI=3
for question, options, correct in questions:
    console.print(question,style="bold yellow")
    for option in options:
        console.print(f"{option}\n",style="red")
    user_answer: str = input("your answer (A/B/C/D): ".strip().upper())
    if user_answer  == correct:
        total_correct += 1
        score += CORRECT_BUONS
        console.print('Correct!,\n')
    else:
        score -= PENALTI
        console.print(f"wrong! the correct answer is {correct}.\n ")
print(f"yourr score is:{score}")
print(f"your total correct answer{total_correct}")