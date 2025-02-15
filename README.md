# Stanford-Pupper_Beer_Project
Stanford Pupper Beer Robot
## 🐶 Overview
This repository documents my project to build a quadruped robot (Stanford Pupper Bot) using a Raspberry Pi Pico, MG996R servos, and an L298N motor driver. The robot will be capable of walking, grabbing objects with a robotic arm, and returning to its starting point.

---
## 📂 Project Structure
```
stanford-pupper-bot/
├── README.md                # Project Overview
├── BOM.md                   # Bill of Materials
├── docs/                    # Wiring diagrams, schematics
├── code/                    # Python scripts for control
│   ├── servo_test.py        # Script to test servos
│   ├── gait_control.py      # Walking gait algorithm
│   └── arm_control.py       # Robotic arm control
└── LICENSE                  # License file
```

---
## 📦 Bill of Materials (BOM)
### 🛠️ Components:
- **Microcontroller:** Raspberry Pi Pico
- **Servos:** 4 x MG996R High-Torque Servos
- **Motor Driver:** L298N Dual H-Bridge Motor Driver
- **Battery:** Blomiky 7.4V 2S 3000mAh LiPo with T-Plug
- **Power Distribution Board:** PCB007 12-Position Board
- **Switch:** XINYIELE 12V Round Rocker Switch
- **Fuse:** 10A Inline Fuse Holder
- **BEC:** JINOARC 5V/6V Switchable UBEC
- **Connectors:** Amass XT60EW-M and T-Plug to XT60 Adapter
- **Wiring:** Servo Extension Cables, Dupont Jumper Wires

### 🧰 Tools:
- **Multimeter:** AstroAI Digital Multimeter
- **Prototyping Board:** Breadboard Kit
- **Screws and Mounting Kit:** 720 pcs Assorted Nuts and Bolts

---
## 📝 Next Steps:
1. **[ ] Wiring Diagram:** Design and upload the wiring schematic.
2. **[ ] Servo Test:** Create and upload `servo_test.py`.
3. **[ ] Motor Test:** Create `motor_test.py` for L298N.
4. **[ ] Walking Algorithm:** Develop `gait_control.py`.
5. **[ ] Arm Control:** Program `arm_control.py`.

---
## 💡 License
This project is licensed under the MIT License.