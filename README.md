# CrowdCountingTools
Result evaluation and annotation visualization tools for HumanNet dataset task 1 - crowd counting.
[Our website](http://www.gigavision.cn) 

## cc_evaluste_tools.py
Tool to calculate 3 evaluation results of crowd counting.
The crowd distribution of this crowd counting task is represented by crowd number vector. 
First, the whole image will be divided into 1x1, 4x4, 8x8 blocks. 
After that, the number of human in each block will be estimated. 
Finally, the crowd number vector is generated from the estimate human number of these blocks.

### Input:
order: image division order.

et: crowd number vector predicted by model. It is a vector of size order * order.

gt: ground truth crowd number vector. It is a vector of size order * order.

### Return:
3 evaluation results: mae, mse, evaluate_error.

## cc_visualize_tools.py
Tool to visualize crowd counting ground truth annotations.
### Input:
json_path: the path to json annotation files.

json format:  
```
{
   "JPG_FILE_PATH":[
       {"x": x_coordinate,
        "y": x_coordinate
       },
       {"x": x_coordinate,
        "y": x_coordinate
       },
       ...
   ],
   ...
}
```
scale: image zoom scale.

is_show: is show image with annotation or not.

is_save: is save image with annotation or not.
