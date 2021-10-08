import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from operator import itemgetter

logger = logging.getLogger(__name__)
__all__ = ['Hazard_analysis']

class Hazard_analysis: #Mother class

    # Attributes
    distribution = ['norm', 'lognorm', 'beta', 'weibull_min', 't', 'expon']

    #Constructor
    def __init__(self, hazard, damage):
        self.hazard = hazard
        self.damage = damage

    # Instance variables
    def x_line(self):
        #return Instance Vector of hazard
        return np.linspace(np.min(self.hazard), np.max(self.hazard), len(self.hazard))

    def __results(self):
        #Results Storage
        self.pdf_all = []
        self.pdf_mag = {}
        self.cdf_all = []
        self.cdf_mag = {}
        self.intensity_all = []
        self.intensity_mag = {}

    def __model_results(self):
        #Model Parameter, stats eval
        self.model_fit = {}
        self.parameter = {}
        self.aic = {}
        self.loglik = {}

    #Method
    def _parameter_estimate(self):
        pass

    def _fit_distribution(self):
        pass

    def _evaluate_stat(self):
        pass

