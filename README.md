---
title: Interview Training Env
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
---

# Adaptive Interview Training Environment
# Adaptive Interview Training Environment

## 🚀 Overview
This project implements a real-world OpenEnv environment where an AI agent learns how to prepare a student for interviews.

The environment simulates interview preparation by tracking:
- Skill level
- Weak topics
- Confidence level

---

## ⚙️ How It Works
The agent interacts with the environment using:
- `reset()` → initializes the state
- `step(action)` → performs an action
- `state()` → returns current state

---

## 🎯 Action Space
- select_topic (string)
- difficulty (string)

---

## 👀 Observation Space
- skill_level (int)
- weak_topics (list)
- confidence (float)

---

## 🧪 Tasks
- **Easy** → Basic topic selection  
- **Medium** → Focus on weak topics  
- **Hard** → Multi-step optimization  

---

## 🧠 Reward Logic
- Rewards correct topic selection  
- Rewards proper difficulty level  
- Penalizes incorrect choices  
- Encourages confidence improvement  

---

## ▶️ Run the Project

```bash
python baseline.py