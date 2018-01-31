# HW2_PotterCart
usage:
#python PotterCartTest.py
e.g.
all pass:
test_buy_1_vol1_0_vol2_0_vol3_0_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_1_vol2_0_vol3_0_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_1_vol2_1_vol3_0_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_1_vol2_1_vol3_1_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_1_vol2_1_vol3_1_vol4_1_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_1_vol2_2_vol3_0_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_2_vol2_2_vol3_0_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_2_vol1_2_vol2_2_vol3_2_vol4_1_vol5 (__main__.TestPotterCart) ... ok
test_buy_4_vol1_4_vol2_4_vol3_2_vol4_2_vol5 (__main__.TestPotterCart) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.002s

OK

e.g.
last one fail:
test_buy_1_vol1_0_vol2_0_vol3_0_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_1_vol2_0_vol3_0_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_1_vol2_1_vol3_0_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_1_vol2_1_vol3_1_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_1_vol2_1_vol3_1_vol4_1_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_1_vol2_2_vol3_0_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_1_vol1_2_vol2_2_vol3_0_vol4_0_vol5 (__main__.TestPotterCart) ... ok
test_buy_2_vol1_2_vol2_2_vol3_2_vol4_1_vol5 (__main__.TestPotterCart) ... ok
test_buy_4_vol1_4_vol2_4_vol3_2_vol4_2_vol5 (__main__.TestPotterCart) ... FAIL

======================================================================
FAIL: test_buy_4_vol1_4_vol2_4_vol3_2_vol4_2_vol5 (__main__.TestPotterCart)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "PotterCartTest.py", line 94, in test_buy_4_vol1_4_vol2_4_vol3_2_vol4_2_vol5
    self.assertEqual(actual, expected)
AssertionError: 1290 != 1280

----------------------------------------------------------------------
Ran 9 tests in 0.002s

FAILED (failures=1)

