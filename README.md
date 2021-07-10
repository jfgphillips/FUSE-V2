# FUSE-V2 A boutique framework program for lithium and sodium mining and extraction processes

## 1 Data files 
### 1.1 Mining_attributes.xlsx
an excel file with sheet names for various initialising steps

common to all mining operations (underline this)
* __macro details__
* __utility__
* __shuttle car__
* __conveyor belt__
* __ventilation__
* __hoist__
#### 1.1.1 room and pillar method
for a continuous room and pillar miner to operate:
1 continuous miner feeds ore to 2 shuttle cars
1 quadbolter moves behind providing structure to the rooms
1 electric LHD on maintenance ops
shuttle cars feed a belt mounted feeder breaker

* __belt mounted feeder breaker__
* __continuous miner__
* __roof bolter__
#### 1.1.2 longwall method
for a longwall shearer to operate:
3 borer miners are required, 2 for longwall development and 1 for ventialtion work
2 AFC drives are required to pull 1 longwall shearer along the face of the mine in both directions
AFC carries the rock + ore to the stage loader
stage loader feeds a crusher
crusher feeds ore + rock to a shuttle car or a belt conveyor

* __longwall shearer__
* __AFC drive__
* __stage loader__
* __borer miner__ 
* __t shields__
* __operation equipment__


### 1.2 solvay_attributes.xlsx
an excel file with sheet names for various initialising steps

#### 1.2.1 infrastructure

* __ammonia saturator__
* __solvay tower__
* __filter__
* __calciner__
* __lime kiln__
* __slaker__
* __ammonia recovery tower__

#### 1.2.2 reactants
* __brine__
* __limestone__
* __ammonia__
* __coke__

### 1.3 solution_mining.xlsx #TODO: implement this
#### 1.3.1 alkali extraction process
#### 1.3.2 sequesqicarbonate extraction process

### 1.4 brine_evaporation.xlsx #TODO: implement this (maria)

#### 1.4.1 from solution mining
#### 1.4.2 from lake deposits
#### 1.4.3 from desalination waste

### 1.5 geothermal_extraction.xlsx # TODO: implement this (Chantal)

### 1.6 transportation_methods.xlsx #TODO implement this (adrian)

### 1.x # TODO: any more methods?

## 2 IO handling packages
### 2.1 MineIO
#### 2.1.1 underground
each machine has a self initiator which reads from the data files
the important thing to note is that object attributes are degenerate
this is for when you want to find something e.g. roofBolter_att.power 
is the same as shuttleCar_att.power; differentiated by their prefix
#### 2.1.2 open pit # TODO: Implement this if required

### 2.2 SolvayIO
• each machine has self initiator which reads from the data files

• each machine has a forward reaction, and a reverse reaction (forward reaction is to 
tune the machines with existing data). reverse reaction will be used to determine how many machines 
are required for production requirements

• each machine has a qmachine method in which the user decides what type of reactor is used
and in the data file specifies the parameters required for the calculation performs calculation using
calculators.QReactors.tubeFurnace(parameters) for example

### 2.3 solutionIO
### 2.4 brineIO
### 2.5 geothermalIO
### 2.6 transportationIO


## 3 Calculator package
### 3.1 kilowat hours calculators
#### 3.1.1 QReactors.py
__methods__
1. fixed bed reactor

    requirements:

        reaction temperature
        reaction time
        surface area
        thermal conductivity
        wall_thickness
2. batch reactor
   
   requirements:
   
       reaction temperature
       reaction time
       surface area
       thermal conductivity 
       wall thickness
       liq density
3. tube furnace
   
    requirements:

        reaction temperature
        reaction time
        reactor volume
        weighted av density

4. continuous stirred tank reactor
#### 3.1.2 QMachines.py
__methods__
1. haulage vehicle
   applies to shuttle cars, transportation vehicles, LHD vehicles
   
   requirements:
   
       motor_kW
       haulage running load
       haulage load rating
       unit run time
       per unit time
       operating hours
   
2. belt conveyor 
  applies to all belt conveyors with inclines and declines
   
   requirements:
   
       belt speed
       belt length
       gradient
       conveyor output
       drive train efficicency

``
### 3.2 optimal mine practices
#### 3.2.1 drumHoist.py
#### 3.2.2 taylorsLaw.py

### 3.3 unitConversions.py
this python file contains all required conversions for the overall program




