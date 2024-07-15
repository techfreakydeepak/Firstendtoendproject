#!/bin/bash

echo "[`date`] START"

# Create conda environment
conda create --name env python=3.11

# Activate conda environment
conda activate env

# Install required packages
pip install -r requirements.txt

echo "[`date`] END"