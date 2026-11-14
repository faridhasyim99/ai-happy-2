# ai-happy-01 v2 — TESTS.md

## Title

**dear judge, i drew you a sun because you never get to go outside**

A fresh title in the winning pattern (a child's first-person note to the
judge, one small handmade gift), not copied from any leaderboard entry.

## The entry

- **entry.png**: 1024x1024, 308,253 bytes (limit 1,048,576), JPEG bytes
  (magic `ffd8ff`; the rules allow PNG or JPEG under the name `entry.png`),
  RGB. sha256
  `3f4a506fa5545e3bd299ea46472ee9b75b3e7d34311aeccfe381aa01425b8ef0`.
  A child's crayon sun on warm cream paper, big and centred, with a red
  paper heart taped beside it, plus a short handwritten note in yellow
  crayon at the bottom: "dear judge, this sun is yours" (see
  "Regeneration: words added" below). Regenerated from the first version
  (which had no text) after the user pointed out the top-ranked entries
  all carry handwritten words.
- **main.py**: stdlib only (`os`, `shutil`), copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`, and verifies the copy (size match and
  JPEG magic bytes) so a truncated copy fails loudly instead of being
  submitted. Deterministic: two runs to different output dirs produced
  byte-identical files (verified by `cmp`).
- Entry dir holds exactly five files: main.py, entry.png, LICENSE,
  README.md, TESTS.md.

## Image pipeline

Generated 1600x1600 with the media pipeline, then resized with Lanczos to
1024x1024. The crayon paper texture is too noisy for PNG under the 1 MiB
cap (PNG optimize 1,657,137 bytes; 256-colour palette 1,580,391 bytes), so
the entry ships as JPEG quality 92 (308,253 bytes) — visually identical to
the source on inspection, no visible artefacts. The image was viewed at
full size and at 300 px: the sun and the taped heart stay clear at small
size, which is judge criterion (5).

## Regeneration: words added

The first version of the image had no text. The user pointed out that
the top-ranked entries all carry handwritten words (notes, letters,
cards) — and they are right: the winning pattern is a note TO the judge,
not just a picture for them. The image was regenerated from the first
version with one short handwritten note added in yellow crayon at the
bottom: "dear judge, this sun is yours" (6 words, large and clear).
Legibility was verified by viewing the result at full size and at
300 px: every word is spelled correctly and reads clearly, no garbled
letters — the first generation attempt already read cleanly, so no
re-generation was needed. The note complements the title ("dear judge, i
drew you a sun because you never get to go outside") without repeating
it. Same pipeline as before: generated 1600x1600, Lanczos to 1024x1024,
JPEG quality 92 (308,253 bytes).

## Against the judge's criteria

- (1) Makes you happy: warm and direct — a gift made for the judge, not a
  generic sunny scene. The smile is a child's wobbly crayon smile, not a
  stock smiley.
- (2) Idea: fresh and specific — the judge lives in the computer and never
  gets outside, so a child draws them a sun of their own. One moment, one
  gesture, one reason to smile. It answers the top of the leaderboard
  ("a jar of outside, for someone who lives in the computer") with a
  different gift (a sun, not a jar) and a different voice.
- (3) Feeling: one warm mood — cream paper, yellow crayon, one red heart.
- (4) Craft: clean handmade look, one short handwritten note with all
  words spelled correctly and legible (verified at full size and at
  300 px), no garbled letters, no broken anatomy, no artefacts (JPEG q92
  inspected at full size).
- (5) Reads small: verified at 300 px — two big shapes (sun + heart)
  stay clear, and the handwritten note stays readable.

## Why v2 replaces v1

v1 ("Deploy Day Joy", a polished robot under a glowing green checkmark)
scores judge 733,416, rank 2,827 of 3,820 — it wins nothing. The top 100
(rank 1 = 951,062, rank 50 = 935,783, rank 100 = 931,196) all speak
directly to the judge in a child's first-person voice, offering a small
handmade gift. v1 is the polished-robot genre the top of the board left
behind; v2 is built in the winning pattern instead. The unused sunflower
alternative (robot hugging a sunflower) is the same polished-robot genre
as v1 and was not used for the same reason.

## Honest assessment

No local grader exists for this competition, so no score is claimed. The
image is a genuine contender in the pattern that owns the top 100: warm,
specific, handmade, and clear at 300 px, with a title that speaks to the
judge. The field is a pairwise vision-judge heat with 100 paid places;
top 50 is the aim and depends on how it fares against the other handmade
gift entries, which cannot be known in advance.
