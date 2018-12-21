import tensorflow as tf


def update_manager_command_parser(parser):
    parser.add_argument('--u_m', dest='update_manager', choices=['adagrad', 'adadelta', 'rmsprop', 'nesterov', 'adam'],
                        help='Update mechanism', default='adagrad')
    parser.add_argument('--u_l', help='Learning rate', default=0.1, type=float)
    parser.add_argument('--u_rho', help='rho parameter for Adadelta and RMSProp (momentum for Nesterov momentum)',
                        default=0.9, type=float)
    parser.add_argument('--u_b1', help='Beta 1 parameter for Adam', default=0.9, type=float)
    parser.add_argument('--u_b2', help='Beta 2 parameter for Adam', default=0.999, type=float)


def get_update_manager(args):
    if args.update_manager == 'adagrad':
        return Adagrad(learning_rate=args.u_l)
    elif args.update_manager == 'adadelta':
        return Adadelta(learning_rate=args.u_l, rho=args.u_rho)
    elif args.update_manager == 'rmsprop':
        return RMSProp(learning_rate=args.u_l, rho=args.u_rho)
    elif args.update_manager == 'nesterov':
        return NesterovMomentum(learning_rate=args.u_l, momentum=args.u_rho)
    elif args.update_manager == 'adam':
        return Adam()
    else:
        raise ValueError('Unknown update option')


class Adagrad(object):

    def __init__(self, learning_rate=0.01, **kwargs):
        super(Adagrad, self).__init__(**kwargs)

        self.learning_rate = learning_rate
        self.name = 'Ug_lr' + str(self.learning_rate)

    def __call__(self):
        return tf.train.AdagradOptimizer(learning_rate=self.learning_rate)


class Adadelta(object):

    def __init__(self, learning_rate=1.0, rho=0.95, **kwargs):
        super(Adadelta, self).__init__(**kwargs)

        self.learning_rate = learning_rate
        self.rho = rho
        self.name = 'Ud_lr' + str(self.learning_rate) + '_rho' + str(self.rho)

    def __call__(self):
        return tf.train.AdadeltaOptimizer(learning_rate=self.learning_rate, rho=self.rho)


class RMSProp(object):

    def __init__(self, learning_rate=1.0, rho=0.9, **kwargs):
        super(RMSProp, self).__init__(**kwargs)

        self.learning_rate = learning_rate
        self.rho = rho
        self.name = 'Ur_lr' + str(self.learning_rate) + '_rho' + str(self.rho)

    def __call__(self):
        return tf.train.RMSPropOptimizer(learning_rate=self.learning_rate, decay=self.rho)


class NesterovMomentum(object):

    def __init__(self, learning_rate=1.0, momentum=0.9, **kwargs):
        super(NesterovMomentum, self).__init__(**kwargs)

        self.learning_rate = learning_rate
        self.momentum = momentum
        self.name = 'Un_lr' + str(self.learning_rate) + '_m' + str(self.momentum)

    def __call__(self):
        return tf.train.MomentumOptimizer(learning_rate=self.learning_rate, momentum=self.momentum, use_nesterov=True)


class Adam(object):

    def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999, **kwargs):
        super(Adam, self).__init__(**kwargs)

        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.name = 'Ua_lr' + str(self.learning_rate) + '_b1_' + str(self.beta1) + '_b2_' + str(self.beta2)

    def __call__(self):
        return tf.train.AdamOptimizer(learning_rate=self.learning_rate, beta1=self.beta1, beta2=self.beta2)
