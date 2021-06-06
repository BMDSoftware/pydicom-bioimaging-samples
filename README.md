# pydicom biomedical examples

This repository only contains a few examples of use `pydicom` to handle some DICOM files. 

## Requirements 

- Python3
- pip 
- python3-venv
- DICOM samples (this repository does not supply any DICOM file samples)


## How to use?

If you would like to use virtual env, run the following commands:

```
python3 -m venv dicomenv # this creates your enviroment 
source dicomenv/bin/activate # this activate your enviroment
```

Now, all dependencies that you install will be located in `dicomenv` directory. Try to install them:

```
pip3 install -r requirements.txt
```


To run examples, you can try the follow command line executions. 

```
python3 wsi_sample.py
```

```
python3 lsm_sample.py
```




