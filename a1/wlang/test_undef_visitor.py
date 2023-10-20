import unittest

from . import ast, undef_visitor


class TestUndefVisitor(unittest.TestCase):
    def test1(self):
        prg1="havoc x;if x>10 then y:=x+1 else z:=10;x:=z+1"
        ast1 = ast.parse_string(prg1)

        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)

        print(uv.get_undefs())
        # UNCOMMENT to run the test
        ## self.assertEquals (set ([ast.IntVar('z')]), uv.get_undefs ())
