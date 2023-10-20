include "part.dfy"


method qsort(a:array<int>, l:nat, u:nat)
  requires a != null;
  requires l <= u < a.Length;
  modifies a;

  ensures sorted_between(a, l, u+1);
{
  // complete the code for quicksort and verify the implementation
  if(l>=0&&u>=0&&l<=u)
  {
    var p:nat :=partition(a,l,u);
    qsort(a,l,p);
    qsort(a,p+1,u);
  }
}
