from typing import Tuple, Any, Union
from syncvtools.data.image import ImgSize
import numpy as np
from syncvtools.metrics.coco_eval import iou_run_norm

def normalize_bbox(bbox: Tuple[int,int,int,int], img_size: Tuple[int,int]) -> Tuple[float,float,float,float]:
    if bbox is None or len(bbox) < 4 or len(bbox) > 5:
        raise ValueError("Bbox is either None or not a tuple of size 4,5: (xmin, ymin, xmax, ymax)")

    img_size = ImgSize(width = img_size[0], height= img_size[1])
    norm_coords = (float(bbox[0] / img_size.width), float(bbox[1] / img_size.height), float(bbox[2] / img_size.width), float(bbox[3] / img_size.height))
    for coord in norm_coords:
        if coord < 0 or coord > 1:
            raise ValueError("Norm coordinates should be [0;1]: {}".format(bbox[:4]))
    return norm_coords


def denormalize_bbox(bbox: Tuple[float,float,float,float], img_size: Tuple[int,int]) -> Tuple[int,int,int,int]:
    def cl(v, mn, mx):
        return max(min(v,mx),mn)
    #just to validate width/height
    img_size = ImgSize(width=img_size[0], height=img_size[1])
    bbox = validate_norm_coords(bbox=bbox)
    abs_coords = bbox[0] * img_size.width, bbox[1] * img_size.height, bbox[2] * img_size.width, bbox[3] * img_size.height
    abs_coords = list(map(int,map(round, abs_coords)))
    abs_coords = (cl(abs_coords[0],0,img_size.width-1),
                 cl(abs_coords[1],0,img_size.height-1),
                 cl(abs_coords[2],0,img_size.width-1),
                 cl(abs_coords[3],0,img_size.height-1))
    return abs_coords


def validate_norm_coords(bbox: Tuple[float,float,float,float]):
    if bbox is None or len(bbox) != 4:
        raise ValueError("Bbox should take a tuple of float (x1,y1,x2,y2)")
    for coord in bbox[:4]:
        if coord < (0 - 1e-4) or coord > (1 + 1e-4):
            raise ValueError("Norm coordinates should be [0;1]: {}".format(bbox[:4]))
    return (max(0,bbox[0]),min(1,bbox[1]),max(0,bbox[2]),min(1,bbox[3]))


def abs_x1y1x2y2_to_abs_x1y1wh(box_coords)-> Union[list, tuple, np.ndarray]:
    '''
    converting from Synapse to MSCOCO box coordinates
    :param box_coords: x1,y1,x2,y2 abs list/tuple or np.array of shape (N,4)
    :return: abs x1,y1,w,h tuple or np.array of shape (N,4)
    '''
    if not isinstance(box_coords, np.ndarray):
        assert len(box_coords) == 4
        x1,y1,x2,y2 = box_coords[:4]
        w = x2-x1
        h = y2-y1
        if w<= 0 or h <=0:
            raise ValueError("Bounding box is not correct: {}".format(box_coords))
        return (x1,y1,w,h)
    else:
        box_coords[:,2] = box_coords[:,2] - box_coords[:,0]
        box_coords[:, 3] = box_coords[:, 3] - box_coords[:, 1]
        return box_coords

def abs_x1y1wh_to_abs_x1y1x2y2(box_coords)-> Union[list, tuple, np.ndarray]:
    '''
    converting from MSCOCO to Synapse
    :param box_coords: x1,y1,x2,y2 abs list/tuple or np.array of shape (N,4)
    :return: abs x1,y1,w,h tuple or np.array of shape (N,4)
    '''
    if not isinstance(box_coords, np.ndarray):
        assert len(box_coords) == 4
        x1,y1,w,h = box_coords[:4]
        x2 = x1 + w
        y2 = y1 + h
        return (x1,y1,x2,y2)
    else:
        box_coords[:,2] = box_coords[:,2] + box_coords[:,0]
        box_coords[:, 3] = box_coords[:, 3] + box_coords[:, 1]
        return box_coords


def bbox_vflip(bbox):
    """Flip a bounding box vertically around the x-axis. From albumentations.
    Args:
        bbox (tuple): A bounding box `(x_min, y_min, x_max, y_max)`.
        rows (int): Image rows.
        cols (int): Image cols.
    Returns:
        tuple: A bounding box `(x_min, y_min, x_max, y_max)`.
    """
    x_min, y_min, x_max, y_max = bbox[:4]
    return x_min, 1 - y_max, x_max, 1 - y_min


def bbox_hflip(bbox):
    """Flip a bounding box horizontally around the y-axis. From albumentations.
    Args:
        bbox (tuple): A bounding box `(x_min, y_min, x_max, y_max)`.
    Returns:
        tuple: A bounding box `(x_min, y_min, x_max, y_max)`.
    """
    x_min, y_min, x_max, y_max = bbox[:4]
    return 1 - x_max, y_min, 1 - x_min, y_max


def bbox_flip(bbox, d):
    """Flip a bounding box either vertically, horizontally or both depending on the value of `d`. From albumentations.
    Args:
        bbox (tuple): A bounding box `(x_min, y_min, x_max, y_max)`.
        d (int):
        rows (int): Image rows.
        cols (int): Image cols.
    Returns:
        tuple: A bounding box `(x_min, y_min, x_max, y_max)`.
    Raises:
        ValueError: if value of `d` is not 1,2,3
    """
    if d == 2:
        bbox = bbox_vflip(bbox)
    elif d == 1:
        bbox = bbox_hflip(bbox)
    elif d == 3:
        bbox = bbox_hflip(bbox)
        bbox = bbox_vflip(bbox)
    else:
        raise ValueError("Invalid d value {}. Valid values are 1,2,3".format(d))
    return bbox

def bbox_rot90(bbox, factor):
    """Rotates a bounding box by 90 degrees CCW (see np.rot90). From albumentations.
    Args:
        bbox (tuple): A bounding box (0..1) tuple (x_min, y_min, x_max, y_max).
        factor (int): Number of CCW rotations. Must be in set {0, 1, 2, 3} See np.rot90.
        rows (int): Image rows.
        cols (int): Image cols.
    Returns:
        tuple: A bounding box tuple (x_min, y_min, x_max, y_max).
    """
    if factor not in {0, 1, 2, 3}:
        raise ValueError("Parameter n must be in set {0, 1, 2, 3}")
    x_min, y_min, x_max, y_max = bbox[:4]
    if factor == 1:
        bbox = y_min, 1 - x_max, y_max, 1 - x_min
    elif factor == 2:
        bbox = 1 - x_max, 1 - y_max, 1 - x_min, 1 - y_min
    elif factor == 3:
        bbox = 1 - y_max, x_min, 1 - y_min, x_max
    return bbox


def box_fusion(boxes_list_by_model):
    '''
    :param boxes_list: (class, score, x1, y1,x2,y2)
    :return:
    '''

    def _set_avg(L_box, models_num):
        avg_np = np.empty(shape=(len(L_box), 4))
        score_np = np.empty(shape=(len(L_box)))
        for i in range(len(L_box)):
            L_box_np = np.asarray(L_box[i])
            box_set_score = L_box_np[:, 0:1]
            box_set = L_box_np[:, 1:] * box_set_score
            box_set = np.sum(box_set, axis=0)
            conf_sum = np.sum(box_set_score)
            avg_np[i] = box_set / conf_sum
            score_np[i] = conf_sum / models_num

        return avg_np, score_np

    def _add_to_L(L, boxes_per_model, models_num):
        if not boxes_per_model:
            return
        if not L:
            for box in boxes_per_model:
                L.append([list(box)])
            return
        F_np, F_score_np = _set_avg(L, models_num=models_num)
        f_inds = np.argsort(-F_score_np, kind='mergesort')

        boxes_per_model_np = np.asarray(boxes_per_model)

        boxes_np = boxes_per_model_np[:, 1:]
        scores_np = boxes_per_model_np[:, 0]
        b_inds = np.argsort(-scores_np, kind='mergesort')
        F_np_sorted = F_np[f_inds]
        boxes_np_sorted = boxes_np[b_inds]
        iou = iou_run_norm(F_np_sorted, boxes_np_sorted)
        for box_i in range(len(boxes_np_sorted)):
            f_found_index = -1
            for f_i in range(len(F_np_sorted)):
                if iou[f_i, box_i] > 0.55:
                    L[f_inds[f_i]].append([scores_np[b_inds[box_i]]] + list(boxes_np_sorted[box_i]))
                    f_found_index = f_i
                    break
            if f_found_index == -1:
                # not matched box to any prior boxes
                L.append([[scores_np[b_inds[box_i]]] + list(boxes_np_sorted[box_i])])
            else:
                iou[f_found_index, :] = 0  # don't match to this group any boxes from the same model

    if len(boxes_list_by_model) <= 1:
        return boxes_list_by_model[0]
    #
    # boxes_list = [[]] * len(dt_bboxes)
    # for model_i in range(len(dt_bboxes)):
    #     for bbox_i, bbox in enumerate(dt_bboxes[model_i]):
    #         # model_i => [class, score, x1,y1,x2,y2]
    #         boxes_list[model_i].append([dt_classes[model_i][bbox_i], dt_scores[model_i][bbox_i]] + list(
    #             dt_bboxes[model_i][bbox_i]))


    boxes_list_by_class = {}

    for model_i, model_boxes in enumerate(boxes_list_by_model):
        for box in model_boxes:
            if box[0] not in boxes_list_by_class:
                boxes_list_by_class[box[0]] = []
                for i in range(len(boxes_list_by_model)):
                    boxes_list_by_class[box[0]].append([])
            boxes_list_by_class[box[0]][model_i].append(box[1:])
    merged_boxes = []
    #scores = []
    #classes = []
    for label in boxes_list_by_class:
        L = []
        for boxex_per_model in boxes_list_by_class[label]:
            _add_to_L(L = L, boxes_per_model=boxex_per_model, models_num=len(boxes_list_by_model))
        F_np, F_score_np = _set_avg(L, models_num=len(boxes_list_by_model))
        for i in range(len(F_np)):
            #label, class, x1,y1,x2,y2
            merged_boxes.append([label, F_score_np[i]] + list(F_np[i]))
            # boxes.append(F_np[i])
            # scores.append(F_score_np[i])
            # classes.append(label)


    return merged_boxes