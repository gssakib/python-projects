from __future__ import print_function

import sys
sys.path.insert(0,'C:\Users\gazi\Documents\OpenMDAO')
import openmdao


import numpy as np

from openmdao.api import Component

class SellarDisc1(Component):
	def __init__(self):
		super(SellarDisc1,self).__init__()
		
		self.add_param('z', val = np.zeros(2))
		self.add_param('x1', val = 0.0)
		self.add_param('y2', val = 1.0)
		self.add_output('y1', val = 1.0)
		
	
	def solve_nonlinear(self, params, unknowns, resids):
		z1 = params['z'][0]
		z2 = params['z'][1]
		x = params['x1']
		
		y2 = params['y2']
		
		y1 = unknowns['y1']
		
		y1 = z1**2 + x + z2 -0.2*y2 
	def linearize(self, params, unknowns, resids):
		# "Jacobian method.."
		
		J = {}
		J['y1','y2'] = -0.2
		J['y1', 'z'] = np.array([[2*params['z'][0] , 1.0]])
		J['y1', 'x1'] = 1.0
		
		
		
			
		return J
		
class SellarDisc2(Component):
	def __init__(self):
		super(SellarDisc2, self).__init__()
		self.add_param('z', val = np.zeros(2))
		self.add_param('y1', val = 1.0)
		
		self.add_output('y2', val = 1.0)
		
	
	def solve_nonlinear(self,params,unknowns, resids):
		y2 = unknowns['y2']
		z1 = params['z'][0]
		z2 = params['z'][1]
		y1 = abs(params['y1'])
	
		y2 = y1**(0.5) + z1 + z2
		
	
	
	
	def linearize(self, params, uknowns, resids):
	
		#'Jacobian methods......'
		
		J ={}
		
		J['y2', 'z' ] = np.array([[1.0,1.0]])
		
		J['y2', 'y1'] = 0.5*params['y1']**(-0.5)
		
		return J
		

from openmdao.api import ExecComp, IndepVarComp, Group, NLGaussSeidel, ScipyGMRES

class SellarDerivatives(Group):
	def __init__(self):
		super(SellarDerivatives,self).__init__()
		
		self.add('px',IndepVarComp('x1',1.0), promotes = ['x1'])
		self.add('pz', IndepVarComp('z', np.array([5.0,2.0])), promotes = ['z'])
		
		self.add('d1', SellarDisc1(),promotes =['z','x1','y1','y2'])
		self.add('d2', SellarDisc2(), promotes = ['z', 'y1', 'y2'])
		
		self.add('obj_cmp', ExecComp('obj = x1**2 + z[1] + y1 + exp(-y2)', z = np.array([5.0,2.0]), x1 = 1.0, y1 = 0.0, y2 = 0.0), promotes = ['obj','x1','z','y1','y2'])
		self.add('con_cmp1', ExecComp('con1 = -y1 + 3.16', y1 = 0.0), promotes=['y1', 'con1'])
		self.add('con_cmp2', ExecComp('con2 = y2 - 24.0',y2 = 0.0), promotes=['y2', 'con2'])
		
		self.n1_solver = NLGaussSeidel()
		self.n1_solver.options['atol'] = 1.0e-12
		
		
		self.ln_solver = ScipyGMRES()
		
		

from openmdao.api import Problem, ScipyOptimizer

top = Problem()
top.root = SellarDerivatives()
top.driver = ScipyOptimizer()
top.driver.options['optimizer'] = 'SLSQP'
top.driver.options['tol'] = 1.0e-8

top.driver.add_desvar('z', lower = np.array([-10.0,0.0]), upper = np.array([10.0,10.0]))
top.driver.add_desvar('x1', lower = 0.0, upper = 10.0)
top.driver.add_objective('obj')
top.driver.add_constraint('con1', upper = 0.0)
top.driver.add_constraint('con2', upper = 0.0) 


top.setup()
top['x1'] = 1.0
top['z'] = np.array([5.0,2.0])

top.run()

print("\n")
print ("Minimum found at (%f,%f,%f)"% (top['z'][0],top['z'][1],top['x1']))

print ("Coupling vars: %f, %f" %(top['y1'],top['y2']))
print ("Minimum Objective: %f" %(top['obj'])) 








		
		