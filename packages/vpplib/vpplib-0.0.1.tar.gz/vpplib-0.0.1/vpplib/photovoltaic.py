# -*- coding: utf-8 -*-
"""
Info
----
This file contains the basic functionalities of the Photovoltaic class.

"""

from .component import Component

import pandas as pd

# pvlib imports
import pvlib

from pvlib.pvsystem import PVSystem
from pvlib.location import Location
from pvlib.modelchain import ModelChain

class Photovoltaic(Component):

    def __init__(self, unit, identifier, environment=None,
                 user_profile=None, cost=None,
                 module_lib='SandiaMod',
                 module='Canadian_Solar_CS5P_220M___2009_',
                 inverter_lib='cecinverter',
                 inverter='ABB__MICRO_0_25_I_OUTD_US_208_208V__CEC_2014_',
                 surface_tilt=20, surface_azimuth=200,
                 modules_per_string=1, strings_per_inverter=1):
        """
        Info
        ----
        ...
        
        Parameters
        ----------
        
        ...
        	
        Attributes
        ----------
        
        ...
        
        Notes
        -----
        
        ...
        
        References
        ----------
        
        ...
        
        Returns
        -------
        
        ...
        
        """

        # Call to super class
        super(Photovoltaic, self).__init__(unit, environment, user_profile, cost)
    
    
        # Configure attributes
        self.identifier = identifier

        self.limit = 1.0
        
        # load some module and inverter specifications
        sandia_modules = pvlib.pvsystem.retrieve_sam(module_lib)
        cec_inverters = pvlib.pvsystem.retrieve_sam(inverter_lib)
        
        self.module = sandia_modules[module]
        self.inverter = cec_inverters[inverter]

        self.location = Location(latitude=self.user_profile.latitude, 
                                 longitude=self.user_profile.longitude)
        
        self.system = PVSystem(surface_tilt=surface_tilt, 
                               surface_azimuth=surface_azimuth,
                               module_parameters=self.module,
                               inverter_parameters=self.inverter,
                               modules_per_string=modules_per_string,
                               strings_per_inverter=strings_per_inverter)
        
        self.modelchain = ModelChain(self.system, self.location, 
                                     name=identifier)
        
        self.peak_power = (self.module.Impo * self.module.Vmpo/1000 * 
                           self.system.modules_per_string * 
                           self.system.strings_per_inverter)
        
        self.timeseries = None

    def prepare_time_series(self):
        
        if len(self.environment.pv_data) == 0:
            raise ValueError("self.environment.pv_data is empty.")
            
        self.modelchain.run_model(
                times=self.environment.pv_data.loc[
                        self.environment.start:self.environment.end].index, 
                weather=self.environment.pv_data.loc[
                        self.environment.start:self.environment.end])
        
        timeseries = pd.DataFrame(self.modelchain.ac/1000)  # convert to kW
        timeseries.rename(columns={0: self.identifier}, inplace=True)
        timeseries.set_index(timeseries.index, inplace=True)
        timeseries.index = pd.to_datetime(timeseries.index)
        
        self.timeseries = timeseries
        
        return timeseries

    def reset_time_series(self):
        
        self.timeseries = None
        
        return self.timeseries
		
		
    # ===================================================================================
    # Controlling functions
    # ===================================================================================

    # This function limits the power of the photovoltaic to the given percentage.
    # It cuts the current power production down to the peak power multiplied by
    # the limit (Float [0;1]).
    def limit_power_to(self, limit):

        # Validate input parameter
        if 0 <= limit <= 1:

            # Parameter is valid
            self.limit = limit

        else:

            # Parameter is invalid

            raise ValueError("Limit-parameter is not valid")
        

    # ===================================================================================
    # Balancing Functions
    # ===================================================================================

    # Override balancing function from super class.
    def value_for_timestamp(self, timestamp):
        
        if type(timestamp) == int:
            
            return self.timeseries[self.identifier].iloc[timestamp] * self.limit
        
        elif type(timestamp) == str:
            
            return self.timeseries[self.identifier].loc[timestamp] * self.limit
        
        else:
            raise ValueError("timestamp needs to be of type int or string. "+
                             "Stringformat: YYYY-MM-DD hh:mm:ss")
            

    def observations_for_timestamp(self, timestamp):
        
        """
        Info
        ----
        This function takes a timestamp as the parameter and returns a 
        dictionary with key (String) value (Any) pairs. 
        Depending on the type of component, different status parameters of the 
        respective component can be queried. 
        
        For example, a power store can report its "State of Charge".
        Returns an empty dictionary since this function needs to be 
        implemented by child classes.
        
        Parameters
        ----------
        
        ...
        	
        Attributes
        ----------
        
        ...
        
        Notes
        -----
        
        ...
        
        References
        ----------
        
        ...
        
        Returns
        -------
        
        ...
        
        """
        if type(timestamp) == int:
            
            el_generation = self.timeseries.iloc[timestamp]
        
        elif type(timestamp) == str:
            
            el_generation = self.timeseries.loc[timestamp]
        
        else:
            raise ValueError("timestamp needs to be of type int or string. "+
                             "Stringformat: YYYY-MM-DD hh:mm:ss")
        
        
        observations = {'el_generation': el_generation}
        
        return observations