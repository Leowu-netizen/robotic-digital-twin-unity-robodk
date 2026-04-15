# Unity–RoboDK Digital Twin Integration
Digital twin of an industrial robotic system using Unity and RoboDK with real-time control integration.


## 1. Introduction
This project presents a basic implementation of a digital twin system by integrating Unity with RoboDK using a Python Flask server. The objective is to enable interaction between a virtual interface (Unity) and a robotic simulation environment (RoboDK).

The system allows a user to control robot operations such as pick-and-place tasks and conveyor movement through keyboard inputs in Unity.

---

## 2. Objective
The primary objective of this project is to:
- Establish communication between Unity and RoboDK
- Implement command-based control of a robotic system
- Demonstrate a foundational approach toward digital twin systems in industrial automation

---

## 3. System Architecture

The system follows a three-layer architecture:

User Input (Unity)
        ↓
Unity (C# Script)
        ↓
HTTP Request
        ↓
Flask Server (Python)
        ↓
RoboDK API
        ↓
Robot Execution (RoboDK Simulation)

---

## 4. Methodology

### 4.1 Unity (Frontend)
Unity is used as the user interface where keyboard inputs are captured. Based on the input, HTTP POST requests are generated and sent to the Flask server.

### 4.2 Flask Server (Middleware)
A Flask-based server is implemented in Python to act as an intermediary between Unity and RoboDK. It defines API endpoints such as:
- `/pick_place`
- `/start_conveyor`

These endpoints receive requests from Unity and translate them into commands using the RoboDK API.

### 4.3 RoboDK (Backend)
RoboDK executes the robotic operations. Predefined programs such as pick-and-place and conveyor movement are triggered through the API.

---

## 5. Workflow

1. The user presses a key in Unity  
2. Unity sends an HTTP request to the Flask server  
3. Flask processes the request and identifies the corresponding endpoint  
4. The RoboDK API is invoked to execute the desired robot program  
5. The robot performs the action within the simulation environment  

---

## 6. Technologies Used

- Unity (C#)
- Python (Flask)
- RoboDK API

---

## 7. Results

The system successfully demonstrates command-based synchronization between Unity and RoboDK. Robot actions such as pick-and-place operations and conveyor movement can be triggered from Unity.

---

## 8. Limitations

- The system currently supports one-way communication (Unity to RoboDK)
- Real-time feedback and synchronization are not implemented
- Object manipulation (e.g., dynamic spawning) faced API compatibility challenges

---

## 9. Future Scope

- Implementation of bidirectional communication
- Real-time synchronization using pose and joint data
- Integration with advanced communication protocols such as WebSockets or ROS

---

## 10. Conclusion

This project demonstrates a foundational digital twin system where a virtual interface can control robotic operations in a simulation environment. It highlights the importance of middleware in enabling communication between heterogeneous systems and provides a basis for further development in industrial automation.

---

## 11. Author
Agnes Simson
