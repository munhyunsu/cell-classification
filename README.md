# cell-classification
Cell classification using transfer learning of Tensorflow


## Transfer learning with TF Hub


## Requirements
- Python 3 pip library
```bash
pip3 install -r requirements.txt
```


## TODO
- Object segmentation: (Ref: )

## Cell image segmentation

### Create Visual Object Classes(VOC) Datasets

#### Requirements
- labelme

```
git clone LABELME_GITHUB.git
```

#### Make VOC dataset

```
python3 ./examples/semantic_segmentation/labelme2voc.py INPUT OUTPUT --labels labels.txt
```
