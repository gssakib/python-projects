from __future__ import print_function

from openmdao.api import Group, Problem, Component, IndepVarComp

class MultiplyByTwoComponent(Component):
    def __init__(self):
        super(MultiplyByTwoComponent, self).__init__() # always call the base class constructor first
        self.add_param('x_input', val=0.) # the input that will be multiplied by 2
        self.add_output('y_output', shape=1) # shape=1 => a one dimensional array of length 1 (a scalar)

        # an internal variable that counts the number of times this component was executed
        self.counter = 0

    def solve_nonlinear(self, params, unknowns, resids):
        unknowns['y_output'] = params['x_input']*2
        self.counter += 1

root = Group()
root.add('indep_var', IndepVarComp('x', 7.0))
root.add('my_comp', MultiplyByTwoComponent())
root.connect('indep_var.x', 'my_comp.x_input')

prob = Problem(root)
prob.setup()
prob.run()

result = prob['my_comp.y_output']
count = prob.root.my_comp.counter
print(result)
print(count)