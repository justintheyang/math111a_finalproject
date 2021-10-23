# math111a_finalproject
Final project for Math 111A, asking the question: can we use the similarity structure of our written language to model the spatial relationships of everyday objects in our environment?

`preprocess_data.ipynb`: reads in the `.mat` file from the [NYU Depth Dataset V2](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html), and processes the data into relevant `.npy` and `.csv` files. Creates the following files within `data/`:
- `depth_arr.npy`: A (N, W, H) numpy array of depth clouds for each image in the sample.
- `image_arr.npy`: A (N, W, H, 3) numpy array representing the RGB values of each image.
- `label_arr.npy`: A (N, W, H) numpy array of object category labels, for each WxH pixel on the screen.
- `instance_arr.npy`: A (N, W, H) numpy array of instance labels, for each WxH pixel on the screen.
- `metadata.csv`: contains metadata for each image, including the image's scene ID, scene type, unique semantic labels, and unique instances.

