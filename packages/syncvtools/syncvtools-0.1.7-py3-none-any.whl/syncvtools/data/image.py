import numpy as np
import syncvtools.utils.file_tools as ft
import os, logging
from typing import Any
import syncvtools.config as synconfig

class ImgSize:
    def __init__(self, width: int, height: int, channels: int = None):
        self.width = width
        self.height = height
        self.channels = channels

    def as_tuple(self):
        if self.channels is not None:
            return self.width, self.height, self.channels
        else:
            return self.width, self.height





class Image:
    def __init__(self, img_np: np.ndarray, img_filename = None, img_src = None):
        #TODO need to be immutable
        self._img_np = img_np
        self.img_filename = img_filename
        self.img_src = img_src
        self._img_size = None
        if img_np is not None:
            self._img_size = ImgSize(width=self.img_np.shape[1], height=self.img_np.shape[0], channels=self.img_np.shape[2])

    def size(self):
        return self.img_np.shape

    @property
    def img_size(self):
        if not self._img_size:
            self._img_size = ImgSize(width=self.img_np.shape[1], height=self.img_np.shape[0], channels=self.img_np.shape[2])
        return self._img_size



    @property
    def img_np(self):
        if self._img_np is None:
            img_np = ft.img_np_from_disk(self.img_src)
            self._img_size = ImgSize(width=img_np.shape[1], height=img_np.shape[0],
                                    channels=img_np.shape[2])
            return img_np
        return self._img_np

    @img_np.setter
    def img_np(self, img_np):
        assert img_np is not None
        self._img_np = img_np
        self._img_size = ImgSize(width=img_np.shape[1], height=img_np.shape[0],
                                 channels=img_np.shape[2])

    @staticmethod
    def from_src(file_src, lazy = False):
        if not os.path.exists((file_src)):
            raise ValueError("File doesn't exist: {}".format(file_src))
        file_size = os.path.getsize(file_src)
        if file_size == 0:
            raise ValueError("Empty file size: {}".format(file_src))
        if lazy:
            img_np = None
        else:
            img_np = ft.img_np_from_disk(file_src)
        return Image(img_np=img_np, img_filename=os.path.basename(file_src), img_src=file_src)

    @staticmethod
    def from_numpy(img_np: np.ndarray, file_name: str = None, file_src=None):
        if img_np.dtype != np.uint8:
            raise ValueError("Image should be uint8! Given: {}".format(img_np.dtype))
        if img_np is None:
            raise ValueError("None value is provided instead of numpy array")
        if len(img_np.shape) != 3:
            raise ValueError("Image shape should be always 3. Given: {}".format(img_np.shape))
        img = Image(img_np=img_np, img_filename=file_name, img_src=file_src)
        return img


# def image_from_numpy(img_np: np.ndarray, file_name: str = None, file_src=None) -> Image:
#     if img_np.dtype != np.uint8:
#         raise ValueError("Image should be uint8! Given: {}".format(img_np.dtype))
#     if img_np is None:
#         raise ValueError("None value is provided instead of numpy array")
#     if len(img_np.shape) != 3:
#         raise ValueError("Image shape should be always 3. Given: {}".format(img_np.shape))
#     img = Image(img_np=img_np, img_filename=file_name, img_src=file_src)
#     return img

# def img_read_from_disk(file_src: str, lazy = False) -> Image:
#     '''
#     Read image from disk to Image object.
#     :param file_src:
#     :return:
#     '''
#     if not os.path.exists((file_src)):
#         raise ValueError("File doesn't exist: {}".format(file_src))
#
#     file_size = os.path.getsize(file_src)
#     if file_size == 0:
#         raise ValueError("Empty file size: {}".format(file_src))
#
#     if lazy:
#         img_np = None
#     else:
#         img_np = ft.img_np_from_disk(file_src)
#
#     img = image_from_numpy(img_np, file_name=os.path.basename(file_src), file_src=file_src)
#     return img

def imgs_read_from_dir(img_dir: Any, lazy = False, types = ('jpg','png','jpeg','bmp','tif')) -> dict:
    '''
    Read images into dict of Image objects (img_name => Image obj) from given directory
    :param img_dir: str with path to directory or list/tuple of paths
    :param types: tuple of valid extensions (no dot)
    :return: Dictionary with key: image name without extension (common key in our data), value: Image
    '''

    imgs_src = []
    img_dirs = []
    if isinstance(img_dir, str):
        img_dirs.append(img_dir)
    elif isinstance(img_dir, list) or isinstance(img_dir, tuple):
        img_dirs += list(img_dir)

    for i in range(len(img_dirs)):
        if not os.path.isdir(img_dirs[i]):
            storage_path = os.path.join(synconfig.ANNOTATION_DIR, img_dirs[i])
            if os.path.isdir(storage_path):
                img_dirs[i] = storage_path
            else:
                raise ValueError("Inp dir doesn't exist: {} or {}".format(img_dirs[i], storage_path))
        imgs_src += ft.get_file_list_by_ext(dir=img_dirs[i], ext=types, recursive=True)






    result_dict = {}
    for img_src in imgs_src:
        try:
            img = Image.from_src(file_src = img_src, lazy = lazy)
        except Exception as e:
            logging.warning("Image can't be read: {}. Msg: {}".format(img_src, str(e)))
            continue
        file_name = ft.dataset_filename_to_key(img_src)
        result_dict[file_name] = img
    return result_dict