# candy_robot
This is the code for the candy_robot project. 

Here is what the robot does:

check www.rasppiproject.com for more details

Button for random candy:
	The user can press R to initiate a sort of roulette game. The lights will flicker
and become exponentially slower, until the light blinks on one of the sides, and therefore the candy
will automatically come out of that side. 

General Movement:

	The robot runs on tank tracks, rather slowly, but surely

Selecting candy:
	The user can press A or B to select candy from one of the tubes. They hold
different candies. With this, an auger attached to pulleys will dispense the candy


Candy reserves:
	The robot will constantly check the photoresistors to see if they detect
light or if they don't. If they do not detect light, that means there is a good amount of candy
left in the candy tubes. The robot will constantly be reading these photoresistors with a .1 uF 
ceramic capacitor. If there is not a lot of candy left, then the robot light will turn on, on that side.
