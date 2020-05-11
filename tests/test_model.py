#!/usr/bin/env python
import pytest
from bike_classifier_whisk_0_1_21.models.model import Model

def test_predict():
    model = Model()
    model.predict([[1,2],[3,4]])
