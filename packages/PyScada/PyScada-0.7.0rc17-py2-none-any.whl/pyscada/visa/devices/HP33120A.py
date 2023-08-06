# -*- coding: utf-8 -*-
from pyscada.visa.devices import GenericDevice
from pyscada.models import VariableProperty

import logging

logger = logging.getLogger(__name__)


class Handler(GenericDevice):
    """
    HP 33120A and other Devices with the same command set
    """

    def read_data(self, device_property):
        """
        read values from the device
        """
        if self.inst is None:
            logger.error("Visa-AFG1022-read data-Self.inst : None")
            return None
        if device_property == 'present_value':
            return self.parse_value(self.inst.query(':READ?'))
        else:
            value = self.inst.query(device_property)
            logger.info("Visa-read data-property : %s - value : %s" % (device_property, value))
#            return value.split(',')[0]
            return self.parse_value(value)
        return None

    def write_data(self, variable_id, value, task):
        """
        write values to the device
        """
        variable = self._variables[variable_id]
        if task.property_name != '':
            # write the freq property to VariableProperty use that for later read
            vp = VariableProperty.objects.update_or_create_property(variable=variable, name=task.property_name.upper(),
                                                                    value=value, value_class='FLOAT64')
            return True
        if variable.visavariable.variable_type == 0:  # configuration
            # only write to configuration variables
            pass
        else:
            return False

    def parse_value(self, value):
        """
        takes a string in the HP 33120A format and returns a float value or None if not parseable
        """
        try:
            return float(value)
        except:
            return None

    # AFG functions
    def afg_prepare_for_bode(self, ch=1):
        return self.inst.query(':OUTPut:LOAD MAX;:AM:STAT OFF;*OPC?;')

    def afg_set_output_state(self, ch=1, state=True):
        return False

    def afg_set_offset(self, ch=1, offset=0):
        return self.inst.query(':VOLTage:OFFSet %s' % offset)

    def afg_set_vpp(self, ch=1, vpp=1):
        return self.inst.query(':VOLT %s;:VOLT:UNIT VPP;*OPC?;' % str(vpp))

    def afg_set_function_shape(self, ch=1, function_shape=0):
        shape_list = {
            0: "SIN",
            1: "RAMP",
            2: "SQUARE",
        }
        return self.inst.query(':FUNC:SHAP %s;*OPC?;' % shape_list.get(function_shape, "SIN"))

    def afg_set_frequency(self, ch=1, frequency=1000):
        return self.inst.query(':FREQ %s;*OPC?;' % str(frequency))

    def reset_instrument(self):
        return self.inst.query('*RST;*OPC?')
