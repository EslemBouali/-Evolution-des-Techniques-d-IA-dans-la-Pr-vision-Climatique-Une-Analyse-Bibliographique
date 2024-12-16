// Charger une image Sentinel-2
var image = ee.ImageCollection('COPERNICUS/S2')
  .filterDate('2024-01-01', '2024-12-31')
  .filterBounds(ee.Geometry.Point([10, 35]))
  .median()
  .clip(roi);

// Sélection des bandes
var bands = ['B2', 'B3', 'B4', 'B8']; // Bleu, vert, rouge, NIR
var inputImage = image.select(bands);

// Points d'entraînement
var trainingPoints = roi.sample({
  scale: 10,
  numPixels: 500
});

// Ajouter une colonne "label" pour classification
var training = trainingPoints.randomColumn('random');
var classifier = ee.Classifier.smileRandomForest(50).train({
  features: training,
  classProperty: 'landcover',
  inputProperties: bands
});

// Classification
var classified = inputImage.classify(classifier);
Map.addLayer(classified, {min: 0, max: 4, palette: ['red', 'green', 'blue', 'yellow', 'cyan']}, 'Random Forest');
