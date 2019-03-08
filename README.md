Industrial Automation Advanced Manufacturing
# glassblowing-robotics

  Started in April 2018
    This project was originally conceptualized as only a torch controller to be operated with a Raspberry Pi Voice Kit and
    the Google Voice API and then continued into a fully automated lathe with robotic tooling arm. Each system(torch, lathe,
    arm, air) have a dedicated Pi which receives commands remotely via Wifi from the voice kit. 
        #Update: Currently in the process of changing from a WIFI remote signal to an MQQT publish/subscribe model, enhancing 
        UI, and integrating web/mobile app control of each system. 
    
   Torch operations:
   
      Basics:
    A keyword is programmed to be recognized by the voice kit which fires a function adjusting the 
    value of a GPIO pin. The torch operates with propane as a fuel and oxygen as the accelerant. The mixture and velocity of 
    the gasses determines the flame atmosphere. Flame atmosphere is what determines how evenly and how fast the glass heats 
    up, as well as how different colored glasses will react. The torch has two rings of fire, the inside for detailed work 
    and an outer ring for heating large surfaces. Each ring is controlled by a propane and oxygen valve for a total of 4 
    valves per torch. Each gas line is controlled with a proportional flow valve which opens and closes depending on the PWM 
    amount of volts it receives. The voltage coming from a GPIO pin ranges from 0 to 3.3v which is altered by programming a 
    value between 0 and 1. This voltage is then passed through an amplifier bringing up the voltage to a maximum of 9.5v. 
    Because the oxygen runs at 40 psi and the propane operates at 10psi each amplifier must be calibrated to account for flow
    rates and pressures in order to achieve an even flame atmosphere. In addition each valve is calibrated at the     manufacturer's
    facility as they use the pressure in the line as part of the force to move the valve. This greatly reduces the amount of
    electricity needed to open and close the valve. 
    
      Improvements:
    The Pi does not produce a pure PWM signal, only a faux one replicated by
    gpiozero libraries. This results in a signal that can veer off over time, creating a different flame atmosphere which
    produces variances in the final glass product. Even a change of .0001 will result in an altered atmosphere. In addition, 
    other factors like fuel tanks running low, being over drawn, freezing, or losing purity all change flame atmosphere. To 
    compensate for unexpected changes sensors adapted from oil valves in combustion engines are placed in the gas lines and
    provide a feedback mechanism to ensure stable flame characteristics. This sensor is both temperature and atmospherically 
    stable to allow the system to work year round. They also transmit their data via I2C communication and required
    a switch from remote signals via gpiozero libraries and Wifi to a MQQT framework with subscribe/publish communications. 
    
   Lathe operations:
   
      Basics:
    A glassblowing lathe is very similar to a metal or wood lathe except that there is a large bore to allow for the open
    tube to extend out of and for air supply to be attached. Tooling is achieved by heating the glass and either blowing
    or manipulating with graphite paddles and reamers as it spins. The glass is held between two chucks, the right chuck
    and the carriage between the two chucks that holds the torches and tooling arm moves in and out along the x axis with
    hand wheels. Stepper motors were set in place of the hand wheels with custom welded mounts. The stepper motors turn
    a step every time a step pin is set high then low. A turn is equal to 200 steps without using microsteps. Another pin 
    determines direction if set high or low. The DC motor that operates the lathe is turned on and off via a relay. Direction
    and speed are preset with an analog controller.
    
       Improvements:
    The stepper motor was geared up to allow it to more easily turn the chuck spindle with a chain driven gear system.
    Plans in place to change from open loop stepper motors to closed loop DC motors with encoders. 
    Changing the DC motor driver to a modern one, allowing for forward, reverse, and speed control of the lathe. 
    Replace chuck keys with high power servos to allow for releasing and gripping of glass while still spinning.
    
   Arm operations:
    
        Basics:
    An aluminum arm with graphite tool allows the molten glass to be paddled or reamed. Base is a DC motor with encoder for
    360 degree movement and the arm consists of two sets of two high power geared servos placed in parallel to allow the 
    tool to be raised and extended along the y and z axis. The arm system came with 10/32 connectors which were drilled to
    allow for active water cooling through the aluminum extrusions, keeping the servo housing cool enough to operate in
    high temp conditions.
    
        Improvements:
    Switching to a ROS programming language to more easily account for compounding changes in arm angles.
    
   Air operations:
   
        Basics: 
     An aquarium pump on a relay controls how long air will be blown into the glass. Some of the variables to overcome are
     the glass being exactly the right temperature, the glass being evenly heated, the back flow of hot air, and variances 
     created by implementing back flow arrestors.
     
        Improvements:
     Switching to a system similar to the torch line operations but with compressed air. The pump works for long(3seconds)
     slow even blowing but short bursts are inconsistent. 
