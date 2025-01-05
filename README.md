# maze_solver

##  1. Maze navigation using Dijkstra's algorithm 
There are many algorithms to solve mazes but I think dijkistra algorithm is one of the most simplest approach to do that. Dijkstra’s Algorithm is one of the popular basic graph theory algorithms. It is used to find the shortest path between nodes on a graph. The image given had only one valid path from start to goal so there was no such case of finding the shortest path but the reason I chose this algorithm was because of **its simplicity** and **its scalibility to other algorithms**(like **A*** which could be an overkill here but can be used for much complex case). The reason I am using a search based method is because of **discrete nature** of the image which I will explain a bit later.

Since we are inputting an image let's see how to parse it and apply dijkstra algorithm here. We can think of an image as a matrix of pixels. Each pixel has an RGB value of 0,0,0 or 255,255,255 (we took gray image as input). Our goal is to create a path which starts in the white and does not cross into the black boundaries. To do so we can treat each pixel as a node and draw edges between neighboring pixels with edge lengths based on RGB value differences. We will use the Euclidean squared distance formula and add 0.1 to ensure no 0-distance path lengths (for white-to-white pixel travel). Hence we can use this to trace the path. 


The result would be something like this: 

![image](https://github.com/user-attachments/assets/94067f78-5110-46ad-ab36-b8a88c487141)


As we can see, the shortest path from source to destination will clearly be around the barrier, not through it. 


## 2. Mobile Robot with Arm

Let's say if the maze is placed on a table and a robot arm is holding a pen to traverse the maze
from the entrance to the exit, what additional factors need to be considered beyond the
solution developed for Problem 1?

```
Well if this is the case then we will need to consider the constraint of the arm. Let's say you need to reach your
hand to grasp something. now your hand can only reach a certain area of space which is called as workspace. This
constraint will also be faced by robotic arm which can only traverse till its workspace area. To cover whole maze
points we need to move the robot to complete the traversal.

Another thing would be motion of the arm and gripper control. We will need to calculate arm's joint angles using
inverse kinematics and have a control system such that gripper could always hold the pen againts the ground
```

## 3. Real-case senario

Now what If it is a mobile robot traversing through a real maze in 3D, what additional factors need
to be considered?

```
1. Here we will discuss about the discrete space that I was talking about earlier. Since image is made up of pixels,
we are just joining the edges between nodes/pixels. That means we have discretized the space which we can't mimick
in the real world. For this, sampling based path planning could be used which gives a smoother path for robot to follow.
Similarly, we also need to define the kinematic motion model of the vehicle to see check if we can follow that path
and then use a path following algorithm on the path.

2. Another thing to keep in mind is that here I have assumed the starting and goal position of the robot and already
know the map by input image. In real life senario that is not the case. We also need to scan the environment/maze to
get the map as well as localize ourself in it which is done by SLAM(Simulataneous Localization and Mapping) techniques.

3. Finally, we need to consider low level planning which is control actions of steering and acceleration or
deceleration to follow the path.

```


## Steps to run code

1. Clone the repository
2. cd under repository
3. run "python3 main.py"


(make sure you have installed numpy, open cv and matplotlib)
