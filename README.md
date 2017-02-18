# FSND Swiss Tournament Results

## Overview
This project uses PostgreSQL and Python to store and report the results of a Swiss-style tournament, and Python to test the functionality of these methods.  A Swiss-style tournament is one in which no players are eliminated after each round.  Rather, each subsequent round pairs players who are equal or nearly equal in number of wins.   

## Repository Contents
Download or clone the git repository project to the host machine, and place the resultant "FSND-Proj-4-master" folder in the home directory. The folder contains five files:  tournament.sql; tournament.py; tournament_test.py; and also Vagrantfile and pg_config.sh, which set up and provision the virtual machine to run the project.   In order to assure a consistent environment and an identical experience across all computer platforms, the project is run using Linux Ubuntu running in a virtual machine.

The virtual machine requires VirtualBox and Vagrant to be downloaded and installed on the host computer.  After installing VirtualBox and Vagrant, you are ready to run the project.

## Prepare to Run the Project
Open a terminal window, such as Mac Terminal or GitBash run in Administrator mode on a Windows machine.

- At the command prompt, navigate to the "FSND-Proj-4-master" folder.

- Type "vagrant up", or "vagrant provision" if the vm has previously run, then ENTER.  This will start the virtual machine.

- When installation is finished, type "vagrant ssh" then ENTER at the prompt.  This will log you into the virtual machine.  You will be running ubuntu-trusty-32.

- When logged in, type "cd /vagrant" then ENTER at the prompt.  This directory contains the files synced between the host machine and the guest machine.  Type "ls" then ENTER to list the synced files, which will include the "FSND-Proj-4-master" folder from the host machine.  Type "cd /vagrant/FSND-Proj-4-master" to navigate to the tournament files, from which the PostgreSQL and Python files may be run.

## Run the Project
- The tournament.sql file sets up the database, creating the database, the players table, the matches table, and the standings view.  It starts with a DROP DATABASE command, to clear out any old tournament database and start anew.  Run tournament.sql by typing "psql -f tournament.sql;" then ENTER, which will create the database, tables, and view.  You will see the message, 'You are now connected to database "tournament" as user "vagrant".

- The tournament_test.py file uses the commands in the tournament.py file to perform the functions required to run the 10 tests listed below.  Run it by typing "python tournament_test.py", then ENTER, at the prompt.  The result of each test is printed when the test is finished, and if any test is failed, the test sequence will stop at that point with an error message.  If all tests pass, the list of test results will be printed, followed by the message:  "Success!  All tests pass!"  The list of tests follows.

 1. countPlayers() returns 0 after initial deletePlayers() execution.
 2. countPlayers() returns 1 after one player is registered.
 3. countPlayers() returns 2 after two players are registered.
 4. countPlayers() returns zero after registered players are deleted.
 5. Player records successfully deleted.
 6. Newly registered players appear in the standings with no matches.
 7. After a match, players have updated standings.
 8. After match deletion, player standings are properly reset.
 9. Matches are properly deleted.
 10. After one match, players with one win are properly paired.

 I don't know why Github is rendering the above numbers as roman numerals.
 