
## Plot Temperature vs Resistance

Before running the script, use the following command to install some python packages.

```
# Install locally
$ pip install -r requirements.txt
# Activate conda and install in conda environment
$ conda create -n ppms python=3.11
$ conda activate ppms
$ conda install --yes --file requirements.txt 
```

Now you should be able to run the following script in each directory.

```
python analysis.py
```

## User configuration

The file path and sample information are configured in data.yaml in the yaml directory.

## Sample information

- 2024-10-22

First measurement using PPMS in Uji campus.
Measured three bilayer samples (Nb + Al) with different thickness combinations.

- 2024-12-26

Measured two bilayer samples (Nb + Al) and simple layer sample (Nb).
However, the third channel was disconnected during the measurement.