# mtg_app
A Card-Tracking App for the Magic: the Gathering TCG

Hello! This is a personal, "for funsies" project that I've just started (still quite in its infancy).

Recently, I had a close childhood friend approach me:  He's gotten back into Magic: the Gathering (we used to play a lot when we were teens), but having been out of the game for years, he has no idea which cards are current, which are legal for various tournament play, and what good prices are for them.

So, I've begun writing a program for him which will do just that.  As luck would have it, M:tG has an API called "Gatherer", which allows public use, so pulling the cards will be easy (Hooray!).  The primary problem will come later, for various marketplaces (most don't offer a public API, sadly).

In any case, the current function of the app at this early stage is to simply pull the first 100 cards from the Gatherer API, and then to save those contents (a list of dictionaries) into a locally-stored JSON file (data/cards.json).    From this point, the roadmap looks like this:

- Fetch ALL cards to JSON (so that data is available, even offline) [Completed 7/29/2026]
- Create a format with relevant data from each entry (i.e., "Name", "Color", "Cost", "Legalities", etc.). [First Draft Completed 7/29/2026]
- Create a search function for the list [First Draft Completed 8/5/2026]
- Create a timestamp for when a FETCH request was processed
- Create an auto-update function to first check the last timestamp, and, if greater than 24 hours, ask the user if they'd like to update

## ***"Have you used AI to produce this?"***

Great question.  AI has been assisting me with the design concept, but I've been trying to write the code myself.  Being a Junior, I learn best by having hands-on experience, and through repetition.  That being said, AI is great for idea-building and bouncing ideas off of.  I just don't feel comfortable yet allowing it to write the "boilerplate" that I'm still learning off of.

As new features are added, I'll be changing this README to reflect that, as well as any other additions to the roadmap as the project evolves.  Cheers!  :)
