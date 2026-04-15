# Unity–RoboDK Digital Twin Integration

## Overview
This project demonstrates a digital twin system by integrating Unity with RoboDK using a Python Flask server. The system enables interaction between a virtual interface and a robotic simulation environment.

## Features
- Digital twin of robotic workcell using Unity and RoboDK
- Real-time command-based control via Flask server
- Execution of robot tasks such as pick-and-place and conveyor operations
- Modular communication between Unity, Python, and RoboDK

## System Architecture
Unity (User Input) → Flask Server (Python) → RoboDK API → Robot Simulation

## Workflow
- User inputs command through Unity interface  
- Unity sends HTTP request to Flask server  
- Flask processes request and triggers RoboDK API  
- Robot executes task in simulation  

## Tools & Technologies
- Unity (C#)
- Python (Flask)
- RoboDK API

## Current Status
- Successful command-based communication between Unity and RoboDK  
- Robot tasks triggered from Unity interface  
- Functional digital twin prototype implemented  

## Limitations
- One-way communication (Unity → RoboDK)  
- No real-time feedback loop  
- Limited object interaction capabilities  

## Future Scope
- Bidirectional communication  
- Real-time synchronization using robot pose data  
- Integration with ROS or advanced communication protocols  
