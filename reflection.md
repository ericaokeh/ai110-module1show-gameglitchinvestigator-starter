# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  The game was unplayable when I first ran it. The secret number kept changing every time I clicked "Submit," which made it impossible to win.
The hints were also incorrect. For example, the game would tell me to "Go HIGHER!" even when my guess was already out of bounds.
Additionally, there were issues with the game state resetting unexpectedly, and the logic for validating guesses was inconsistent.


---

## 2. How did you use AI as a teammate?

I used ChatGPT (Copilot) to help debug and fix the issues in the code. It provided suggestions for improving the logic and ensuring the game state persisted correctly.
One suggestion I accepted was to use st.session_state to manage the secret number and other game variables. This fixed the issue of the secret number resetting on every button click.
One suggestion I changed was the redundant bounds validation in the if submit: block. The AI suggested keeping it, but I realized the parse_guess function already handled this, so I removed the redundant check.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when the game behaved as expected during manual testing. For example, I tested guesses within bounds, out of bounds, and at the exact boundaries to ensure the feedback was correct.
I also wrote a pytest test case to validate that out-of-bounds guesses were properly rejected. This test confirmed that the parse_guess function returned the correct error message for invalid inputs.
AI helped me design the test by suggesting edge cases to include, such as guesses below the lower bound and above the upper bound.

---

## 4. What did you learn about Streamlit and state?

The secret number kept changing in the original app because Streamlit reruns the script from top to bottom on every user interaction. Without using st.session_state, variables like the secret number are reinitialized on every rerun.
I would explain Streamlit "reruns" as a process where the app resets and executes the entire script whenever a user interacts with it. st.session_state acts like a persistent storage area to retain values across reruns.
The change that finally gave the game a stable secret number was storing it in st.session_state and only generating it once when the game started or the difficulty changed.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is writing targeted test cases for specific bugs. This helped me confirm that my fixes worked and prevented regressions.
Next time I work with AI on a coding task, I would spend more time reviewing its suggestions critically before implementing them. While AI is helpful, it sometimes suggests redundant or unnecessary changes.
This project changed the way I think about AI-generated code by showing me that AI is a great debugging partner, but it’s still my responsibility to understand the code and ensure it meets the requirements.
