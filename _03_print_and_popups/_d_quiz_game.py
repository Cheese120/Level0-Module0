from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

        # Make a new window variable, window = Tk()
    window=Tk()
        # Hide the window using the window's .withdraw() method
    window.withdraw()
        # 1. Create a variable to hold the user's score. Set it equal to zero.
    score=0
        # ASK A QUESTION AND CHECK THE ANSWER
    questionone=simpledialog.askstring(title='Question 1', prompt="What is the product of 33 and 3?")
        #      // 2.  Ask the user a question

        #      // 3.  Use an if statement to check if their answer is correct
    if questionone=='99':
        score+=1
    #      // 4.  if the user's answer was correct, add one to their score 
    questiontwo=simpledialog.askstring(title='question 2', prompt="what is the product of 9 and 26?")
    if questiontwo=='234':
        score+=1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    #      // Option: Subtract a point from their score for a wrong answer
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo (message="Score is " +str(score))
    # Run the window's .mainloop() method
