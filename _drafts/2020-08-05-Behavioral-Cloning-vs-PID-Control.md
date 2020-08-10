# **Behavioral Cloning vs PID Control** 

---

During my studies with Udacity, I learned about various ways to control robots. The robots I controlled were cars, flying drones, and other more simple robots/agents. Two methods I'm going to write about today are PID controllers and controllers that use machine learning models.

During the Self-Driving Car Nanodegree program, I used a simulator to drive a car around a track that looked like the following image:

![png](./images/PID vs Behavioral Cloning/simulator.png)

This simulator was configurable for different projects which allowed me to play with different tools. In the behavior cloning project, I was able to record the angle at which the steering wheel was tilted and capture multiple front facing camera images, and in the PID controller project I was given how far from the center of the road I was.

If you'd like to know more about each individual project see this link to my blog post about the PID controller and this link for the behavioral cloning.



The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report

[image1]: ./examples/exampleFirstTurn.jpg "First Obstacle"
[image2]: ./examples/exampleRunOffRoadWithNoLines.jpg "No lines!"
[image3]: ./examples/exampleOfShadows "Hauntings of First Project"

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py .examples/model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model is slightly different, but it is patterned after NVIDIA's archictecture referenced in the class material. It consists of a convolutional neural network with two 5x5 filters followed by two 3x3 filters. It uses maxpooling and dropout between each layer and it ends with fully connected layers of size 1164, 100, 50, 1 using RELU layers for the activation functions.

The data is also normalized in the model using a Keras lambda layer (code line 63-66). 

#### 2. Attempts to reduce overfitting in the model

The model contains dropout layers like I mentioned, but it also has data going in both directions on the easier track, and it contains 1-2 laps of training data on the advanced track.

I of course used training and test data sets and the model was tested by running it through the simulator.

#### 3. Model parameter tuning

I had to experiment with the angle of correction when I used the left and right cameras. I tried various amounts above .2 and when I tried .1 it did much better.

#### 4. Appropriate training data

I focused on staying in the center of the road with periods of course correction when getting to close to the edge of the road. I took several laps from both courses, and the first obstacle I had was the first curve.

![alt text][image1]

I made sure to have plenty of training data on curves, and when I just thought I was getting it to work it struggled where there weren't any painted lines, and where there were large shadows across the road such as the following.

![alt text][image2]

![alt text][image3]


At times it would fail when there was a shadow across the road, and when there weren't any painted lines on the side of the road, but with a few extra training recordings under those situations it successfully learned to drive.

#### 5. Conclusion

Over-all this project was a lot of fun. I learned how to use Generators with lots of images. Transfer learning and using Keras was very helpful and a lot faster. Training a car to steer has given me a lot of ideas for other projects. One area of improvement would be to train it on more roads and get it to drive on the second course.


