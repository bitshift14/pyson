#!/usr/bin/env python

import unittest
import logging
import os.path

from lxml import etree

import pyson.mapc2017
import pyson.runtime


class BeliefTest(unittest.TestCase):

    def test_request_action(self):
        agent = pyson.mapc2017.Agent()
        with open(os.path.join(os.path.dirname(__file__), "request-action.xml")) as xml:
            agent.message_received(etree.parse(xml).getroot())

        term = pyson.Literal("money", (50000, ))
        intention = pyson.runtime.Intention()
        self.assertTrue(agent.test_belief(term, intention))

        agent.dump()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
