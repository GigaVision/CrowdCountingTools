import math

'''
Tool to calculate 3 metrics of crowd counting results.
The crowd distribution of this crowd counting task is represented by crowd number vector. 
First, the whole image will be divided into 1x1, 4x4, 8x8 blocks. 
After that, the number of human in each block will be estimated. 
Finally, the crowd number vector is generated from the estimate human number of these blocks.

Input:
order: image division order.
et: crowd number vector predicted by model. It is a vector of size order * order.
gt: ground truth crowd number vector. It is a vector of size order * order.

Return:
3 evaluation results: mae, mse, evaluate_error
'''


def evaluate(et, gt, order):
    mae = 0.0
    mse = 0.0
    evaluate_error = 0.0
    for i in range(order):
        for j in range(order):
            mae += abs(et[i][j] - gt[i][j])
            mse += (et[i][j] - gt[i][j]) * (et[i][j] - gt[i][j])
            evaluate_error += _evaluate_error_patch(et[i][j], gt[i][j])
    mae = mae / math.pow(order, 2)
    mse = math.sqrt(mse / math.pow(order, 2))
    return mae, mse, evaluate_error


def _evaluate_error_patch(et, gt):
    # calculate error of each little box
    if abs(gt - 0) < 0.0005:
        if et > 1:
            d = 1
        else:
            d = 0
    else:
        d = min(abs(et - gt) / gt, 1)
    return d
