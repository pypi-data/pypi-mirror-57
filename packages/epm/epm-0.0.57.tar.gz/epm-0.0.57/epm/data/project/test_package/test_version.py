import unittest
from epm.api import API


class Test{{ name }}(unittest.TestCase):

    def test_{{ name }}(self):
        sandbox = API().sandbox()
        proc = sandbox.excutor('{{ name }}')
        proc.run()

        self.assertEqual(0, proc.returncode)
        self.assertEqual('{{ name }} {{ version }}', proc.stdout().strip())
