from __future__ import print_function

import sys
sys.path.insert(0,'C:\Users\gazi\Documents\OpenMDAO')
import openmdao


from openmdao.api import IndepVarComp, Component, Problem, Group, ScipyOptimizer

class Paraboloid(Component):
    """ Evaluates the equation f(x,y) = (x-3)^2 + xy + (y+4)^2 - 3 """

    def __init__(self):
        super(Paraboloid, self).__init__()

        self.add_param('x', val=0.0)
        self.add_param('y', val=0.0)

        self.add_output('f_xy', val=0.0)

    def solve_nonlinear(self, params, unknowns, resids):
        """f(x,y) = (x-3)^2 + xy + (y+4)^2 - 3
        """

        x = params['x']
        y = params['y']

        unknowns['f_xy'] = (x-3.0)**2 + x*y + (y+4.0)**2 - 3.0

    def linearize(self, params, unknowns, resids):
        """ Jacobian for our paraboloid."""

        x = params['x']
        y = params['y']
        J = {}

        J['f_xy', 'x'] = 2.0*x - 6.0 + y
        J['f_xy', 'y'] = 2.0*y + 8.0 + x
        return J

if __name__ == "__main__":

    top = Problem()

    root = top.root = Group()

    root.add('p1', IndepVarComp('x', 3.0))
    root.add('p2', IndepVarComp('y', -4.0))
    root.add('my_comp', Paraboloid())

    root.connect('p1.x', 'my_comp.x')
    root.connect('p2.y', 'my_comp.y')

    top.setup()
    top.run()

    print(top['my_comp.f_xy'])
	
if __name__ == "__main__":

    top = Problem()

    root = top.root = Group()

    root.add('p1', IndepVarComp('x', 5.0))
    root.add('p2', IndepVarComp('y', 2.0))
    root.add('p', Paraboloid())

    root.connect('p1.x', 'p.x')
    root.connect('p2.y', 'p.y')

    top.setup()
    top.run()

    print(top['p.f_xy'])
	
print("-" * 10)

top = Problem()
root = top.root = Group()

# Initial value of x and y set in the IndepVarComp.
root.add('p1',IndepVarComp('x',3.0))
root.add('p2',IndepVarComp('y',-4.0))
root.add('p',Paraboloid())

root.connect('p1.x','p.x')
root.connect('p2.y','p.y')
top.driver = ScipyOptimizer()
top.driver.options['optimizer'] = 'SLSQP'

top.driver.add_desvar('p1.x', lower = -50, upper = 50)
top.driver.add_desvar('p2.y', lower= -50, upper = 50)
top.driver.add_objective('p.f_xy')



top.setup()

#you can also specify initial values post setup
top['p1.x'] = 3.0
top['p2.y'] = -4.0

top.run()
print('\n')
print('Minimum of %f found at (%f,%f)' % (top['p.f_xy'],top['p.x'],top['p.y']))

 	

	




# Initial value of x and y set in the IndepVarComp.





















		