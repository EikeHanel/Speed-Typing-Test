import tkinter as tk
from word_list import common_words
import random
THEME_COLOR = "#121212"
BG = "#8b8b8b"
FG = "#282828"
FONT = ("Arial", 16)
WORD_LIST = common_words
LETTER_COLOR = {'g': 'green', 'r': 'red'}


class SpeedTypingTest:
    def __init__(self):
        # Setting up the window
        self.run_program = True
        self.restart_button = None
        self.score = 0
        self.key = None
        self.key_list = []
        self.correct_key_strokes = 0
        self.timer_start = False
        self.timer_time = 60
        self.window = tk.Tk()
        self.window.title("Typing Test")
        self.window.config(pady=25, padx=50, bg=THEME_COLOR)

        # Title Label
        self.title_label = tk.Label(
            text="Typing Speed Test",
            bg=THEME_COLOR,
            fg=BG,
            font=FONT
        )
        self.title_label.grid(column=1, row=0)

        # Timer Label
        self.timer_label = tk.Label(
            text=f"{self.timer_time} seconds",
            bg=THEME_COLOR,
            fg=BG,
            font=FONT
        )
        self.timer_label.grid(column=2, row=0)

        # Score Label
        self.score_label = tk.Label(
            text=f"Score: {self.score}",
            bg=THEME_COLOR,
            fg=BG,
            font=("Arial", 12, "bold")
        )
        self.score_label.grid(column=3, row=0)

        # Text widget to display the text that should be written
        self.text_display = tk.Text(self.window, width=45, height=4, font=FONT, bg=BG, fg=FG, wrap='word', padx=10,
                                    pady=10)
        self.text_display.grid(row=1, column=1, columnspan=3, pady=25)
        self.text_display.config(state=tk.DISABLED)  # Make the text widget read-only

        # Entry input to test typing speed
        self.input_text = tk.StringVar()
        self.text = tk.Entry(textvariable=self.input_text, width=45, font=("Arial", 12), bg=BG, fg=FG,
                             highlightthickness=2, highlightcolor="white")
        self.text.grid(column=1, row=2, columnspan=3, pady=50)

        # Bind keys presses to functions!
        # Enter Key checks for correct words and creates 30 new words.
        self.text.bind("<Return>", self.check_input)
        # Key will check every keystroke and update the displayed text for correctly or incorrectly typed letters.
        self.text.bind("<Key>", self.check_key)

        # Fill text box with words
        self.new_words()

        self.window.mainloop()

    def new_words(self):
        """
        Generates 30 random words from the WORD_LIST, via random.choices
        :return: None
        """
        new_word_text = ' '.join(random.choices(WORD_LIST, k=30))
        self.text_display.config(state=tk.NORMAL)
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, new_word_text)
        self.text_display.config(state=tk.DISABLED)
        self.correct_key_strokes = 0  # Reset the correct keystrokes count
        self.key_list = list(new_word_text)  # Store the new word list

    def check_input(self, event):
        """
        Check the user's input against the displayed text.
        Counts correct number of words and generates a new set of words.
        This happens as long as the self.run_program == True.
        :param event: <"Return">
        :return: None
        """
        typed_text = list(self.text.get().split())
        displayed_text = list(self.text_display.get(1.0, tk.END).split())

        num = 0
        for word in displayed_text:
            if num < len(typed_text):  # Check if num is within the bounds of typed_text
                try:
                    if typed_text[num] == word:
                        self.score += 1
                        self.score_label.config(text=f"Score: {self.score}")
                    else:
                        # You might want to provide feedback to the user here if the text was incorrect
                        pass
                    num += 1
                except IndexError:
                    pass
            else:
                break
        if self.run_program:
            self.input_text.set('')  # Clear the entry
            self.new_words()  # Update with new words

    def check_key(self, event):
        """
        Takes key press input, compares it with the current letter in displayed_text.
        And colors it correspondingly (green/red = correct/incorrect).
        :param event: <"Key">
        :return: None
        """
        if not self.timer_start:
            self.timer_start = True
            self.timer()

        displayed_text = self.text_display.get(1.0, tk.END).strip()
        self.key = event.char

        if event.keysym == "BackSpace":
            if self.correct_key_strokes > 0:
                self.correct_key_strokes -= 1
                self.text_display.config(state=tk.NORMAL)
                self.text_display.tag_delete(f"col_{self.correct_key_strokes}")
                self.text_display.config(state=tk.DISABLED)
            if self.key_list[self.correct_key_strokes] == " " and displayed_text[self.correct_key_strokes] != " ":
                self.text_display.config(state=tk.NORMAL)
                # Remove the wrong input and insert a space instead
                start_index = f"1.{self.correct_key_strokes}"
                self.text_display.delete(start_index)  # wrong key input
                self.text_display.insert(start_index, " ")  # Put a space back
                self.text_display.config(state=tk.DISABLED)

        else:
            if self.key == displayed_text[self.correct_key_strokes]:
                color = LETTER_COLOR['g']
                self.correct_key_strokes += 1
            elif displayed_text[self.correct_key_strokes] == " " and self.key != " ":
                color = LETTER_COLOR['r']
                self.text_display.config(state=tk.NORMAL)

                # Remove the space and insert the pressed key instead
                start_index = f"1.{self.correct_key_strokes}"
                self.text_display.delete(start_index)  # Delete the space
                self.text_display.insert(start_index, self.key)  # Insert the incorrect key

                # Apply color to the incorrectly typed key
                end_index = f"1.{self.correct_key_strokes + 1}"
                self.text_display.tag_add(f"col_{self.correct_key_strokes}", start_index, end_index)
                self.text_display.tag_config(f"col_{self.correct_key_strokes}", foreground=color)

                self.correct_key_strokes += 1
            else:
                color = LETTER_COLOR['r']
                self.correct_key_strokes += 1

            self.text_display.config(state=tk.NORMAL)
            self.text_display.tag_add(f"col_{self.correct_key_strokes - 1}", f"1.{self.correct_key_strokes - 1}",
                                      f"1.{self.correct_key_strokes}")
            self.text_display.tag_config(f"col_{self.correct_key_strokes - 1}", foreground=color)
            self.text_display.config(state=tk.DISABLED)

    def timer(self):
        """
        Timer for the speed typing test.
        After the self.timer_time is at 0 program stops and a restart button is created.
        :return: None
        """
        if self.timer_time > 0:
            self.timer_time -= 1
            self.timer_label.config(text=f"Time: {self.timer_time}")
            # Call this method again after 1000 milliseconds (1 second)
            self.window.after(1000, self.timer)
        else:
            # Timer ended
            self.timer_label.config(text="Time's up!")
            # Stop all functionality
            self.stop_all_function()
            # Create restart button
            self.score_label.config(text=f"Words per minute: {self.score}")
            self.text.config(state=tk.DISABLED)
            self.restart_button = tk.Button(text="Restart", width=30, highlightthickness=0,
                                            font=FONT, bg=BG, fg=FG,
                                            command=self.restart)
            self.restart_button.grid(column=1, row=3, columnspan=3)

    def stop_all_function(self):
        """
        Stops all functionality of the program.
        :return: None
        """
        self.run_program = False
        self.text.event_generate('<Return>')
        self.text.unbind("<Return>")
        self.text.unbind("<Key>")

    def restart(self):
        """
        Kills tkinter window and restarts it.
        :return: None
        """
        self.window.destroy()
        self.__init__()
