openTSNE
========

|Build Status| |ReadTheDocs Badge| |Codacy Badge| |License Badge|

openTSNE is a modular Python implementation of t-Distributed Stochasitc Neighbor Embedding (t-SNE), a popular dimensionality-reduction algorithm for visualizing high-dimensional data sets. openTSNE incorporates the latest improvements to the t-SNE algorithm, including the ability to add new data points to existing embeddings, massive speed improvements, enabling t-SNE to scale to millions of data points and various tricks to improve global alignment of the resulting visualizations.

.. figure:: docs/source/images/macosko_2015.png
   :alt: Macosko 2015 mouse retina t-SNE embedding
   :align: center

   A visualization of 44,808 single cell transcriptomes obtained from the mouse retina [5]_ embedded using the multiscale kernel trick to better preserve the global aligment of the clusters.

- `Documentation <http://opentsne.readthedocs.io>`__
- `User Guide and Tutorial <https://opentsne.readthedocs.io/en/latest/tsne_algorithm.html>`__
- Examples: `basic <https://opentsne.readthedocs.io/en/latest/examples/01_simple_usage/01_simple_usage.html>`__, `advanced <https://opentsne.readthedocs.io/en/latest/examples/02_advanced_usage/02_advanced_usage.html>`__, `preserving global alignment <https://opentsne.readthedocs.io/en/latest/examples/03_preserving_global_structure/03_preserving_global_structure.html>`__, `embedding large data sets <https://opentsne.readthedocs.io/en/latest/examples/04_large_data_sets/04_large_data_sets.html>`__
- `Speed benchmarks <https://opentsne.readthedocs.io/en/latest/benchmarks.html>`__

Installation
------------

openTSNE requires Python 3.6 or higher in order to run.

Conda
~~~~~

openTSNE can be easily installed from ``conda-forge`` with

::

   conda install --channel conda-forge opentsne

`Conda package <https://anaconda.org/conda-forge/opentsne>`__

PyPi
~~~~

openTSNE is also available through ``pip`` and can be installed with

::

   pip install opentsne

`PyPi package <https://pypi.org/project/openTSNE>`__

Note that openTSNE requires a C/C++ compiler. ``numpy`` must also be
installed.

In order for openTSNE to utilize multiple threads, the C/C++ compiler
must also implement ``OpenMP``. In practice, almost all compilers
implement this with the exception of older version of ``clang`` on OSX
systems.

To squeeze the most out of openTSNE, you may also consider installing
FFTW3 prior to installation. FFTW3 implements the Fast Fourier
Transform, which is heavily used in openTSNE. If FFTW3 is not available,
openTSNE will use numpy’s implementation of the FFT, which is slightly
slower than FFTW. The difference is only noticeable with large data sets
containing millions of data points.

A hello world example
---------------------

Getting started with openTSNE is very simple. First, we'll load up some data using scikit-learn

.. code:: python

   from sklearn import datasets

   iris = datasets.load_iris()
   x, y = iris["data"], iris["target"]

then, we'll import and run

.. code:: python

   from openTSNE import TSNE

   embedding = TSNE().fit(x)

Citation
--------

If you make use of openTSNE for your work we would appreciate it if you would cite the paper

.. code::

    @article {Poli{\v c}ar731877,
        author = {Poli{\v c}ar, Pavlin G. and Stra{\v z}ar, Martin and Zupan, Bla{\v z}},
        title = {openTSNE: a modular Python library for t-SNE dimensionality reduction and embedding},
        year = {2019},
        doi = {10.1101/731877},
        publisher = {Cold Spring Harbor Laboratory},
        URL = {https://www.biorxiv.org/content/early/2019/08/13/731877},
        eprint = {https://www.biorxiv.org/content/early/2019/08/13/731877.full.pdf},
        journal = {bioRxiv}
    }


References
----------

.. [1] Maaten, Laurens van der, and Geoffrey Hinton. `“Visualizing data using
    t-SNE.” <http://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf>`__
    Journal of machine learning research 9.Nov (2008): 2579-2605.
.. [2] Van Der Maaten, Laurens. `“Accelerating t-SNE using tree-based algorithms.”
    <http://www.jmlr.org/papers/volume15/vandermaaten14a/vandermaaten14a.pdf>`__
    The Journal of Machine Learning Research 15.1 (2014): 3221-3245.
.. [3] Linderman, George C., et al. `"Fast interpolation-based t-SNE for improved
    visualization of single-cell RNA-seq data." <https://www.nature.com/articles/s41592-018-0308-4>`__ Nature methods 16.3 (2019): 243.
.. [4] Kobak, Dmitry, and Philipp Berens. `“The art of using t-SNE for single-cell
    transcriptomics.” <https://www.biorxiv.org/content/early/2018/10/25/453449>`__
    bioRxiv (2018): 453449.
.. [5] Macosko, Evan Z., et al. \ `“Highly parallel genome-wide expression profiling of
    individual cells using nanoliter droplets.”
    <https://www.sciencedirect.com/science/article/pii/S0092867415005498>`__
    Cell 161.5 (2015): 1202-1214.

.. |Build Status| image:: https://dev.azure.com/pavlingp/openTSNE/_apis/build/status/Test?branchName=master
   :target: https://dev.azure.com/pavlingp/openTSNE/_build/latest?definitionId=1&branchName=master
.. |ReadTheDocs Badge| image:: https://readthedocs.org/projects/opentsne/badge/?version=latest
   :target: https://opentsne.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/ef67c21a74924b548acae5a514bc443d
   :target: https://app.codacy.com/app/pavlin-policar/openTSNE?utm_source=github.com&utm_medium=referral&utm_content=pavlin-policar/openTSNE&utm_campaign=Badge_Grade_Dashboard
.. |License Badge| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause
