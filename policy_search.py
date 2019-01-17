import numpy as np
from task import Task
#when we have continous action space we use Gaussin policy(linear func with gaussian policy)
#ie we can sample action from gaussian dist. where parameter of our dist are determined by our features..mean=simple liner comb. of feat and varience sigma^@ can be fixed or paratermized in similar way.. a~ pi(s,a, w)= N( u, sigma^2) turn them into prob that represent stocastic policy
class PolicySearch_Agent():
    def __init__(self, task):
        # Task (environment) information
        self.task = task
        self.state_size = task.state_size
        self.action_size = task.action_size
        self.action_low = task.action_low
        self.action_high = task.action_high
        self.action_range = self.action_high - self.action_low

        self.w = np.random.normal(
            size=(self.state_size, self.action_size),  # weights for simple linear policy: state_space x action_space
            scale=(self.action_range / (2 * self.state_size))) # start producing actions in a decent range

        # Score tracker and learning parameters
        self.best_w = None
        self.best_score = -np.inf
        self.noise_scale = 0.1

        # Episode variables
        self.reset_episode()

    def reset_episode(self):
        self.total_reward = 0.0
        self.count = 0
        state = self.task.reset()
        return state

    def step(self, reward, done):
        # Save experience / reward
        self.total_reward += reward
        self.count += 1

        # Learn, if at end of episode
        if done:
            self.learn()

    def act(self, state):
        # Choose action based on given state and policy
        action = np.dot(state, self.w)  # simple linear policy
        #q=state[i]*polcy_w[colum i]
        #a=[1,2,3](1x3) * b=[[1 2][4 5][6 7]](3x2)
        #take 'a' as state(x,y,z) and b as prob of selecting a[1] as 1 , p(a[2])=4,p(a[3])=6 
        #so as defination we multiply state with there prob and concate them to (1x2) matrix
        #print("w",self.w);
        #print("action",action)
        return action

    def learn(self):
        # Learn by random policy search, using a reward-based score
        self.score = self.total_reward / float(self.count) if self.count else 0.0
        
        if self.score > self.best_score:
            self.best_score = self.score
            self.best_w = self.w
            self.noise_scale = max(0.5 * self.noise_scale, 0.01)
        else:
            self.w = self.best_w
            self.noise_scale = min(2.0 * self.noise_scale, 3.2)
        self.w = self.w + self.noise_scale * np.random.normal(size=self.w.shape)  # equal noise in all directions
        