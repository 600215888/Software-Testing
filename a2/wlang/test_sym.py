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

import unittest

from . import ast, sym
import z3

class TestSym (unittest.TestCase):
    def test_one(self):
        prg1 = "{x:=1;y:=-1};z:=x+y;z:=x-y;z:=x*y;z:=x/y;skip;print_state;havoc i,j"
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
    def test_two(self):
        prg2 = "x:=1;assume x=1;assume x=2"
        ast2 = ast.parse_string(prg2)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast2, st)]

    def test_three(self):
        prg3 = "x:=1;assert x=1;assert x=2"
        ast3 = ast.parse_string(prg3)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast3, st)]
    def test_four(self):
        prg4 = "x:=1;y:=-1;if x>1 and x>=y then z:=2;if x<=1 or y<2 then z:=1; if (x>1 and true) then skip else skip"
        ast4 = ast.parse_string(prg4)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast4, st)]
    def test_five(self):
        prg5 = "x:=1;while x<5 do x:=x+1;x:=1; while x<5 and not x=0 do x:=x+1"
        ast5 = ast.parse_string(prg5)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast5, st)]
        st.is_error()
        st.add_pc(z3.BoolVal(True))
        st.pick_concrete()
        st.to_smt2()
        st.__repr__()
    def test_six(self):
        prg6 = "havoc x;if x>10 then skip"
        ast6 = ast.parse_string(prg6)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast6, st)]
        st.pick_concrete()
    def test_seven(self):
        prg7 = "x:=1;havoc y,z;while (x<11) inv(y<z) do x:=x+1"
        ast7 = ast.parse_string(prg7)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast7, st)]
    def test_eight(self):
        prg8 = "x:=1;while (x<11) inv(x<5) do x:=x+1"
        ast8 = ast.parse_string(prg8)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast8, st)]