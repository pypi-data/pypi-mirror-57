import pytest
import numpy as np
from LaplaceDiff.LaplaceDiff import Dual
from LaplaceDiff.elemental import *

def test_exp():
	x = Dual(2.0, 2.0)
	y = exp(x)
	assert y.val == np.exp(2.0)
	assert y.der == 2.0 * np.exp(2.0)
	assert exp(3.5) == np.exp(3.5)

def test_log():
	x = Dual(4.0)
	y = log(x)
	assert y.val == np.log(4.0)
	assert y.der == 1/4.0
	assert log(2) == np.log(2)

def test_sin():
	x = Dual(1.0, 5.0)
	y = sin(x)
	assert y.val == np.sin(1.0)
	assert y.der == np.cos(1.0) * 5.0
	assert sin(2) == np.sin(2)

def test_cos():
	x = Dual(1.0, 5.0)
	y = cos(x)
	assert y.val == np.cos(1.0)
	assert y.der == - np.sin(1.0) * 5.0
	assert cos(2) == np.cos(2)

def test_tan():
	x = Dual(1.0, 5.0)
	y = tan(x)
	assert y.val == np.tan(1.0)
	assert y.der == 5.0 / (np.cos(1.0) **2)
	assert tan(2) == np.tan(2)
