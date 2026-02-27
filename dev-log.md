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

Trying to formalise the strings into enums and breaking up the qaulity updating vs the sellin updating. We seem to currently just change the sellin right in the middle of a bunch of checks that use it which is a bit suspect, I reckon there are edge cases we haven't covered there yet but I'm going to deal with those when we come to implementing the spec.

Only just realised instructions don't want me changing the Item class, whoops! Moving the logic out into classmethods for now. I'm focussing on readability so just getting some good structure that'll be easily to refactor again at a later date. Decisions need to be made at a product level about whether we'll need to support many products in future, which may lead us down a config-driven route, or whether it will remain limited in which case we may want to look at creating explicit classes.

There's some ambiguity on whether normal items can be conjured - I'm going to make the assumption that they can't be for now however I think we should revise that in future.

I've started adding more specific tests but in the interest of time I've just covered a couple of the types.

# Task list

## Bootstrap

- [x] Create devcontainer
- [x] Get tests running
- [x] Initialise uv and lock versions

## Stabilise

- [x] Refactor for readability

## Enhance

Core requirements

 - [x] Once the sell by date has passed, Quality degrades twice as fast
 - [x] The Quality of an item is never negative
 - [z] "Aged Brie" actually increases in Quality the older it gets
 - [x] The Quality of an item is never more than 50
 - [x] "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
 - [x] "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    - [x] Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    - [x] Quality drops to 0 after the concert

- [x] We have recently signed a supplier of conjured items. This requires an update to our system:
    - [x] "Conjured" items degrade in Quality twice as fast as normal items

# Summary

The focus on my approach here was:

1. Make the codebase easier to work in by establishing standards-based tooling, commonly used libraries and portable dev environments

2. Reproduce existing tests for stabilisation and start to build up new test patterns for more complex scenarios

3. Improve readability without overengineering so that we can build forward on this repo

## Ease vs simplicity

A major design decision is to focus on keeping item rule configuration *simple* rather than making it *easy*.

The easy approach might involve a more object-oriented approach, factories, decorator pattern etc. however at the size of the current codebase that would overly complicate what is quite a simple ruleset *for now*.

I mention in my notes that there will be key decisions to make as we move forward. If we decide that we're going to very intentionally focus our business on a subset of items, we can build the system oriented around them and bring them into our domain language by creating specific classes. However if we, as a business, decide we're going to integrate with another magical vendor who has 1000s of objects available with different rules through some mystical API, then we may want to with a more configuration-driven route where we negotiate how to communicate the rules, whether there are common categories, whether we create our own webhook API for them to tell us rules rather than us inferring them etc.

Without knowledge of business direction, the best course of action is keeping things clean and small, sticking to a more functional-programming approach for now.
    