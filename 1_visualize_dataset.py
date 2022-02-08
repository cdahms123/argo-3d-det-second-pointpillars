# 0_visualize_dataset.py

from argoverse.data_loading.argoverse_tracking_loader import ArgoverseTrackingLoader
from argoverse.data_loading.object_label_record import ObjectLabelRecord

import plotly.graph_objects as PlotlyGraphObjects
import pprint
from typing import List

ROOT_DIR = '/home/cdahms/argoverse-tracking/sample'

TRIP_INDEX = 0
LIDAR_FRAME_INDEX = 0

SHOW_PLOTLY_MOUSEOVERS = False

def main():
    argoverseLoader = ArgoverseTrackingLoader(ROOT_DIR)
    tripData = argoverseLoader[TRIP_INDEX]
    lidarPoints = tripData.get_lidar(LIDAR_FRAME_INDEX)

    print('\n' + 'lidarPoints: ')
    pprint.pprint(lidarPoints)

    lidarPoints = lidarPoints.transpose()

    objectLabelRecords: List[ObjectLabelRecord] = tripData.get_label_object(LIDAR_FRAME_INDEX)

    ### 3D visualization ############################################

    s3dPoints = PlotlyGraphObjects.Scatter3d(x=lidarPoints[0], y=lidarPoints[1], z=lidarPoints[2], mode='markers', marker={'size': 1})

    # 3 separate lists for the x, y, and z components of each line
    predXLines = []
    predYLines = []
    predZLines = []
    for objLabelRec in objectLabelRecords:
        corners = objLabelRec.as_3d_bbox()

        # see here for documentation of ObjectLabelRecord:
        # https://github.com/argoai/argoverse-api/blob/master/argoverse/data_loading/object_label_record.py

        # 4 lines for front surface of box
        addLineToPlotlyLines(corners[0], corners[1], predXLines, predYLines, predZLines)
        addLineToPlotlyLines(corners[1], corners[2], predXLines, predYLines, predZLines)
        addLineToPlotlyLines(corners[2], corners[3], predXLines, predYLines, predZLines)
        addLineToPlotlyLines(corners[3], corners[0], predXLines, predYLines, predZLines)

        # 4 lines between front points and rear points
        addLineToPlotlyLines(corners[0], corners[4], predXLines, predYLines, predZLines)
        addLineToPlotlyLines(corners[1], corners[5], predXLines, predYLines, predZLines)
        addLineToPlotlyLines(corners[2], corners[6], predXLines, predYLines, predZLines)
        addLineToPlotlyLines(corners[3], corners[7], predXLines, predYLines, predZLines)

        # 4 lines for rear surface of box
        addLineToPlotlyLines(corners[4], corners[7], predXLines, predYLines, predZLines)
        addLineToPlotlyLines(corners[5], corners[4], predXLines, predYLines, predZLines)
        addLineToPlotlyLines(corners[6], corners[5], predXLines, predYLines, predZLines)
        addLineToPlotlyLines(corners[7], corners[6], predXLines, predYLines, predZLines)

    # end for

    s3dPredBoxLines = PlotlyGraphObjects.Scatter3d(x=predXLines, y=predYLines, z=predZLines, mode='lines')

    # make and show a plotly Figure object
    plotlyFig = PlotlyGraphObjects.Figure(data=[s3dPoints, s3dPredBoxLines])
    plotlyFig.update_layout(scene_aspectmode='data')

    if not SHOW_PLOTLY_MOUSEOVERS:
        plotlyFig.update_layout(hovermode=False)
        plotlyFig.update_layout(scene=dict(xaxis_showspikes=False,
                                           yaxis_showspikes=False,
                                           zaxis_showspikes=False))
    # end if

    plotlyFig.show()
# end function

def addLineToPlotlyLines(point1, point2, xLines: List, yLines: List, zLines: List) -> None:
    xLines.append(point1[0])
    xLines.append(point2[0])
    xLines.append(None)

    yLines.append(point1[1])
    yLines.append(point2[1])
    yLines.append(None)

    zLines.append(point1[2])
    zLines.append(point2[2])
    zLines.append(None)
# end function

if __name__ == '__main__':
    main()



