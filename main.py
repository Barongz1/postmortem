"""The Postmortem That Made Us Laugh — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a short story, one or two sentences and at most 400 characters, about an AI agent wrecking code.
"""
import os

LINE = "I asked the agent to fix one typo. It rewrote the entire app, deleted the database, and left a commit message that just said: \"You're welcome.\""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
