# oop-proj-atom-collision 

<img src="./oop_project_demo.gif"/>

# For Ubuntu only
OOP class example game
## How to clone
We have installed the dependencies in the oop-proj-atom-collision docker. 
Most of the movingpandas functions will work well.
```
$ cd ~
$ git clone git@github.com:ARG-NCTU/oop-proj-atom-collision.git
```
## How to run docker
```
$ cd oop-proj-atom-collision
$ source docker_run.sh
```
## How to play
When you're inside the docker just run the following command.
```
$ python3 main.py
```
### stage1 preparing
wasd to move the generator dot, and up down right left to generate your box, then enter when you're finished player 1 or 2.
### stage2 killing
wasd to burn the player1's thruster, up down right left to burn the player2s'.

# For Windows
Install Anaconda from folloing site.
https://docs.anaconda.com/free/anaconda/install/windows/

### activate base env, and start the game
```
$ cd ~
$ conda activate 
$ pip3 install pygame
$ cd oop-proj-atom-collision
$ python3 main.py
```
