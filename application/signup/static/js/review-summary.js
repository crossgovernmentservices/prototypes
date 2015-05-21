var personal_data = [
  {
    className: 'personal', // optional can be used for styling
    axes: [
      {axis: "agile", value: 5, yOffset: 10},
      {axis: "javascript", value: 3},
      {axis: "HTML", value: 4},
      {axis: "CSS", value: 4},
      {axis: "Problem solving", value: 3, xOffset: 25},
      {axis: "User needs", value: 1, xOffset: 15},
      {axis: "Open source", value: 3}
    ]
  }
];
var peer_data = [
  {
    className: 'peer',
    axes: [
      {axis: "agile", value: 5}, 
      {axis: "javascript", value: 3}, 
      {axis: "HTML", value: 5},  
      {axis: "CSS", value: 4},
      {axis: "Problem solving", value: 3, xOffset: 25},
      {axis: "User needs", value: 2, xOffset: 15},
      {axis: "Open source", value: 3}
    ]
  }
];

;(function($) {
  'use strict';

  var renderRadarChart = function(data, selector, config) {
    var chart = RadarChart.chart();
    chart.config(config);

    var svg = d3.select(selector).append('svg')
      .attr('width', config.w)
      .attr('height', config.h);

      svg.append('g').classed('focus', 1).datum(data).call(chart);
  };

  $(function() {
    var config = {
        w: 350,
        h: 300
    };

    // render personal results
    renderRadarChart(personal_data, ".results__personal", config);
    // render peer results
    renderRadarChart(peer_data, ".results__peer", config);
  });

}(jQuery));