# Questions


class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer        

q1 = Question("En iyi programlama dili hangisidir?",["PHP","Java","Python","Javascript"],"python")
q2 = Question("En populer yazilim dili hangisidir?",["C#","R","Python","Ruby"],"python")
q3 = Question("En cok para kazandiran yazilim dili hangisidir?",["PHP","Java","Python","Javascript"],"python")
questions = [q1,q2,q3]


class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.index_of_questions = 0
    def getQuestions(self):
        return self.questions[self.index_of_questions]
    def displayQuestion(self):
        question = self.getQuestions()
        print(f"Soru {self.index_of_questions+1}: {question.text}")
        for q in question.choices:
            print("-"+q)
        answer = input()
        self.quess(answer.lower())
    def quess(self,answer):
        question = self.getQuestions()
        if question.checkAnswer(answer):
            self.score += 1
        self.index_of_questions += 1
        if len(questions) > self.index_of_questions:
            self.displayQuestion()
        else:
            self.showScore()
    def showScore(self):
        print(f"{self.index_of_questions} tane soruya {self.score} dogru cevap verdiniz.Basari oraniniz = {(self.score / self.index_of_questions) * 100}") 
        
        


quiz = Quiz(questions)
quiz.displayQuestion()
