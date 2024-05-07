
import gym
from gym import spaces
import numpy as np

class MultiAgentContinuousPlanningEnv(gym.Env):
    def __init__(self, num_agents, num_actions, num_steps):
        self.num_agents = num_agents
        self.num_actions = num_actions
        self.num_steps = num_steps

        self.action_space = spaces.Box(low=0, high=1, shape=(self.num_agents, self.num_actions), dtype=np.float32)
        self.observation_space = spaces.Box(low=0, high=1, shape=(self.num_agents,), dtype=np.float32)

        self.agents_positions = np.zeros(self.num_agents)
        self.agents_goals = np.random.rand(self.num_agents)
        self.steps_taken = 0

    def step(self, actions):
        assert len(actions) == self.num_agents

        self.agents_positions += actions

        rewards = []
        for i in range(self.num_agents):
            distance_to_goal = abs(self.agents_goals[i] - self.agents_positions[i])
            rewards.append(-distance_to_goal)  # Penalizar la distancia al objetivo

        self.steps_taken += 1
        done = self.steps_taken >= self.num_steps

        return self.agents_positions, rewards, done, {}

    def reset(self):
        self.agents_positions = np.zeros(self.num_agents)
        self.agents_goals = np.random.rand(self.num_agents)
        self.steps_taken = 0
        return self.agents_positions

# Crear entorno
num_agents = 3
num_actions = 1  # Movimiento en una dimensión
num_steps = 10

env = MultiAgentContinuousPlanningEnv(num_agents, num_actions, num_steps)

# Ejecutar simulación
for _ in range(num_steps):
    actions = np.random.rand(num_agents, num_actions)  # Acciones aleatorias para cada agente
    observations, rewards, done, _ = env.step(actions)
    print("Observations:", observations)
    print("Rewards:", rewards)
    if done:
        break
