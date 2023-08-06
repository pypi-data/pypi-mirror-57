import pytest
import numpy as np
from LaplaceDiff.LaplaceDiff import Dual
from LaplaceDiff.elemental import *

def test_exp():
	x = Dual(2.0, 2.0)
	y = exp(x)
	assert np.isclose(y.val, np.exp(2.0))
	assert np.isclose(y.der, 2.0 * np.exp(2.0))
	assert np.isclose(exp(3.5), np.exp(3.5))

	# Arbitrary base:
	z = exp(x, 10)
	assert np.isclose(z.val, np.power(10, 2))
	assert np.isclose(z.der, 2.0 * np.power(10, 2) * np.log(10))

	z = exp(x, 1)
	assert np.isclose(z.val, np.power(1, 2))
	assert np.isclose(z.der, 2.0 * np.power(1, 2) * np.log(1))

	with pytest.raises(ValueError) as excinfo:
		z = exp(x, 0)
	assert "Base must be a positive real number." in str(excinfo.value)

	with pytest.raises(ValueError) as excinfo:
		z = exp(x, -1)
	assert "Base must be a positive real number." in str(excinfo.value)

def test_log():
	x = Dual(4.0)
	y = log(x)
	assert np.isclose(y.val, np.log(4.0))
	assert np.isclose(y.der, 1/4.0)
	assert np.isclose(log(2), np.log(2))

	# Arbitrary base:
	z = log(x, 10)
	assert np.isclose(z.val, np.log(4.0)/np.log(10))
	assert np.isclose(z.der, 1/(np.log(10) * 4.0))

	z = log(x, 0.1)
	assert np.isclose(z.val, np.log(4.0)/np.log(0.1))
	assert np.isclose(z.der, 1/(np.log(0.1) * 4.0))

	with pytest.raises(ValueError) as excinfo:
		z = log(x, 1)
	assert "Base must be a positive real number not equal one." in str(excinfo.value)

	with pytest.raises(ValueError) as excinfo:
		z = log(x, 0)
	assert "Base must be a positive real number not equal one." in str(excinfo.value)

	with pytest.raises(ValueError) as excinfo:
		z = log(x, -1)
	assert "Base must be a positive real number not equal one." in str(excinfo.value)

def test_sin():
	x = Dual(1.0, 5.0)
	y = sin(x)
	assert np.isclose(y.val, np.sin(1.0))
	assert np.isclose(y.der, np.cos(1.0) * 5.0)
	assert np.isclose(sin(2), np.sin(2))

def test_cos():
	x = Dual(1.0, 5.0)
	y = cos(x)
	assert np.isclose(y.val, np.cos(1.0))
	assert np.isclose(y.der, - np.sin(1.0) * 5.0)
	assert np.isclose(cos(2), np.cos(2))

def test_tan():
	x = Dual(1.0, 5.0)
	y = tan(x)
	assert np.isclose(y.val, np.tan(1.0))
	assert np.isclose(y.der, 5.0 / (np.cos(1.0) **2))
	assert np.isclose(tan(2), np.tan(2))

def test_arcsin():
	x = Dual(0.5,5.0)
	y = arcsin(x)
	assert np.isclose(y.val, np.arcsin(0.5))
	assert np.isclose(y.der, 5.0 / np.sqrt(1-np.power(0.5,2)))
	assert np.isclose(arcsin(0.5), np.arcsin(0.5))

def test_arccos():
	x = Dual(0.5,5.0)
	y = arccos(x)
	assert np.isclose(y.val, np.arccos(0.5))
	assert np.isclose(y.der, -5.0 / np.sqrt(1-np.power(0.5,2)))
	assert np.isclose(arccos(0.5), np.arccos(0.5))

def test_arctan():
	x = Dual(0.5,5.0)
	y = arctan(x)
	assert np.isclose(y.val, np.arctan(0.5))
	assert np.isclose(y.der, 5.0 / (1 + np.power(0.5,2)))
	assert np.isclose(arctan(0.5), np.arctan(0.5))


def test_sinh():
	x = Dual(0.5,5.0)
	y = sinh(x)
	assert np.isclose(y.val, np.sinh(0.5))
	assert np.isclose(y.der, 5.0 * np.cosh(0.5))
	assert np.isclose(sinh(0.5), np.sinh(0.5))

def test_cosh():
	x = Dual(0.5,5.0)
	y = cosh(x)
	assert np.isclose(y.val, np.cosh(0.5))
	assert np.isclose(y.der, 5.0 * np.sinh(0.5))
	assert np.isclose(cosh(0.5), np.cosh(0.5))

def test_tanh():
	x = Dual(0.5,5.0)
	y = tanh(x)
	assert np.isclose(y.val, np.tanh(0.5))
	assert np.isclose(y.der, 5.0 / np.power(np.cosh(0.5),2))
	assert np.isclose(tanh(0.5), np.tanh(0.5))

def test_sqrt():
	x = Dual(0.5,5.0)
	y = sqrt(x)
	assert np.isclose(y.val, np.sqrt(0.5))
	assert np.isclose(y.der, 5.0 / (2 * np.sqrt(0.5)))
	assert np.isclose(sqrt(0.5), np.sqrt(0.5))

def test_logistic():
	x = Dual(0.5)
	y = logistic(x)
	assert np.isclose(y.val, 0.6224593312018546)
	assert np.isclose(y.der, 0.2350037122015945)