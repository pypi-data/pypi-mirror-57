from pgmpy.factors import TabularCPD
from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.inference import DBNInference
dbnet = DBN()
dbnet.add_edges_from([(('Z', 0), ('X', 0)), (('X', 0), ('Y', 0)),
                      (('Z', 0), ('Z', 1))])
z_start_cpd = TabularCPD(('Z', 0), 2, [[0.5, 0.5]])
x_i_cpd = TabularCPD(('X', 0), 2, [[0.6, 0.9],
                                   [0.4, 0.1]],
                     evidence=[('Z', 0)],
                     evidence_card=2)
y_i_cpd = TabularCPD(('Y', 0), 2, [[0.2, 0.3],
                                   [0.8, 0.7]],
                     evidence=[('X', 0)],
                     evidence_card=2)
z_trans_cpd = TabularCPD(('Z', 1), 2, [[0.4, 0.7],
                                       [0.6, 0.3]],
                     evidence=[('Z', 0)],
                     evidence_card=2)
dbnet.add_cpds(z_start_cpd, z_trans_cpd, x_i_cpd, y_i_cpd)
dbnet.initialize_initial_state()
dbn_inf = DBNInference(dbnet)
dbn_inf.start_junction_tree.nodes()
print('dbn_inf = %r' % (dbn_inf,))
