import cv2
import json

'''
Tool to visualize crowd counting ground truth annotations.
Input:
json_path: the path to json annotation files
           json format:  {
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
scale: image zoom scale
is_show: is show image with annotation or not
is_save: is save image with annotation or not
'''


def cc_visualize(json_path,
                 scale=0.5,
                 is_show=False,
                 is_save=True):
    # JSON reading
    with open(json_path, 'r') as load_f:
        load_dict = json.load(load_f)
    total_point_num = 0
    for img_path in load_dict:
        pointList = load_dict[img_path]
        print('image path: ', img_path)
        print('total number of points: ', len(pointList))
        total_point_num += len(pointList)
        # load img and resize
        img = cv2.imread(img_path)
        height, width = img.shape[:2]
        img = cv2.resize(img, (int(width * scale), int(height * scale)), interpolation=cv2.INTER_AREA)
        height, width = img.shape[:2]
        for point in pointList:
            cv2.circle(img, (int(point['x'] * width), int(point['y'] * height)),
                       radius=3, color=(0, 0, 255), thickness=-1)
        if is_show:
            cv2.imshow('img', img)
            cv2.waitKey(0)
        if is_save:
            cv2.imwrite('Pointed_' + img_path.replace('/', '_'), img, [int(cv2.IMWRITE_JPEG_QUALITY), 75])

    print('Finished! Total point number:', total_point_num)

