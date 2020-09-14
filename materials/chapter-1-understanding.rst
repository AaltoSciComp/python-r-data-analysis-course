================================================
Chapter 1: Understanding data analysis workflows
================================================

Data analysis pipeline
----------------------

Data analysis workflows are commonly split to four steps:


1. Data perparation and loading
2. Modeling
3. Model evaluation
4. Presentation

From now on will call this the **data analysis pipeline**.

Data preparation and loading represents the process of preparing your
data into a format that is usable for analysis. One might think that
this is a very simple procedure, but in reality it is usually the most
time intensive part. Without proper data there can be no data analysis
and data is rarely provided in a format that is perfect to the task at
hand.

Cleaning up data, combining it with other data and creating a
efficient data pipeline depends heavily on the task at hand and thus
it requires a lot of manual effort. Badly done data preparation will
also propagate throughout the data analysis pipeline.

Let's call the input data ``d_raw`` and let's denote our input data
processing steps as ``I(x)``. After we have run the data processing we
will obtain a clean version of data called ``d``. So basically,
``d = I(d_raw)``.

.. image:: images/pipeline-1.svg

Modeling in this context refers to applying some algorithm, model or
statistics calculation to the data. So based on the data ``d``, we
apply some model ``M(x)`` to the data and we obtain an output ``p``.
Here output ``p`` can mean anything from statistics (e.g. mean, var)
to fit parameters. So basically, ``p=M(d)``. 

.. image:: images/pipeline-2.svg

The process of choosing a suitable model based on our problem and
obtaining the output ``p`` is what is usually thought of being the whole
data analysis, but the whole data analysis pipeline contains other
steps as well.

After we have obtained the output ``p`` from our model we need to
evaluate whether our model suits the task at hand. This step can be
automatic (we choose best performing model based on fit performance,
we test model on test data) or manual (we look at the parameters, we look
at a plot of fit). Let's call this step as ``E(x)`` and its output
as ``v``. So again, ``v=E(p)``.

.. image:: images/pipeline-3.svg
