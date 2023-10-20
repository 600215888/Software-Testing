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

from . import ast


class UndefVisitor(ast.AstVisitor):
    """Computes all variables that are used before being defined"""

    def __init__(self):
        super(UndefVisitor, self).__init__()
        self._hasdefined= set()
        self._undefined= set()
        self._maybeunreach=set()
        self._state=0

    def check(self, node,*args,**kwargs):
        self._state = 1
        """Check for undefined variables starting from a given AST node"""
        # # do the necessary setup/arguments and call self.visit (node, args)
        #kwargs=int.State()
        #self.visit(node,*args,kwargs)
        #self.visit(self,node,*args,*kwargs)
        method = "visit_" + node.__class__.__name__
        visitor = getattr(self, method)
        return visitor(node, *args, **kwargs)
        pass

    # def visit(self, node, *args, **kwargs):
    #     method = "visit_" + node.__class__.__name__
    #     visitor = getattr(self, method)
    #     return visitor(node, *args, **kwargs)

    def get_undefs(self):
        """Return the set of all variables that are used before being defined
        in the program.  Available only after a call to check()
        """
        if (self._state==1):
            return self._undefined
        pass

    def get_defined(self):
        if (self._state==1):
            return self._hasdefined
        pass

    def visit_StmtList(self, node, *args, **kwargs):
        if node.stmts is None:
            return
        for s in node.stmts:
            self.visit(s)

    def visit_IntVar(self, node, *args, **kwargs):
        # return kwargs["state"].env[node.name]
        # visitor = getattr(self, "visit_" + ast.AExp.__name__)
        # return visitor(node, *args, **kwargs)
        pass

    def visit_Const(self, node, *args, **kwargs):
        pass
        # visitor = getattr(self, "visit_" + ast.Const.__name__)
        # return visitor(node, *args, **kwargs)

    def visit_Stmt(self, node, *args, **kwargs):
        pass

    def visit_AsgnStmt(self, node, *args, **kwargs):
        # st = kwargs["state"]
        # st.env[node.lhs.name] = self.visit(node.rhs, *args, **kwargs)
        # self._hasdefined.add(st.env[node.lhs.name])
        #print("jinru asgn")
        # print(node.lhs.name)
        # self._hasdefined.add(node.lhs.name)
        if node.lhs.name not in self._undefined:
            self._hasdefined.add(node.lhs.name)
        self.visit(node.rhs)
        # visitor = getattr(self, "visit_" + ast.Stmt.__name__)
        # return visitor(node, *args, **kwargs)
    def visit_AExp(self, node, *args, **kwargs):
        #kids = [self.visit(a, *args, **kwargs) for a in node.args]
        for a in node.args:
            if (is_number(str(a))==True):
                pass
            else:
                if (str(a) not in self._hasdefined):
                    self._undefined.add(a)
        pass
        # visitor = getattr(self, "visit_" + ast.Exp.__name__)
        # return visitor(node, *args, **kwargs)
    def visit_Exp(self, node, *args, **kwargs):
        pass

    def visit_HavocStmt(self, node, *args, **kwargs):
        self.visit_Stmt(node)
        for v in node.vars:
            if str(v) not in self._undefined:
                self._hasdefined.add(str(v))
        pass
        # visitor = getattr(self, "visit_" + ast.Stmt.__name__)
        # return visitor(node, *args, **kwargs)

    def visit_AssertStmt(self, node, *args, **kwargs):
        pass

    def visit_AssumeStmt(self, node, *args, **kwargs):
        pass

    def visit_IfStmt(self, node,*args, **kwargs):
            self.visit(node.then_stmt)
            if node.has_else():
                #self.visit(node.else_stmt)
                pass

    def visit_WhileStmt(self, node, *args, **kwargs):
        # visitor = getattr(self, "visit_" + ast.Stmt.__name__)
        # return visitor(node, *args, **kwargs)
        pass
    def visit(self, node, *args, **kwargs):
        """Visit a node."""
        method = "visit_" + node.__class__.__name__
        visitor = getattr(self, method)
        return visitor(node, *args, **kwargs)

def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False
