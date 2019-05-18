Download at: https://drive.google.com/drive/folders/1o_q1-rMoASCFZjqWO8L4zyqIU8t4DlEL

To ensure reproducibility, follow this folder structure:

Input
    ├─Facility X
    |    ├─Sample A
    |    |    ├─Day 1
    |    |    |    ├─Class 1
    |    |    |    |    ├─Cell_1_Ch_1.TIF
    |    |    |    |    ├─Cell_1_Ch_2.TIF
    |    |    |    |    ├─Cell_1_Ch_3.TIF
    |    |    |    |    ├─Cell_2_Ch_1.TIF
    |    |    |    |    ├─Cell_2_Ch_2.TIF
    |    |    |    |    └─Cell_2_Ch_3.TIF
    |    |    |    ├─Class 2
    |    |    |    |    ├─Cell_1_Ch_1.TIF
    |    |    |    |    ├─Cell_1_Ch_2.TIF
    |    |    |    |    ├─Cell_1_Ch_3.TIF
    |    |    |    |    ├─Cell_2_Ch_1.TIF
    |    |    |    |    ├─Cell_2_Ch_2.TIF
    |    |    |    |    └─Cell_2_Ch_3.TIF	
...



Expected output structure:

Output
    ├─Facility X
    |    ├─Sample A
    |    |    ├─Day 1
    |    |    |    ├─Class 1
    |    |    |    |    ├─Cell_1.NPY
    |    |    |    |    ├─Cell_2.NPY
    |    |    |    |    ├─Cell_3.NPY   
    |    |    |    ├─Class 2
    |    |    |    |    ├─Cell_1.NPY
    |    |    |    |    ├─Cell_2.NPY
...