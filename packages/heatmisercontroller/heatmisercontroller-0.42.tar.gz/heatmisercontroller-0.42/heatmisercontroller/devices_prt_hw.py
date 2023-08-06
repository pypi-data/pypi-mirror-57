"""Heatmiser Device Classes

PRT-HW Thermostat classes on the Heatmiser network

Ian Horsley 2018
"""

from genericdevice import DEVICETYPES
from devices_prt_e import ThermoStatWeek, ThermoStatDay
from fields import HeatmiserFieldWater, HeatmiserFieldHotWaterDemand, HeatmiserFieldHotWaterVersion
from hm_constants import MAX_AGE_LONG, MAX_AGE_MEDIUM, MAX_AGE_USHORT
from schedule_functions import SchedulerDayWater, SchedulerWeekWater, SCH_ENT_TEMP

class ThermoStatHotWaterWeek(ThermoStatWeek):
    """Device class for thermostats with hotwater operating weekly programmode
    Heatmiser prt_hw_model."""
    is_hot_water = True
    
    def __init__(self, adaptor, devicesettings, generalsettings={}):
        self.water_schedule = None #placeholder for hot water schedule
        super(ThermoStatHotWaterWeek, self).__init__(adaptor, devicesettings, generalsettings)
        #thermostat specific
        self.version = HeatmiserFieldHotWaterVersion('version', 3, [], MAX_AGE_LONG) # override field after creation to add functitionality
    
    def _buildfields(self):
        """add to list of fields"""
        super(ThermoStatHotWaterWeek, self)._buildfields()
        self.fields.extend([
            HeatmiserFieldHotWaterDemand('hotwaterdemand', 42, [0, 2], MAX_AGE_USHORT),  # read [0=off, 1=on],  write [0=as prog, 1=override on, 2=overide off]
            HeatmiserFieldWater('wday_water', 71, [[0, 24], [0, 59]], MAX_AGE_MEDIUM),  # pairs,  on then off repeated,  hour,  min
            HeatmiserFieldWater('wend_water', 87, [[0, 24], [0, 59]], MAX_AGE_MEDIUM)
            #7day progamming
        ])

        self.water_schedule = SchedulerWeekWater()
    
    def _connect_observers(self):
        """connect obersers to fields"""
        super(ThermoStatHotWaterWeek, self)._connect_observers()
        self.wday_water.add_notifable_changed(self.water_schedule.set_raw_field)
        self.wend_water.add_notifable_changed(self.water_schedule.set_raw_field)
    
    def display_water_schedule(self):
        """Prints water schedule to stdout"""
        if not self.water_schedule is None:
            self.water_schedule.display()
            
    ### UNTESTED # last part about scheduletarget doesn't work
    def read_water_state(self):
        """Returns the current hot water control state from off to following program"""
        #does runmode affect hot water state?
        self.read_fields(['mon_water', 'tues_water', 'wed_water', 'thurs_water', 'fri_water', 'wday_water', 'wend_water'], -1)
        self.read_fields(['onoff', 'holidayhours', 'hotwaterdemand'])
        
        if self.onoff == WRITE_ONOFF_OFF:
            return self.TEMP_STATE_OFF
        elif self.holidayhours != 0:
            return self.TEMP_STATE_HOLIDAY
        else:
            self.read_field('currenttime', MAX_AGE_MEDIUM)
            
            locatimenow = self.currenttime.localtimearray()
            scheduletarget = self.water_schedule.get_current_schedule_item(locatimenow)

            if scheduletarget[SCH_ENT_TEMP] != self.hotwaterdemand:
                return self.TEMP_STATE_OVERRIDDEN
        return self.TEMP_STATE_PROGRAM
                
    def set_water_schedule(self, day, schedule):
        """Set water schedule for a single day"""
        padschedule = self.water_schedule.pad_schedule(schedule)
        for fieldname in self.water_schedule.get_entry_names(day):
            self.set_field(fieldname, padschedule)
    
class ThermoStatHotWaterDay(ThermoStatDay, ThermoStatHotWaterWeek):
    """Device class for thermostats with hotwater operating daily programmode
    Heatmiser prt_hw_model."""

    def _buildfields(self):
        """add to list of fields"""
        super(ThermoStatHotWaterDay, self)._buildfields()
        self.fields.extend([
            #7day progamming
            HeatmiserFieldWater('mon_water', 187, [[0, 24], [0, 59]], MAX_AGE_MEDIUM),
            HeatmiserFieldWater('tues_water', 203, [[0, 24], [0, 59]], MAX_AGE_MEDIUM),
            HeatmiserFieldWater('wed_water', 219, [[0, 24], [0, 59]], MAX_AGE_MEDIUM),
            HeatmiserFieldWater('thurs_water', 235, [[0, 24], [0, 59]], MAX_AGE_MEDIUM),
            HeatmiserFieldWater('fri_water', 251, [[0, 24], [0, 59]], MAX_AGE_MEDIUM),
            HeatmiserFieldWater('sat_water', 267, [[0, 24], [0, 59]], MAX_AGE_MEDIUM),
            HeatmiserFieldWater('sun_water', 283, [[0, 24], [0, 59]], MAX_AGE_MEDIUM)
        ])
        self.water_schedule = SchedulerDayWater()

    def _connect_observers(self):
        """connect obersers to fields"""
        super(ThermoStatHotWaterDay, self)._connect_observers()
        fieldnames = ['mon_water', 'tues_water', 'wed_water', 'thurs_water', 'fri_water', 'sat_water', 'sun_water']
        for fieldname in fieldnames:
            getattr(self, fieldname).add_notifable_changed(self.water_schedule.set_raw_field)

DEVICETYPES.setdefault('prt_hw_model', {'week': ThermoStatHotWaterWeek, 'day': ThermoStatHotWaterDay})
