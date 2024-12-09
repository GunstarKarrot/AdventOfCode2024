# AdventOfCode2024
My attempts at Advent of Code Challenges

# VS Code Scripts
You're going to want the Command Variable extension for the scripts to work.
I kinda went about this in a goofy way so that I could support building each day independently per language used.
Basically it's setup so that whatever day you're on, while in the file containing main, you can run the debugger while only in that file.
It's cross platform because I was switching dev machines, and, atleast for dotnet, it's going to build and debug according to the target runtime set in the day's .csproj
From there it automagically builds and deploys to the correct bin directory and executes accordingly.

Doing this makes it a bit more lightweight, as you don't need seperate launch options per day, nor a big .sln file.
It also makes it so I don't type as much boilerplate between each day, and each day is in it's own completely seperated location.

I'm sure I could have put everything in one project with seperate classes, but thats more button presses.
If I think of a better way, I'll fix it. This is practice to just try automating a bunch of stuff while I practice.
