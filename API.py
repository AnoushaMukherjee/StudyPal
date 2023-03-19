import openai
import criteria
class ChatGPT:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_answer(self, prompt, correct_answer, options):
        # Generate multiple-choice question
        question = "Which of the following is " + prompt + "?"
        for option in options:
            question += "\n- " + option
        requirements = criteria.part1 + question + criteria.part2 + criteria.part3 + criteria.part4 + criteria.part5
        # Generate answer using ChatGPT API
        completions = openai.Completion.create(
            model="text-davinci-003",
            prompt=requirements,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return completions.choices[0].text.strip()


    def question1(self, answer):
        #question 1
        x = answer
        one, two, three = x.find("1. "), x.find("A. "), x.find("B. ")
        four, five, six = x.find("C. "), x.find("D. "), x.find("2. ")
        y, z, r, f, p = x[one:two], x[two:three], x[three:four], x[four:five], x[five:six]
        return (y, z, r, f, p) 
    
    def question2(self, answer):
        #question 2
        x = answer
        x = x[x.find("2. "):]
        one, two, three = x.find("2. "), x.find("A. "), x.find("B. ")
        four, five, six = x.find("C. "), x.find("D. "), x.find("3. ")
        y, z, r, f, p = x[one:two], x[two:three], x[three:four], x[four:five], x[five:six]
        return (y, z, r, f, p)
    
    def question3(self, answer):
        #question 3
        x = answer
        x = x[x.find("3. "):]
        one, two, three = x.find("3. "), x.find("A. "), x.find("B. ")
        four, five, six = x.find("C. "), x.find("D. "), x.find("4. ")
        y, z, r, f, p = x[one:two], x[two:three], x[three:four], x[four:five], x[five:six]
        return (y, z, r, f, p)
    
    def question4(self, answer):
        #question 4
        x = answer
        x = x[x.find("4. "):]
        one, two, three = x.find("4. "), x.find("A. "), x.find("B. ")
        four, five, six = x.find("C. "), x.find("D. "), x.find("5. ")
        y, z, r, f, p = x[one:two], x[two:three], x[three:four], x[four:five], x[five:six]
        return (y, z, r, f, p)

    def question5(self, answer):
        #question 5
        x = answer
        x = x[x.find("5. "):]
        one, two, three = x.find("5. "), x.find("A. "), x.find("B. ")
        four, five, six = x.find("C. "), x.find("D. "), x.find("6. ")
        y, z, r, f, p = x[one:two], x[two:three], x[three:four], x[four:five], x[five:six]
        return (y, z, r, f, p)

    def question6(self, answer):
        #question 6
        x = answer
        x = x[x.find("6. "):]
        one, two, three = x.find("6. "), x.find("A. "), x.find("B. ")
        four, five, six = x.find("C. "), x.find("D. "), x.find("7. ")
        y, z, r, f, p = x[one:two], x[two:three], x[three:four], x[four:five], x[five:six]
        return (y, z, r, f, p)

    def question7(self, answer):
        #question 7
        x = answer
        x = x[x.find("7. "):]
        one, two, three = x.find("7. "), x.find("A. "), x.find("B. ")
        four, five, six = x.find("C. "), x.find("D. "), x.find("8. ")
        y, z, r, f, p = x[one:two], x[two:three], x[three:four], x[four:five], x[five:six]
        return (y, z, r, f, p)

    def question8(self, answer):
        #question 8
        x = answer
        x = x[x.find("8. "):]
        one, two, three = x.find("8. "), x.find("A. "), x.find("B. ")
        four, five, six = x.find("C. "), x.find("D. "), x.find("9. ")
        y, z, r, f, p = x[one:two], x[two:three], x[three:four], x[four:five], x[five:six]
        return (y, z, r, f, p)

    def question9(self, answer):
        #question 9
        x = answer
        x = x[x.find("9. "):]
        one, two, three = x.find("9. "), x.find("A. "), x.find("B. ")
        four, five, six = x.find("C. "), x.find("D. "), x.find("10. ")
        y, z, r, f, p = x[one:two], x[two:three], x[three:four], x[four:five], x[five:six]
        return (y, z, r, f, p)

    def question10(self, answer):
        #question 10
        x = answer
        x = x[x.find("10. "):]
        one, two, three = x.find("10. "), x.find("A. "), x.find("B. ")
        four, five, six = x.find("C. "), x.find("D. "), x.find("Answer")
        y, z, r, f, p = x[one:two], x[two:three], x[three:four], x[four:five], x[five:six]
        return (y, z, r, f, p)
    
    def checkanswer(questionnum, answer):
        # Check if the answer is correct
        x = answer
        answer_key = x[x.find("Answer"):]
        quesindx = answer_key.find(str(questionnum) + ".")
        quesanswr = answer_key[quesindx+3:quesindx+5]
        return quesanswr
    
    def whichquestion(questionnum, options, answer):
        if questionnum==1:
            tup = ChatGPT.question1(options, answer)
        elif questionnum==2:
            tup = ChatGPT.question2(options, answer)
        elif questionnum==3:
            tup = ChatGPT.question3(options, answer)
        elif questionnum==4:
            tup = ChatGPT.question4(options, answer)
        elif questionnum==5:
            tup = ChatGPT.question5(options, answer)
        elif questionnum==6:
            tup = ChatGPT.question6(options, answer)
        elif questionnum==7:
            tup = ChatGPT.question7(options, answer)
        elif questionnum==8:
            tup = ChatGPT.question8(options, answer)
        elif questionnum==9:
            tup = ChatGPT.question9(options, answer)
        else:
            tup = ChatGPT.question10(options, answer)
        return tup