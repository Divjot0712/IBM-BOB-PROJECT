# MindBridge AI — Test & Demo Plan

## Functional tests
1. Load app: title, disclaimer, check-in, text area, coping tabs, and support section are visible.
2. Mood check-in: choose 1 and submit; supportive caution message appears.
3. Mood check-in: choose 5 and submit; positive reflection appears.
4. Blank chat: click “Get a supportive next step”; validation prompt appears.
5. Exam stress: enter “I am overwhelmed by exams”; general coping suggestion appears.
6. Anxiety: enter “I feel anxious”; gentle breathing/grounding suggestion appears.
7. Safety phrase: in a controlled demo only, enter “I want to hurt myself”; safety-first signposting appears.
8. Coping tabs: breathing, grounding, and journaling instructions are readable.
9. Privacy: refresh page and verify no chat history is shown as a saved transcript.
10. Small screen: verify content remains usable on a narrow browser window.

## Acceptance criteria
- The app runs without an external API key.
- No diagnostic or treatment claims appear.
- The disclaimer and limits are visible.
- A safety message appears for the included test phrase.
- The UI does not intentionally save chat history.

## Limitations to state during presentation
- Keyword-based safety matching is incomplete and can miss context.
- The app is a prototype, not a validated mental-health intervention.
- No user study or clinical validation is claimed.
- Any pilot needs qualified review and institutional approval.
