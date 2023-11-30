# BM Truck Loading Problem
- Container/Truck Loading Problem or Geometric Assignment Problem.
- We would like to arrange around 15-20 trips from 4 trucks each day (each truck does 4-5 trips per day taking 2 hours each trip) to deliver plasterboards and compound pallets from Knauf to our Lidcombe and Cabramatta stores.
- Problem: given a list of items required, please recommend a plan to arrange the 4 trucks to optimize the total cost.

## Problem Statement
Given M containers/trucks (cubic large objects) and N cargos/goods (three-dimensional items) such that:
-	All cargos/items lie entirely within the containers.
-	The items do not overlap.
-	The item on the top of other items must have something at the bottom.
-	Total weight of the items lying in the containers does not over the capacity of the container

## Data
- Trucks
  + Name: Matt     
  +	Length 9.3m /0.15 each cell = 62 cells
  +	Width 2.5m / 0.15 each cell = 16.7 cells
  +	Height 2.4m/ 0.15 each cell = 16 cells
  +	Weight 18,500 kg
  +	Cost $200

- Cargos
  + Product name: 13SO1260
  +	Length 6m / 0.15 = 40 cells	
  +	Width 1.35m / 0.15 = 9 cells	
  +	Height 0.75m / 0.15 = 5 cells	
  +	Weight 2892 kg

## Examples:
- Input:

- Output:

## Subproblem 1
- Input:
  + Given a truck with capacity of length, width, height and weight.
  + Given a list of items need to deliver.
- Output:
  + Yes/No: is possible to load all items to the truck?
        
## Subproblem 1
- Input:
  + Given a truck with capacity of length, width, height and weight.
  + Given a list of items need to load on the truck.
- Output:
  + A way to maximize the truck usage: weight optimization.
