import json
from tkinter import Entry, Tk, Label, Button

with open('questions.json', 'r') as openfile:
    try:
        json_object = json.load(openfile)
    except json.decoder.JSONDecodeError:
        raise Exception("'questions.json' file is empty")

qList = list(json_object.keys())

aList = list(json_object.values())

max = len(qList)
num = 0


root = Tk()
root.geometry("1000x500+700+500")
root.title('Quiz')
label1 = Label(root, text=qList[num])


def display():
    # myLabel = Label(root, text=json_object)
    # myLabel.pack()
    # label1 = Label(root, text=qList[num])
    label1.config(text=f'Q{num+1}: {qList[num]}')
    label1.pack()
    entry1.delete(0, "end")


def Finish():
    label2 = Label(root, fg="green", width=30, borderwidth=30,
                   text=f'Correct Answers:{Score}', font=('SansSerif 40'))
    label3 = Label(root, fg="red", width=30, borderwidth=30,
                   text=f'Wrong Answers:{max - Score}', font=('SansSerif 40'))
    finishLabel = Label(root, fg='black', width=30, borderwidth=30,
                        text='Quiz Completed Successfully', font=('Arial 50'))
    label2.pack()
    label3.pack()
    finishLabel.pack()


entry1 = Entry(root, width=50, font=('Arial 24'))
entry1.pack()
Score = 0
display()


def Checker():
    global max, num, Score

    if num < max:

        if json_object[qList[num]].lower() == entry1.get().lower():
            msg = Label(root, text=f'Q{num + 1}: correct')
            msg.pack()
            num += 1
            Score += 1
            if num < max:
                display()
            else:
                myButton.destroy()
                Finish()

        elif json_object[qList[num]].lower() != entry1.get().lower():
            msg = Label(root, text=f'Q{num + 1}: wrong')
            msg.pack()
            num += 1
            if num < max:
                display()
            else:
                myButton.destroy()
                Finish()

        else:
            myButton.destroy()


myButton = Button(root, text='Submit', command=Checker, fg='Blue', bg="white")

myButton.pack()
root.mainloop()
