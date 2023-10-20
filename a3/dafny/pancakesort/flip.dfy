// flips (i.e., reverses) array elements in the range [0..num]
method flip (a: array<int>, num: int)
requires a.Length>0;
requires 0<=num<a.Length;
//ensures multiset(a[..])==multiset(old(a[..]));
ensures forall i :: 0<=i<=num ==> a[i]==old(a[num-i]);
ensures forall i :: num<i<a.Length ==> a[i]==old(a[i]);

modifies a;
{
  var tmp:int;

  var i := 0;
  var j := num;
  while (i < j)
  invariant i+j==num;
  invariant j<a.Length;
  invariant forall k :: 0<=k<i ==> a[k]==old(a[num-k]) && a[num-k]==old(a[k]);
  invariant forall k :: num<k<a.Length ==> a[k]==old(a[k]);
  invariant forall k :: i<=k<=j ==> a[k]==old(a[k])
  decreases j,num-i;

  {
    tmp := a[i];
    a[i] := a[j];
    a[j] := tmp;
    i := i + 1;
    j := j - 1;
  }
}


