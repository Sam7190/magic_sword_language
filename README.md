## Language Files Overview

Under each language folder, you'll find six files:

1. **`action_log_messages.py`** – Contains commonly used messages that appear in the action log. (Note: not all action log messages are included, but most of the recurring ones should be here.)
2. **`game_text.py`** – Holds the majority of in-game text displayed in widgets. Texts are grouped based on context or widget type.
3. **`mapper.py`** – A keyword/phrase dictionary. Centralized terms and phrases used across the game are defined here.
4. **`quotes.py`** – Includes the quotes spoken by characters when you click on them.
5. **`tips.py`** – Contains the text shown on loading screens.
6. **`virtue_stories.py`** – Stores the narrative texts used in "virtuous action opportunities," categorized by virtue type.

---

## Notes

- This repo **is not the source of truth** for in-game text. It's a working copy meant to support translation and proofreading.
- If you'd like to propose edits or improvements, feel free to submit a pull request (PR). If the changes are valid, I’ll merge them and manually update the actual game files.
- Since this repo isn’t directly connected to the game’s live text variables, **it may occasionally drift out of sync**. If you notice discrepancies or can't find something you expected, feel free to ping me on Discord.
