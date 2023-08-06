from AutoDiff.ForwardAD import Var, MultiFunc
import numpy as np

def test_constructor():
    x = Var(1.0)
    y = Var(2.0)   
    # scalar input and scalar output
    def test_scalar_scalar():
        assert x.get_value() == 1.0
        assert type(x.get_value()) == float
        assert x.get_der() == [1.0]
        
    # vector input and scalar output    
    def test_vec_scalar():
        z = 2*x+y**2
        assert z.get_value() == 6.0
        assert type(z.get_value()) == float
        assert z._get_derivative_of(x) == 2.0
        assert z._get_derivative_of(y) == 4.0
        assert type(z._get_derivative_of(x)) == float
        assert type(z._get_derivative_of(y)) == float
        assert z.get_der([x,y]) == [2.0, 4.0]
        assert type(z.get_der([x,y])) == list
        
    # scalar input and vector output
    def test_scalar_vector():
        vec = MultiFunc([x, x**2]) 
        assert vec.get_value() == [1.0, 1.0]
        assert vec.get_der([x]) == [[1.0], [2.0]]
        assert type(vec.get_value()) == list
        assert type(vec.get_der([x])) == list
        
    # vector input and vector output
    def test_vector_vector():
        z = MultiFunc([x+y, y**2])
        assert z.get_value() == [3.0, 4.0]
        assert z.get_der([x,y]) == [[1.0, 1.0], [0, 4.0]]
        ## partial derivative
        assert type(z.get_value()) == list
        assert type(z.get_der([x,y])) == list

    test_scalar_scalar()
    test_vec_scalar()
    test_scalar_vector()
    test_vector_vector()

def test_scalar_input_scalar_output():
    def test_overloading():
        x = Var(4.0)
        #y = Var(3.0)
        def test_add():
            # scalar->scalar   
            z1 = x+2+x+10
            assert z1.get_value() == 20.0
            assert z1.get_der() == [2.0]
            # x not modified
            assert x.get_value() == Var(4.0).get_value()

        def test_radd():
            z1 = 2+x+10+x
            assert z1.get_value() == 20.0
            assert z1.get_der() == [2.0]

            z2 = 1.0+(3.0+2.0)+x+x
            assert z2.get_value() == 14.0
            assert z1.get_der() == [2.0]

        def test_subtract():
            x = Var(4.0)

            z2 = x -1.0 -2.0 -x
            assert z2.get_value() == -3.0
            assert z2.get_der() == [0]

            # x not modified
            assert x.get_value() == Var(4.0).get_value()

        def test_rsubtract():
            x = Var(4.0)
            z1 = 10.0-x
            assert z1.get_value() == 6.0
            assert z1.get_der() == [-1.0]

            z2 = 20.0-3.0-x-x
            assert z2.get_value() == 9.0
            assert z2.get_der() == [-2.0]

        def test_mul():
            x = Var(4.0)

            z2 = x*2*3
            assert z2.get_value() == 24.0
            assert z2.get_der() == [6.0]

            z3 = x*x+x*2
            assert z3.get_value() == 24.0
            assert z3.get_der() == [10.0]

        def test_rmul():
            z1 = 3*x
            assert z1.get_value()  == 12.0
            assert z1.get_der() == [3.0]

            z2 = 3*10*x*x
            assert z2.get_value() == 480.0
            assert z2.get_der() == [240.0]

        def test_div():
            z2 = x/4
            assert z2.get_value() == 1.0
            assert z2.get_der() == [0.25]

            z3 = (x/0.5)/0.1
            assert z3.get_value() == 80.0
            assert np.round(z3.get_der(), 10) == np.round([20.0], 10)

        def test_rdiv():
            z1 = 8.0/x
            assert z1.get_value() == 2.0
            assert z1.get_der() == [-0.5]

            z2 = (24.0/x)/1.5
            assert z2.get_value() == 4.0
            assert z2.get_der() == [-1.0]

        def test_pow():
            z1 = x**2
            z3 = x*x
            assert z1.get_value() == 16.0
            assert z1.get_der() == [8.0]
            assert z1.get_value() == z3.get_value()

            z2 = x**(0.5)
            z3 = Var.sqrt(x)
            z4 = x.sqrt()
            assert z2.get_value() == 2.0
            assert z2.get_der() == [0.25]
            assert z2.get_value() == z3.get_value() == z4.get_value()

        def test_rpow():
            a = 2
            z1 = a**x
            assert z1.get_value() == 16.0
            assert z1.get_der() == [np.log(a)*16.0]

        test_add()
        test_radd()
        test_subtract()
        test_rsubtract()
        test_mul()
        test_rmul()
        test_div()
        test_rdiv()
        test_pow()
        test_rpow()

    def test_comparison():
        x = Var(4.0)
        y = Var(1.5)
        q = Var(4.0)
        m1 = x + x
        m2 = 2*x
        z1 = x*4.0/2.0
        z2 = x*2.0
            
        def test_eq():
            assert not x == y
            assert not x == q
            
            assert m1 == m2
            assert m1.__eq__(m2)
            
            assert z1 == z2
            
        def test_ne():
            z3 = -z1
            assert not z3 == z2
            
            m3 = -m1
            m3.get_value() == -8.0
            
        '''    
        def test_less():
            assert x > y
            assert not z < y
            assert x <10.0
            assert not y <0.0
            
        def test_lesseq():
            assert x <= z
            assert not x<=y
            assert z <= 4.0
            assert y <= 10.0
            
        def test_greater():
            assert x > y
            assert not y >z
            assert x+2.0 > z
            
        def test_greatereq():
            assert x >=z 
            assert x>=y
            assert y+10.0 >= x
            assert not y >=z
        '''
        

        test_eq()
        test_ne()
        '''
        test_less()
        test_lesseq()
        test_greater()
        test_greatereq()
        '''
    def test_elementary():

        def test_negative():
            x1 = Var(2.0)
            f1 = -x1
            assert f1.get_value() == -2.0
            assert f1.get_der() == [-1.0]

            x2 = Var(0.0)
            f2 = -x2
            assert f2.get_value() == 0.0
            assert f2.get_der() == [-1.0]

            # test for operator order
            f3 = - x1 / x1
            assert f3.get_value() == -1.0
            assert f3.get_der() == [0.0]

        def test_abs():
            # abs() not differentiable at zero
            with np.testing.assert_raises(ValueError):
                x1 = Var(0.0)
                f1 = abs(x1)

            x2 = Var(5.0)
            f2 = abs(x2)
            assert f2.get_value() == 5.0
            assert f2.get_der() == [1.0]

            x3 = Var(-5.0)
            f3 = abs(x3)
            assert f3.get_value() == 5.0
            assert f3.get_der() == [-1.0]

        def test_sin():
            x1 = Var(np.pi)
            f1 = 10e16 * Var.sin(x1)
            assert np.round(f1.get_value(), 2) == 12.25
            assert np.round(f1.get_der(), 2) == [-1.e+17]

            x2 = Var(np.pi * 3 / 2)
            f2 = 10e16 * Var.sin(x2)
            assert np.round(f2.get_value(), 2) == -1.e+17
            assert np.round(f2.get_der(), 2) == [-18.37]

        def test_cos():
            x1 = Var(np.pi)
            f1 = 10e16 * Var.cos(x1)
            assert np.round(f1.get_value(), 2) == -1.e+17
            assert np.round(f1.get_der(), 2) == [-12.25]

            x2 = Var(np.pi * 3 / 2)
            f2 = 10e16 * Var.cos(x2)
            assert np.round(f2.get_value(), 2) == -18.37
            assert np.round(f2.get_der(), 2) == [1.e+17]

        def test_tan():
            # tan() not define for multiples of pi/2
            with np.testing.assert_raises(ValueError):
                x0 = Var(np.pi / 2)
                f0 = Var.tan(x0)

            x1 = Var(np.pi / 3)
            f1 = Var.tan(x1)
            assert np.round(f1.get_value(), 2) == 1.73
            assert np.round(f1.get_der(), 2) == [4.0]

            x2 = Var(np.pi / 6)
            f2 = Var.tan(x2)
            assert np.round(f2.get_value(), 2) == 0.58
            assert np.round(f2.get_der(), 2) == [1.33]

        def test_arcsin():
            # arcsin() is undefined for |x| > 1
            with np.testing.assert_raises(ValueError):
                x = Var(3)
                Var.arcsin(x)

            with np.testing.assert_raises(ZeroDivisionError):
                x = Var(1)
                f = Var.arcsin(x)

            x = Var(0)
            f = Var.arcsin(x)
            assert f.get_value() == [0.0]
            assert f.get_der() == [1.0]

        def test_arccos():
            # arccos() is undefined for |x| > 1
            with np.testing.assert_raises(ValueError):
                x = Var(3)
                Var.arccos(x)

            x = Var(0)
            f = Var.arccos(x)
            assert np.round(f.get_value(), 2) == 1.57
            assert np.round(f.get_der(), 2) == [-1.0]

        def test_arctan():
            x = Var(1)
            f = Var.arctan(x)
            assert np.round(f.get_value(), 2) == 0.79
            assert np.round(f.get_der(), 2) == [0.5]

        def test_sinh():
            x = Var(1)
            f = Var.sinh(x)
            assert np.round(f.get_value(), 2) == 1.18
            assert np.round(f.get_der(), 2) == [1.54]

        def test_cosh():
            x = Var(1)
            f = Var.cosh(x)
            assert np.round(f.get_value(), 2) == 1.54
            assert np.round(f.get_der(), 2) == [1.18]

        def test_tanh():
            x = Var(1)
            f = Var.tanh(x)
            assert np.round(f.get_value(), 2) == 0.76
            assert np.round(f.get_der(), 2) == [0.42]

        def test_sqrt():
            # derivative does not exist if x = 0
            x = Var(0)
            with np.testing.assert_raises(ZeroDivisionError):
                f = Var.sqrt(x)

            x1 = Var(9)
            f1 = Var.sqrt(x1)
            assert f1.get_value() == 3
            assert np.round(f1.get_der(), 2) == [0.17]

        def test_log():
            # log() not defined for x <= 0
            with np.testing.assert_raises(ValueError):
                x0 = Var(0)
                f0 = Var.log(x0, 10)

            x1 = Var(1000)
            f1 = Var.log(x1, 10)
            assert np.round(f1.get_value(), 2) == 3.0
            assert np.round(f1.get_der(), 4) == [0.0004]

        def test_exp():
            x = Var(5)
            f = Var.exp(x)
            assert np.round(f.get_value(), 2) == 148.41
            assert np.round(f.get_der(), 2) == [148.41]

        test_negative()
        test_abs()
        test_sin()
        test_cos()
        test_tan()
        test_arcsin()
        test_arccos()
        test_arctan()
        test_sinh()
        test_cosh()
        test_tanh()
        test_sqrt()
        test_log()
        test_exp()


    def test_composition():
        x = Var(np.pi)

        def test_1_trig():
            z1 = Var.sin(Var.cos(x))
            assert np.round(z1.get_value(),10) == -0.8414709848
            assert np.round(z1.get_der(),10) == [0]

        def test_2():
            z2 = Var.sin(x**2)
            assert np.round(z2.get_value(), 9) == -0.430301217
            assert np.round(z2.get_der(),10) == -5.6717394031
        test_1_trig()
        test_2()

    test_overloading()
    test_comparison()
    test_elementary()
    test_composition()



def test_multivariate_input_scalar_output():
    def test_overloading():
        x = Var(4.0)
        y = Var(3.0)
        z = Var(5.0)
        def test_add():
            z1 = x+y
            assert z1.get_value() == 7.0
            assert z1.get_der() == [1.0, 1.0]
            assert z1._get_derivative_of(x) == 1.0
            assert z1._get_derivative_of(y) == 1.0

        def test_radd():
            z1 = 2+y+10+x
            assert z1.get_value() == 19.0
            assert z1.get_der() == [1.0, 1.0]
            assert z1._get_derivative_of(x) == 1.0
            assert z1._get_derivative_of(y) == 1.0

        def test_subtract():
            z1 = z-x-y-1
            assert z1.get_value() == -3.0
            assert z1.get_der([x, y, z]) == [-1.0, -1.0, 1.0]
            assert z1._get_derivative_of(x) == -1.0
            assert z1._get_derivative_of(y) == -1.0
            assert z1._get_derivative_of(z) == 1.0

            # z not modified
            assert z.get_value() == Var(5.0).get_value()

        def test_rsubtract():
            z1 = 10.0-x-y
            assert z1.get_value() == 3.0
            assert z1.get_der() == [-1.0, -1.0]
            assert z1._get_derivative_of(x) == -1.0
            assert z1._get_derivative_of(y) == -1.0

        def test_mul():
            z1 = x*y*z*10
            assert z1.get_value() == 600.0
            assert z1.get_der() == [150.0, 200.0, 120.0]
            assert z1._get_derivative_of(x) == 150.0
            assert z1._get_derivative_of(y) == 200.0
            assert z1._get_derivative_of(z) == 120.0

        def test_rmul():
            z1 = 2*x*5*y*z
            assert z1.get_value() == 600.0
            assert z1.get_der() == [150.0, 200.0, 120.0]
            assert z1._get_derivative_of(x) == 150.0
            assert z1._get_derivative_of(y) == 200.0
            assert z1._get_derivative_of(z) == 120.0

        def test_div():
            z1 = (z/x)/10
            assert z1.get_value() == 5.0/40.0
            assert z1.get_der([x,z]) == [ -5.0/160.0, 1.0/40.0]
            assert z1._get_derivative_of(z) == 1.0/40.0
            assert z1._get_derivative_of(x) == -5.0/160.0

        def test_rdiv():
            z1 = 6.0/(y/x)
            assert z1.get_value() == 8.0
            assert z1.get_der() == [-8.0/3.0, 2.0]  #dz1/dy first, dz1/dx second
            assert z1._get_derivative_of(y) == -8.0/3.0
            assert z1._get_derivative_of(x) == 2.0

        def test_pow():
            z1 = x**y
            assert z1.get_value() == 64.0
            np.testing.assert_array_equal(np.round(z1.get_der([x,y]),10), np.round([48.0, 64*np.log(4)], 10))
            assert np.round(z1._get_derivative_of(x), 10) == np.round(48.0, 10)
            assert np.round(z1._get_derivative_of(y), 10) == np.round(64*np.log(4), 10)

        def test_rpow():
            z1 = (2**x)**y
            assert z1.get_value() == 4096.0
            np.testing.assert_array_equal(np.round(z1.get_der(), 10), np.round([12288*np.log(2), 16384*np.log(2)], 10))
            assert np.round(z1._get_derivative_of(x), 10) == np.round(12288*np.log(2), 10)
            assert np.round(z1._get_derivative_of(y), 10) == np.round(16384*np.log(2), 10)

        test_add()
        test_radd()
        test_subtract()
        test_rsubtract()
        test_mul()
        test_rmul()
        test_div()
        test_rdiv()
        test_pow()
        test_rpow()

    def test_comparison():
        x = Var(4.0)
        y = Var(1.5)
        z1 = x + y
        z2 = abs(x+y)
            
        def test_eq():
            assert z1 == z2
            assert z1.__eq__(z2)
            assert not x == y
                
            m1 = x*4.0/2.0
            m2 = x*2.0
            assert m1 == m2
            
        def test_ne():
            z3 = -z1
            assert not z3 == z2
            
            x2 = -x
            x2.get_value() == -4.0
            
            
        '''    
        def test_less():
            assert x > y
            assert not z < y
            assert x <10.0
            assert not y <0.0
            
        def test_lesseq():
            assert x <= z
            assert not x<=y
            assert z <= 4.0
            assert y <= 10.0
            
        def test_greater():
            assert x > y
            assert not y >z
            assert x+2.0 > z
            
        def test_greatereq():
            assert x >=z 
            assert x>=y
            assert y+10.0 >= x
            assert not y >=z
        '''    
        test_eq()
        test_ne()
        '''
        test_less()
        test_lesseq()
        test_greater()
        test_greatereq()
        '''

    def test_composition():
        x = Var(np.pi)
        y = Var(0)
        z = Var(np.pi/2)

        def test_1_trig():
            z1 = Var.sin(Var.cos(x))+ Var.sin(y)
            assert np.round(z1.get_value(),10) == -0.8414709848
            np.testing.assert_array_equal(np.round(z1.get_der([x,y]), 10), np.round([0, 1.0], 10))
            assert np.round(z1._get_derivative_of(x), 10) == np.round(0, 10)
            assert np.round(z1._get_derivative_of(y), 10) == np.round(1.0, 10)
            

        def test_2():
            z2 = Var.sin(x**2) + Var.sin(z)
            assert np.round(z2.get_value(), 9) == -0.430301217+1.0
            np.testing.assert_array_equal(np.round(z2.get_der([x,z]),10), np.round([-5.6717394031, 0], 10))
            
        test_1_trig()
        test_2()

    test_overloading()
    test_comparison()
    test_composition()

    def suite_negative():
        x = Var(4.0)
        y = Var(5.0)
        f = x ** 3 + 3 * y
        f1 = -f
        assert f1.get_value() == np.array([-79.])
        np.testing.assert_array_equal(f1.get_der([x, y]), np.array([-48., -3.]))

        f1.get_der([x, y])

    def suite_abs():
        x = Var(-4.0)
        y = Var(-5.0)
        f = x ** 3 - 3 * y
        f1 = abs(f)
        np.testing.assert_array_equal(f1.get_value(), np.array([49.]))
        np.testing.assert_array_equal(f1.get_der([x, y]), np.array([-48., 3.]))

        # abs() not differentiable at zero
        with np.testing.assert_raises(ValueError):
            x = Var(0.0)
            y = Var(0.0)
            f = x ** 3 - 3 * y
            f1 = abs(f)

    def suite_sin():
        x = Var(3 * np.pi / 2)
        y = Var(np.pi / 2)
        f = 3 * Var.sin(x) - 5 * Var.sin(y)
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([-8.]))
        np.testing.assert_array_equal(np.round(f.get_der([x, y]), 2), np.array([-0., -0.]))

    def suite_cos():
        x = Var(3 * np.pi / 2)
        y = Var(np.pi / 2)
        f = 3 * Var.cos(x) - 5 * Var.cos(y)
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([-0.]))
        np.testing.assert_array_equal(np.round(f.get_der([x, y]), 2), np.array([3., 5.]))

    def suite_tan():
        x = Var(np.pi / 6)
        y = Var(np.pi / 4)
        f = 3 * Var.tan(x) - 5 * Var.tan(y)
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([-3.27]))
        np.testing.assert_array_equal(np.round(f.get_der([x, y]), 2), np.array([4., -10.]))

        with np.testing.assert_raises(ValueError):
            z = Var(np.pi / 2)
            f = Var.tan(z) - Var.tan(x)

    def suite_arcsin():
        x = Var(1)
        y = Var(-1)

        with np.testing.assert_raises(ZeroDivisionError):
            f = Var.arcsin(x) - 3 * Var.arcsin(y)

        x = Var(0.5)
        y = Var(0.2)
        f = Var.arcsin(x) - 3 * Var.arcsin(y)
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([-0.08]))
        np.testing.assert_array_equal(np.round(f.get_der([x, y]), 2), np.array([1.15, -3.06]))

        # not defined for |x| > 1
        with np.testing.assert_raises(ValueError):
            x = Var(-1.01)
            f = 3 * Var.arcsin(x) + 2 * Var.arcsin(y)

    def suite_arccos():
        x = Var(0)
        y = Var(0.5)
        f = Var.arccos(x) - 3 * Var.arccos(y)
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([-1.57]))
        np.testing.assert_array_equal(np.round(f.get_der([x, y]), 2), np.array([-1., 3.46]))

        # not defined for |x| > 1
        with np.testing.assert_raises(ValueError):
            x = Var(2)
            f = Var.arccos(x) - Var.arccos(y)

        x = Var(1)
        y = Var(-1)
        with np.testing.assert_raises(ZeroDivisionError):
            f = Var.arccos(x) - Var.arccos(y)

    def suite_arctan():
        x = Var(1)
        y = Var(- np.pi / 2)
        f = Var.arctan(x) - 3 * Var.arctan(y)
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([3.8]))
        np.testing.assert_array_equal(np.round(f.get_der([x, y]), 2), np.array([0.5, -0.87]))

    def suite_sinh():
        x = Var(3)
        y = Var(1)
        f = Var.sinh(x) - 3 * Var.sinh(y)
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([6.49]))
        np.testing.assert_array_equal(np.round(f.get_der([x, y]), 2), np.array([10.07, -4.63]))

    def suite_cosh():
        x = Var(3)
        y = Var(1)
        f = Var.cosh(x) - 3 * Var.cosh(y)
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([5.44]))
        np.testing.assert_array_equal(np.round(f.get_der([x, y]), 2), np.array([10.02, -3.53]))

    def suite_tanh():
        x = Var(3)
        y = Var(1)
        f = Var.tanh(x) - 3 * Var.tanh(y)
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([-1.29]))
        np.testing.assert_array_equal(np.round(f.get_der([x, y]), 2), np.array([0.01, -1.26]))

    def suite_sqrt():
        x = Var(1.0)
        y = Var(2.0)
        z = Var(3.0)
        f = 2 * x + y + z
        f1 = Var.sqrt(f)
        np.testing.assert_array_equal(np.round(f1.get_value(), 2), np.array([2.65]))
        np.testing.assert_array_equal(np.round(f1.get_der([x, y, z]), 2), np.array([0.38, 0.19, 0.19]))

        # derivative of 0^x does not exist if x < 1
        with np.testing.assert_raises(ZeroDivisionError):
            f = Var.sqrt(2 * x - y)

    def suite_log():
        x = Var(10)
        y = Var(1000)
        f = 2 * x + y
        f1 = f.log(10)
        np.testing.assert_array_equal(np.round(f1.get_value(), 2), np.array([3.01]))
        np.testing.assert_array_equal(np.round(f1.get_der([x, y]), 5), np.array([0.00085, 0.00043]))

        # log() not defined for x <= 0
        with np.testing.assert_raises(ValueError):
            f2 = y - 100 * x
            f3 = f2.log(2)

    def suite_exp():
        x = Var(1.0)
        y = Var(2.0)
        z = Var(3.0)
        f = 2 * x - y + z
        f1 = Var.exp(f)
        np.testing.assert_array_equal(np.round(f1.get_value(), 2), np.array([20.09]))
        np.testing.assert_array_equal(np.round(f1.get_der([x, y, z]), 2), np.array([40.17, -20.09, 20.09]))

    def suite_logistic():
        x = Var(1.0)
        y = Var(2.0)
        z = Var(3.0)
        f = x + y + z
        f1 = Var.logistic(f)
        print(f1.get_der([x, y, z]))
        np.testing.assert_array_equal(np.round(f1.get_value(), 3), np.array([0.998]))
        np.testing.assert_array_equal(np.round(f1.get_der([x, y, z]), 3), np.array([0.002, 0.002, 0.002]))

    suite_negative()
    suite_abs()
    suite_sin()
    suite_cos()
    suite_tan()
    suite_arcsin()
    suite_arccos()
    suite_arctan()
    suite_sinh()
    suite_cosh()
    suite_tanh()
    suite_sqrt()
    suite_log()
    suite_exp()
    suite_logistic()


def test_scalar_input_vector_output():
    def test_overloading():
        x = Var(4.0)
        y = MultiFunc([2*x, x**2])
        z = MultiFunc([x, 2*x])
        def test_add():
            z1 = y + 1
            assert z1.get_value() == [9.0, 17.0]
            assert z1.get_der([x]) == [[2.0], [8.0]]
            
            z2 = z + MultiFunc([x, x])
            assert z2.get_value() == [8.0, 12.0]
            assert z2.get_der([x]) == [[2.0], [3.0]]

        def test_radd():
            z1 = 2 + y
            assert z1.get_value() == [10.0, 18.0]
            assert z1.get_der([x]) == [[2.0], [8.0]]

        def test_subtract():
            z1 = y - z - 1  # = [x, x^2 - 2x]
            assert z1.get_value() == [3.0, 7.0]
            assert z1.get_der([x]) == [[1.0], [6.0]]

            # z not modified
            assert z.get_value() == MultiFunc([x, 2*x]).get_value()

        def test_rsubtract():
            z1 = 10.0-y-z
            assert z1.get_value() == [-2.0, -14.0]
            assert z1.get_der([x]) == [[-3.0], [-10.0]]

        def test_mul():
            z1 = y*z*2
            assert z1.get_value() == [64.0, 256.0]
            assert z1.get_der([x]) == [[32.0], [192.0]]

        def test_rmul():
            z1 = 2*y*z
            assert z1.get_value() == [64.0, 256.0]
            assert z1.get_der([x]) == [[32.0], [192.0]]

        def test_div():
            z1 = (y/z)/10
            assert z1.get_value() == [0.2, 0.2]
            assert z1.get_der([x]) == [[0.0], [0.05]]

        def test_rdiv():
            z1 = 10/(y/x)
            assert z1.get_value() == [5.0, 2.5]
            assert z1.get_der([x]) == [[0], [-0.625]]

        def test_pow():
            z1 = y**2
            assert z1.get_value() == [64.0, 256.0]
            assert z1.get_der([x]) == [[32.0], [256.0]]  #=【8x, 4x^3]

        def test_rpow():
            z1 = 2**y
            assert z1.get_value() == [256.0, 65536.0]
            np.testing.assert_array_equal(np.round(z1.get_der([x]), 10), np.round([[512.0*np.log(2)], [524288.0*np.log(2)]], 10))

        test_add()
        test_radd()
        test_subtract()
        test_rsubtract()
        test_mul()
        test_rmul()
        test_div()
        test_rdiv()
        test_pow()
        test_rpow()
        
    def test_comparison():
        x = Var(4.0)
        y = MultiFunc([x**2, x+x])
        z = MultiFunc([x*x, 2*x])
        
        def test_eq():
            assert y == z
            assert y.__eq__(z)
                
            y1 = y*4.0/2.0
            z1 = z*2.0
            assert y1 == z1
        
        def test_ne():
            x1 = -x
            x1.get_value() == -4.0
            y1 = -y
            y1.get_value() == [-16.0, -8.0]
        
        '''    
        def test_less():
            assert x > y
            assert not z < y
            assert x <10.0
            assert not y <0.0
            
        def test_lesseq():
            assert x <= z
            assert not x<=y
            assert z <= 4.0
            assert y <= 10.0
            
        def test_greater():
            assert x > y
            assert not y >z
            assert x+2.0 > z
            
        def test_greatereq():
            assert x >=z 
            assert x>=y
            assert y+10.0 >= x
            assert not y >=z
        '''
        
        test_eq()
        test_ne()
        '''
        test_less()
        test_lesseq()
        test_greater()
        test_greatereq()
        '''

    def test_composition():
        x = Var(np.pi)
        y = MultiFunc([x, x])
        def test_1_trig():
            f = y.apply(Var.cos)
            z1 = f.apply(Var.sin)
            np.testing.assert_array_equal(np.round(z1.get_value(),10), np.round([-0.8414709848, -0.8414709848], 10))
            np.testing.assert_array_equal(np.round(z1.get_der([x]),10), np.round([[0], [0]], 10))
            

        '''
        def test_2():
            z2 = Var.sin(x**2) + Var.sin(z)
            assert np.round(z2.get_value(), 9) == -0.430301217+1.0
            assert np.round(z2.get_der(),10) == [-5.6717394031, 0]
        '''   
        test_1_trig()


    test_overloading()
    test_comparison()
    test_composition()
    
    def suite_negative():
        x = Var(2.0)
        f = MultiFunc([x, 2 * x, x ** 2])
        f1 = -f
        np.testing.assert_array_equal(f1.get_value(), np.array([-2., -4., -4.]))
        np.testing.assert_array_equal(f1.get_der([x]), np.array([[-1.], [-2.], [-4.]]))

    def suite_abs():
        # abs() not differentiable at zero
        with np.testing.assert_raises(ValueError):
            x = Var(0.0)
            f = MultiFunc([x, x ** 2, x ** 3])
            f1 = abs(f)

        x = Var(3.0)
        f = MultiFunc([x, 2 * x, x ** 3])
        f1 = abs(f)
        np.testing.assert_array_equal(f1.get_value(), np.array([3., 6., 27.]))
        np.testing.assert_array_equal(f1.get_der([x]), np.array([[1.], [2.], [27.]]))

    def suite_sin():
        x = Var(np.pi / 2)
        f = MultiFunc([Var.sin(x) + 1, 3 * Var.sin(x), Var.sin(x) ** 3])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([2., 3., 1.]))
        np.testing.assert_array_equal(np.round(f.get_der([x]), 2), np.array([[0.], [0.], [0.]]))

    def suite_cos():
        x = Var(np.pi / 2)
        f = MultiFunc([Var.cos(x) + 1, 3 * Var.cos(x), Var.cos(x) ** 3])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([1., 0., 0.]))
        np.testing.assert_array_equal(np.round(f.get_der([x]), 2), np.array([[-1.], [-3.], [0.]]))

    def suite_tan():
        x = Var(np.pi / 4)
        f = MultiFunc([Var.tan(x) + 1, Var.tan(x), Var.tan(x) ** 2])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([2., 1., 1.]))
        np.testing.assert_array_equal(np.round(f.get_der([x]), 2), np.array([[2.], [2.], [4.]]))

    def suite_arcsin():
        x = Var(0.5)
        f = MultiFunc([2 * Var.arcsin(x), Var.arcsin(x) + 1, Var.arcsin(x) ** 3])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([1.05, 1.52, 0.14]))
        np.testing.assert_array_equal(np.round(f.get_der([x]), 2), np.array([[2.31], [1.15], [0.95]]))

        with np.testing.assert_raises(ZeroDivisionError):
            x = Var(1)
            f = MultiFunc([2 * Var.arcsin(x), Var.arcsin(x) + 1, Var.arcsin(x) ** 3])

        # not defined for |x| > 1
        with np.testing.assert_raises(ValueError):
            z = Var(2)
            f = MultiFunc([Var.arcsin(z), Var.arcsin(z) ** 2])

    def suite_arccos():
        x = Var(0.5)
        f = MultiFunc([2 * Var.arccos(x), Var.arccos(x) + 1, Var.arccos(x) ** 3])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([2.09, 2.05, 1.15]))
        np.testing.assert_array_equal(np.round(f.get_der([x]), 2), np.array([[-2.31], [-1.15], [-3.8]]))

        with np.testing.assert_raises(ZeroDivisionError):
            x = Var(1)
            f = MultiFunc([2 * Var.arccos(x), Var.arccos(x) + 1, Var.arccos(x) ** 3])

        # not defined for |x| > 1
        with np.testing.assert_raises(ValueError):
            z = Var(2)
            f = MultiFunc([Var.arccos(z), Var.arccos(z) ** 2])

    def suite_arctan():
        x = Var(1)
        f = MultiFunc([Var.arctan(x) ** 3, 2 * Var.arctan(x)])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([0.48, 1.57]))
        np.testing.assert_array_equal(np.round(f.get_der([x]), 2), np.array([[0.93], [1.]]))

    def suite_sinh():
        x = Var(1)
        f = MultiFunc([Var.sinh(x) ** 3, 2 * Var.sinh(x)])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([1.62, 2.35]))
        np.testing.assert_array_equal(np.round(f.get_der([x]), 2), np.array([[6.39], [3.09]]))

    def suite_cosh():
        x = Var(1)
        f = MultiFunc([Var.cosh(x) ** 3, 2 * Var.cosh(x)])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([3.67, 3.09]))
        np.testing.assert_array_equal(np.round(f.get_der([x]), 2), np.array([[8.39], [2.35]]))

    def suite_tanh():
        x = Var(1)
        f = MultiFunc([Var.tanh(x) ** 3, 2 * Var.tanh(x)])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([0.44, 1.52]))
        np.testing.assert_array_equal(np.round(f.get_der([x]), 2), np.array([[0.73], [0.84]]))


    def suite_sqrt():
        x = Var(2.0)
        f = MultiFunc([x + 2, 3 * x, x ** 2])
        f1 = f.apply(Var.sqrt)
        np.testing.assert_array_equal(np.round(f1.get_value(), 2), np.array([2., 2.45, 2.]))
        np.testing.assert_array_equal(np.round(f1.get_der([x]), 2), np.array([[0.25], [0.61], [1.]]))

        # The derivative of sqrt(x), 1/2 * 1/sqrt(x), is undefined on x = 0.
        with np.testing.assert_raises(ZeroDivisionError):
            x = Var(0.0)
            f = MultiFunc([x, 3 * x])
            f = f.apply(Var.sqrt)


    def suite_log():
        x = Var(5.0)
        f = MultiFunc([x + 2, x ** 3, 2 * x])
        f1 = f.apply(Var.log, 2)
        np.testing.assert_array_equal(np.round(f1.get_value(), 2), np.array([2.81, 6.97, 3.32]))
        np.testing.assert_array_equal(np.round(f1.get_der([x]), 2), np.array([[0.21], [0.87], [0.29]]))

        # log() not defined for x <= 0
        with np.testing.assert_raises(ValueError):
            f2 = MultiFunc([x, -x, x ** 2])
            f3 = f2.apply(Var.log)


    def suite_exp():
        x = Var(2.0)
        f = MultiFunc([x + 2, 3 * x, x ** 2])
        f1 = f.apply(Var.exp)
        np.testing.assert_array_equal(np.round(f1.get_value(), 2), np.array([54.6, 403.43, 54.6]))
        np.testing.assert_array_equal(np.round(f1.get_der([x]), 2), np.array([[54.6], [1210.29], [218.39]]))

    def suite_logistic():
        x = Var(2.0)
        f = MultiFunc([x + 2, 3 * x, x ** 2])
        f1 = f.apply(Var.logistic)
        np.testing.assert_array_equal(np.round(f1.get_value(), 3), np.array([0.982, 0.998, 0.982]))
        np.testing.assert_array_equal(np.round(f1.get_der([x]), 3), np.array([[0.018], [0.007], [0.071]]))

    suite_negative()
    suite_abs()
    suite_sin()
    suite_cos()
    suite_tan()
    suite_arcsin()
    suite_arccos()
    suite_arctan()
    suite_sinh()
    suite_cosh()
    suite_tanh()
    suite_sqrt()
    suite_log()
    suite_exp()
    suite_logistic()


def test_vector_input_vector_output():
    def test_overloading():
        x = Var(3.0)
        y = Var(2.0)
        z = MultiFunc([x, y])
        p = MultiFunc([y*2, x+2])
        def test_add():
            z1 = z + 1
            assert z1.get_value() == [4.0, 3.0]
            assert z1.get_der([x, y]) == [[1.0, 0], [0, 1.0]]
            assert z1.get_der([x]) == [[1.0], [0]]
            assert z1.get_der([y]) == [[0], [1.0]]
            #assert z1._get_derivative_of(x) = 1.0
            #assert z1._get_derivative_of(x2) = 8.0
            
            z2 = MultiFunc([y, x]) + MultiFunc([x, x])
            assert z2.get_value() == [5.0, 6.0]
            assert z2.get_der([x,y]) == [[1.0, 1.0], [2.0, 0]]
            assert z2.get_der([x]) == [[1.0], [2.0]]
            assert z2.get_der([y]) == [[1.0], [0]]

        def test_radd():
            z1 = 1 + z
            assert z1.get_value() == [4.0, 3.0]
            assert z1.get_der([x, y]) == [[1.0, 0], [0, 1.0]]
            assert z1.get_der([x]) == [[1.0], [0]]
            assert z1.get_der([y]) == [[0], [1.0]]

        def test_subtract():
            z1 = z - 1  # = [x, x^2 - 2x]
            assert z1.get_value() == [2.0, 1.0]
            assert z1.get_der([x, y]) == [[1.0, 0], [0, 1.0]]
            assert z1.get_der([x]) == [[1.0], [0]]
            assert z1.get_der([y]) == [[0], [1.0]]
            
            # z not modified
            assert z.get_value() == MultiFunc([Var(3.0), Var(2.0)]).get_value()
            
            z2 = z - MultiFunc([y, x])
            assert z2.get_value() == [1.0, -1.0]
            assert z2.get_der([x,y]) == [[1.0, -1.0], [-1.0, 1.0]]
            assert z2.get_der([x]) == [[1.0], [-1.0]]
            assert z2.get_der([y]) == [[-1.0], [1.0]]

        def test_rsubtract():
            z1 = 10.0-z
            assert z1.get_value() == [7.0, 8.0]
            assert z1.get_der([x, y]) == [[-1.0, 0], [0, -1.0]]
            assert z1.get_der([x]) == [[-1.0], [0]]
            assert z1.get_der([y]) == [[0], [-1.0]]

        def test_mul():
            z1 = z*2
            assert z1.get_value() == [6.0, 4.0]
            assert z1.get_der([x,y]) == [[2.0, 0], [0, 2.0]]
            assert z1.get_der([x]) == [[2.0], [0]]
            assert z1.get_der([y]) == [[0], [2.0]]
            
            z2 = z*p  # = [x*y^2, y(x+2)]
            assert z2.get_value() == [12.0, 10.0]
            assert z2.get_der([x,y]) == [[4.0, 6.0], [2.0, 5.0]]
            assert z2.get_der([x]) == [[4.0], [2.0]]
            assert z2.get_der([y]) == [[6.0], [5.0]]

        def test_rmul():
            z1 = 2*z
            assert z1.get_value() == [6.0, 4.0]
            assert z1.get_der([x,y]) == [[2.0, 0], [0, 2.0]]
            assert z1.get_der([x]) == [[2.0], [0.0]]
            assert z1.get_der([y]) == [[0], [2.0]]

        def test_div():
            z1 = z/10
            assert z1.get_value() == [0.3, 0.2]
            assert z1.get_der([x,y]) == [[0.1, 0], [0, 0.1]]
            assert z1.get_der([x]) == [[0.1], [0]]
            assert z1.get_der([y]) == [[0], [0.1]]
            
            z2 = p/z
            np.testing.assert_array_equal(np.round(z2.get_value(), 10), np.round([4.0/3, 2.5], 10))
            np.testing.assert_array_equal(np.round(z2.get_der([x,y]), 10), np.round([[-4.0/9, 2.0/3], [0.5, -5.0/4]], 10))
            np.testing.assert_array_equal(np.round(z2.get_der([x]),10), np.round([[-4.0/9], [0.5]], 10))
            np.testing.assert_array_equal(np.round(z2.get_der([y]), 10), np.round([[2.0/3], [-5.0/4]], 10))

        def test_rdiv():
            z1 = 10/z
            np.testing.assert_array_equal(np.round(z1.get_value(), 10), np.round([10.0/3, 5.0], 10))
            np.testing.assert_array_equal(np.round(z1.get_der([x,y]), 10), np.round([[-10.0/9, 0], [0, -2.5]], 10))
            np.testing.assert_array_equal(np.round(z1.get_der([x]),10), np.round([[-10.0/9], [0]], 10))
            np.testing.assert_array_equal(np.round(z1.get_der([y]), 10), np.round([[0], [-2.5]], 10))

        def test_pow():
            z1 = z**2
            assert z1.get_value() == [9.0, 4.0]
            assert z1.get_der([x,y]) == [[6.0, 0], [0, 4.0]] 
            assert z1.get_der([x]) == [[6.0], [0]]
            assert z1.get_der([y]) == [[0], [4.0]]
            
            z2 = z**p
            assert z2.get_value() == [81.0, 32.0]
            np.testing.assert_array_equal(np.round(z2.get_der([x,y]), 10), np.round([[108.0, 162.0*np.log(3)], [32.0*np.log(2), 80.0]], 10))
            np.testing.assert_array_equal(np.round(z2.get_der([x]),10), np.round([[108.0], [32.0*np.log(2)]], 10))
            np.testing.assert_array_equal(np.round(z2.get_der([y]), 10), np.round([[162.0*np.log(3)], [80.0]], 10))

        def test_rpow():
            z1 = 2**z
            assert z1.get_value() == [8.0, 4.0]
            np.testing.assert_array_equal(np.round(z1.get_der([x,y]), 10), np.round([[8.0*np.log(2), 0], [0, 4.0*np.log(2)]], 10))
            np.testing.assert_array_equal(np.round(z1.get_der([x]),10), np.round([[8.0*np.log(2)], [0]], 10))
            np.testing.assert_array_equal(np.round(z1.get_der([y]), 10), np.round([[0], [4.0*np.log(2)]], 10))
            

        test_add()
        test_radd()
        test_subtract()
        test_rsubtract()
        test_mul()
        test_rmul()
        test_div()
        test_rdiv()
        test_pow()
        test_rpow()



    
    def test_comparison():
        x = Var(4.0)
        y = Var(1.5)
        temp = Var(0.5)
        z = MultiFunc([x+y+y, x-y-y])
        p = MultiFunc([x+2*y, x-2*y])
        q = MultiFunc([x*2-temp, x-y-y])
            
        def test_eq():
            assert p == z
            assert p.__eq__(z)
            assert not z == q
                
            z1 = z*4.0/2.0
            p1 = p*2.0
            assert z1 == p1
        
        def test_ne():
            z1 = -z
            p1 = -p
            assert z1 == p1
            z1.get_value() == [7.0, 1.0]
            z1.get_der([x,y]) == [[1.0, 2.0], [1.0, -2.0]]
        
        '''    
        def test_less():
            assert x > y
            assert not z < y
            assert x <10.0
            assert not y <0.0
            
        def test_lesseq():
            assert x <= z
            assert not x<=y
            assert z <= 4.0
            assert y <= 10.0
            
        def test_greater():
            assert x > y
            assert not y >z
            assert x+2.0 > z
            
        def test_greatereq():
            assert x >=z 
            assert x>=y
            assert y+10.0 >= x
            assert not y >=z
        '''
        test_eq()
        test_ne()

    def test_composition():
        

        def test_1_trig():
            x = Var(np.pi)
            y = Var(np.pi/2)
            z = MultiFunc([x, y])
            f = z.apply(Var.cos)
            z1 = f.apply(Var.sin)
            np.testing.assert_array_equal(np.round(z1.get_value(),10), np.round([-0.8414709848, 0], 10))
            np.testing.assert_array_equal(np.round(z1.get_der([x,y]),10), np.round([[0, 0], [0, -1.0]], 10))  # = -sin(x)cos(cos(x)) - sin(y)cos(cos(y))
            np.testing.assert_array_equal(np.round(z1.get_der([x]), 10), np.round([[0], [0]], 10))
            assert z1.get_der([y]) == [[0], [-1.0]]
        
        def test_2():
            x = Var(1.0)
            y = Var(2.0)
            z = MultiFunc([x, y])  
            z1 = z**2+2
            assert z1.get_value() == [3.0, 6.0]    
            assert z1.get_der([x,y]) == [[2.0,0], [0, 4.0]]
            assert z1.get_der([x]) == [[2.0], [0]]
            assert z1.get_der([y]) == [[0], [4.0]]
              
        test_1_trig()
        test_2()


    test_overloading()
    test_comparison()
    test_composition()
    
    def suite_neg():
        x = Var(1.0)
        y = Var(2.0)
        z = Var(3.0)
        f = MultiFunc([x * y, y ** z, 3 * z])
        f1 = -f
        np.testing.assert_array_equal(f1.get_value(), np.array([-2., -8., -9.]))
        np.testing.assert_array_equal(np.round(f1.get_der([x,y,z]), 2), np.array([[-2., -1., 0.],
                                                                          [0., -12., -5.55],
                                                                          [0., 0., -3.]]))

    def suite_abs():
        x = Var(1.0)
        y = Var(2.0)
        z = Var(3.0)
        f = MultiFunc([x * y, y ** z, 3 * z])
        f1 = abs(f)
        np.testing.assert_array_equal(f1.get_value(), np.array([2., 8., 9.]))
        np.testing.assert_array_equal(np.round(f1.get_der([x, y, z]), 2), np.array([[2., 1., 0.], [0., 12., 5.55], [0., 0., 3.]]))

    def suite_sin():
        x = Var(np.pi / 2)
        y = Var(np.pi / 3)
        z = Var(np.pi / 4)
        f = MultiFunc([Var.sin(x), 2 * Var.sin(y), Var.sin(z) ** 3])
        f2 = f.apply(Var.sin)
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([1., 1.73, 0.35]))
        np.testing.assert_array_equal(np.round(f.get_der([x,y,z]), 2), np.array([[0., 0., 0.],
                                                                    [0., 1., 0.],
                                                                    [0., 0., 1.06]]))
    def suite_cos():
        x = Var(np.pi / 2)
        y = Var(np.pi / 3)
        z = Var(np.pi / 4)
        f = MultiFunc([Var.cos(x), 2 * Var.cos(y), Var.cos(z) ** 3])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([0., 1., 0.35]))
        np.testing.assert_array_equal(np.round(f.get_der([x,y,z]), 2), np.array([[-1., 0., 0.],
                                                                    [0., -1.73, 0.],
                                                                    [0., 0., -1.06]]))

    def suite_tan():
        x = Var(np.pi / 3)
        y = Var(np.pi / 4)
        z = Var(np.pi / 6)
        f = MultiFunc([Var.tan(x), 2 * Var.tan(y), Var.tan(z) ** 3])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([1.73, 2., 0.19]))
        np.testing.assert_array_equal(np.round(f.get_der([x,y,z]), 2), np.array([[4., 0., 0.],
                                                                    [0., 4., 0.],
                                                                    [0., 0., 1.33]]))
    def suite_arcsin():
        with np.testing.assert_raises(ValueError):
            x = Var(np.pi / 3)
            y = Var(np.pi / 4)
            z = Var(np.pi / 6)
            f = MultiFunc([Var.arcsin(x), 2 * Var.arcsin(y), Var.arcsin(z) ** 3 + 1])

        with np.testing.assert_raises(ZeroDivisionError):
            x = Var(0)
            y = Var(1)
            z = Var(-1)
            f = MultiFunc([Var.arcsin(x), 2 * Var.arcsin(y), Var.arcsin(z) ** 3 + 1])

        x = Var(0)
        y = Var(0.6)
        f = MultiFunc([Var.arcsin(x), 3 * Var.arcsin(y)])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([0, 1.93]))
        np.testing.assert_array_equal(np.round(f.get_der([x,y]), 2), np.array([[1., 0.],
                                                                    [0., 3.75]]))

    def suite_arccos():
        with np.testing.assert_raises(ValueError):
            x = Var(np.pi / 3)
            y = Var(np.pi / 4)
            z = Var(np.pi / 6)
            f = MultiFunc([Var.arcsin(x), 2 * Var.arcsin(y), Var.arcsin(z) ** 3 + 1])

        with np.testing.assert_raises(ZeroDivisionError):
            x = Var(0)
            y = Var(1)
            z = Var(-1)
            f = MultiFunc([Var.arccos(x), 2 * Var.arccos(y), Var.arccos(z) ** 3 + 1])

        x = Var(0)
        y = Var(0.6)
        f = MultiFunc([Var.arccos(x), 3 * Var.arccos(y)])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([1.57, 2.78]))
        np.testing.assert_array_equal(np.round(f.get_der([x,y]), 2), np.array([[-1., 0.],
                                                                    [0., -3.75]]))

    def suite_arctan():
        x = Var(np.pi / 3)
        y = Var(np.pi / 4)
        z = Var(np.pi / 6)
        f = MultiFunc([Var.arctan(x), 2 * Var.arctan(y), Var.arctan(y) ** 3 + 1])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([0.81, 1.33, 1.3]))
        np.testing.assert_array_equal(np.round(f.get_der([x,y,z]), 2), np.array([[0.48, 0., 0.],
                                                                    [0., 1.24, 0.],
                                                                    [0., 0.82, 0.]]))
    def suite_sinh():
        x = Var(2)
        y = Var(3)
        f = MultiFunc([Var.sinh(x) ** 2, 2 * Var.sinh(y), Var.sinh(x) * Var.sinh(y)])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([13.15, 20.04, 36.33]))
        np.testing.assert_array_equal(np.round(f.get_der([x,y]), 2), np.array([[27.29, 0.], [0., 20.14], [37.69, 36.51]]))

    def suite_cosh():
        x = Var(2)
        y = Var(3)
        f = MultiFunc([Var.cosh(x) ** 2, 2 * Var.cosh(y), Var.cosh(x) * Var.cosh(y)])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([14.15, 20.14, 37.88]))
        np.testing.assert_array_equal(np.round(f.get_der([x,y]), 2), np.array([[27.29, 0.], [0., 20.04], [36.51, 37.69]]))

    def suite_tanh():
        x = Var(2)
        y = Var(3)
        f = MultiFunc([Var.tanh(x) ** 2, 2 * Var.tanh(y), Var.tanh(x) * Var.tanh(y)])
        np.testing.assert_array_equal(np.round(f.get_value(), 2), np.array([0.93, 1.99, 0.96]))
        np.testing.assert_array_equal(np.round(f.get_der([x,y]), 2), np.array([[0.14, 0.], [0., 0.02], [0.07, 0.01]]))

    def suite_sqrt():
        x = Var(3.0)
        y = Var(1.0)
        f = MultiFunc([x ** 3, 2 * y, x * y])
        f1 = f.apply(Var.sqrt)
        np.testing.assert_array_equal(np.round(f1.get_value(), 2), np.array([5.2, 1.41, 1.73]))
        np.testing.assert_array_equal(np.round(f1.get_der([x,y]), 2), np.array([[2.6, 0.],
                                                                          [0., 0.71],
                                                                          [0.29, 0.87]]))

        # derivative of 0^x does not exist if x < 1
        with np.testing.assert_raises(ZeroDivisionError):
            x = Var(0.0)
            f = MultiFunc([x, 3 * x])
            f1 = f.apply(Var.sqrt)

    def suite_log():
        x = Var(3.0)
        y = Var(1.0)
        f = MultiFunc([x + 2, 3 * y, x ** y])
        f1 = f.apply(Var.log, 10)
        np.testing.assert_array_equal(np.round(f1.get_value(), 2), np.array([0.7, 0.48, 0.48]))
        np.testing.assert_array_equal(np.round(f1.get_der([x,y]), 2), np.array([[0.09, 0.], [0., 0.43], [0.14, 0.48]]))
        # not defined for |x| < 0
        with np.testing.assert_raises(ValueError):
            f2 = MultiFunc([-x, 3 * y, x ** y])
            f3 = f2.apply(Var.log, 2)

    def suite_exp():
        x = Var(3.0)
        y = Var(1.0)
        f = MultiFunc([x + 2, 3 * y, x ** y])
        f1 = f.apply(Var.exp)
        np.testing.assert_array_equal(np.round(f1.get_value(), 2), np.array([148.41, 20.09, 20.09]))
        np.testing.assert_array_equal(np.round(f1.get_der([x,y]), 2), np.array([[148.41, 0.],
                                                                     [0., 60.26],
                                                                     [20.09, 66.2]]))

    def suite_logistic():
        x = Var(2.0)
        y = Var(3.0)
        f = MultiFunc([x + 2, 3 * y, x ** y])
        f1 = f.apply(Var.logistic)
        np.testing.assert_array_equal(np.around(f1.get_value(), 3), np.array([0.982, 1., 1.]))
        np.testing.assert_array_equal(np.around(f1.get_der([x,y]), 3), np.array([[0.018, 0.000],
                                                                      [0.000, 0.000],
                                                                      [0.004, 0.002]]))
    suite_neg()
    suite_abs()
    suite_sin()
    suite_cos()
    suite_tan()
    suite_arcsin()
    suite_arccos()
    suite_arctan()
    suite_sinh()
    suite_cosh()
    suite_tanh()
    suite_sqrt()
    suite_log()
    suite_exp()
    suite_logistic()

test_constructor()
test_scalar_input_scalar_output()
test_multivariate_input_scalar_output()
test_scalar_input_vector_output()
test_vector_input_vector_output()
