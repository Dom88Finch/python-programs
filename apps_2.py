from Quiz import Quiz


quiz_questions  = [" What is batmans' secret identity?\n(a) clark kent \n(b) lex luthor \n(c)bruce wayne \n\n",
					" Who is green arrows' nememsis?\n(a)black canary \n(b) deathstroke \n(c) barry allen \n\n",
					" What island whas oliver queen trapped on for 5 years?\n(a)lianyu \n(b)northern ireland \n(c)isle of man \n\n",
					"Who has not oliver queen in the past?\n(a) Felicity Smoak \n(b) Nyssa Raatko \n(c) Amanda wallace \n\n",
]



quiz_prompt = [	Quiz(quiz_questions[0], "c"),
				Quiz(quiz_questions[1], "b"),
				Quiz(quiz_questions[2], "a"),
				Quiz(quiz_questions[3], "c"),
				]


def run_test(quiz_prompt):
	score  = 0

	for quiz in quiz_prompt:

		answer = input(quiz.intial_input)


		if answer == quiz.answer:
			score += 1

	print("Hello, you have achieved "+ str(score)+ "/"+str(len(quiz_prompt))+ " correct. Well done")


run_test(quiz_prompt)




