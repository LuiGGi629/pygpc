import pygpc
import numpy as np
from collections import OrderedDict
import examples.MyModel as MyModel

fn_results = "/tmp/MyAnalysis"

# define model
model = MyModel

# define problem (the parameter names have to be the same as in the model)
parameters = OrderedDict()
parameters["x1"] = pygpc.Beta(pdf_shape=[1, 1], pdf_limits=[1.2, 2])
parameters["x2"] = 1.25
parameters["x3"] = pygpc.Beta(pdf_shape=[1, 1], pdf_limits=[1.2, 2])
problem = pygpc.Problem(model, parameters)

# gPC options
options = dict()
options["order_start"] = 1
options["order_end"] = 10
options["interaction_order"] = 2
options["solver"] = "Moore-Penrose"
options["settings"] = None
options["seed"] = 1
options["matrix_ratio"] = 1.5
options["eps"] = 1e-2
options["n_cpu"] = 0    # n_cpu = 0; the model is capable of to compute multiple grid-points in parallel
options["fn_results"] = fn_results
options["print_func_time"] = True

# define algorithm
algorithm = pygpc.RegAdaptive(problem=problem, options=options)

# run gPC algorithm
gpc, coeffs, results = algorithm.run()

# plot 2D grid (only feasible for 2D problems)
pygpc.plot_2d_grid(coords=gpc.grid.coords,
                   fn_plot=fn_results + '_grid')

# Post-process gPC
pygpc.get_sensitivities_hdf5(fn_gpc=options["fn_results"],
                             output_idx=None,
                             calc_sobol=True,
                             calc_global_sens=True,
                             calc_pdf=True)

# Validate gPC vs original model function (Monte Carlo)
nrmsd = pygpc.validate_gpc_mc(gpc=gpc,
                              coeffs=coeffs,
                              n_samples=int(1e4),
                              output_idx=0,
                              fn_out=options["fn_results"] + '_validation_mc')

# Validate gPC vs original model function (2D-slice)
pygpc.validate_gpc_plot(gpc=gpc,
                        coeffs=coeffs,
                        random_vars=["x3", "x1"],
                        n_grid=[10, 25],
                        output_idx=[0, 1],
                        fn_out=options["fn_results"] + '_validation_2d')

print("\t > Maximum NRMSD (gpc vs original): {:.2}%".format(np.max(nrmsd)))

print("done!\n")