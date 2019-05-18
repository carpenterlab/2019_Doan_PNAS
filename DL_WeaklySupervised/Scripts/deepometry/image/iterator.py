import sys
sys.path.insert(0, '/home/paul/.conda/envs/tensorflow/lib/python3.6/site-packages')

import os

import keras.backend
import keras.preprocessing.image
import numpy
import skimage.io


class NumpyArrayIterator(keras.preprocessing.image.Iterator):
    def __init__(self, x, y, image_data_generator,
                 batch_size=32,
                 shuffle=False,
                 seed=None,
                 save_to_dir=None,
                 save_prefix="",
                 save_format="tif",
                 mixup_alpha=0.0):
        if y is not None and len(x) != len(y):
            raise ValueError(
                u"X (images tensor) and y (labels) should have the same length. "
                "Found: X.shape = {0:s}, y.shape = {1:s}".format(numpy.asarray(x).shape, numpy.asarray(y).shape)
            )

        self.x = numpy.asarray(x, dtype=keras.backend.floatx())

        if self.x.ndim != 4:
            raise ValueError(
                "Input data in `NumpyArrayIterator` should have rank 4. You passed an array with shape", self.x.shape
            )

        if y is not None:
            self.y = numpy.asarray(y)
        else:
            self.y = None

        self.image_data_generator = image_data_generator

        self.save_to_dir = save_to_dir

        self.save_prefix = save_prefix

        self.save_format = save_format

        self.mixup_alpha = mixup_alpha

        super(NumpyArrayIterator, self).__init__(x.shape[0], batch_size, shuffle, seed)

    def next(self):
        """For python 2.x.

        # Returns
            The next batch.
        """
        # Keeps under lock only the mechanism which advances the indexing of each batch.
        with self.lock:
            index_array = next(self.index_generator)

        if self.mixup_alpha == 0.0:
            return self._get_batches_of_transformed_samples(index_array)
        else:

            # The transformation of images is not under thread lock so it can be done in parallel
            batch_1 = self._get_batches_of_transformed_samples(index_array)
            batch_2 = self._get_batches_of_transformed_samples(index_array)

            # Mixup!
            lam = numpy.random.beta(self.mixup_alpha, self.mixup_alpha)
            x = (1 - lam)*batch_1[0] + lam*batch_2[0]
            y = (1 - lam)*batch_1[1] + lam*batch_2[1]

            return x,y

    def _get_batches_of_transformed_samples(self, index_array):
        batch_x = numpy.zeros(tuple([len(index_array)] + list(self.x.shape)[1:]), dtype=keras.backend.floatx())

        for i, j in enumerate(index_array):
            x = self.x[j]

            # `image_data_generator.preprocessing_function` call moved from `image_data_generator.standardize` in 2.1.5
            # Moved back to `image_data_generator.standardize` in a later release.
            if self.image_data_generator.preprocessing_function:
                x = self.image_data_generator.preprocessing_function(x)

            x = self.image_data_generator.random_transform(x.astype(keras.backend.floatx()))

            x = self.image_data_generator.standardize(x)

            batch_x[i] = x

        if self.save_to_dir:
            for i, j in enumerate(index_array):
                fname = "{prefix}_{index}_{hash}.{format}".format(
                    prefix=self.save_prefix,
                    index=j,
                    hash=numpy.random.randint(1e4),
                    format=self.save_format
                )

                img = skimage.img_as_uint(batch_x[i])

                skimage.io.imsave(os.path.join(self.save_to_dir, fname), img)

        if self.y is None:
            return batch_x

        batch_y = self.y[index_array]

        return batch_x, batch_y
