import os
import random
import unittest

import numpy as np
import SimpleITK as sitk

from random import uniform
from numpy.random import rand, randint

import pydeform
import _stk as stk

# Use a known, random seed for each assert when
# testing with random data.
def _set_seed():
    seed = int.from_bytes(os.urandom(4), byteorder="big")
    np.random.seed(seed)
    random.seed(seed)
    return seed


def _gauss3(size=(200, 200, 200), mu=(100, 100, 100), sigma=20, gamma=1):
    x = np.linspace(0, size[2], size[2])
    y = np.linspace(0, size[1], size[1])
    z = np.linspace(0, size[0], size[0])
    x, y, z = np.meshgrid(x, y, z, indexing='ij', sparse=True)
    return gamma * np.exp(-((x-mu[2])/sigma)**2 - ((y-mu[1])/sigma)**2 - ((z-mu[0])/sigma)**2)


def _show(image, origin=(0, 0, 0), spacing=(1, 1, 1), direction=(1, 0, 0, 0, 1, 0, 0, 0, 1)):
    image = sitk.GetImageFromArray(image)
    image.SetOrigin(origin)
    image.SetSpacing(spacing)
    image.SetDirection(direction)
    sitk.Show(image)


def _jaccard(a, b):
    return np.sum(np.logical_and(a, b)) / np.sum(np.logical_or(a, b))


def _transform(img,
               d,
               fixed_origin=(0, 0, 0),
               fixed_spacing=(1, 1, 1),
               fixed_direction=(1, 0, 0, 0, 1, 0, 0, 0, 1),
               moving_origin=(0, 0, 0),
               moving_spacing=(1, 1, 1),
               moving_direction=(1, 0, 0, 0, 1, 0, 0, 0, 1),
               interpolator=sitk.sitkLinear
               ):
    img = sitk.GetImageFromArray(img)
    img.SetOrigin(moving_origin)
    img.SetSpacing(moving_spacing)
    img.SetDirection(moving_direction)

    d = sitk.GetImageFromArray(d)
    d.SetOrigin(fixed_origin)
    d.SetSpacing(fixed_spacing)
    d.SetDirection(fixed_direction)

    warp = sitk.WarpImageFilter()
    warp.SetOutputParameteresFromImage(d)
    warp.SetInterpolator(interpolator)
    res = warp.Execute(img, d)

    return sitk.GetArrayFromImage(res)


class Test_API(unittest.TestCase):

    def test_register(self):

        with self.assertRaises(RuntimeError):
            pydeform.register(None, None)

        fixed = rand(10, 10, 10)
        with self.assertRaises(RuntimeError):
            pydeform.register(fixed, None)

        moving = rand(10, 10, 10)
        with self.assertRaises(RuntimeError):
            pydeform.register(None, moving)

        fixed = rand(10, 10, 10)
        moving = [fixed, fixed]
        with self.assertRaises(ValueError):
            pydeform.register(fixed, moving)

        moving = rand(10, 10, 10)
        fixed = [moving, moving]
        with self.assertRaises(ValueError):
            pydeform.register(fixed, moving)

        fixed = (_gauss3(size=(40, 50, 60), mu=(20, 25, 30), sigma=8) > 0.3).astype(np.float32)
        moving = (_gauss3(size=(40, 50, 60), mu=(30, 20, 25), sigma=8) > 0.3).astype(np.float32)

        settings = {
            'regularization_weight': 0.05,
        }

        d = pydeform.register(fixed, moving, settings=settings)

        res = _transform(moving, np.array(d), interpolator=sitk.sitkNearestNeighbor)

        self.assertGreater(_jaccard(res > 0.1, fixed > 0.1), 0.97)

    def test_transform(self):
        for _ in range(100):
            seed = _set_seed()

            # Generate some random image data
            pad = 5
            fixed_origin = [uniform(-5, 5) for i in range(3)]
            fixed_spacing = [uniform(0.1, 5) for i in range(3)]
            moving_origin = [uniform(-5, 5) for i in range(3)]
            moving_spacing = [uniform(0.1, 5) for i in range(3)]
            shape_no_pad = [randint(50, 80) for i in range(3)]
            img = np.pad(rand(*shape_no_pad), pad, 'constant')
            d = 5 * (2.0 * rand(*shape_no_pad, 3) - 1.0)
            d = np.pad(d, 3 * [(pad, pad)] + [(0, 0)], 'constant')

            # SimpleITK oracle
            res_sitk = _transform(img,
                                  d,
                                  fixed_origin=fixed_origin,
                                  fixed_spacing=fixed_spacing,
                                  moving_origin=moving_origin,
                                  moving_spacing=moving_spacing,
                                  interpolator=sitk.sitkLinear,
                                  )

            # Compute transform
            res = pydeform.transform(stk.Volume(img, origin=moving_origin, spacing=moving_spacing),
                                     stk.Volume(d, origin=fixed_origin, spacing=fixed_spacing),
                                     interpolator=pydeform.Interpolator.Linear,
                                     )

            np.testing.assert_almost_equal(np.array(res), res_sitk, decimal=4,
                                           err_msg='Mismatch between `transform` and sitk, seed %d' % seed)

    def test_jacobian(self):
        for _ in range(100):
            seed = _set_seed()

            # Generate some random image data
            pad = 1
            origin = [uniform(-5, 5) for i in range(3)]
            spacing = [uniform(0.1, 5) for i in range(3)]
            shape_no_pad = [randint(50, 80) for i in range(3)]
            d = 5 * (2.0 * rand(*shape_no_pad, 3) - 1.0)
            d = np.pad(d, 3 * [(pad, pad)] + [(0, 0)], 'constant')

            # SimpleITK oracle
            d_sitk = sitk.GetImageFromArray(d)
            d_sitk.SetOrigin(origin)
            d_sitk.SetSpacing(spacing)
            jacobian_sitk = sitk.DisplacementFieldJacobianDeterminant(d_sitk)
            jacobian_sitk = sitk.GetArrayFromImage(jacobian_sitk)

            # Compute Jacobian
            jacobian = pydeform.jacobian(stk.Volume(d, origin=origin, spacing=spacing))

            np.testing.assert_almost_equal(np.array(jacobian), jacobian_sitk, decimal=2,
                                           err_msg='Mismatch between `jacobian` and sitk, seed %d' % seed)


    def test_regularize(self):
        df = stk.Volume(rand(10,10,10,3).astype(np.float32))
        full_mask = stk.Volume(np.ones((10,10,10)).astype(np.uint8))

        out = pydeform.regularize(df)
        self.assertFalse(np.array_equal(np.array(out) , np.array(df)))

        # Should fully replicate constraint values
        constraints = stk.Volume(rand(10,10,10,3).astype(np.float32))
        out = pydeform.regularize(df, constraint_mask=full_mask, constraint_values=constraints)
        np.testing.assert_equal(np.array(out), np.array(constraints))


    def test_affine(self):
        # Test affine initialization

        affine_transform = pydeform.AffineTransform(
            np.array((
                (2, 0, 0),
                (0, 3, 0),
                (0, 0, 4)
            )),
            np.array((10, 10, 10))
        )

        # Do a registration pass without actual iterations to see if affine transform is
        # applied to the resulting displacement field
        settings = {
            'max_iteration_count': 0
        }

        fixed = pydeform.Volume(np.zeros((10,10,10), dtype=np.float32))
        moving = pydeform.Volume(np.zeros((10,10,10), dtype=np.float32))

        df = pydeform.register(
            fixed,
            moving,
            settings=settings,
            affine_transform=affine_transform
        )

        df = np.array(df, copy=False)

        # Ax + b -> A(1, 1, 1) + b -> (2, 3, 4) + (10, 10, 10) -> (12, 13, 14)
        # u(x) = Ax + b - x
        self.assertEqual(df[1,1,1,0], 11)
        self.assertEqual(df[1,1,1,1], 12)
        self.assertEqual(df[1,1,1,2], 13)

    def test_read_affine(self):
        affine_str = \
            "#Insight Transform File V1.0\n" \
            "#Transform 0\n" \
            "Transform: AffineTransform_double_3_3\n" \
            "Parameters: 1 2 3 4 5 6 7 8 9 10 11 12\n" \
            "FixedParameters: 13 14 15\n"

        with open('affine_test.txt', 'w') as f:
            f.write(affine_str)

        affine_transform = pydeform.read_affine_transform('affine_test.txt')

        np.testing.assert_equal(affine_transform.matrix,
            np.array((1,2,3,4,5,6,7,8,9)).reshape((3,3)))
        
        # offset = translation + fixed - matrix * fixed
        np.testing.assert_equal(affine_transform.offset, np.array((-63, -187, -311)))
        
        with self.assertRaises(ValueError):
            pydeform.read_affine_transform('doesnotexist.txt')



if __name__ == '__main__':
    unittest.main()

