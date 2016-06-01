## importing functions from python lib

from __future__ import print_function

##setting path to openmdao parent directory
import sys
sys.path.insert(0,'C:\Users\gazi\Documents\OpenMDAO')
import openmdao

##importing openmdao classes
from openmdao.api import Group, Problem, Component, IndepVarComp

##creating customizedclass "MultiplyByTwoComponent" that is-a Component

class MultiplyByTwoComponent(Component):
	def __init__(self):
		
		super(MultiplyByTwoComponent, self).__init__()#always call the base class constructor first
		## class MultiplyByTwoComponent has-a function add_param that takes 'x_input' and 'val' as parameters
		self.add_param('x_input',val = 0.0) # the input that will be multiplied by 2.
		
		## class MultiplyByTwoComponent has-a function add_output that takes 'y_input' and 'shape' as parameters
		self.add_output('y_output', val = 0.0)#shape = 1 => a one dimensional array of length 1(a scalar)
		
		#an internal variable that counts the number of times this component was executed.
		self.counter = 0
	
	##class MultiplyByTwoComponent has-a function solve_nonlinear that takes 'self','params', 'unknowns' and 'resids' as parameters
	def solve_nonlinear(self,params,unknowns,resids):
		unknowns['y_output'] = params['x_input']**2
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


