"""Full References:
https://github.com/microsoft/AIforEarthDataSets#noaa-high-resolution-rapid-refresh-hrrr
https://github.com/microsoft/AIforEarthDataSets/blob/main/data/noaa-hrrr.md
https://nbviewer.org/github/microsoft/AIforEarthDataSets/blob/main/data/noaa-hrrr.ipynb
"""

# Import necessary libraries
import requests
import tempfile
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cmocean
import os
from matplotlib.ticker import FuncFormatter


class NOMADS:

    @staticmethod
    def get_NOMADS_url_idx(day, cycle, forecast_hour):
        """
        Fetches the URL and index for NOMADS data for the specified day, cycle, and forecast hour.
        """
        blob_container = "https://noaahrrr.blob.core.windows.net/hrrr"
        sector = "conus"
        product = "wrfsfcf"  # 2D surface levels

        file_path = f"hrrr.t{cycle:02}z.{product}{forecast_hour:02}.grib2"
        url = f"{blob_container}/hrrr.{day:%Y%m%d}/{sector}/{file_path}"
        r = requests.get(f"{url}.idx")
        idx = r.text.splitlines()

        return url, r, idx

    @staticmethod
    def download_data(idx, search_string, url):
        """
        Downloads data from the given URL based on the specified index and search string.
        """
        # Extract index information for the given search string
        target_idx = [l for l in idx if search_string in l][0].split(":")

        # Determine the byte range
        line_num = int(target_idx[0])
        range_start = target_idx[1]
        next_line = idx[line_num].split(':') if line_num < len(idx) else None
        range_end = next_line[1] if next_line else None

        # print(f"Downloading data for {search_string} in byte range: {range_start}-{range_end}")

        # Download data
        file = tempfile.NamedTemporaryFile(prefix="tmp_", delete=False)
        headers = {"Range": f"bytes={range_start}-{range_end}"}
        resp = requests.get(url, headers=headers, stream=True)

        with file as f:
            f.write(resp.content)

        return file.name

    @staticmethod
    def save_weather_img(xarr_temp, xarr_ghi, xarr_rh, xarr_va, day, cycle, forecast_hour, save_path):
        """
        Plots and saves weather data from xarray datasets.
        """
        # Assuming attrs are same or similar for all datasets
        attrs = xarr_temp.t2m.attrs
        assert attrs['GRIB_gridType'] == 'lambert'

        # Define the CRS with attributes from the temperature DataArray
        prj_kwargs = dict(
            globe=ccrs.Globe(ellipse='sphere'),
            central_latitude=attrs['GRIB_LaDInDegrees'],
            central_longitude=attrs['GRIB_LoVInDegrees'],
            standard_parallels=(attrs['GRIB_Latin1InDegrees'], attrs['GRIB_Latin2InDegrees'])
        )
        prj = ccrs.LambertConformal(**prj_kwargs)

        # Define common plot kwargs
        plt_kwargs = dict(x='longitude', y='latitude', cmap=cmocean.cm.thermal, transform=ccrs.PlateCarree(),
                          add_colorbar=False)

        def format_func(value, tick_number):
            formatted_value = f"{value:03.0f}"
            if formatted_value.startswith('00'):
                return '  ' + formatted_value[2:]  # Replace the first two '00' with spaces
            elif formatted_value.startswith('0'):
                return ' ' + formatted_value[1:]  # Replace the first '0' with a space if only one '0' is present
            return formatted_value

        # Create a 2x2 subplot
        fig, axs = plt.subplots(2, 2, figsize=(15, 8), subplot_kw={'projection': prj})
        fig.suptitle(f"HRRR Forecasts {day} {cycle + forecast_hour:02}:00 UTC", fontsize=16)

        # Plot Temperature and add colorbar
        im_temp = xarr_temp.t2m.plot(ax=axs[0, 0], **plt_kwargs)
        cbar_temp = fig.colorbar(im_temp, ax=axs[0, 0], format=FuncFormatter(format_func))
        cbar_temp.set_label('Temperature')
        axs[0, 0].set_title('Temperature')
        axs[0, 0].coastlines(linewidth=0.5)
        axs[0, 0].add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5)

        # Plot Global Horizontal Irradiance
        im_ghi = xarr_ghi.dswrf.plot(ax=axs[0, 1], **plt_kwargs)
        cbar_ghi = plt.colorbar(im_ghi, ax=axs[0, 1], format=FuncFormatter(format_func))
        cbar_ghi.set_label('Global Horizontal Irradiance')
        axs[0, 1].set_title('Global Horizontal Irradiance')
        axs[0, 1].coastlines(linewidth=0.5)
        axs[0, 1].add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5)

        # Plot Relative Humidity
        im_rh = xarr_rh.r2.plot(ax=axs[1, 0], **plt_kwargs)
        cbar_rh = plt.colorbar(im_rh, ax=axs[1, 0], format=FuncFormatter(format_func))
        cbar_rh.set_label('Relative Humidity')
        axs[1, 0].set_title('Relative Humidity')
        axs[1, 0].coastlines(linewidth=0.5)
        axs[1, 0].add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5)

        # Plot Wind Velocity
        im_va = xarr_va.si10.plot(ax=axs[1, 1], **plt_kwargs)
        cbar_va = plt.colorbar(im_va, ax=axs[1, 1], format=FuncFormatter(format_func))
        cbar_va.set_label('Wind Velocity')
        axs[1, 1].set_title('Wind Velocity')
        axs[1, 1].coastlines(linewidth=0.5)
        axs[1, 1].add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5)

        # Save the plot
        plt.savefig(save_path, dpi=500, bbox_inches='tight', transparent=True)


    def plot_and_save_weather_img(xarr_temp, xarr_ghi, xarr_rh, xarr_va, day, cycle, forecast_hour, save_path):
        """
        Plots and saves weather data from xarray datasets.
        """
        # Assuming attrs are same or similar for all datasets
        attrs = xarr_temp.t2m.attrs
        assert attrs['GRIB_gridType'] == 'lambert'

        # Define the CRS with attributes from the temperature DataArray
        prj_kwargs = dict(
            globe=ccrs.Globe(ellipse='sphere'),
            central_latitude=attrs['GRIB_LaDInDegrees'],
            central_longitude=attrs['GRIB_LoVInDegrees'],
            standard_parallels=(attrs['GRIB_Latin1InDegrees'], attrs['GRIB_Latin2InDegrees'])
        )
        prj = ccrs.LambertConformal(**prj_kwargs)

        # Define common plot kwargs
        plt_kwargs = dict(x='longitude', y='latitude', cmap=cmocean.cm.thermal, transform=ccrs.PlateCarree(),
                          add_colorbar=False)

        def format_func(value, tick_number):
            formatted_value = f"{value:03.0f}"
            if formatted_value.startswith('00'):
                return '  ' + formatted_value[2:]  # Replace the first two '00' with spaces
            elif formatted_value.startswith('0'):
                return ' ' + formatted_value[1:]  # Replace the first '0' with a space if only one '0' is present
            return formatted_value

        # Create a 2x2 subplot
        fig, axs = plt.subplots(2, 2, figsize=(15, 8), subplot_kw={'projection': prj})
        fig.suptitle(f"HRRR Forecasts {day} {cycle + forecast_hour:02}:00 UTC", fontsize=16)

        # Plot Temperature and add colorbar
        im_temp = xarr_temp.t2m.plot(ax=axs[0, 0], **plt_kwargs)
        cbar_temp = fig.colorbar(im_temp, ax=axs[0, 0], format=FuncFormatter(format_func))
        cbar_temp.set_label('Temperature')
        axs[0, 0].set_title('Temperature')
        axs[0, 0].coastlines(linewidth=0.5)
        axs[0, 0].add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5)

        # Plot Global Horizontal Irradiance
        im_ghi = xarr_ghi.dswrf.plot(ax=axs[0, 1], **plt_kwargs)
        cbar_ghi = plt.colorbar(im_ghi, ax=axs[0, 1], format=FuncFormatter(format_func))
        cbar_ghi.set_label('Global Horizontal Irradiance')
        axs[0, 1].set_title('Global Horizontal Irradiance')
        axs[0, 1].coastlines(linewidth=0.5)
        axs[0, 1].add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5)

        # Plot Relative Humidity
        im_rh = xarr_rh.r2.plot(ax=axs[1, 0], **plt_kwargs)
        cbar_rh = plt.colorbar(im_rh, ax=axs[1, 0], format=FuncFormatter(format_func))
        cbar_rh.set_label('Relative Humidity')
        axs[1, 0].set_title('Relative Humidity')
        axs[1, 0].coastlines(linewidth=0.5)
        axs[1, 0].add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5)

        # Plot Wind Velocity
        im_va = xarr_va.si10.plot(ax=axs[1, 1], **plt_kwargs)
        cbar_va = plt.colorbar(im_va, ax=axs[1, 1], format=FuncFormatter(format_func))
        cbar_va.set_label('Wind Velocity')
        axs[1, 1].set_title('Wind Velocity')
        axs[1, 1].coastlines(linewidth=0.5)
        axs[1, 1].add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5)

        # Save the plot
        plt.savefig(save_path, dpi=500, bbox_inches='tight', transparent=True)

        # Show the plot
        plt.show()


    def save_xarray_to_netcdf(xarray_dataset, variable_name, day, cycle, forecast_hour, save_path):
        """
        Save an xarray dataset to a NetCDF file with a specific naming convention.

        Args:
            xarray_dataset (xarray.Dataset): The xarray dataset to save.
            variable_name (str): Name of the variable to include in the file name.
            day (datetime.date): Date for the file naming.
            cycle (int): Cycle value for the file naming.
            forecast_hour (int): Forecast hour value for the file naming.
            folder_path (str): Path to the folder where the files will be saved.
        """
        # Ensure the folder exists
        os.makedirs(save_path, exist_ok=True)

        # Define the file name
        file_name = f'{variable_name}_{day}_{cycle + forecast_hour}.nc'

        # Construct the full file path
        file_path = os.path.join(save_path, file_name)

        # Save the xarray dataset to the NetCDF file
        xarray_dataset.to_netcdf(file_path)