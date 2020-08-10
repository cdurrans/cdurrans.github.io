---
# layout: post
---

#### In this blog post, I want to share some of my experiences with Controllers and their applications. My first introduction to PID controllers was in Udacity's Self Driving Car Nanodegree where we learned to control the car's steering wheel and speed.

![png](/images/PID vs Behavioral Cloning/simulator.png)


[//]: # (Image References)

[image1]: ./images/PID/steadyPatternImprovement.png "Steady Progress"
[image_p]: ./images/PID/p_controller_tau_0.1.png "P controller example"
[image_pm]: ./images/PID/p_controller_multi_tau.png "P controller multiple tau"
[image_p_pd]: ./images/PID/P_PD_example.png "P and PD controller"
[image_compare]: ./images/PID/Controller_Examples_with_bias_example.png "Controller comparison"
[video1]: ./images/PID/project_video.mp4 "Video"

### Controllers and the Control Loop

A controller is a device or software that controls the settings of another device to achieve a goal. Let's look at controlling a car's speed as an example. Car's have a gas pedal, a brake, an odometer, and a controller to change the car's speed. If the controller or driver in this case wants to go 50 mph then the person will press the gas pedal down until the odometer says the car has reached 50 mph. If the car is going faster than 50 mph the driver will either stop pressing the gas or will press the brake to slow down. In this way the car will go the intended speed, but we are interested in automating the controller, so lets move on to the PID controller.

A PID controller is the most common way to design a controller, because it is effective and simple. PID stands for proportional–integral–derivative, and I'll talk about each part.

#### Proportional (P)

Continuing with the car's speed, the proportional part changes the speed in proportion to the difference between the goal and current speed. So when the car is going 50 mph slower than the goal speed the car will accelerate faster than it would if it was going 5 mph under. This makes intuitive sense, and one would be tempted to call it good enough, but the car will reach a point where it oscilates around the goal. See the image below.

![png](/images/PID/p_controller_tau_0.1.png)

Image shows difference from goal. In the case of speed this 1 +/- mph difference around goal doesn't seem like a big deal, but minimizing this oscilation can be very important in other applications. One way to minimize it is with tuning because the distance from the goal or error is multiplied by a supplied value called tau. See in the above image how tau was set to 0.1? Below are some examples of how adjusting tau changes the behavior.

![png](/images/PID/p_controller_multi_tau.png)

As you can see, as tau gets smaller the controller adjusts its speed much more slowly which causes the longer oscilations.

Below is what the p part of the controller looks like in my code.

```c++
// P part of PID Controller
// Kp is the p tau while p_error is the proportion error.
totalError = (-Kp * p_error);
```

#### Derivative (D)

To further improve the controller we will implement the other parts of the PID controller. We will skip the Integral portion for now, so the derivative part of the equation takes the derivative of the car's speed and subtracts it from the proportional value. This works to smooth the oscillations until the point where the car aligns itself with the goal.

![png](/images/PID/P_PD_example.png)

```c++
// PD controller
// Kp = p tau 
// Kd = d tau
p_error = cte; //proportional error
d_error = cte - previous_step_cte;
totalError = (-Kp * p_error) - (Kd * d_error)
```

In a perfect world we would be done, but real world systems have bias or errors. In our case the odometer could be consistently misreading the car's speed causing the car's computer to miscalculate how to reach its goal. What's worse is that the bias or error could change over time with slippery rain conditions. That is where the integral part comes in.

#### Integral (I)

The integral part of the controller takes all of the errors over each time step and sums them up to calculate the integral of the function. So as the device has mistakes in its measurements the accumulating error will cause the controller to correct itself. Below we have a comparison of a PD controller and a PID controller. When the controller has systematic errors the PD controller will behave correctly, but it will be off dependent upon the error. In the chart below it follows the reference line, but it is off by roughly 0.5. With the PID controller it corrects for the error and follows the reference line.

![png](/images/PID/Controller_Examples_with_bias_example.png)

```c++
// PID controller
// Kp = p tau 
// Kd = d tau
// Ki = i tau
p_error = cte; // error
d_error = cte - previous_step_cte;
i_error = i_error + cte; // i_error steadily changes by adding cte at each time step
totalError = (-Kp * p_error) - (Kd * d_error) - (Ki * i_error);
```


### Summary

So we've seen how PID controllers work, and how the different parts are necessary and helpful. It is beautiful in its design and simplicity, and I love using it in projects. In a future blog post I'll talk about how to find parameters for the PID controller and alternatives.

Below is my submission video for the self-driving car PID project. If I could do it again, I would smooth out the jerky turns, and I would start by playing more with the derivative part of the controller. I was having a hard time getting it to react quickly on the sharp turns while also making it drive smoother. It was my first work with a PID controller, and it could definitely be better. Cheers!

<!-- 
### Experience tuning the PID

In order to tune the PID controllers automatically, I implemented the twiddle algorithmn we learned in class to automatically explore variations in parameters, but it was taking forever to converge to a working solution. The problem was that I started out with my numbers being too small. I was also trying to use another controller for the speed, so trying to get a working solution for both controllers at the same time was getting no-where with my initial parameter settings.

To illustrate what was happenning I've provided a description and a video below:

Description:
    As I tried tuning the PID controller, I started out with all three of the tau parameters being small and of equal size. First I tried 0.001 for all three then I went smaller and smaller all while trying to get it to not turn so sharp. What ended up happening though was it took too long to correct itself once the car turned from a far side to start heading back to the center. The car ended up sideways going slow and not being able to turn fast enough. See the example video A.

Video A:

<video width="800" height="550" controls>
  <source src="https://media.githubusercontent.com/media/cdurrans/cdurrans.github.io/master/images/PID/Turn_Too_Far.mp4" type="video/mp4">
</video>


After much trial and error and some reading about other techniques for tuning PID controllers, I found a solution that worked for me. After I found a working solution though I found that I was still able to make my average error smaller, but it came at a cost of making the car drive jerkier. I continued to use twiddle and as you can see below, I had steady "improvements" after I found a working solution. The parameters P=0.15, I=0.0001, and D=2.5 worked and drove smoothly, but the parameters P=0.465, I=0.00031 and D=5 was more abrupt when turning. I ended up using: P=0.15, I=0.0001, and D=2.5.

![png](/images/PID/steadyPatternImprovement.png)

I'm sure I can make the car drive smoother with further trial and error and some better use of Twiddle, but I'll come back to that at another time. Below I've included a video of my current solution driving around the track. -->

<video width="800" height="550" controls>
  <source src="https://media.githubusercontent.com/media/cdurrans/cdurrans.github.io/master/images/PID/final_run_around.mp4" type="video/mp4">
  <!-- https://github.com/cdurrans/cdurrans.github.io/tree/master/images/Histogram%20Segments -->
</video>