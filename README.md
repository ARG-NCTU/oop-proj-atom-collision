# oop-proj-atom-collision 

<img src="./oop_project_demo.gif"/>

# For Ubuntu 
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
When you're inside the docker, please run the following commands.
```
$ python3 main.py
```
### stage1 preparing
wasd to move the generator dot, and up down right left to generate your box, then enter when you're finished player 1 or 2.
### stage2 killing
wasd to burn the player1's thruster, up down right left to burn the player2s'.

# For Windows
# Install Anaconda
Install Anaconda from following site.
https://docs.anaconda.com/free/anaconda/install/windows/
# Download oop-proj-atom-collision
Download oop-proj-atom-collision as a zip, and unzip.
### activate base env, and start the game
You can change "oop_env" to what ever the name you like.
```
$ conda create --name oop_env python=3.8.10
$ conda activate oop_env
$ conda install -c conda-forge pygame
$ conda install -c conda-forge numpy
```
cd to your oop-proj-atom-collision dir location, and run the game.
```
$ cd oop-proj-atom-collision
$ python main.py
```
