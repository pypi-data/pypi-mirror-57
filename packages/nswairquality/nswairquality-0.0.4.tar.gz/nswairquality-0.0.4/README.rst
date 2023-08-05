====================
NSW Air Quality Data
====================
Retrieves current data from the `NSW Air Quality Monitoring Network <https://datasets.seed.nsw.gov.au/dataset/air-quality-monitoring-network2b91e>`_ and returns a consumable object, or JSON.

*******
Example
*******

.. code-block:: python

    import nswairquality
    
    if __name__ == "__main__":
        x = nswairquality.NSWAirQuality()
        print(x.toJSON(True))
 
****
Note
****
This is not an authorised or approved method of access the data.

© State Government of NSW and Department of Planning, Industry and Environment 1994