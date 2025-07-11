# 6-DOF Inverse Kinematics Prediction using Deep Learning

This project explores the use of supervised learning to approximate inverse kinematics (IK) for a 6-degree-of-freedom industrial robot — the **ABB IRB 2400** manipulator.

Rather than analytically solving the complex IK equations, this approach trains a neural network to directly predict joint angles (`q1–q6`) from desired end-effector poses (`x, y, z, roll, pitch, yaw`) and a given initial joint configuration. The method demonstrates the potential of machine learning for efficient motion planning, especially in redundant or highly articulated systems.

> Developed by Thomas Schaeffer  
> Date: Dec 2023  
> Dataset: [ABB IRB 2400 Kinematics Dataset](https://www.kaggle.com/datasets/luisatencio/abb-irb-2400-arm-robot-kinematics-dataset)

---

## Objectives

- Predict joint angles for a desired end-effector pose using a trained neural network
- Integrate learned IK into simulated motion planning (linear + circular paths)
- Use forward kinematics to visualize and validate predicted trajectories
- Lay the groundwork for future planning-aware IK models with obstacle avoidance and motor constraints

---

## Dataset

- ~400,000+ samples of joint inputs and outputs (`q1–q6`) with corresponding end-effector frames (`x, y, z, roll, pitch, yaw`)
- Source: Real or simulated kinematic solutions from ABB IRB 2400 robot

---

## Model Architecture

- Input:  
  `[x, y, z, roll, pitch, yaw, q1_in, q2_in, q3_in, q4_in, q5_in, q6_in]`  
- Output:  
  `[q1, q2, q3, q4, q5, q6]` (joint angles to achieve the desired pose)

```python
model = Sequential([
    Dense(128, activation='relu', input_shape=(12,)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(6)  # Output layer for joint angles
])
