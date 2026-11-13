# Title
Nova Drift Build Planner

## Repository
https://github.com/NathanG79/PFDA-Final-Project

## Description
Program that displays all the upgrades in the video game Nova Drift. The program will allow you to click upgrades to mark them, allowing the user to create a cheatsheet for what upgrades they wish to get in a run. Probably done with pygame.

## Features
- Toggleable buttons for every upgrade.
	- Highlight selected upgrades, dim the rest.
- Display requirements for upgrades.
    - Highlight requirements when hovering over an upgrade.
- Mutually exclusive upgrades.
    - Disable mutually exclusive upgrades when selecting an upgrade.
- The in game icons for all upgrades.
    - Image files for every upgrade stored in a folder the program has access to.
- Full stats for every upgrade.
	- Display a box of text when hovering over an upgrade.
- Easily changable stats, when game updates inevitably change things.
    - Upgrade stats stored in text files, separated from the code.
- Import/export builds as codes.
	- Translate selected upgrades to a string of characters that can be copy pasted in and out of the program.
- Scrollable window.
    - To be researched.


## Challenges
- Taking keyboard input with pygame.
- Allowing user to copy text from pygame and paste it elsewhere.
- Creating a scrollable window with pygame.
- Adding images to the screen in pygame.

## Outcomes
Ideal Outcome:
- A clean and easy to use program that allows for the creation, saving, loading, and sharing of planned builds for Nova Drift. To be "clean and easy to use", it must conveniently display all information the game gives about upgrades.

Minimal Viable Outcome:
- A program that displays all the upgrades in Nova Drift, the stats of all the upgrades, and the ability to put some form of indicator on upgrades by clicking them.

## Milestones

- Week 1
  1. Gather image files for the icons of all the upgrades (from the Nova Drift wiki).
  2. Learn how to display image files in pygame.
  3. Create toggleable markers on upgrades.
  4. Implement system to allow the user to scroll up and down on the window, so that upgrades can be spread out more/not be tiny.

- Week 2
  1. Gather stats for all upgrades (from the Nova Drift wiki).
  2. Create system to pull stats from the text files.
  3. Display text box containing upgrades stats when hovering over that upgrades icon.  

- Week 3
  1. Display the requirements to upgrades, where applicable.
  2. Display which upgrades are mutually exclusive to the one the user is hovering over.
  3. Automatically enable required upgrades when selecting an upgrade.
  4. When deselecting an upgrade that is a requirement for another selected upgrade, disable that other upgrade as well.
  5. When selecting an upgrade, automatically disable upgrades that are mutually exclusive with it.

- Week 4
  1. Implement system to create copyable code for a build.
  2. Implement system to import a build code, automatically selecting all relevant upgrades. 