from questions import Questions
from data import quiz_data
from quiz_brain import QuizBrain
logo = r'''
     
     ______
    /     /\
   /     /##\
  /     /####\
 /     /######\
(     (########)
 \     \######/
  \     \####/
   \     \##/
    \     \/
     ------

'''
# newq = []
# for i in range(len(gk_questions)):
#     newq.append(Questions(gk_questions[i]['text'],gk_questions[i]['answer']))
#     print(newq[i].quiz)
#     print(newq[i].ans)

question_bank = []
for question in quiz_data:
    question_text = question['text']
    question_ans = question['answer']
    new_question = Questions(question_text,question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print('\n Kya Aap Panchvi Pass se tez hain?')
print(logo)
while quiz.still_has_question():
    quiz.next_question()
print('You have completed the Quiz')
print(f'Your final score is {quiz.score}')
