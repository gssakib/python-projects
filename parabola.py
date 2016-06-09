#from __future__ import print_function

import sys
sys.path.insert(0,'C:\Users\gazi\Documents\OpenMDAO')
import openmdao


from openmdao.api import IndepVarComp, Component, Problem, Group, ScipyOptimizer, ExecComp, SqliteRecorder
class Parabola(Component):
    """ Evaluates the equation f(x,y) = (x-3)^2 + xy + (y+4)^2 - 3 """

    def __init__(self):
        super(Parabola, self).__init__()

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

		
#########Calculation of explicit unkowns given parameters
#if __name__ == '__main__':


root = Group()
top = Problem(root)



root.add('p1', IndepVarComp('x', 5.0), promotes = ['x'])
root.add('p2', IndepVarComp('y', 2.0), promotes = ['y'])
root.add('my_comp', Parabola(), promotes = ['x', 'y'])

#root.connect('p1.x', 'my_comp.x')
#root.connect('p2.y', 'my_comp.y')




top.setup()
top.run()

print(top['my_comp.f_xy'])

	

print("-" * 20)
    
	
###########Optimization given parameters
root =  Group()
top = Problem(root)


# Initial value of x and y set in the IndepVarComp.
root.add('p1',IndepVarComp('x',3.0))
root.add('p2',IndepVarComp('y',-4.0))
root.add('my_comp',Parabola())

root.connect('p1.x','my_comp.x')
root.connect('p2.y','my_comp.y')
top.driver = ScipyOptimizer()
top.driver.options['optimizer'] = 'SLSQP'

top.driver.add_desvar('p1.x', lower = -50, upper = 50)
top.driver.add_desvar('p2.y', lower= -50, upper = 50)
top.driver.add_objective('my_comp.f_xy')





top.setup()

#you can also specify initial values post setup
top['p1.x'] = 3.0
top['p2.y'] = -4.0

top.run()


print('\n')
print'Minimum of %f found at (%f,%f)' % (top['my_comp.f_xy'],top['my_comp.x'],top['my_comp.y'])

 
######Optimization given parameters and constraints

root = Group()
top = Problem(root)

root.add('p1',IndepVarComp('x',3.0))
root.add('p2',IndepVarComp('y',-4.0))
root.add('my_comp',Parabola())
root.add('con', ExecComp('c = x-y'))

root.connect('p1.x','my_comp.x' )
root.connect('p2.y', 'my_comp.y')
root.connect('my_comp.x', 'con.x')
root.connect('my_comp.y', 'con.y')

top.driver = ScipyOptimizer()
top.driver.options['optimizer'] = 'SLSQP'
 
top.driver.add_desvar('p1.x',lower = -50,upper = 50)
	
top.driver.add_desvar('p2.y', lower = -50, upper =50)
top.driver.add_objective('my_comp.f_xy')
top.driver.add_constraint('con.c', lower = 15.0, upper = 16)

recorder = SqliteRecorder('Parabola')
recorder.options['record_params'] = True
recorder.options['record_metadata'] = True
top.driver.add_recorder(recorder)


top.setup()
top.run()
top.cleanup()
print('\n')
print'Minimum of %s found at (%s,%s)' %(top['my_comp.f_xy'],top['my_comp.x'],top['my_comp.y'])




	
