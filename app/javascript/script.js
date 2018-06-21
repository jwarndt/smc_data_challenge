var chicagoLoopLocation = ol.proj.fromLonLat([-87.623177, 41.875820]);

var view = new ol.View({
  center: chicagoLoopLocation,
  zoom: 15
});

var source = new ol.source.Stamen({layer: 'terrain'})

var map = new ol.Map({
  target: 'map',
  layers: [
    new ol.layer.Tile({
      source: source
    })
  ],
  view: view
});