// Charger une image Landsat
var image = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')
  .filterDate('2023-01-01', '2023-12-31')
  .filterBounds(roi)
  .median()
  .clip(roi);

// Sélection des bandes
var bands = ['B2', 'B3', 'B4', 'B5']; // Bleu, vert, rouge, NIR
var inputImage = image.select(bands);

// Points d'entraînement
var trainingPoints = roi.sample({
  scale: 30,
  numPixels: 500
});

// Classifier SVM
var svm = ee.Classifier.libsvm({
  kernelType: 'RBF',
  gamma: 0.5,
  cost: 10
}).train({
  features: trainingPoints,
  classProperty: 'landcover',
  inputProperties: bands
});

// Classification
var classified = inputImage.classify(svm);
Map.addLayer(classified, {min: 0, max: 4, palette: ['red', 'green', 'blue', 'yellow']}, 'SVM Classification');
