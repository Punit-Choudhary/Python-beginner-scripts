from tkinter import Tk, Label, Entry, Button
import json
root = Tk()
root.geometry("1500x600+900+800")
root.config(bg="aqua")
root.title('Add Questions For Quiz')

diction = {}

questionLabel = Label(root, width=30, text="Enter questions below", bg="aqua")
questionLabel.pack()
question = Entry(root, width=50, font=('Arial 34'))
question.pack(padx=10, pady=10)

answerLabel = Label(root, width=30, text="Enter Answers below", bg="aqua")
answerLabel.pack()
answer = Entry(root, width=50, font=('Arial 24'))
answer.pack(padx=10, pady=10)


def Click():
    diction.update({question.get(): answer.get()})
    myLabel = Label(root, text=str(diction))
    myLabel.pack()
    question.delete(0, "end")
    answer.delete(0, "end")
    with open('questions.json', 'w') as outfile:
        json.dump(diction, outfile)


def Finish():
    label = Label(root, fg="green",
                  text="Stored Question succesfully in 'questions.json'",
                  font=('SansSerif 40'), bg="aqua")
    finishLabel = Label(root, fg='black', width=30, borderwidth=30,
                        text='Quiz Making Completed Successfully',
                        font=('Arial 50'), bg="aqua")
    label.pack()
    finishLabel.pack()


myButton = Button(root, text='Submit', command=Click, fg='Blue', bg="white")
myButton.pack(pady=10)
finishButton = Button(root, text='Finish',
                      command=Finish, fg='white', bg='black')
finishButton.pack(pady=10)


root.mainloop()
