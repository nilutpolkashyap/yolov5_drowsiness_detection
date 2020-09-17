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
         
   5) Building a ROS package
      `$ cd ~/dev/catkin_ws/` <br/>
      `$ catkin_make` <br/>
      **Remember that you should run the catkin_make command line in the workspace folder.**
   6) Creating Nodes
      Navigate to the chapter2_tutorials/src/ folder using the following command: <br/>
      `$ roscd chapter2_tutorials/src/' <br/>
      Inside the src folder, create the two C++ files example1_a.cpp and example1_b.cpp which are the publisher and subscriber respsctively. <br/>
   7) Building the nodes
         Edit the CMakesList.txt file inside the chapter2_tutorials/src/ folder and at the end of the fle, add the following lines:
         `include_directories(` <br/>
         `include` <br/>
         `${catkin_INCLUDE_DIRS}` <br/>
         `)` <br/>
         `add_executable(chap2_example1_a src/example1_a.cpp)` <br/> 
         `add_executable(chap2_example1_b src/example1_b.cpp)` <br/>
         `add_dependencies(chap2_example1_a chapter2_tutorials_generate_messages_cpp)` <br/>
         `add_dependencies(chap2_example1_b chapter2_tutorials_generate_messages_cpp)` <br/>
         `target_link_libraries(chap2_example1_a ${catkin_LIBRARIES})` <br/>
         `target_link_libraries(chap2_example1_b ${catkin_LIBRARIES})` <br/>
   8) Compiling the nodes
          To build the package and compile all the nodes, use the catkin_make tool as follows: <br/>
      `$ cd ~/dev/catkin_ws/` <br/>
      `$ catkin_make chapter2_tutorials <br/>
