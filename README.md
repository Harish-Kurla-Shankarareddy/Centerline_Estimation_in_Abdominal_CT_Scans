# Centerline_Estimation_in_Abdominal_CT_Scans

In order to create computer-aided diagnosis systems using computed tomography (CT) images, colon segmentation is a crucial step. This information can be used by the surgeon to plan any necessary treatments and to guide themselves throughout the procedure. The centerline without branches is an essential tool for safe and precise medical procedures because it provides a reliable and effective means of navigation through the colon.      
![image](https://github.com/Harish-Kurla-Shankarareddy/Centerline_Estimation_in_Abdominal_CT_Scans/assets/75476784/b04d8418-727d-46f7-b34c-0c9ebbc6cf71)


Centerline Estimation:


1) Skeletonization process is performed on segmented colon image using “skimage.morphology.skeletonize3d()”  that returns a thinned image with branch like structures shown in Figure 2a.

2) The skeletonized image is converted into a graph with nodes and edges, where the end of each branch is represented as a node (black points). The centerlines between two consecutive nodes are plotted with different colours.

3) A graph search is performed to find all the possible paths in the graph. The longest path is then selected thus eliminating undesired branches, as seen in Figure 2b.

4) Further path smoothing techniques Savitzky-Golay Filter and Piecewise Cubic Hermite Interpolator are used in order to obtain a smooth and continuous centerline as seen in Figure 2c.

   
![image](https://github.com/Harish-Kurla-Shankarareddy/Centerline_Estimation_in_Abdominal_CT_Scans/assets/75476784/dc27d168-4847-4938-b56c-13192995b6d3)
![Figure](https://github.com/Harish-Kurla-Shankarareddy/Centerline_Estimation_in_Abdominal_CT_Scans/assets/75476784/6bc09cd0-c197-48d6-82ee-ef970c8f7fec)





