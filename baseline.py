from environment import InterviewEnv

env = InterviewEnv()
state = env.reset()

action = {
    "select_topic": state["weak_topics"][0],
    "difficulty": "medium"
}

state, reward, done, _ = env.step(action)

print("Final State:", state)
print("Reward:", reward)