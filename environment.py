class InterviewEnv:
    def __init__(self):
        self.initial_state = {
            "skill_level": 3,
            "weak_topics": ["python", "sql"],
            "confidence": 0.5
        }
        self.state_data = self.initial_state.copy()

    def reset(self):
        self.state_data = self.initial_state.copy()
        return self.state_data

    def step(self, action):
        reward = 0

        topic = action.get("select_topic")
        difficulty = action.get("difficulty")

        if topic in self.state_data["weak_topics"]:
            reward += 0.4

        if self.state_data["skill_level"] <= 3 and difficulty == "easy":
            reward += 0.2
        elif self.state_data["skill_level"] <= 5 and difficulty == "medium":
            reward += 0.3
        elif difficulty == "hard":
            reward += 0.4

        self.state_data["confidence"] += 0.1
        reward += 0.2

        if topic not in self.state_data["weak_topics"]:
            reward -= 0.2

        done = self.state_data["confidence"] >= 1.0

        return self.state_data, round(reward, 2), done, {}

    def state(self):
        return self.state_data