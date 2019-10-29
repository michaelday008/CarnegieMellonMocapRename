# CarnegieMellonMocapRename
Rename the Carnegie-Melon University Mocap animations to include keywords in the file name

## Prerequisites

1. Install Python
2. Install xlrd (pip install xlrd)
3. Download all 3 parts of the Carnegie-Melon University Mocap Library From:
  * https://assetstore.unity.com/packages/3d/animations/huge-fbx-mocap-library-part-1-19991
  * https://assetstore.unity.com/packages/3d/animations/huge-fbx-mocap-library-part-2-20282
  * https://assetstore.unity.com/packages/3d/animations/huge-fbx-mocap-library-part-3-20285

## Directions

1. Open cmu-mocap-index-spreadsheet.xls in the "mocap animations" directory and delete cell B1, shifting all the cells in the column up
2. Move this script into the same directory as cmu-mocap-index-spreadsheet.xls
3. Run the script, the files will be renamed from (142/142_21.fbx) to include the description such as : 142/142_21_Singing_in_the_rain_jump.fbx