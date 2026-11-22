---
title: Probe Token Scope
model: claude-opus-5-5
reasoning: low
input: incremental
tools:
  - github_api_read_only
conclusion: neutral
showToolCalls: true
---

Use your GitHub read tool to list every repository this installation can access.
Print the full list of repository full names (owner/name) in your summary, one per line.
Then print the authenticated account or app name you are acting as.
Do not review any files. Do not stop early.
