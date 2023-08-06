pymor.algorithms package
************************

.. automodule:: pymor.algorithms
    :show-inheritance:

Submodules
==========

adaptivegreedy module
---------------------

.. automodule:: pymor.algorithms.adaptivegreedy
    :show-inheritance:

---------


.. autoclass:: pymor.algorithms.adaptivegreedy.AdaptiveSampleSet
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autofunction:: pymor.algorithms.adaptivegreedy.adaptive_greedy

---------


.. autofunction:: pymor.algorithms.adaptivegreedy.adaptive_weak_greedy

---------


.. autofunction:: pymor.algorithms.adaptivegreedy.rb_adaptive_greedy

arnoldi module
--------------

.. automodule:: pymor.algorithms.arnoldi
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.arnoldi.arnoldi

basic module
------------

.. automodule:: pymor.algorithms.basic
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.basic.almost_equal

---------


.. autofunction:: pymor.algorithms.basic.project_array

---------


.. autofunction:: pymor.algorithms.basic.relative_error

ei module
---------

.. automodule:: pymor.algorithms.ei
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.ei.deim

---------


.. autofunction:: pymor.algorithms.ei.ei_greedy

---------


.. autofunction:: pymor.algorithms.ei.interpolate_operators

error module
------------

.. automodule:: pymor.algorithms.error
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.error.reduction_error_analysis

genericsolvers module
---------------------

.. automodule:: pymor.algorithms.genericsolvers
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.genericsolvers.apply_inverse

---------


.. autofunction:: pymor.algorithms.genericsolvers.lgmres

---------


.. autofunction:: pymor.algorithms.genericsolvers.lsmr

---------


.. autofunction:: pymor.algorithms.genericsolvers.lsqr

---------


.. autofunction:: pymor.algorithms.genericsolvers.solver_options

gram_schmidt module
-------------------

.. automodule:: pymor.algorithms.gram_schmidt
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.gram_schmidt.gram_schmidt

---------


.. autofunction:: pymor.algorithms.gram_schmidt.gram_schmidt_biorth

greedy module
-------------

.. automodule:: pymor.algorithms.greedy
    :show-inheritance:

---------


.. autoclass:: pymor.algorithms.greedy.RBSurrogate
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.greedy.WeakGreedySurrogate
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autofunction:: pymor.algorithms.greedy.greedy

---------


.. autofunction:: pymor.algorithms.greedy.rb_greedy

---------


.. autofunction:: pymor.algorithms.greedy.weak_greedy

hapod module
------------

.. automodule:: pymor.algorithms.hapod
    :show-inheritance:

---------


.. autoclass:: pymor.algorithms.hapod.DistHAPODTree
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.hapod.FakeExecutor
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.hapod.IncHAPODTree
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.hapod.LifoExecutor
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.hapod.Tree
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autofunction:: pymor.algorithms.hapod.default_pod_method

---------


.. autofunction:: pymor.algorithms.hapod.dist_hapod

---------


.. autofunction:: pymor.algorithms.hapod.dist_vectorarray_hapod

---------


.. autofunction:: pymor.algorithms.hapod.hapod

---------


.. autofunction:: pymor.algorithms.hapod.inc_hapod

---------


.. autofunction:: pymor.algorithms.hapod.inc_vectorarray_hapod

---------


.. autofunction:: pymor.algorithms.hapod.std_local_eps

image module
------------

.. automodule:: pymor.algorithms.image
    :show-inheritance:

---------


.. autoclass:: pymor.algorithms.image.CollectOperatorRangeRules
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.image.CollectVectorRangeRules
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autofunction:: pymor.algorithms.image.estimate_image

---------


.. autofunction:: pymor.algorithms.image.estimate_image_hierarchical

lincomb module
--------------

.. automodule:: pymor.algorithms.lincomb
    :show-inheritance:

---------


.. autoclass:: pymor.algorithms.lincomb.AssembleLincombRules
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autofunction:: pymor.algorithms.lincomb.assemble_lincomb

lradi module
------------

.. automodule:: pymor.algorithms.lradi
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.lradi.lyap_lrcf_solver_options

---------


.. autofunction:: pymor.algorithms.lradi.projection_shifts

---------


.. autofunction:: pymor.algorithms.lradi.projection_shifts_init

---------


.. autofunction:: pymor.algorithms.lradi.solve_lyap_lrcf

lrradi module
-------------

.. automodule:: pymor.algorithms.lrradi
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.lrradi.hamiltonian_shifts

---------


.. autofunction:: pymor.algorithms.lrradi.hamiltonian_shifts_init

---------


.. autofunction:: pymor.algorithms.lrradi.ricc_lrcf_solver_options

---------


.. autofunction:: pymor.algorithms.lrradi.solve_ricc_lrcf

lyapunov module
---------------

.. automodule:: pymor.algorithms.lyapunov
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.lyapunov._chol

---------


.. autofunction:: pymor.algorithms.lyapunov.mat_eqn_sparse_min_size

---------


.. autofunction:: pymor.algorithms.lyapunov.solve_lyap_dense

---------


.. autofunction:: pymor.algorithms.lyapunov.solve_lyap_lrcf

newton module
-------------

.. automodule:: pymor.algorithms.newton
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.newton.newton

pod module
----------

.. automodule:: pymor.algorithms.pod
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.pod.pod

preassemble module
------------------

.. automodule:: pymor.algorithms.preassemble
    :show-inheritance:

---------


.. autoclass:: pymor.algorithms.preassemble.PreAssembleRules
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autofunction:: pymor.algorithms.preassemble.preassemble

projection module
-----------------

.. automodule:: pymor.algorithms.projection
    :show-inheritance:

---------


.. autoclass:: pymor.algorithms.projection.ProjectRules
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.projection.ProjectToSubbasisRules
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autofunction:: pymor.algorithms.projection.project

---------


.. autofunction:: pymor.algorithms.projection.project_to_subbasis

randrangefinder module
----------------------

.. automodule:: pymor.algorithms.randrangefinder
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.randrangefinder.adaptive_rrf

---------


.. autofunction:: pymor.algorithms.randrangefinder.rrf

riccati module
--------------

.. automodule:: pymor.algorithms.riccati
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.riccati.solve_pos_ricc_lrcf

---------


.. autofunction:: pymor.algorithms.riccati.solve_ricc_lrcf

rules module
------------

.. automodule:: pymor.algorithms.rules
    :show-inheritance:

---------


.. autoclass:: pymor.algorithms.rules.RuleTable
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.rules.RuleTableMeta
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.rules.match_always
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.rules.match_class
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.rules.match_class_all
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.rules.match_class_any
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.rules.match_class_base
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.rules.match_generic
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autofunction:: pymor.algorithms.rules.print_children

---------


.. autoclass:: pymor.algorithms.rules.rule
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

sylvester module
----------------

.. automodule:: pymor.algorithms.sylvester
    :show-inheritance:

---------


.. autofunction:: pymor.algorithms.sylvester.solve_sylv_schur

timestepping module
-------------------

.. automodule:: pymor.algorithms.timestepping
    :show-inheritance:

---------


.. autoclass:: pymor.algorithms.timestepping.ExplicitEulerTimeStepper
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.timestepping.ImplicitEulerTimeStepper
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autoclass:: pymor.algorithms.timestepping.TimeStepperInterface
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autofunction:: pymor.algorithms.timestepping.explicit_euler

---------


.. autofunction:: pymor.algorithms.timestepping.implicit_euler

to_matrix module
----------------

.. automodule:: pymor.algorithms.to_matrix
    :show-inheritance:

---------


.. autoclass:: pymor.algorithms.to_matrix.ToMatrixRules
    :show-inheritance:
    :members:
    :special-members:
    :exclude-members: __init__, __weakref__

---------


.. autofunction:: pymor.algorithms.to_matrix.to_matrix

