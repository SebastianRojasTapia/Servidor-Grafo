
(function (d3, vega, vegaLite, vl, vegaTooltip) {
  'use strict';

  vega = vega && Object.prototype.hasOwnProperty.call(vega, 'default') ? vega['default'] : vega;
  vegaLite = vegaLite && Object.prototype.hasOwnProperty.call(vegaLite, 'default') ? vegaLite['default'] : vegaLite;
  vl = vl && Object.prototype.hasOwnProperty.call(vl, 'default') ? vl['default'] : vl;

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
        fontSize: 13,
        fill: dark
      },
      "guide-title": {
        fontSize: 17,
        fill: dark
      }
    }
  };

  const csvUrl = 'https://gist.githubusercontent.com/Sebans31/9c6838ad91acf03537a75ec4ba54910e/raw/c402b5da25a0c588b804f2eceab7c43ef74e1ab3/PostPerformance.csv';

  console.log(csvUrl);
  // función para cargar el data del csv
  const getData = async () => {
    const data = await d3.csv(csvUrl);
    return data;
  };

  // subquery de data por red social
  const getDataFrom = async (network) => {
  	const data = await getData();
    console.log(data[0]);
  	return data.filter(d => d['Network'] == network);
  };

  const getDataFromColumns = async (network) => {
  	const data = await getData();
  	const dataNetwork = data.filter(d => d['Network'] == network);
  	const dataPicked = dataNetwork.map(d => (({Date, Likes, Comments , Shares , Engagements , Post,"Post Link Clicks":PostLinkClicks, "Other Post Clicks":OtroPostClicks,"Post Clicks (All)":PostClicksAll,"Video Views":VideoViews }) => ({Date, Likes,Comments,Shares, Engagements, Post,PostLinkClicks,OtroPostClicks,PostClicksAll,VideoViews}))(d));
    return dataPicked;
  };

  const getGraphLikes = async (data) => {
    const x = vl.x().fieldT('Date').title(null);
    const y = vl.y().fieldQ('Likes');
    const width = 500;
    const brush = vl.selectInterval().encodings('x');
    const selector = vl
    	.markBar({color:'#fb6900'})
    	.encode(x, y)
    	.width(width);

  	const grafico = vl
    .markCircle({ opacity: 0.5})
  	.transform(vl.filter(brush))
    .encode(
      x, y,
      vl.color().fieldQ('Engagements').scale({range :['blue', '#fb6900', 'yellow']}),
      vl.size().fieldQ('Engagements').scale({range : [30, 1000]}),
      vl.tooltip([
        x,
        vl.fieldN('Engagements'),
        vl.fieldN('Post'),
        vl.fieldN('Comments'),
        vl.fieldN('Shares'),
        vl.fieldN('PostLinkClicks'),
        vl.fieldN('OtroPostClicks'),
        vl.fieldN('PostClicksAll'),
        vl.fieldN('VideoViews'),
      ]))
    	.width(width)
      .height(width)
      .autosize({ type: 'fit', contains: 'padding' })
      .config(config);
    
  	const g = vl.data(data)
      .vconcat(
        grafico.encode( x.scale({domain: brush}) ),
        selector.select(brush).height(60),
      );
    return g;
  };
  
  const getGraphShare = async (data) => {
    const x = vl.x().fieldT('Date').title(null);
    const y = vl.y().fieldQ('Shares');
    const width = 500;
    const brush = vl.selectInterval().encodings('x');
    const selector = vl
    	.markBar({color:'#fb6900'})
    	.encode(x, y)
    	.width(width);

  	const grafico = vl
    .markCircle({ opacity: 0.5})
  	.transform(vl.filter(brush))
    .encode(
      x, y,
      vl.color().fieldQ('Engagements').scale({range :['red', '#fb6900', 'green']}),
      vl.size().fieldQ('Engagements').scale({range : [30, 1000]}),
      vl.tooltip([
        x,
        vl.fieldN('Engagements'),
        vl.fieldN('Post'),
        vl.fieldN('Likes'),
        vl.fieldN('PostLinkClicks'),
        vl.fieldN('OtroPostClicks'),
        vl.fieldN('PostClicksAll'),
        vl.fieldN('VideoViews'),
      ]))
    	.width(width)
      .height(width)
      .autosize({ type: 'fit', contains: 'padding' })
      .config(config);
    
  	const g = vl.data(data)
      .vconcat(
        grafico.encode( x.scale({domain: brush}) ),
        selector.select(brush).height(60),
      );
    return g;
  };

  vl.register(vega, vegaLite, {
    view: { renderer: 'canvas' },
    init: view => { view.tooltip(new vegaTooltip.Handler().call); }
  });

  const run = async () => {

    const twitter = await getDataFromColumns('Twitter');
    const graphLikes = await getGraphLikes(twitter);
    const graphShare = await getGraphShare(twitter);

    document.getElementById("grafico-likes").appendChild(await graphLikes.render());
    document.getElementById("grafico-Share").appendChild(await graphShare.render());
  };

  run();

}(d3, vega, vegaLite, vl, vegaTooltip));
