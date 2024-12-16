// Charger une image Sentinel-2
var image = ee.ImageCollection('COPERNICUS/S2')
  .filterDate('2023-01-01', '2023-12-31')
  .filterBounds(roi)
  .median()
  .clip(roi);

// Export de données pour analyse hors GEE
Export.table.toDrive({
  collection: image.sample({
    region: roi,
    scale: 10,
    numPixels: 500
  }),
  description: 'ExportDataForDeepLearning',
  fileFormat: 'CSV'
});
