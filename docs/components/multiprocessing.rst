Multiprocessing
===============


.. warning::
    This component is not activated by default.

Why do we need it?
------------------

Many people around the web who talked about PyFunceble were talking about one thing: We take time to run.

This component allows you to use more than one process if your machine has multiple CPU.

.. note::
    If you use this component you have to take some limits into consideration:

    * Your connection speed.
    * Your machine.

    You might not even see a speed if one of both is slow or very slow.


    The following might not be touched by the limits but it really depends:

    * URL availability test.
    * Syntax test.
    * Test with DNS LOOKUP only - without WHOIS.

How does it work?
-----------------

We test multiple subjects at the same time over several processes (1 process = 1 subject tested) and generate our results normally.

.. note::
    While using the JSON format for the database you might have to wait a bit at the very end
    as we need to merge all data we generated across the past created processes.

    Therefore, we recommend using the SQLite or even better the MySQL/MariaDB format which will get rid of that
    as everything is saved/synchronized at an almost real-time scale.

How to use it?
--------------

Activation
^^^^^^^^^^

You can simply change

::

    multiprocess: False

to

::

    multiprocess: True

Number of processes to create
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Simply update the default value of

::

    maximal_processes: 25
