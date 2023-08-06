# Organic Navigation Reference Data

The purpose of the `onvadata` module is to make reference data sets easily accessible for the design, development, and testing of navigation algorithms.  The defining characteristic of reference data sets are that they are well understood, documented, and purged of data logging artifacts.

## Quick Start

### List Data Available
All data sets are referenced using their shortname.
```python
>> import onavdata
>> onavdata.print_shortnames()
	 2011 UMN-UAV GPSFASER1
	 2012 UMN-UAV FASER5
	 2012 UMN-UAV GPSFASER3
	 2012 UMN-UAV THOR79
	 2012 UMN-UAV THOR77
	 2012 UMN-UAV THOR75
	 2012 UMN-UAV THOR60
	 SIM-PERFECT-CAR NORTH VARY-SPEED FIXED-HEADING
	 SIM-MEASURED-CAR NORTH VARY-SPEED FIXED-HEADING
	 SIM-PERFECT-CAR NORTH VARY-SPEED VARY-HEADING
	 SIM-MEASURED-CAR NORTH VARY-SPEED VARY-HEADING
	 SIM-PERFECT-CAR NORTH FIXED-SPEED VARY-HEADING
	 SIM-MEASURED-CAR NORTH FIXED-SPEED VARY-HEADING
	 SIM-PERFECT-CAR NORTH FIXED-SPEED FIXED-HEADING
	 SIM-MEASURED-CAR NORTH FIXED-SPEED FIXED-HEADING
```

### Load a Reference Data Set
An abitrary data set can be loaded if no shortname is specified.  In this case the data from `2014 UMN-UAV THOR77` was returned.
```python
>> import onavdata
>> df = onavdata.get_data()
	get_data(): No shortname specified so choice will be arbitrary.  Returning: 2014 UMN-UAV THOR77
>> df.head()
		           AccelX (m/s^2)  AccelY (m/s^2)  AccelZ (m/s^2)       ...         AngleHeading (rad)  AnglePitch (rad)  AngleRoll (rad)
	TimeFromStart (s)                                                       ...
	0.00                     1.862795       -0.392167       -9.673463       ...                   1.004700          0.192806         0.006130
	0.02                     1.895476       -0.424848       -9.640783       ...                   1.004225          0.192856         0.006130
	0.04                     1.895476       -0.359487       -9.706145       ...                   1.003786          0.192888         0.006259
	0.06                     1.895476       -0.392167       -9.640783       ...                   1.003258          0.192990         0.006354
	0.08                     1.895476       -0.392167       -9.640783       ...                   1.002907          0.193056         0.006482

	[5 rows x 12 columns]
```

This module manages easy access to multiple navigation-sensor data sets.

## Meta Data Supported

### Sampling Time

TODO

### Rename Data Columns

TODO

### Transformation from sensor-frame to body-frame

Transformation matrices can be defined under the table heading `[Rsensor2body]`.  The subsequent key/value pairs will define the prefix of the sensor column followed by the rotation matrix.  Since the transformation is applied AFTER any column renaming (see above), the renamed column entires must be used.

#### Example
![docs/map-chip-to-body.png](docs/map-chip-to-body.png)
The above transformation can be defined for the accelerometer columns.  Assuming our accelerometer columns are:

	['AccelX (m/s^2)', 'AccelY (m/s^2)', 'AccelZ (m/s^2)']

We define the following associated meta data entry:
```
[Rsensor2body]
Accel = [[ 0, -1,  0], 
         [-1,  0,  0],
         [ 0,  0, -1]]
```
The module will automatically find the associated columns with the `Accel` prefix and apply the defined rotation matrix.
