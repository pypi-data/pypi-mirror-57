Bonsai SDK
==========

A python library for integrating data sources with Bonsai BRAIN.


Installation
------------
To install the current release version:
    `$ pip install bonsai-ai`


Usage
-----

Clients will subclass `bonsai.Simulator` and implement the required methods.

Example:
::

    #!/usr/bin/env python3

    import sys
    from bonsai_ai import Simulator, Brain, Config

    class MySim(Simulator):
        def episode_start(self, parameters):
            initial = {"value": 1.0}
            return initial

        def simulate(self, action, objective):
            terminal = True
            state = {"value": 1.0}
            return (state, 1.0, terminal)

Then, the simulator is configured and assigned a BRAIN and run.
::

    def example():
        config = Config(sys.argv)
        brain = Brain(config)
        sim = MySim(brain, 'example_simulator')
        while sim.run():
            continue
