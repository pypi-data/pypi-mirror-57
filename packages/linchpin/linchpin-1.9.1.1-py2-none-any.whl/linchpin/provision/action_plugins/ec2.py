from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase
import zmq


def instance_id(result):
    return result['instance_id']


class ActionModule(ActionBase):
    ''' Send events to Nanomsg '''

    TRANSFERS_FILES = False
    # _VALID_ARGS = frozenset(('nanomsg',))

    def run(self, tmp=None, task_vars=None):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5599")
        socket.RCVTIMEO = 2000

        if task_vars is None:
            task_vars = dict()
        if self._task.args.get('state', 'present') == 'present':
            action = 'present'
            base = self._task.args['instance_tags']['name']
            count = int(self._task.args.get('count', '1'))
            for index in range(1, count):
                name = "{}({})".format(base, index)
                msg = dict(status=dict(target=name, state='Provisioning'),
                           bar=10)
                socket.send_string(str(msg))
                socket.recv_string()
        elif self._task.args['state'] == 'absent':
            action = 'absent'
            name = "{}({})".format(self._task.args['instance_tags']['name'],
                                   self._task.args['instance_ids'])
            msg = dict(status=dict(target=name, state='Destryoing'), bar=10)
            socket.send(str(msg).encode('utf-8'))
            socket.recv_string()

        result = super(ActionModule, self).run(tmp, task_vars)
        result = self._execute_module(task_vars=task_vars,
                                      wrap_async=self._task.async_val)

        del tmp  # tmp no longer has any effect
        done = False
        old_state = ''
        while not done:
            facts_args = dict(instance_ids=result['instance_ids'],
                              aws_access_key=self._task.args['aws_access_key'],
                              aws_secret_key=self._task.args['aws_secret_key'],
                              region=self._task.args['region'])
            info = self._execute_module(
                module_name='ec2_instance_facts',
                module_args=facts_args,
                task_vars=task_vars)
            done = True
            for instance in info['instances']:
                state = instance['state']['name']
                if state not in ['running', 'terminated']:
                    done = False
                if state != old_state:
                    old_state = state
                    if state == 'pending':
                        bar = 40
                    if state == 'running':
                        state = 'Done'
                        bar = 50
                    if state == 'shutting-down':
                        bar = 40
                    if state == 'terminated':
                        state = 'Done'
                        bar = 50
                else:
                    bar = 0
                base = instance['tags']['name']
                if action == 'present':
                    index = info['instances'].index(instance)
                elif action == 'absent':
                    index = instance['instance_id']
                name = "{}({})".format(base, index)
                msg = dict(status=dict(target=name, state=state), bar=bar)
                socket.send(str(msg).encode('utf-8'))
                socket.recv_string()

        return result
