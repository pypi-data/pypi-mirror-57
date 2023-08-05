import unittest
from pyapprox.density import *
import numpy as np

def helper_gradient(function,gradient,sample,
                  eps=np.sqrt(np.finfo(float).eps)):
    """
    Test the analytical (adjoint) gradient of a function using finite
    differences.

    This function uses forward finite difference and so assumes sample
    is more than eps away from any bounds of the function variables.

    Parameters
    ----------
    function : callable function
        Vector-valued function f(x) that for a single sample returns
        a (num_qoi x 1) vector

    gradient : callable function
        Jacobian of the vector-valued function that for a single sample
        returns a (num_dims x num_qoi) matrix.

    sample : (num_dims x 1) vector
        A sample of the function variables x

    eps : float
        The finite difference step size

    Returns
    -------
    """
    value = function(sample)
    num_dims = sample.shape[0]
    num_qoi = value.shape[0]
    grad = np.empty((num_dims,num_qoi),float)
    for i in range(num_dims):
        perturbed_sample = sample.copy()
        perturbed_sample[i] += eps
        perturbed_value = function(perturbed_sample)
        grad[i,:] = (perturbed_value-value)/eps
    assert np.allclose(gradient(sample).squeeze(),grad.squeeze(),atol=eps*10)

class TestNormalDensity(unittest.TestCase):
    def test_normal_density_pdf(self):
        num_dims = 20
        mu = 0*np.ones((num_dims)); sigma2 = 1.
        density = NormalDensity(mu,covariance=sigma2)

        from scipy.stats import multivariate_normal
        sample = np.zeros((num_dims),float)
        assert np.allclose(multivariate_normal.pdf(sample,mu,sigma2),
                              density.pdf(sample))

        sample = np.random.normal(0.,1.,(num_dims))
        assert np.allclose(multivariate_normal.pdf(sample,mu,sigma2),
                              density.pdf(sample))

    def test_normal_density_grad(self):
        num_dims = 20
        mu = 0*np.ones((num_dims)); sigma2 = 1.
        density = NormalDensity(mu,covariance=sigma2)

        sample = np.random.normal(0.,1.,(num_dims))
        helper_gradient(density.pdf,density.gradient,sample)

    def test_normal_density_neg_log_pdf(self):
        num_dims = 20
        mu = 0*np.ones((num_dims)); sigma2 = 1.
        density = NormalDensity(mu,covariance=sigma2)

        sample = np.random.normal(0.,1.,(num_dims))
        assert np.allclose(
            np.log(density.pdf(sample)),density.log_pdf(sample))

        num_dims = 20; sigma2 = 0.25
        mu = 0*np.ones((num_dims)); covariance = np.eye(num_dims)*sigma2
        density = NormalDensity(mu,covariance=covariance)

        sample = np.random.normal(0.,sigma2,(num_dims))
        assert np.allclose(
            np.log(density.pdf(sample)),density.log_pdf(sample))

    def test_normal_density_neg_log_pdf_grad(self):
        num_dims = 20
        mu = 0*np.ones((num_dims)); sigma2 = 1.
        density = NormalDensity(mu,covariance=sigma2)

        sample = np.random.normal(0.,1.,(num_dims))
        helper_gradient(density.log_pdf,density.log_pdf_gradient,sample)

        num_dims = 20; sigma2 = 0.25
        mu = 0*np.ones((num_dims)); covariance = np.eye(num_dims)*sigma2
        density = NormalDensity(mu,covariance=covariance)

        sample = np.random.normal(0.,sigma2,(num_dims))
        helper_gradient(density.log_pdf,density.log_pdf_gradient,sample)

    def test_map_gaussian_samples_to_canonical_domain(self):
        num_dims = 3;
        num_samples = 10000
        mean = np.ones((num_dims),float)
        A = np.random.normal(0.,1.,(num_dims,num_dims))
        covariance = np.dot(A.T,A)
        density = NormalDensity(mean=mean,covariance=covariance)

        canonical_samples = np.random.normal(
            0.,1.,(num_dims,num_samples))
        samples = map_from_canonical_gaussian(
            canonical_samples, density.mean, density.chol_factor)
        assert np.allclose(np.mean(samples,axis=1),mean,rtol=1e-1)
        new_samples = map_to_canonical_gaussian(
            samples, density.mean, density.chol_factor)
        assert np.allclose(new_samples,canonical_samples)

class TestUniformDensity(unittest.TestCase):
    def test_uniform_density_pdf(self):
        num_dims = 3
        ranges = np.ones(2*num_dims); ranges[::2]=-1.
        density = UniformDensity(ranges)

        sample = density.generate_samples(1)[:,0]
        assert np.allclose(1./8., density.pdf(sample))

    def test_uniform_density_grad(self):
        num_dims = 3
        ranges = np.ones(2*num_dims); ranges[::2]=-1.
        density = UniformDensity(ranges)

        sample = density.generate_samples(1)[:,0]
        helper_gradient(density.pdf,density.gradient,sample)

    def test_uniform_density_neg_log_pdf(self):
        num_dims = 3
        ranges = np.ones(2*num_dims); ranges[::2]=-1.
        density = UniformDensity(ranges)

        sample = density.generate_samples(1)[:,0]
        assert np.allclose(
            np.log(density.pdf(sample)),density.log_pdf(sample))

    def test_uniform_density_neg_log_pdf_grad(self):
        num_dims = 3
        ranges = np.ones(2*num_dims); ranges[::2]=-1.
        density = UniformDensity(ranges)

        sample = density.generate_samples(1)[:,0]
        helper_gradient(density.log_pdf,density.log_pdf_gradient,sample)

class TestCoulaDensities(unittest.TestCase):
    def test_multivariate_student_t_density_1d(self):
        from scipy.stats import t as student_t_rv

        mean=np.zeros(1)
        covariance=np.eye(1)
        df = 1
        lb,ub = student_t_rv.ppf([0.01,0.99],df)
        samples = np.linspace(lb,ub,100)
        true_vals = student_t_rv.pdf(samples,df,mean[0],covariance[0,0])
        vals = multivariate_student_t_density(
            samples[np.newaxis,:],mean,covariance,df)
        assert np.allclose(vals,true_vals)

        mean=np.zeros(1)
        covariance=np.eye(1)
        df = 100
        lb,ub = student_t_rv.ppf([0.01,0.99],df)
        samples = np.linspace(lb,ub,100)
        true_vals = student_t_rv.pdf(samples,df,mean[0],covariance[0,0])
        vals = multivariate_student_t_density(
            samples[np.newaxis,:],mean,covariance,df)
        assert np.allclose(vals,true_vals)

        mean=np.array([2])
        covariance=3*np.eye(1)
        df = 10
        lb,ub = student_t_rv.ppf([0.01,0.99],df)
        samples = np.linspace(lb,ub,100)
        true_vals = student_t_rv.pdf(samples,df,mean[0],np.sqrt(covariance[0,0]))
        vals = multivariate_student_t_density(
            samples[np.newaxis,:],mean,covariance,df)
        assert np.allclose(vals,true_vals)


if __name__ == '__main__':
    unittest.main()
