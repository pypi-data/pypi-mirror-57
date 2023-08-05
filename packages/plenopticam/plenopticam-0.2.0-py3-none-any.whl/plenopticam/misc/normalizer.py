import numpy as np
from plenopticam import misc

class Normalizer(object):

    def __init__(self, img=None, min=None, max=None, dtype=None, sta=None):

        self._dtype = img.dtype.__str__() if dtype is None else dtype
        self._img = np.asarray(img, dtype='float64') if img is not None else None

        self._min = self._img.min() if min is None else min
        self._max = self._img.max() if max is None else max

        self.sta = sta if sta is not None else misc.PlenopticamStatus()

    def uint16_norm(self):
        ''' normalize image array to 16-bit unsigned integer '''

        return np.asarray(np.round(self.norm_fun()*(2**16-1)), dtype=np.uint16)

    def uint8_norm(self):
        ''' normalize image array to 8-bit unsigned integer '''

        return np.asarray(np.round(self.norm_fun()*(2**8-1)), dtype=np.uint8)

    def type_norm(self, lim_min=None, lim_max=None):
        ''' normalize numpy image array for provided data type '''

        # e.g.         # RGB image normalization
        #         #self._rgb_img = misc.type_norm(self._rgb_img, dtype='float32', lim_min=2**10, lim_max=2**16-2**10)

        if self._dtype.startswith('float'):
            lim_max = np.finfo(np.dtype(self._dtype)).max if lim_max is None else lim_max
            lim_min = np.finfo(np.dtype(self._dtype)).min if lim_min is None else lim_min
            img_norm = self.norm_fun()*(lim_max-lim_min)+lim_min

        elif self._dtype.startswith(('int', 'uint')):
            lim_max = np.iinfo(np.dtype(self._dtype)).max if lim_max is None else lim_max
            lim_min = np.iinfo(np.dtype(self._dtype)).min if lim_min is None else lim_min
            img_norm = np.round(self.norm_fun()*(lim_max-lim_min)+lim_min)

        else:
            lim_max = 1.0 if lim_max is None else lim_max
            lim_min = 0.0 if lim_min is None else lim_min
            img_norm = self.norm_fun()*(lim_max-lim_min)+lim_min

        return np.asarray(img_norm, dtype=self._dtype)

    def norm_fun(self):
        ''' normalize image to values between 1 and 0 '''

        if self.sta.interrupt:
            return False

        norm = (self._img - self._min) / (self._max - self._min) if self._max != self._min else self._img

        # prevent wrap-around
        norm[norm < 0] = 0
        norm[norm > 1] = 1

        return norm
