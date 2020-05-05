# ROS EXAMPLE 1
This is the very first **HELLO WORLD** example from the book **Learning ROS for Robotics Programming by Aaron Martinez and Enrique Fernandez**

**Prerequisites-**
   1) Ubuntu 16.04 or higher 
   2) ROS Melodic/Hydro/Kinetic
   
## Steps (Everything has to be done in the Ubuntu Terminal)
  1) Setting up the environment <br/>
      `$ source /opt/ros/<ROS_VERSION>/setup.bash` <br/>
      
  2) Creating the workspace <br/>
      `$ mkdir –p ~/dev/catkin_ws/src` <br/>
      `$ cd ~/dev/catkin_ws/src` <br/>
      `$ catkin_init_workspace` <br/>
  3) Building the workspace <br/>
      `$ cd ~/dev/catkin_ws` <br/>
      `$ catkin_make <br/>
      
  4) Creating a ROS package
      `$ cd ~/dev/catkin_ws/src` <br/>
      `$ catkin_create_pkg chapter2_tutorials std_msgs roscpp` <br/>
      Note- Here we have installed dependencies-<br/>
         **std_msgs:** This contains common message types representing primitive data 
         types and other basic message constructs, such as MultiArray.<br/>
         **roscpp:** This is a C++ implementation of ROS. It provides a client library 
         that enables C++ programmers to quickly interface with ROS topics, services, 
         and parameters
