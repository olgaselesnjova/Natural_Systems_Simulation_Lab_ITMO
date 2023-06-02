import netCDF4 as nc
import os
import numpy as np


def copy_var(fixed_obj, original_obj, fixed_var, original_var=None):
    standard_vars = ['algorithm_standard_uncertainty', 'smearing_standard_uncertainty',
                     'total_standard_uncertainty', 'raw_ice_conc_values',
                     'ice_conc', 'status_flag']
    original_var = fixed_var if not original_var else original_var
    print(f'Variable to fix: {fixed_var}')
    values = original_obj[original_var][:]
    if original_var in ['nav_lat', 'nav_lon']:
        values = np.array(values)[0:125, 85:210]
    elif original_var in standard_vars:
        values = np.array(values)[:, 0:125, 85:210]
    elif original_var == 'x':
        values = np.array(values)[0:125]
    elif original_var == 'y':
        values = np.array(values)[85:210]
    fixed_obj[fixed_var][:] = values
    all_attrs = original_obj.variables[original_var].ncattrs()
    delete_attrs = ['_FillValue', 'scale_factor', 'add_offset', 'units']  # 'coordinates', 'grid_mapping'
    attrs = [x for x in all_attrs if x not in delete_attrs]
    for atr in attrs:
        try:
            value = getattr(original_obj.variables[original_var], atr)
            setattr(fixed_obj.variables[fixed_var], atr, value)
        except AttributeError:
            print(f'issue with adding attributes to {fixed_var}')
    # fixed_obj[fixed_var].coordinates = 'lat lon'


# Open original file
full_original_path = '/Users/lizzy/Documents/WORK/rosneft/plots/ice_conc_nh_ease2-250_cdr-v3p0_200601011200-reprojected.nc'
original_obj = nc.Dataset(full_original_path, 'r')

# Create new file
full_path = '/Users/lizzy/Documents/WORK/rosneft/plots/ice_conc_nh_20060101-reprojected-arctic.nc'
try:
    os.unlink(full_path)
except FileNotFoundError:
    print('Creating new file')
new_nc_obj = nc.Dataset(full_path, "w", format="NETCDF4")
new_nc_obj.close()
new_nc_obj = nc.Dataset(full_path, "a")

new_nc_obj.createDimension('time', size=None)

try:
    new_nc_obj.createDimension('bnds', original_obj.dimensions['bnds'].size)
    new_nc_obj.createVariable('time_bnds', 'f8', ('time', 'bnds'))
except Exception as e:
    print("Issue with bnds:")
    print(full_original_path)


new_nc_obj.createDimension('x', 125)
new_nc_obj.createDimension('y', 125)

# Create empty variables
new_nc_obj.createVariable('nav_lon', 'f8', ('y', 'x'))
new_nc_obj.createVariable('nav_lat', 'f8', ('y', 'x'))

variables = ['algorithm_standard_uncertainty', 'smearing_standard_uncertainty', 'total_standard_uncertainty', 'raw_ice_conc_values',
             'ice_conc']
for var in variables:
    new_nc_obj.createVariable(var, 'i4', ('time', 'y', 'x'), fill_value=-32767)

new_nc_obj.createVariable('status_flag', 'i2', ('time', 'y', 'x'), fill_value=-32768)
new_nc_obj.createVariable('time', 'f8', ('time'))


new_nc_obj.createVariable('xc', 'f8', ('x'))
new_nc_obj.createVariable('yc', 'f8', ('y'))


variables = ['algorithm_standard_uncertainty', 'smearing_standard_uncertainty',
             'total_standard_uncertainty', 'raw_ice_conc_values',
             'ice_conc', 'status_flag', 'time_bnds',
             'time', 'nav_lat', 'nav_lon']

for var in variables:
    copy_var(new_nc_obj, original_obj, var)

original_obj.close()
new_nc_obj.close()
