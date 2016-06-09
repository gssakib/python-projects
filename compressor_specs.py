import sys
sys.path.insert(0,'C:\Users\gazi\Documents\OpenMDAO')
import openmdao

##importing openmdao classes
from openmdao.api import Group, Problem, Component, IndepVarComp

class Inlet_Condition(Component):
    def __init__(self):
	super(Inlet_Condition, self).__init__()
	
	#adding constraints and initial conditions
	 self.add_param('ambient_temp', 298.0, desc='Ambient Temp', units='K')
	 self.add_param('tube_pressure', 100.0, desc='Tube Pressure', units='Pa')
	 self.add_param('Density', 1.17E-03, desc='Density', units='kg/m^3')
	 self.add_param('R', 287.0, desc='Gas Constant', units='J/kg*K')
	 self.add_param('sound_speed', 298.0, desc='Ambient Temp', units='K')
	 self.add_param('inlet_area', 1008.0, desc='Inlet Area', units='m^2')
	 self.add_param('total_CR', 15.0, desc='Total CR', units='None')
	 self.add_param('spec_air', 1008.0, desc='Specific Heat of Air', units='J/kg*K')
	self.add_param('vent_dia', 0.254, desc='Vent Diameter', units='m')
	
	 #adding derived set of initial conditions
	 self.add_output('speed_sound', 0.0, desc='Speed of Sound', units='m/s')
	 self.add_output('inlet_velocity', 0.0, desc='Speed of Sound', units='m/s')
	 self.add_output('mass_flow', 0.0, desc='Mass Flow', units='kg/s')
	 self.add_output('stag_temp', 0.0, desc='Mass Flow', units='K')
	 self.add_output('stag_pressure', 0.0, desc='Stagnation Pressure', units='Pa')
	 self.add_output('c_cross', 0.0, desc='Critical Cross Section', units='m^2')
	 self.add_output('stag_pressure', 0.0, desc='Stagnation Pressure', units='Pa')
	 self.add_output('c_d_velocity', 0.0, desc='Compressor Downstream Velocity', units='m/s')
	 self.add_output('local_temp_comp_air', 0.0, desc='Local Temperature of Compressed Air', units='K')
	 self.add_output('local_pressure_comp_air', 0.0, desc='Local Pressure of Compressed Air', units='Pa')
	 self.add_output('mach_check', 0.0, desc='Mach Check Number', units='None')
	 self.add_output('stag_pressure', 0.0, desc='Stagnation Pressure', units='Pa')
	 self.add_output('comp_outlet_area', 0.0, desc='Area of the compressor outlet', units='m^2')
	 self.add_output('local_temp_comp_air', 0.0, desc='Local Temperature of Compressed Air', units='K')


	self.add_output('critical_ratio', 0.0, desc='Cross Section / Critical Cross Section', units='K')
	self.add_output('local_temp_comp_air', 0.0, desc='Local Temperature of Compressed Air', units='K')
	self.add_output('mach_in_ven', 0.0, desc='Mach number inside vent tube', units='None')
	self.add_output('pressure_in_ven', 0.0, desc='Pressure inside vent tube.', units='Pa')
	self.add_output('powr_single', 0.0, desc='Single Cycle POwer ', units='KW')
	
	self.add_output('powr_total', 0.0, desc='Total Cycle Power', units='KW')
	self.add_output('cooling_load', 0.0, desc='Cooling Load of Intercooling', units='K')
	self.add_output('vent_cross', 0.0, desc='Cross section of vent tube', units='K') 
	
	def solve_nonlinear(self, params, unknowns, resids):
	
	
	
		
		