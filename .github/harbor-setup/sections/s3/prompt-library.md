# Harbor prompt library

Prompts that kept their format over three runs. Copy one, fill in the brackets, attach the file, and check every row against the source.

## User stories from meeting notes

Attach the notes file, then paste this:

```text
Make user stories from section [number] of the attached notes, "[section title]".
Stakeholder: [stakeholder].
Sprint: [sprint].
Use only that section of the attached notes.
Format: one table with the columns ID, As a, I want, So that, Acceptance criteria. IDs: US-1, US-2 and so on.
Write each acceptance criterion as one sentence: Given ..., When ..., Then ... Separate criteria with a semicolon, no HTML.
Maximum length of the answer: 600 words.
Tone: neutral and plain, for a client who will read it.
Coherence: the same word for the same thing in every row.
Creativity: none in facts. Add no topic, case, number or rule that the section does not state. If the section leaves a point open, write "Open point" in the row.
```
