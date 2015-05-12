var personal_data = [
  {
    className: 'personal', // optional can be used for styling
    axes: [
      {axis: "agile", value: 3, yOffset: 10},
      {axis: "javascript", value: 3},
      {axis: "HTML", value: 5},
      {axis: "CSS", value: 4},
      {axis: "Python", value: 1},
      {axis: "User needs", value: 2, xOffset: -20}
    ]
  }
];
var peer_data = [
  {
    className: 'peer',
    axes: [
      {axis: "agile", value: 5}, 
      {axis: "javascript", value: 3}, 
      {axis: "HTML", value: 1},  
      {axis: "CSS", value: 4},
      {axis: "Python", value: 2},
      {axis: "User needs", value: 1}
    ]
  }
];

var renderRadarChart = function(data, selector, config) {
  var chart = RadarChart.chart();
  chart.config(config);

  var svg = d3.select(selector).append('svg')
    .attr('width', config.w)
    .attr('height', config.h);

    svg.append('g').classed('focus', 1).datum(data).call(chart);
};

var config = {
    w: 450,
    h: 300
};

// render personal results
renderRadarChart(personal_data, ".results__personal", config);
// render peer results
renderRadarChart(peer_data, ".results__peer", config);