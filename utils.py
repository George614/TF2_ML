import configargparse

PARSER = configargparse.ArgParser(default_config_files=['configs/mountainCar.config'])
PARSER.add('-c', '--config_path', required=False, is_config_file=True, help='config file path')
PARSER.add('--exp_name', required=True, help='name of experiment')
PARSER.add('--env_name', required=True, help='name of environment')
PARSER.add('--max_frames', required=True, type=int, help='max number of frames in episode')
PARSER.add('--min_frames', required=True, type=int, help='min number of frames in episode')
PARSER.add('--max_trials', required=True, type=int, help='max number of trials')
PARSER.add('--buffer_size', required=True, type=int, help='buffer size for caching data')
PARSER.add_argument('--full_episode', dest='full_episode', action='store_true', help='ignore dones')
PARSER.add_argument('--no_full_episode', dest='full_episode', action='store_false', help='ignore dones')
PARSER.add_argument('--render_mode', dest='render_mode', action='store_true')
PARSER.add_argument('--no_render_mode', dest='render_mode', action='store_false')
PARSER.add('--n_actions', required=True, type=int, help='number of discrete actions agent can take')
PARSER.add('--a_width', required=True, type=int, help='width of action vector')
PARSER.add('--o_size', required=True, type=int, help='observation size')
PARSER.add('--z_size', required=True, type=int, help='hidden state size')
PARSER.add('--data_path', required=True, type=str, help='path to the training data', default='./')

PARSER.add('--vae_batch_size', required=True, type=int, help='batch size for vae train')
PARSER.add('--vae_learning_rate', required=True, type=float, help='vae learning rate')
PARSER.add('--vae_kl_tolerance', required=True, type=float, help='vae kl tolerance for clipping')
PARSER.add('--vae_kl_weight', required=True, type=float, help='vae kl-d weight')
PARSER.add('--vae_num_epoch', required=True, type=int, help='vae num epoch for training')
PARSER.add('--vae_optimizer', type=str, help='Adam, RMSprop, SGD.', default='Adam')

PARSER.add('--planner_lookahead', type=int, default=30, help='num of time steps to repeat an action')
PARSER.add('--planner_plan_depth', type=int, default=3, help='depth in the planning horizon')
PARSER.add('--planner_n_samples', type=int, default=100, help='num of samples to draw during the state rollout')
PARSER.add('--planner_rho', type=float, default=0.1, help='risk aversion or greediness of the agent')
PARSER.add('--planner_gamma', type=float, default=1.0, help='temperature parameter used in policy selection')
PARSER.add_argument('--planner_full_efe', dest='planner_full_efe', action='store_true')
PARSER.add_argument('--planner_no_full_efe', dest='planner_full_efe', action='store_false')
PARSER.set_defaults(render_mode=True)