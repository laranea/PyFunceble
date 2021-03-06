Autosave
========

.. warning::
    This component is not activated by default.

Why do we need it?
------------------

This component comes along with the auto-continue one.
Indeed, after constructing the logic to auto-continue we needed something to autosave.

From now only Travis CI is supported but in the future another backup/saving logics
might be implemented.

How does it work?
-----------------

.. note::
    Want to read the code ? It's here :func:`PyFunceble.auto_save.AutoCoAutoSaventinue`!

After a given amount of minutes, we stop the tool, generate the percentage,
run a given command (if found), commit all the changes we made to the repository
and finally, push to the git repository.

How to use it?
--------------

For Travis CI
^^^^^^^^^^^^^

The following (from the configuration) or their equivalent from the CLI are required.

::

    travis: False
    travis_autosave_commit: "Your awesome commit message"
    travis_autosave_final_commit: "Your awesome final commit message"
    travis_autosave_minutes: 15
    travis_branch: master

.. note::
    If you give the :code:`command` index something, we will run it at the end of each commits except the last one.

    The command on the last commit is executed based on the given :code:`command_before_end` index.
