# The MIT License (MIT)
# Copyright (c) 2016 Arie Gurfinkel

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#import parser
import unittest

from . import ast, int, parser
from .ast import AstVisitor
from .parser import WhileLangSemantics






class TestInt(unittest.TestCase):
    def test_one(self):
        prg1 = "x := 10;print_state;{x:=10};skip;if x=10 then x:=10;if x=5 then x:=10 else skip;" \
               "assert x=10;assume x=10;havoc y,z;y:=5;if x>0 and y>0 then skip; if x>0 or y>0 then skip; x:=-10;" \
               "x:=10;x:=x*1;x:=x/1;x:=x+y;x:=x-y;x:=(x+3);x:=10;y:=5;x:=x not y;x:=true;x:=false;" \
               "x:=true and false;x:=(true);x:=(true and false)or(true and false);x:=10;y:=5;if (x+y)>=(x-y) then skip"
        # test parser
        ast1 = ast.parse_string(prg1)
        ast1_2=ast.parse_string(prg1)
        print(ast1==ast1_2)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        print(str(ast1))



        prg2 = "if (1<10) or (true and false) then skip"
        ast2 = ast.parse_string(prg2)
        interp2 = int.Interpreter()
        st2=int.State()
        st2=interp2.run(ast2, st2)
        print(str(ast2))

        prg3 = "if not(1<10) then skip"
        ast3 = ast.parse_string(prg3)
        interp3 = int.Interpreter()
        st3 = int.State()
        st3 = interp3.run(ast3, st3)


        prg4 = "x:=10;y:=5;y:=(x+y)"
        ast4 = ast.parse_string(prg4)
        interp4 = int.Interpreter()
        st4 = int.State()
        st4 = interp4.run(ast4, st4)
        print(str(ast4))

        prg5="x:=5;while (x<10) do x:=(x+1); while (x<20) inv (x>10) do x:=(x+1)"
        ast5=ast.parse_string(prg5)
        ast5_2=ast.parse_string(prg5)
        interp5=int.Interpreter()
        st5=int.State()
        st5=interp5.run(ast5,st5)
        print(ast5==ast5_2)
        print(str(ast5))

        prg6="if(5>=1) then skip; if (1<=5) then skip"
        ast6=ast.parse_string(prg6)
        interp6=int.Interpreter()
        st6=int.State()
        st6=interp6.run(ast6,st6)


        prg7="x:=(6/3)/(2/1)"
        ast7=ast.parse_string(prg6)
        interp7=int.Interpreter()
        st7=int.State()
        st7=interp7.run(ast7,st7)



        self.assertIsNotNone(st)
        # x is defined
        self.assertIn("x", st.env)
        # x is 10
        self.assertEquals(st.env["x"], 10)
        # no other variables in the state
        self.assertEquals(len(st.env), 3)



        WhileLangSemantics_test = WhileLangSemantics()
        WhileLangSemantics_test.start(ast1)
        WhileLangSemantics_test.stmt_list(ast1)
        WhileLangSemantics_test.stmt(ast1)
        WhileLangSemantics_test.asgn_stmt(ast1)
        WhileLangSemantics_test.block_stmt(ast1)
        WhileLangSemantics_test.skip_stmt(ast1)
        WhileLangSemantics_test.print_state_stmt(ast1)
        WhileLangSemantics_test.if_stmt(ast1)
        WhileLangSemantics_test.while_stmt(ast1)
        WhileLangSemantics_test.assert_stmt(ast1)
        WhileLangSemantics_test.assume_stmt(ast1)
        WhileLangSemantics_test.havoc_stmt(ast1)
        WhileLangSemantics_test.var_list(ast1)
        WhileLangSemantics_test.bexp(ast1)
        WhileLangSemantics_test.bterm(ast1)
        WhileLangSemantics_test.bfactor(ast1)
        WhileLangSemantics_test.batom(ast1)
        WhileLangSemantics_test.bool_const(ast1)
        WhileLangSemantics_test.rexp(ast1)
        WhileLangSemantics_test.rop(ast1)
        WhileLangSemantics_test.aexp(ast1)
        WhileLangSemantics_test.addition(ast1)
        WhileLangSemantics_test.subtraction(ast1)
        WhileLangSemantics_test.term(ast1)
        WhileLangSemantics_test.mult(ast1)
        WhileLangSemantics_test.division(ast1)
        WhileLangSemantics_test.factor(ast1)
        WhileLangSemantics_test.neg_number(ast1)
        WhileLangSemantics_test.atom(ast1)
        WhileLangSemantics_test.name(ast1)
        WhileLangSemantics_test.number(ast1)
        WhileLangSemantics_test.INT(ast1)
        WhileLangSemantics_test.NAME(ast1)
        WhileLangSemantics_test.NEWLINE(ast1)


class MyVisitor(ast.AstVisitor):
    def __init__(self):
        super(MyVisitor, self).__init__()
    def visit_Stmt(self,node):
        pass
    def visit_Exp(self,node):
        pass


class Mytest_AstVisitor(unittest.TestCase):
    def test_havoc(self):
        prg1="havoc x"
        ast1=ast.parse_string(prg1)
        visitor=MyVisitor()
        visitor.visit_HavocStmt(ast1)
    def test_IntVar(self):
        prg1="x:=1"
        ast1=ast.parse_string(prg1)
        visitor=MyVisitor()
        visitor.visit_IntVar(ast1)
    def test_SkipStmt(self):
        prg1 = "x:=1"
        ast1 = ast.parse_string(prg1)
        visitor = MyVisitor()
        visitor.visit_SkipStmt(ast1)
    def test_PrintStmt(self):
        prg1 = "x:=1"
        ast1 = ast.parse_string(prg1)
        visitor = MyVisitor()
        visitor.visit_PrintStateStmt(ast1)
    def test_AsgnStmt(self):
        prg1 = "x:=1"
        ast1 = ast.parse_string(prg1)
        visitor = MyVisitor()
        visitor.visit_AsgnStmt(ast1)
    def test_IfStmt(self):
        prg1 = "x:=1"
        ast1 = ast.parse_string(prg1)
        visitor = MyVisitor()
        visitor.visit_IfStmt(ast1)
    def test_WhileStme(self):
        prg1 = "x:=1"
        ast1 = ast.parse_string(prg1)
        visitor = MyVisitor()
        visitor.visit_WhileStmt(ast1)
    def test_AssertStmt(self):
        prg1 = "x:=1"
        ast1 = ast.parse_string(prg1)
        visitor = MyVisitor()
        visitor.visit_AssertStmt(ast1)
    def test_AssumeStmt(self):
        prg1 = "x:=1"
        ast1 = ast.parse_string(prg1)
        visitor = MyVisitor()
        visitor.visit_AssumeStmt(ast1)
    def test_parsefile(self):
        ast.parse_file("wlang/test1.prg")

    def test_Exp_isunary(self):
        prg1 = "x:=1;x:=(1+1)"

        a=ast.Exp("+",prg1)
        a.is_binary()
    def test_Const(self):
        a=ast.Const(1)
        str(a)
        repr(a)
        hash(a)
    def test_IntVar0(self):
        a=ast.IntVar("x")
        str(a)
        repr(a)
        hash(a)
    def test_pVisitor(self):
        ast.PrintVisitor(out=None)
    def test_Exp(self):
        ast.Exp([1,2],"x:=10")


    # def test_int_repr(self):
    #     a=int.State()
    #     repr(a)













