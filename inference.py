import os
from environment import InterviewEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "dummy-model")
HF_TOKEN = os.getenv("HF_TOKEN", "dummy")

env = InterviewEnv()
state = env.reset()

task_name = "interview-task"
benchmark = "interview-env"

print(f"[START] task={task_name} env={benchmark} model={MODEL_NAME}")

rewards = []
steps = 0

try:
    for i in range(3):
        action = {
            "select_topic": state["weak_topics"][0],
            "difficulty": "medium"
        }

        state, reward, done, _ = env.step(action)
        rewards.append(f"{reward:.2f}")
        steps += 1

        print(f"[STEP] step={steps} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

        if done:
            break

    success = done

except Exception as e:
    success = False
    print(f"[STEP] step={steps} action=null reward=0.00 done=true error={str(e)}")

print(f"[END] success={str(success).lower()} steps={steps} rewards={','.join(rewards)}")