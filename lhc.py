
import sys
sys.path.insert(0,'C:\Users\gazi\Documents\OpenMDAO')
import openmdao


from openmdao.api import IndepVarComp, Group, Problem, ScipyOptimizer, ExecComp, DumpRecorder
from openmdao.test.paraboloid import Paraboloid

from openmdao.drivers.latinhypercube_driver import OptimizedLatinHypercubeDriver

top = Problem()
root = top.root = Group()

root.add('p1', IndepVarComp('x', 50.0), promotes=['x'])
root.add('p2', IndepVarComp('y', 50.0), promotes=['y'])
root.add('comp', Paraboloid(), promotes=['x', 'y', 'f_xy'])

top.driver = OptimizedLatinHypercubeDriver(num_samples=4, seed=0, population=20, generations=4, norm_method=2)
top.driver.add_desvar('x', lower=-50.0, upper=50.0)
top.driver.add_desvar('y', lower=-50.0, upper=50.0)

top.driver.add_objective('f_xy')

recorder = DumpRecorder('paraboloid')
recorder.options['record_params'] = True
recorder.options['record_unknowns'] = False
recorder.options['record_resids'] = False
top.driver.add_recorder(recorder)

top.setup()
top.run()

top.cleanup()