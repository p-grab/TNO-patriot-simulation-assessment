# Patriot Air Defense Simulation

This repo is a solution for Code Assessment TNO Mission Simulation & Training

## Assumptions
- One row represent 1 second of radar data (as file is 20 rows and simulation should be 1 second)
- Values in each row are seprearterd by ";" and are binary integers
- Each scan is processed seperately (because the file can be updated)
- The simulation runs for a maximum of 20 seconds and will terminate earlier if not input is provided
- Simulation time is represented by printing 1second steps but no real-time delay was added

## Run
python main.py

## Test
python -m pytest -v

## Requirements
- Python 3.9+
- pytest (for test only)

## Design Structure
Patriot:
 - Radar
 - IFF
 - FiringUnit
