# 0_argo_intro.py

from argoverse.data_loading.argoverse_tracking_loader import ArgoverseTrackingLoader
from argoverse.data_loading.object_label_record import ObjectLabelRecord

import numpy as np
from typing import List

ARGOVERSE_TRACKING_TRAIN_DIR = '/home/cdahms/argoverse-tracking/train'

def main():
    # good general sources for Argoverse info:
    # https://www.argoverse.org/data.html
    # https://arxiv.org/pdf/1911.02620.pdf

    # Argoverse tracking data is divided up into 4 directories:
    # sample (1 trip)
    # test (24 trips, no ground truths provided)
    # train (65 trips)
    # val (24 trips)

    # in Argoverse, trips are called "logs"

    # Lidar frequency is 10 Hz

    argoTrainLoader = ArgoverseTrackingLoader(ARGOVERSE_TRACKING_TRAIN_DIR)

    print('\n' + 'type(argoTrainLoader): ')
    print(type(argoTrainLoader))

    print('\n' + 'len(argoTrainLoader.log_list): ')
    print(len(argoTrainLoader.log_list))

    # the ArgoverseTrackingLoader object can be indexed or iterated through

    tripData = argoTrainLoader[42]
    print('\n' + 'tripData index 42: ')
    print(tripData)
    print('\n' + 'type(tripData)')
    print(type(tripData))

    # use the current_log property to get the "log ID" (i.e. trip ID) of a tripData instance
    print('\n' + 'tripData.current_log: ')
    print(tripData.current_log)
    print('')

    print('')
    for idx, tripData in enumerate(argoTrainLoader):
        # only print the first 3
        if idx > 2: break

        print('tripData idx = ' + str(idx))
        print('tripData: ')
        print(tripData)
        print('')
    # end for

    # the result of indexing the instance of ArgoverseTrackingLoader is also an instance of ArgoverseTrackingLoader,
    # the important thing is it's the trip data

    tripData = argoTrainLoader[0]

    # tripData has a property "lidar_list" which is a list of lidar data that can be index or iterated through

    print('\n' + 'len(tripData.lidar_list): ')
    print(len(tripData.lidar_list))

    print('type(tripData.lidar_list): ')
    print(type(tripData.lidar_list))

    # it's easy to get lidar points from the lidar_list, just call get_lidar with an index

    lidarFrameIdx = 31
    lidarPoints: np.ndarray = tripData.get_lidar(lidarFrameIdx)

    print('\n' + 'type(lidarPoints): ')
    print(type(lidarPoints))
    print('lidarPoints.dtype: ')
    print(lidarPoints.dtype)
    # format of points is n cols (number of points) x 3 rows (x, y, z)  # ToDo: verify points are in x, y, z order !!!
    print('lidarPoints.shape: ')
    print(lidarPoints.shape)
    # print just the first 5 points
    print('first 5 lidar points: ')
    for i in range(lidarPoints.shape[0]):
        if i > 4: break
        print(lidarPoints[i])
    # end for

    # here is how to get ground truth data for a lidar frame

    objectLabelRecords: List[ObjectLabelRecord] = tripData.get_label_object(lidarFrameIdx)

    for idx, objLabelRec in enumerate(objectLabelRecords):
        # only print the first 3
        if idx > 2: break

        # each ObjectLabelRecord is for one annotation in the lidar frame

        # see here for more info on ObjectLabelRecord:
        # https://github.com/argoai/argoverse-api/blob/master/argoverse/data_loading/object_label_record.py

        # you can access member variables for each instance of ObjectLabelRecord, for example:
        print('\n' + 'objLabelRec idx = ' + str(idx))
        print('objLabelRec.quaternion: ')
        print(objLabelRec.quaternion)
        # see here for a list of fields available:
        # https://github.com/argoai/argoverse-api/blob/master/argoverse/data_loading/object_label_record.py#L70

        # ObjectLabelRecord also has useful functions especially this one:
        bboxCorners: np.ndarray = objLabelRec.as_3d_bbox()
        print('bboxCorners: ')
        print(bboxCorners)
        # see here for ASCII art of the returned corners:
        # https://github.com/argoai/argoverse-api/blob/master/argoverse/data_loading/object_label_record.py#L111
    # end for

    print('\n')
# end function

if __name__ == '__main__':
    main()



