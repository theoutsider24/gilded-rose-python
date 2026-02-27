# Dev Log

The purpose of this file is to track my work over time as I work through this kata
I'm starting by reading over the existing code to come up with an action plan. My general approach will be to get my dev environment set up, make some devEx enhancements then check what's working now, add tests to cover all existing behaviour then, with the context, of the task, refactor and add the new functionality.

First step, I want to run the tests - I'm going to spin up a dev container to work in
I can already see we're using requirements.txt with unpinned versions so once we get this working we'll need to switch to something more modern (probably uv) and get those versions locked down.

We'll also want to start from a clean state so I'll be setting up a linter, formatter and type-checker.

Turns out neither git nor docker and wsl were installed on this machine, creating some issues for tracking until that's ready.

Devcontainer is working and I can run one of the tests but the approval test setup seems a bit complicated and non-standard so I think we can improve it. It's pretty trying to intercept what would be sent to stdout. Since there are few tests, I'm also going to migrate to pytest since the ergonomics are a bit nicer (it's actually already installed, handy!). I'll see if it's worth reproducing much of the test logic.
From what I can tell, the approval test setup is pretty messed up - I think the approved version should probably represent what we expect but it seems to be empty? That library already looks pretty unsupported so I don't think we should use it. Just noticed the instructions also tell us to do a 'trust me bro' and commit whatever it outputs as the approved version which may lock in the expected behaviour, I'll just achieve the same thing by setting up my basic assertions and setting the quality values so the tests pass.

After cleaning up and doing some coverage testing it actually looks like we've got all branches covered so I can start refactoring!

# Task list

## Bootstrap

- [x] Create devcontainer
- [x] Get tests running
- [x] Initialise uv and lock versions

## Stabilise

- [ ] Refactor for readability

## Enhance