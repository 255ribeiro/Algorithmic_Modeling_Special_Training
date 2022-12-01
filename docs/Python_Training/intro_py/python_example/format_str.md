| Number	| Format	| Output	| Description |
|--------|-----------|-----------|----------------|
3.141592 | {:.2f} | 3.1 | Format float 2 decimal places
3.1415926 |	{:+.2f} |	+3.14 |	Format float 2 decimal places with sign
-1 |	{:+.2f} |	-1.00 |	Format float 2 decimal places with sign
2.71828 |	{:.0f}	| 3 |	Format float with no decimal places
4 |	{:0>2d} |	04 |	Pad number with zeros (left padding, width 2)
4 |	{:x<4d} |	4xxx |	Pad number with x’s (right padding, width 4)
10 |	{:x<4d} |	10xx |	Pad number with x’s (right padding, width 4)
1000000 |	{:,} |	1,000,000 |	Number format with comma separator
0.35 |	{:.2%} |	35.00% |	Format percentage
1000000000 |	{:.2e} |	1.00e+09 |	Exponent notation
11 |	{:11d} |	        11 |	Right-aligned (default, width 10)
11 |	{:<11d} |	11 |	Left-aligned (width 10)
11 |	{:^11d} |	    11 |	Center aligned (width 10)


