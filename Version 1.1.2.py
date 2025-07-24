"""
Author:         [Vangie Coloma]
Date:           2025/05/15
Version:        1.1.2
Description:    This program is a math quiz for primary school students. It uses a simple Tkinter interface to ask questions, check answers,
                and give feedback to help kids practice basic and medium math skills.
Language:       Python 3.10
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Initialize the main app window
app = tk.Tk()
app.title("MATH QUIZ")
app.geometry("1200x650")
app.resizable(False, False)

# Function to close the app
def close_window():
    app.destroy()
    print("Closing app...")

    
# List of easy level math questions and answers
easy_questions = [
    {"question": "Vangie has 15 apples. She ate 5 apples. How many apples does she have now?", "answer": "10" },
    {"question": "There are 6 birds on a tree. 4 fly away. How many are left?", "answer": "2" },
    {"question": "Pranav has 5 pencils. He gives 3 to his friends. How many does he have left?","answer": "2" },
    {"question": "Ralph baked 8 cookies. He ate 3. How many are left?", "answer": "5" },
    {"question": "You have 10 candies. You give away 4. How many do you have now?","answer": "6" },
    {"question": "Liam has 7 toy cars. He buys 2 more. How many does he have?", "answer": "9" },
    {"question": "A jar has 9 sweets. You eat 5. How many are in the jar now?", "answer": "4" },
    {"question": "There are 4 frogs. 3 more join. How many frogs are there now?", "answer": "7" },
    {"question": "Abhishek has 20 balloons. 7 flies away. How many are left?", "answer": "13" },
    {"question": "You have 20 dollars.You buy an apple worth 4 dollars. How much money do you have?", "answer": "16" },
]

#List of medium level match questions and answers
medium_questions = [
    {"image": "fig8.png", "question": "What is the gradient of the line EF?", "answer": "3"},
    {"image": "fig1.png", "question": "What is y-intercept?", "answer": "3"},
    {"image": "fig10.png","question": "How would you describe the gtradient of all the lines? Positive, Negative, or Zero", "answer": "Positive"},
    {"image": "fig3.png", "question": "What is the slope of the line?", "answer": "-4"},
    {"image": "fig5.png","question": "How would you describe the gradient of all the lines? Positive, Negative, or Zero", "answer": "Negative"},
    {"image": "fig4.png", "question": "What is the y-intercept?", "answer": "4"},
    {"image": "fig6.png", "question": "What is the gradient of the line KL?", "answer": "-1"},
    {"image": "fig7.png", "question": "How would you describe the gradient of all the lines? Positive, Negative, or Zero", "answer": "Zero"},
    {"image": "fig9.png", "question": "What is the gradient of the line GH?", "answer": "-2/11"},
    {"image": "fig2.png", "question": "What is the slope?", "answer": "-2"},
    ]

#Open the medium quiz window
def open_medium_quiz():
    global score
    score = 0
    medium_win = tk.Toplevel(app)
    medium_win.title("Medium Math Quiz")
    medium_win.geometry("1200x650")
    medium_win.resizable(False,False)

    current_question_index = [0]
    
    # Load and display the current question and its image
    def show_question():
        question_data = medium_questions[current_question_index[0]]
        question_label.config(text=f"Q{current_question_index[0] + 1}: {question_data['question']}")

        try:
            # Load and resize the image for the question
            image = Image.open(question_data["image"])
            image = image.resize((400, 300), Image.LANCZOS)
            img = ImageTk.PhotoImage(image)
            image_label.config(image=img)
            image_label.image = img
        except Exception as e:
            print(f"Error loding image: {e}")
            image_label.config(image="", text="Image not found", font=("Arial", 14))
            
        # Clear answer box
        answer_entry.delete(0, tk.END)
        # Clear result feedback 
        result_label.config(text="")

        
    def next_question():
        current_question_index[0] +=1
        if current_question_index[0] < len (medium_questions):
            show_question()
        else:
            medium_win.destroy()
            show_score_window()
    # Move to the next question or end the quiz
    def check_answer():
        global score
        
        #Get user answer
        user_input = answer_entry.get()
        

        correct_answer = medium_questions[current_question_index[0]]["answer"]

        if user_input == correct_answer:
            result_label.config(text="Correct 🎉", fg="green")
            score += 1
        else:
            result_label.config(text=f"Wrong! Correct answer: {correct_answer}", fg="red",)
            
       # Wait seconds before showing the next question, This allows students to see if they got it right or wrong
        medium_win.after(1500, next_question)

     # Display the question text
    question_label = tk.Label(medium_win, text="", font=("Arial", 20), wraplength=800)
    question_label.pack(pady=20)
     # Display the image related to the question
    image_label = tk.Label(medium_win)
    image_label.pack(pady=10)
    # Entry box for the user to type their answer
    answer_entry = tk.Entry(medium_win, font=("Arial", 18))
    answer_entry.pack(pady=10)
     # Label to display feedback
    result_label = tk.Label(medium_win, text="", font=("Arial", 16))
    result_label.pack(pady=10)
    
    # Submit button to check the user's answer
    tk.Button(medium_win, text="Submit", font=("Arial", 16), command=check_answer).pack(pady=10)
    # Show the first question when the medium quiz window opens
    show_question()
    
#Open the easy quiz window
def open_easy_quiz():
    global score
    score = 0
    easy_win = tk.Toplevel(app)
    easy_win.title("Easy Math Quiz")
    easy_win.geometry("1200x650")
    easy_win.resizable(False,False)

    current_question_index = [0]
    
    #Show the current  question
    def show_question():
        question_data = easy_questions[current_question_index[0]]
        question_label.config(text=f"Q{current_question_index[0] + 1}: {question_data['question']}")
        answer_entry.delete(0, tk.END)
        result_label.config(text="")
        
    #Move to the next question or end the quiz
    def next_question():
        current_question_index[0] += 1
        if current_question_index[0] < len(easy_questions):
            show_question()
        else:
            easy_win.destroy()
            show_score_window()
            
    #Check if the user name is correct
    def check_answer():
        global score
        user_input = answer_entry.get()

        if not validate_input(user_input):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        user_input = int(user_input)
        correct_answer = int(easy_questions[current_question_index[0]]["answer"])

        if user_input == correct_answer:
            result_label.config(text="Correct 🎉", fg="green")
            score += 1
        else:
            result_label.config(text=f"Wrong! Correct answer: {correct_answer}", fg="red",)
            
        easy_win.after(1500, next_question)
        
    #Validate input is a number and not empty 
    def validate_input(input_value):
        """Validate that the input is a non-empty numeric value."""
        if input_value.strip() =="":
            return False
        if not input_value.isdigit():
            return False
        return True

    # Label to display the current math question
    question_label = tk.Label(easy_win, text="", font=("Adamina", 16), wraplength=550)
    question_label.pack(pady=20)
    # Entry box for the user to type their answer
    answer_entry = tk.Entry(easy_win, font=("Nico Moji", 18))
    answer_entry.pack(pady=10)
   # Button to submit the answer and trigger the check_answer function
    submit_btn = tk.Button(easy_win, text="SUBMIT", font=("Nico Moji", 16), command=check_answer)
    submit_btn.pack(pady=10)
   # Label to show the result after submitting (e.g., Correct or Wrong)
    result_label = tk.Label(easy_win, text="", font=("Nico Mmoji", 16))
    result_label.pack(pady=10)
    #Start with the first question
    show_question()
     


# Show the score screen after quiz ends
def show_score_window():
    score_win = tk.Toplevel(app)
    score_win.title("Final Score")
    score_win.geometry("1200x650")
    score_win.resizable(False,False)

    # Background image
    bg_score_image = tk.PhotoImage(file="court.png")
    bg_label_score = tk.Label(score_win, image=bg_score_image)
    bg_label_score.image = bg_score_image
    bg_label_score.place(x=0, y=0, relwidth=1, relheight=1)
    
    user_name = name_entry.get() or "Player"

    #Name and score display  
    name_label = tk.Label(score_win, text=f"{user_name}", font=("Adamina", 18), fg="#FF5349", bg="black")
    name_label.place(relx=0.5, rely=0.50, anchor="center")

    #Score Display
    score_display = tk.Label(score_win, text=f"Your Score: {score} / {len(easy_questions)}", font=("Adamina", 14), fg="white", bg="black")
    score_display.place(relx=0.5, rely=0.55, anchor="center")
    
    #Message Display
    msg_label = tk.Label(score_win, text="NICE  WORK!", font=("Nico Moji", 60), fg="white", bg="black")
    msg_label.place(relx=0.5, rely=0.4, anchor="center") 

    #Restart the quiz
    def easy_restart_quiz():
        score_win.destroy()
        open_easy_quiz()

    def medium_restart_quiz():
        score_win.destroy()
        open_medium_quiz()

    #Continue to next level
    def continue_quiz():
        score_win.destroy()
        open_difficulty_window()
        
    #Exit the progam
    def exit_quiz():
        app.destroy()

    # Buttons for score window
    restart_btn = tk.Button(score_win, text="RESTART", font=("Nico Moji", 18), command=easy_restart_quiz, bg="black", fg="white")
    restart_btn.place(relx=0.28, rely=0.60, relwidth=0.13, relheight=0.09)

    restart_btn = tk.Button(score_win, text="RESTART", font=("Nico Moji", 18), command=medium_restart_quiz, bg="black", fg="white")
    restart_btn.place(relx=0.28, rely=0.60, relwidth=0.13, relheight=0.09)

    continue_btn = tk.Button(score_win, text="CONTINUE", font=("Nico Moji", 18), command=continue_quiz, bg="black", fg="white")
    continue_btn.place(relx=0.59, rely=0.60, relwidth=0.13, relheight=0.09)

    exit_btn = tk.Button(score_win, text="EXIT", font=("Nico Moji", 18), fg="white", bg="black", command=exit_quiz)
    exit_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)


#Difficulties Window, Image Background and Difficcultiy Button
def open_difficulty_window():
    print("Difficulties Window Opening...")
    diff_win = tk.Toplevel(app)
    diff_win.title("MATH QUIZ")
    diff_win.geometry("1200x650")
    diff_win.resizable(False, False)
    
    #Difficulty Image Window
    bg_diff_image = tk.PhotoImage(file="court.png")
    bg_label_diff = tk.Label(diff_win, image=bg_diff_image)
    bg_label_diff.image = bg_diff_image
    bg_label_diff.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(diff_win, text="NETMATICS", font=("Nico Moji", 65), fg="white", bg="black").place(relx=0.5, rely=0.4, anchor="center")
    tk.Label(diff_win, text="Choose Difficulty", font=("Adamina", 24), fg="white", bg="black").place(relx=0.5, rely=0.5, anchor="center")
    #Easy Button
    easy_btn = tk.Button(diff_win, text="EASY", font=("Nico Moji", 18), fg="white", bg="black", command=open_easy_quiz)
    easy_btn.place(relx=0.28, rely=0.55, relwidth=0.13, relheight=0.09)
    #Medium Button   
    medium_btn = tk.Button(diff_win, text="MEDIUM", font=("Nico Moji", 18), fg="white", bg="black", command=open_medium_quiz )
    medium_btn.place(relx=0.59, rely=0.55, relwidth=0.13, relheight=0.09)
    #Hard Buton
    hard_btn = tk.Button(diff_win, text="HARD", font=("Nico Moji", 18), fg="white", bg="black")
    hard_btn.place(relx=0.44, rely=0.65, relwidth=0.13, relheight=0.09)
    #Exit Button
    exit_btn = tk.Button(diff_win, text="EXIT", font=("Nico Moji", 18), fg="white", bg="black", command=diff_win.destroy)
    exit_btn.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)


# Starts the quiz by validating the name entry and opening difficulty selection
def start(name_entry):
    user_input = name_entry.get()
    
    if user_input =="":
        messagebox.showerror("Invalid Name", "Plase enter your name to start.")
        print ("Plase no Blanks!")
    else:
        open_difficulty_window()


#Main window background image
bg_image = PhotoImage(file="court.png")
bg_label = tk.Label(app, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# User name profile
name_label = tk.Label(app, text="Enter Name", font=("Adamina", 18), fg="white", bg="black")
name_label.place(relx=0.5, rely=0.59, anchor="center")

name_entry = tk.Entry(app, font=("Nico Moji", 15), justify="center")
name_entry.place(relx=0.5, rely=0.65, anchor="center") 

# NETMATICS label
n_label = tk.Label(app, text="NETMATICS", font=("Nico Moji", 70), fg="white", bg="black")
n_label.place(relx=0.5, rely=0.4, anchor="center")

# Start button
start_btn = tk.Button(app, text="START", font=("Nico Moji", 18), fg="white", bg="black", command=lambda: start(name_entry))
start_btn.place(relx=0.44, rely=0.75, relwidth=0.13, relheight=0.09)

# Exit button
exit_button = tk.Button(app, text="EXIT", font=("Nico Moji", 18), fg="white", bg="black", command=close_window)
exit_button.place(relx=0.01, rely=0.88, relwidth=0.10, relheight=0.09)



# Start the Tkinter event loop
app.mainloop()
