# Trilateration

<h3> Overview 
<h5> The purpose of this project is to develop an easy method for indoor localization utilizing distance beacons. It currently can have an input of as many beacons as you would like, however, it takes the three closest and uses them to calculate the point of the device. 
<h5>
This should be the output: 
<img width="825" alt="Screen Shot 2021-12-14 at 9 12 21 AM" src="https://user-images.githubusercontent.com/95883134/146015035-3e45c55f-7a42-40e0-928a-db532541ba19.png">
<h5>
The magenta text is printing the coordinates of the beacons in use in relation to the Array 'b'. The first yellow text is the calculated coordinate point, and the second text is the degree needed to turn to face the "destination point" as is defined on line 14. 

<h3> Moving Forward
<h5> I want to do some experimentation to find a percentage error of the beacons for this project and take multiple distance samples to find a more accurate distance. Then impliment the code on a robotic platform with dynamic destinations (i.e. An app is connected that allows for commands to be sent. There are then predefined points that it can go to to retrieve items or complete a task, and then return to the point where the iphone is therefore finding the person to signal the task is complete.)
  
 <h3> Further Research
 <h5>https://www.101computing.net/cell-phone-trilateration-algorithm/
  
