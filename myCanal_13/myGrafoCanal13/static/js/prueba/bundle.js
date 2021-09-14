(function (d3, vega, vegaLite, vl, vegaTooltip) {
  'use strict';

  vega = vega && Object.prototype.hasOwnProperty.call(vega, 'default') ? vega['default'] : vega;
  vegaLite = vegaLite && Object.prototype.hasOwnProperty.call(vegaLite, 'default') ? vegaLite['default'] : vegaLite;
  vl = vl && Object.prototype.hasOwnProperty.call(vl, 'default') ? vl['default'] : vl;

  const csvUrl = 'https://gist.githubusercontent.com/HiImSebastian/d8fb2b8c2392308ef87a414228f39a45/raw/abc7de08559a688a4d110449aeb0353d88fb21c1/LI_concatenado.csv';
  const getData = async () => {
    const data = await d3.csv(csvUrl);
    console.log(data[0]);
    return data;
  };

  // Appearance customization to improve readability.
  // See https://vega.github.io/vega-lite/docs/
  const dark = '#3e3c38';
  const config = {
    axis: {
      domain: false,
      tickColor: 'lightGray'
    },
    style: {
      "guide-label": {
        fontSize: 15,
        fill: dark
      },
      "guide-title": {
        fontSize: 20,
        fill: dark
      }
    }
  };

  const circles = vl
    .markPoint({ opacity: 0.8 })
    .encode(
      vl.x().fieldT('Date').timeUnit('daymonth'),
      vl.y().fieldN('Network'),
      vl.color().fieldN('Sentiment'),
      vl.size().fieldQ('Likes').scale({domain: [0, 3000]}),
      vl.tooltip().fieldQ('Likes'),
    );

  const circles2 = vl
    .markCircle({
      //fill: true,
      stroke: true,
      //size: 10,
      opacity: 0.6
    })
    .encode(
      vl.x().fieldT('Date').timeUnit("date"),
      vl.y().fieldN('Network'),
      vl.size().fieldQ('Likes').scale({domain: [0 , 3000]}),
      vl.color().fieldN('Sentiment'),
      vl.tooltip().fieldT('Date').timeUnit('date')
    );

  vl.register(vega, vegaLite, {
    view: { renderer: 'canvas' },
    init: view => { view.tooltip(new vegaTooltip.Handler().call); }
  });

  const run = async () => {
    const marks = circles
      .data(await getData())
      .width(900)
      .height(500)
      .autosize({ type: 'fit', contains: 'padding' })
      .config(config);
    
  	const marks2 = circles2
      .data(await getData())
      .width(900)
      .height(500)
      .autosize({ type: 'fit', contains: 'padding' })
      .config(config);
    
    document.getElementById("grafico1").appendChild(await marks.render());
    document.getElementById("grafico2").appendChild(await marks2.render());
  };


  run();

}(d3, vega, vegaLite, vl, vegaTooltip));
