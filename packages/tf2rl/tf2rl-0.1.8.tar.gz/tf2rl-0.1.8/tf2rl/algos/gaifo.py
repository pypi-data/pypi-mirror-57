import tensorflow as tf

from tf2rl.algos.gail import GAIL


class GAIfO(GAIL):
    def train(self, agent_states, agent_next_states, expert_states, expert_next_states):
        loss, accuracy, js_divergence = self._train_body(
            agent_states, agent_next_states, expert_states, expert_next_states)
        tf.summary.scalar(name=self.policy_name+"/DiscriminatorLoss", data=loss)
        tf.summary.scalar(name=self.policy_name+"/Accuracy", data=accuracy)
        tf.summary.scalar(name=self.policy_name+"/JSdivergence", data=js_divergence)

    @tf.function
    def _train_body(self, agent_states, agent_next_states, expert_states, expert_next_states):
        epsilon = 1e-8
        with tf.device(self.device):
            with tf.GradientTape() as tape:
                real_logits = self.disc([expert_states, expert_next_states])
                fake_logits = self.disc([agent_states, expert_acts])
                loss = -(tf.reduce_mean(tf.math.log(real_logits + epsilon)) +
                         tf.reduce_mean(tf.math.log(1. - fake_logits + epsilon)))
            grads = tape.gradient(loss, self.disc.trainable_variables)
            self.optimizer.apply_gradients(
                zip(grads, self.disc.trainable_variables))

        accuracy = \
            tf.reduce_mean(tf.cast(real_logits >= 0.5, tf.float32)) / 2. + \
            tf.reduce_mean(tf.cast(fake_logits < 0.5, tf.float32)) / 2.
        js_divergence = self._compute_js_divergence(
            fake_logits, real_logits)
        return loss, accuracy, js_divergence

    def inference(self, states, actions):
        if states.ndim == actions.ndim == 1:
            states = np.expand_dims(states, axis=0)
            actions = np.expand_dims(actions, axis=0)
        return self._inference_body(states, actions)

    @tf.function
    def _inference_body(self, states, actions):
        with tf.device(self.device):
            return self.disc.compute_reward([states, actions])
