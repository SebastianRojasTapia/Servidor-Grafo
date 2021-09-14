import vl from 'vega-lite-api';

export const circles = vl
  .markPoint({ size: 300, opacity: 0.5 })
  .encode(
    vl.x().fieldT('Date').timeUnit('daymonth'),
    vl.y().fieldN('Network'),
    vl.color().fieldN('Sentiment'),
    vl.size().fieldQ('Likes').scale({domain: [250, 300]}),
    vl.tooltip().fieldQ('Likes')
  );

export const circles2 = vl
  .markCircle({
    //fill: true,
    stroke: true,
    //size: 10,
    opacity: 0.4
  })
  .encode(
    vl.x().fieldT('Date').timeUnit("date"),
    vl.y().fieldN('Network'),
    vl.size().fieldQ('Likes').scale({domain: [0 , 300]}),
    vl.color().fieldN('Sentiment'),
    vl.tooltip().fieldT('Date').timeUnit('date')
  );