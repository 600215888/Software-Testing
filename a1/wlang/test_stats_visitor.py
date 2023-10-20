import unittest

from . import ast, stats_visitor


class TestStatsVisitor(unittest.TestCase):
    def test_one(self):
        #prg1 = "skip;skip;x:=10;{x:=10;skip};if (x>10) then x:=10 else skip;while (x<20) inv (x>10) do x:=x+5;"\
        #       "x:=10; assert (x=10); assume (x=10); havoc y,z;print_state"
        prg1 = "x := 10;print_state;{x:=10};skip;if x=10 then x:=10;if x=5 then x:=10 else skip;" \
               "assert x=10;assume x=10;havoc y,z;y:=5;if x>0 and y>0 then skip; if x>0 or y>0 then skip; x:=-10;" \
               "x:=10;x:=x*1;x:=x/1;x:=x+y;x:=x-y;x:=(x+3);x:=10;y:=5;x:=x not y"
        ast1 = ast.parse_string(prg1)

        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        # UNCOMMENT to run the test
        self.assertEquals(sv.get_num_stmts(), 27)
        #self.assertEquals(sv.visit_StmtList(), 2)
        self.assertEquals(sv.get_num_vars(), 3)
