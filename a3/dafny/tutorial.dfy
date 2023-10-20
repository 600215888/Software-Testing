method Abs(x: int) returns (y: int)
requires true;
ensures y>=0 && y>=0;
ensures x>=0 ==> y==x;
ensures x<0 ==> y==-x;
{
    if (x<0)
    {return -x;}
    else
    {return x;}
}

method Testing()
{
    var v:int :=Abs(3);
    assert 0 <= v;
    assert v==3;
}
method Findmax(a:array<int>) returns (val:int)
requires a.Length>=1;
{
    val := a[0];
    var i:=1;
    while(i<a.Length){
        if(a[i]>val){
            val:=a[i];
        }
        i:=i+1;
    }
    return val;
}