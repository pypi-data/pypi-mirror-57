'''
cost.py

Cedrick Argueta
cdrckrgt@stanford.edu

cost models
'''
import numpy as np

class CostModel(object):
   def __init__(self):
        raise Exception("please instantiate a specific cost model, this is just a base class!")

   def getCost(self, domain, drone, filter_, action):
        raise Exception("please instantiate a specific cost model, this is just a base class!")

class ConstantCostModel(CostModel):
    '''
    returns a constant cost
        - cost should be negative to disincentivize living longer
    '''
    def __init__(self, cost):
        self.cost = cost

    def getCost(self, domain, drone, filter_, action):
        return self.cost

class DistanceCostModel(CostModel):
    '''
    returns the negative norm of the difference of the position of the target and seeker.
        - incentivizes ending the episode ASAP, lest it continue to accumulate negative rewards
        - rewards are scaled based on how far the seeker is from the target
    '''
    def __init__(self):
        pass

    def getCost(self, domain, drone, filter_, action):
        x, y, _ = drone.getPose()
        x_theta, y_theta = domain.getTheta()
        return -np.linalg.norm(np.array([x, y]) - np.array([x_theta, y_theta]))

class EntropyCostModel(CostModel):
    '''
    returns the negative entropy of the filter.
        - incentivizes ending the episode ASAP, lest it continue to accumulate large negative rewards
        - also incentivizes keeping entropy low
    '''
    def __init__(self):
        pass

    def getCost(self, domain, drone, filter_, action):
        entropy = filter_.entropy()
        return -entropy

class EntropyDistanceCostModel(CostModel):
    '''
    louis' cost model. cost is:
        entropy + lambda * expectation over all bins (collision occurs)
    
    incentivizes keeping entropy low, while also staying a distance away from target
    '''
    def __init__(self, lambda_, threshold):
        self.lambda_ = lambda_
        self.threshold = threshold

    def getCost(self, domain, drone, filter_, action):
        entropy = filter_.entropy()

        it = np.nditer(filter_.getBelief(), flags=['multi_index'])
        expectation = 0
        while not it.finished:
            prob = it[0] # value of prob in this bucket
            idx = it.multi_index # index of this bucket in filter (channel, x, y)
            x = (idx[1] + 0.5) * filter_.cellSize
            y = (idx[2] + 0.5) * filter_.cellSize
 
            x_seeker, y_seeker, _ = drone.getPose()
            norm = np.linalg.norm(np.array([x, y]) - np.array([x_seeker, y_seeker]))

            if norm < self.threshold: # if there's a collision for this bin
                expectation += prob

            it.iternext()

        expectation *= self.lambda_

        return -(entropy + expectation) # cost negative to discourage high entropy and collisions
        
class HighestProbDistanceCostModel(CostModel):
    '''
    rewards highest prob in a bucket
    penalizes near collisions
    '''
    def __init__(self, lambda_, threshold):
        self.lambda_ = lambda_
        self.threshold = threshold

    def getCost(self, domain, drone, filter_, action):

        max_prob = filter_.maxProbBucket()
        expectation = 0.0

        F = filter_.getBelief().squeeze()
        i, j = np.nonzero(F)
        x = (j + 0.5) * filter_.cellSize
        y = (i + 0.5) * filter_.cellSize

        centers = np.dstack((x, y)).squeeze()

        x_seeker, y_seeker, _ = drone.getPose()
        pose = np.array([x_seeker, y_seeker])

        if centers.shape == pose.shape:
            norms = np.linalg.norm(centers - pose)
        else:
            norms = np.linalg.norm(centers - pose, axis=1)

        expectation = np.sum(F[i, j][norms < self.threshold])
        expectation *= self.lambda_

        return (max_prob - expectation)

class MaxEigenvalDistanceCostModel(CostModel):
    '''
    max eigenvalue of covariance matrix corresponds to variance in most uncertain direction
    penalize this and also near-collisions
    '''
    def __init__(self, lambda_, threshold):
        self.lambda_ = lambda_
        self.threshold = threshold

    def getCost(self, domain, drone, filter_, action):
        max_eig = filter_.maxEigenvalue()

        it = np.nditer(filter_.getBelief(), flags=['multi_index'])
        expectation = 0
        while not it.finished:
            prob = it[0] # value of prob in this bucket
            idx = it.multi_index # index of this bucket in filter (channel, x, y)
            x = (idx[1] + 0.5) * filter_.cellSize
            y = (idx[2] + 0.5) * filter_.cellSize
            
            x_seeker, y_seeker, _ = drone.getPose()
            norm = np.linalg.norm(np.array([x, y]) - np.array([x_seeker, y_seeker]))

            if norm < self.threshold: # if there's a collision for this bin
                expectation += prob

            it.iternext()

        expectation *= self.lambda_

        return -(max_eig + expectation)

class DiscreteProbDistanceCostModel(CostModel):
    '''
    rewards if highest prob above threshold
    penalizes if near collisions above threshold
    '''
    def __init__(self, distance_threshold, entropy_threshold, collision_threshold):
        self.distance_threshold = distance_threshold
        self.entropy_threshold = entropy_threshold
        self.collision_threshold = collision_threshold

    def getCost(self, domain, drone, filter_, action):

        max_prob = filter_.maxProbBucket()
        expectation = 0.0

        F = filter_.getBelief().squeeze()
        i, j = np.nonzero(F)
        x = (j + 0.5) * filter_.cellSize
        y = (i + 0.5) * filter_.cellSize

        centers = np.dstack((x, y)).squeeze()

        x_seeker, y_seeker, _ = drone.getPose()
        pose = np.array([x_seeker, y_seeker])

        if centers.shape == pose.shape:
            norms = np.linalg.norm(centers - pose)
        else:
            norms = np.linalg.norm(centers - pose, axis=1)

        expectation = np.sum(F[i, j][norms < self.distance_threshold])

        reward = 1 if max_prob > self.entropy_threshold else 0
        reward = -1 if expectation > self.collision_threshold else reward
        return reward

class ThresholdProbDistanceCostModel(CostModel):
    '''
    rewards if highest prob above threshold
    penalizes if near collisions above threshold
    linear reward between threshold to 1, lambda * expectation for penalty
    '''
    def __init__(self, distance_threshold, entropy_threshold, lambda_):
        self.distance_threshold = distance_threshold
        self.entropy_threshold = entropy_threshold
        self.lambda_ = lambda_

    def getCost(self, domain, drone, filter_, action):

        max_prob = filter_.maxProbBucket()
        expectation = 0.0

        F = filter_.getBelief().squeeze()
        i, j = np.nonzero(F)
        x = (j + 0.5) * filter_.cellSize
        y = (i + 0.5) * filter_.cellSize

        centers = np.dstack((x, y)).squeeze()

        x_seeker, y_seeker, _ = drone.getPose()
        pose = np.array([x_seeker, y_seeker])

        if centers.shape == pose.shape:
            norms = np.linalg.norm(centers - pose)
        else:
            norms = np.linalg.norm(centers - pose, axis=1)

        expectation = np.sum(F[i, j][norms < self.distance_threshold])

        belief_reward = max(float(max_prob - self.entropy_threshold) / float(1 - self.entropy_threshold), 0.0)
        collision_reward = self.lambda_ * expectation
        return belief_reward - collision_reward 

class WeightedThresholdCostModel(CostModel):
    '''
    rewards if highest prob above threshold
    penalizes if near collisions above threshold
    rewards if tracking error below threshold

    each term weighted
    '''
    def __init__(self, distance_threshold, entropy_threshold, tracking_threshold, lambda_1, lambda_2, lambda_3):
        self.distance_threshold = distance_threshold # distance from target that triggers collision
        self.entropy_threshold = entropy_threshold # uncertainty measure that triggers reward in belief
        self.tracking_threshold = tracking_threshold # fraction of map that triggers penalty
        self.lambda_1 = lambda_1
        self.lambda_2 = lambda_2
        self.lambda_3 = lambda_3

    def getCost(self, domain, drone, filter_, action):

        # entropy
        # max_prob = filter_.maxProbBucket()
        # belief_reward = self.lambda_2 * max(float(max_prob - self.entropy_threshold) / float(1 - self.entropy_threshold), 0.0)
        entropy = filter_.entropy()
        belief_reward = self.lambda_2 * -entropy
        

        # near collisions
        # F = filter_.getBelief().squeeze()
        # i, j = np.nonzero(F)
        # x = (j + 0.5) * filter_.cellSize
        # y = (i + 0.5) * filter_.cellSize

        # centers = np.dstack((x, y)).squeeze()

        # x_seeker, y_seeker, _ = drone.getPose()
        # pose = np.array([x_seeker, y_seeker])

        # if centers.shape == pose.shape:
        #     norms = np.linalg.norm(centers - pose)
        # else:
        #     norms = np.linalg.norm(centers - pose, axis=1)

        # expectation = np.sum(F[i, j][norms < self.distance_threshold])

        x_seeker, y_seeker, _ = drone.getPose()
        pose = np.array([x_seeker, y_seeker])
        norms = np.linalg.norm(np.asarray([filter_.x_particles, filter_.y_particles]) - pose[:, np.newaxis], axis=0)
        expectation = np.sum(norms < self.distance_threshold) / filter_.nb_particles
        assert (expectation <= 1) and (expectation >= 0), 'expectation out of bounds'
        collision_reward = self.lambda_1 * expectation


        # tracking error
        tracking_error = np.linalg.norm(np.array(filter_.centroid()) - np.array(domain.getTheta()))
        # # normalize by the domain length
        # tracking_error = 1 - tracking_error / domain.length
        # tracking_reward = self.lambda_3 * max(float(tracking_error - self.tracking_threshold) / float(1 - self.tracking_threshold), 0.0)
        tracking_reward = self.lambda_3 * int(tracking_error < 10.)

        # dist = np.linalg.norm(np.array([x_seeker, y_seeker]) - np.asarray(domain.getTheta()))
        # if dist < self.distance_threshold and tracking_error < 15:
        #     print('real distance: ', dist)
        #     print('tracking error: ', tracking_error)
        #     # print('F: ', F)
        #     # print('centers: ', centers)

        #     print('particles shape: ', np.asarray([filter_.x_particles, filter_.y_particles]).shape)
        #     print('pose shape: ', pose.shape)
        #     particle_norms = np.linalg.norm(np.asarray([filter_.x_particles, filter_.y_particles]) - pose[:, np.newaxis], axis=0)
        #     particle_expectation = np.sum(particle_norms < self.distance_threshold) / filter_.nb_particles
        #     print('particle_norms: ', particle_norms)
        #     print('particle_expectation: ', particle_expectation)


        #     print('centers norms: ', norms)
        #     print('expectation: ', expectation)
        #     print('entropy: ', entropy)

        # print('belief_reward: ', belief_reward)
        # print('collision_reward: ', collision_reward)
        # print('tracking_reward: ', tracking_reward)

        assert np.isfinite(belief_reward), 'belief_reward contains nan values. pose: {}'.format(belief_reward)
        assert np.isfinite(collision_reward), 'collision_reward contains nan values. pose: {}'.format(collision_reward)
        assert np.isfinite(tracking_reward), 'tracking_reward contains nan values. pose: {}'.format(tracking_reward)
        return belief_reward + tracking_reward - collision_reward


class ThresholdTrackingCostModel(CostModel):
    '''
    rewards if highest prob above threshold
    penalizes if near collisions above threshold
    rewards if tracking error below threshold
    linear reward between threshold to 1, lambda * expectation for penalty, 
        includes tracking error  reward
    '''
    def __init__(self, distance_threshold, entropy_threshold, tracking_threshold, lambda_):
        self.distance_threshold = distance_threshold # distance from target that triggers collision
        self.entropy_threshold = entropy_threshold # uncertainty measure that triggers reward in belief
        self.tracking_threshold = tracking_threshold # fraction of map that triggers penalty
        self.lambda_ = lambda_

    def getCost(self, domain, drone, filter_, action):

        max_prob = filter_.maxProbBucket()
        expectation = 0.0

        F = filter_.getBelief().squeeze()
        i, j = np.nonzero(F)
        x = (j + 0.5) * filter_.cellSize
        y = (i + 0.5) * filter_.cellSize

        centers = np.dstack((x, y)).squeeze()

        x_seeker, y_seeker, _ = drone.getPose()
        pose = np.array([x_seeker, y_seeker])

        if centers.shape == pose.shape:
            norms = np.linalg.norm(centers - pose)
        else:
            norms = np.linalg.norm(centers - pose, axis=1)

        expectation = np.sum(F[i, j][norms < self.distance_threshold])

        tracking_error = np.linalg.norm(np.array(filter_.centroid()) - np.array(domain.getTheta()))
        # normalize by the domain length
        tracking_error = 1 - tracking_error / domain.length

        belief_reward = max(float(max_prob - self.entropy_threshold) / float(1 - self.entropy_threshold), 0.0)
        collision_reward = self.lambda_ * expectation
        tracking_reward = max(float(tracking_error - self.tracking_threshold) / float(1 - self.tracking_threshold), 0.0)

        # print('belief_reward: ', belief_reward)
        # print('collision_reward: ', collision_reward)
        # print('tracking_reward: ', tracking_reward)

        return belief_reward + tracking_reward - collision_reward

class SimpleHCTCostModel(CostModel):
    '''
    H - minimize entropy
    C - avoid collisions
    T - minimize tracking error
    '''
    def __init__(self, distance_threshold, lambda_1, lambda_2, lambda_3):
        self.distance_threshold = distance_threshold
        self.lambda_1 = lambda_1 # entropy
        self.lambda_2 = lambda_2 # collision
        self.lambda_3 = lambda_3 # tracking

    def getCost(self, domain, drone, filter_, action):

        norm_entropy = filter_.entropy() / np.log(filter_.buckets)

        x_seeker, y_seeker, _ = drone.getPose()
        pose = np.array([x_seeker, y_seeker])

        expectation = 0.0

        F = filter_.getBelief().squeeze()
        i, j = np.nonzero(F)
        x = (j + 0.5) * filter_.cellSize
        y = (i + 0.5) * filter_.cellSize

        centers = np.dstack((x, y)).squeeze()

        if centers.shape == pose.shape:
            norms = np.linalg.norm(centers - pose)
        else:
            norms = np.linalg.norm(centers - pose, axis=1)

        expectation = np.sum(F[i, j][norms < self.distance_threshold])

        tracking_error = np.linalg.norm(np.array(filter_.centroid()) - np.array(domain.getTheta()))
        # normalize by the domain length
        tracking_error = tracking_error / (domain.length * np.sqrt(2))

        belief_reward = 1 - norm_entropy
        collision_reward = 1 - expectation
        tracking_reward = 1 - tracking_error

        belief_reward = self.lambda_1 * belief_reward
        collision_reward = self.lambda_2 * collision_reward
        tracking_reward = self.lambda_3 * tracking_reward

        # print('belief_reward: ', belief_reward)
        # print('collision_reward: ', collision_reward)
        # print('tracking_reward: ', tracking_reward)

        return belief_reward + collision_reward + tracking_reward
