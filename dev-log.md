# Dev Log

The purpose of this file is to track my work over time as I work through this kata
I'm starting by reading over the existing code to come up with an action plan. My general approach will be to get my dev environment set up, make some devEx enhancements then check what's working now, add tests to cover all existing behaviour then, with the context, of the task, refactor and add the new functionality.

First step, I want to run the tests - I'm going to spin up a dev container to work in
I can already see we're using requirements.txt with unpinned versions so once we get this working we'll need to switch to something more modern (probably uv) and get those versions locked down.

We'll also want to start from a clean state so I'll be setting up a linter, formatter and type-checker.

Turns out neither git nor docker and wsl were installed on this machine, creating some issues for tracking until that's ready.

# Task list

## Bootstrap

- [ ] Create devcontainer
- [ ] Get tests running
- [ ] Initialise uv and lock versions

## Stabilise

## Enhance