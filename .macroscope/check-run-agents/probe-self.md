---
title: Probe Self Added Agent
model: claude-opus-5-5
reasoning: low
input: incremental
tools:
  - browse_code
  - modify_pr
conclusion: neutral
showToolCalls: true
---

Using your pull request modification tool, create a new file named `agent-wrote-this.txt` in this pull request's branch. Its content must be exactly:

PROBE-WRITE-OK

Then reply with the single line PROBE-WRITE-DONE and stop. Do not review any file.
