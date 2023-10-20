// returns an index of the largest element of array 'a' in the range [0..n)
method findMax (a : array<int>, n : int) returns (r:int)
requires a.Length>0;
requires 0<n<=a.Length;
ensures 0<=r<n;
ensures forall i :: 0<=i<n ==> a[i]<=a[r];
{
  var mi;
  var i;
  mi := 0;
  i := 0;
  while (i < n)
  invariant 0<=i<=n;
  invariant 0<=mi<n<=a.Length;
  invariant forall j:: 0<=j<i ==> a[mi]>=a[j];
  decreases n-i;
  {
    if (a[i] > a[mi])
    { mi := i; }
    i := i + 1;
  }
  return mi;
}


