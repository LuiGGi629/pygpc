.. note::
    :class: sphx-glr-download-link-note

    Click :ref:`here <sphx_glr_download_auto_algorithms_plot_algorithm_mestatic.py>` to download the full example code
.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_algorithms_plot_algorithm_mestatic.py:


Algorithm: MEStatic
===================


.. code-block:: default

    import pygpc
    from collections import OrderedDict

    fn_results = 'tmp/mestatic'       # filename of output
    save_session_format = ".hdf5"     # file format of saved gpc session ".hdf5" (slow) or ".pkl" (fast)








Loading the model and defining the problem
------------------------------------------


.. code-block:: default


    # define model
    model = pygpc.testfunctions.SurfaceCoverageSpecies()

    # define problem
    parameters = OrderedDict()
    parameters["rho_0"] = pygpc.Beta(pdf_shape=[1, 1], pdf_limits=[0, 1])
    parameters["beta"] = pygpc.Beta(pdf_shape=[1, 1], pdf_limits=[0, 20])
    parameters["alpha"] = 1.
    problem = pygpc.Problem(model, parameters)








Setting up the algorithm
------------------------


.. code-block:: default


    # gPC options
    options = dict()
    options["method"] = "reg"
    options["solver"] = "Moore-Penrose"
    options["settings"] = None
    options["order"] = [10, 10]
    options["order_max"] = 10
    options["interaction_order"] = 2
    options["matrix_ratio"] = 2
    options["n_cpu"] = 0
    options["gradient_enhanced"] = True
    options["gradient_calculation"] = "FD_2nd"
    options["gradient_calculation_options"] = {"dx": 0.05, "distance_weight": -2}
    options["error_type"] = "loocv"
    options["qoi"] = "all"
    options["n_grid_gradient"] = 5
    options["classifier"] = "learning"
    options["classifier_options"] = {"clusterer": "KMeans",
                                     "n_clusters": 2,
                                     "classifier": "MLPClassifier",
                                     "classifier_solver": "lbfgs"}
    options["fn_results"] = fn_results
    options["save_session_format"] = save_session_format
    options["grid"] = pygpc.Random
    options["grid_options"] = None

    # generate grid
    grid = pygpc.Random(parameters_random=problem.parameters_random,
                        n_grid=1000,  # options["matrix_ratio"] * n_coeffs
                        seed=1)

    # define algorithm
    algorithm = pygpc.MEStatic(problem=problem, options=options, grid=grid)








Running the gpc
---------------


.. code-block:: default


    # Initialize gPC Session
    session = pygpc.Session(algorithm=algorithm)

    # run gPC algorithm
    session, coeffs, results = session.run()





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    Performing 1000 simulations!

    Total parallel function evaluation: 0.9397580623626709 sec
    Gradient evaluation: 0.055585384368896484 sec
    Determine gPC coefficients using 'Moore-Penrose' solver (gradient enhanced)...
    Determine gPC coefficients using 'Moore-Penrose' solver (gradient enhanced)...

























    LOOCV computation time: 0.42769742012023926 sec
    -> relative loocv error = 0.019449331878849545

























    LOOCV computation time: 0.2946758270263672 sec

























    LOOCV computation time: 0.32419443130493164 sec




Postprocessing
--------------


.. code-block:: default


    # read session
    session = pygpc.read_session(fname=session.fn_session, folder=session.fn_session_folder)

    # Post-process gPC
    pygpc.get_sensitivities_hdf5(fn_gpc=options["fn_results"],
                                 output_idx=None,
                                 calc_sobol=True,
                                 calc_global_sens=True,
                                 calc_pdf=True,
                                 algorithm="sampling",
                                 n_samples=1e3)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    > Loading gpc session object: tmp/mestatic.hdf5
    > Loading gpc coeffs: tmp/mestatic.hdf5
    > Adding results to: tmp/mestatic.hdf5




Validation
----------
Validate gPC vs original model function (2D-surface)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code-block:: default

    pygpc.validate_gpc_plot(session=session,
                            coeffs=coeffs,
                            random_vars=list(problem.parameters_random.keys()),
                            n_grid=[51, 51],
                            output_idx=[0],
                            fn_out=None,
                            folder=None,
                            n_cpu=session.n_cpu)



.. image:: /auto_algorithms/images/sphx_glr_plot_algorithm_mestatic_001.png
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none






Validate gPC vs original model function (Monte Carlo)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code-block:: default

    nrmsd = pygpc.validate_gpc_mc(session=session,
                                  coeffs=coeffs,
                                  n_samples=int(1e4),
                                  output_idx=[0],
                                  fn_out=None,
                                  folder=None,
                                  plot=True,
                                  n_cpu=session.n_cpu)

    print("> Maximum NRMSD (gpc vs original): {:.2}%".format(max(nrmsd)))


.. image:: /auto_algorithms/images/sphx_glr_plot_algorithm_mestatic_002.png
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    > Maximum NRMSD (gpc vs original): 0.0078%





.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  57.765 seconds)


.. _sphx_glr_download_auto_algorithms_plot_algorithm_mestatic.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download

     :download:`Download Python source code: plot_algorithm_mestatic.py <plot_algorithm_mestatic.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: plot_algorithm_mestatic.ipynb <plot_algorithm_mestatic.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_