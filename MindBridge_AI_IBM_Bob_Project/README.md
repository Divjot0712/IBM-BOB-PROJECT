# MindBridge AI — IBM Bob Final Project

A lightweight, student-focused mental wellbeing companion prototype aligned with **SDG 3: Good Health and Well-being**.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```
6. Open the local URL printed by Streamlit.

## Use with IBM Bob
1. Open IBM Bob and create/open a workspace from this project folder.
2. Ask Bob to inspect `app.py`, `requirements.txt`, and this README.
3. Use the prompt in `IBM_Bob_Build_Prompt.txt` to request improvements.
4. Run the app and test the scenarios in `TEST_PLAN.md`.

## Features
- Mood check-in from 1 to 5
- Optional emotion selection
- Supportive rule-based responses for common concerns
- Breathing, grounding, and journaling tools
- Basic keyword-based safety signposting
- No login and no chat-history persistence

## Important limitations
This is an educational prototype, not a clinical product. It does not diagnose, treat, predict clinical risk, or replace professional care. Keyword checks can miss context and must not be treated as reliable crisis detection. Before real-world deployment, obtain qualified mental-health review, privacy/security review, accessibility testing, and a documented escalation process. Avoid collecting or storing sensitive personal information.

## Suggested demo flow
1. Show the home screen and disclaimer.
2. Complete a mood check-in.
3. Enter a sample exam-stress message.
4. Demonstrate a breathing or grounding exercise.
5. Demonstrate the safety message using a test phrase only in a controlled demo.
6. Explain prototype limits and next steps.

## Project files
- `app.py` — Streamlit app
- `requirements.txt` — dependencies
- `IBM_Bob_Build_Prompt.txt` — prompt for Bob
- `TEST_PLAN.md` — demo and test cases
- `MindBridge_AI_Lean_Canvas.pdf`
- `MindBridge_AI_Concept_Note.pdf` and `.docx`
- `MindBridge_AI_Final_Presentation.pptx`
