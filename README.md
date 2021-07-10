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

### 1.x # TODO: any more methods?

### 1.5 transportation_methods.xlsx #TODO implement this (adrian)

## 2 IO handling
### 2.1 trona mining
### 2.1.1 trona refining 
### 2.2 solvay process

## 3 Calculators
### 3.1 kilowat hours calculators
#### 3.1.1 QReactors
#### 3.1.2 QMachines
__methods__
1. haulage vehicle
  applies to shuttle cars, transportation vehicles, LHD vehicles
2. belt conveyor 
  applies to all belt conveyors with inclines and declines




