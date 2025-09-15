# Compare different quadrature rules for integration

There are two examples provided for calculating the weights and abscissas for gaussian quadrature rules, try:

```
make
./gqconstants
```

or

```
python gqconstants.py
```

You can also use the C++ example as a guide to build your own executable

There is no need to look at rules >~25 for Gaussian quadrature.  And you can also stop at ~ 1000 divisions for the trapezoidal and Simpson's rules.  If you run much longer you'll see the numerical errors bevome visible for the trapezoidal, but hyou'll need to think about how to code efficiently or the running time may be very long.
Assignment answers:
The table is as follows
   N  Trapezoidal Error  Simpson Error  Gaussian Error
   2       1.311463e-02   2.131212e-04    1.417993e-04
 102       5.063113e-06   3.244305e-11    1.000000e-16
 202       1.290969e-06   2.109202e-12    4.440892e-16
 302       5.775701e-07   4.222178e-13    6.661338e-16
 402       3.259617e-07   1.345590e-13    9.992007e-16
 502       2.090312e-07   5.528911e-14    2.220446e-16
 602       1.453536e-07   2.675637e-14    5.551115e-16
 702       1.068918e-07   1.454392e-14    2.886580e-15
 802       8.189736e-08   8.437695e-15    5.551115e-16
 902       6.474490e-08   5.329071e-15    4.440892e-16
1002       5.246664e-08   3.441691e-15    5.551115e-16
1102       4.337660e-08   2.331468e-15    3.330669e-16
1202       3.645942e-08   1.554312e-15    2.220446e-15
1302       3.107397e-08   1.221245e-15    6.661338e-16
1402       2.679925e-08   7.771561e-16    3.108624e-15
1502       2.334957e-08   6.661338e-16    8.881784e-16
1602       2.052550e-08   5.551115e-16    1.665335e-15
1702       1.818443e-08   4.440892e-16    4.440892e-15
1802       1.622218e-08   3.330669e-16    1.887379e-15
1902       1.456122e-08   1.110223e-16    8.104628e-15

The answer to the fits are:
Estimated order (alpha) = -1.999, coefficient C ≈ 5.249e-02
Estimated order (alpha) = -4.022, coefficient C ≈ 3.824e-03

Part 2 answers:

The reason that my function is not working is because it changes rapidly. 
To fix this we can take parts of the problem and partition them, we can also use integrators that are meant for oscillations. 
