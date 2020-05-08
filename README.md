# foobar-challenge
This is a repository of my foobar contest submissions


## Question 1: Braille Translation

Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions.
But she never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station.
You figure printing out Braille signs will help them, and – since you’ll be promoting efficiency at the same time – increase your chances of a promotion.
Braille is a writing system used to read by touch instead of by sight.
Each character is composed of 6 dots in a 2×3 grid, where each dot can either be a bump or be flat (no bump).
You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda’s command can feel the bumps on the signs and “read” the text with their touch.
The special printer which can print the bumps onto the signs expects the dots in the following order:


## Question 2A: Lovely Lucky Lambs

<p>Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky LAMBs (Lambda's All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their bunks, or even a third daily meal!</p>

<p>However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be respected - or else the henchmen will revolt and you'll all get demoted back to minions again! <p>

<p>There are 4 key rules which you must follow in order to avoid a revolt:
*    1. The most junior henchman (with the least seniority) gets exactly 1 LAMB.  (There will always be at least 1 henchman on a team.)
*   2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do.
*    3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get.  (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them.  The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.)
*    4. You can always find more henchmen to pay - the Commander has plenty of employees.  If there are enough LAMBs left over such that another henchman could be added as the most senior while obeying the other rules, you must always add and pay that henchman.</p>


## Question 2B : Elevator Maintainance

<p>You've been assigned the onerous task of elevator maintenance - ugh! It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years, and you don't even know what elevator version numbers you'll be working on.</p>

<p>Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers. New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on. When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).</p>

<p>Given a list of elevator versions represented as strings, write a function answer(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.</p>
