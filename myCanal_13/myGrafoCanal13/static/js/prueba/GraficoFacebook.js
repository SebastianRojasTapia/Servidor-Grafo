
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

  const getDataFromColumns = async (network) => {
  	const data = await getData();
  	const dataNetwork = data.filter(d => d['Network'] == network);
  	const dataPicked = dataNetwork.map(d => (({Date, Likes, "Love Reactions":Love , "Haha Reactions":Divertido , "Wow Reactions":Wow , "Sad Reactions":Sad , "Angry Reactions":Angry , Engagements, Post ,Shares, Impressions}) => ({Date, Likes, Love, Divertido, Wow, Sad, Angry, Engagements, Post,Shares, Impressions}))(d));
    return dataPicked;
  };
  //Crear un selecto general para modificar la fecha para todos v.1
  const getGraphMegusta = async (data) => {
    
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
      vl.color().fieldQ('Engagements').scale({range :['blue', '#fb6900', 'green']}),
      vl.size().fieldQ('Engagements').scale({range : [30, 1000]}),
      vl.tooltip([
        x,
        vl.fieldN('Engagements'),
        vl.fieldN('Post'),
        vl.fieldN('Shares'),
        vl.fieldN('Impressions'),
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

  const getGraphLove = async (data) => {
    
    const x = vl.x().fieldT('Date').title(null);
    const y = vl.y().fieldQ('Love');
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
        vl.fieldN('Shares'),
        vl.fieldN('Impressions'),
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

  const getGraphHaha = async (data) => {
    
    const x = vl.x().fieldT('Date').title(null);
    const y = vl.y().fieldQ('Divertido');
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
      vl.color().fieldQ('Engagements').scale({range :['yellow', '#fb6900', 'green']}),
      vl.size().fieldQ('Engagements').scale({range : [30, 1000]}),
      vl.tooltip([
        x,
        vl.fieldN('Engagements'),
        vl.fieldN('Post'),
        vl.fieldN('Shares'),
        vl.fieldN('Impressions'),
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

  const getGraphWow = async (data) => {
    
    const x = vl.x().fieldT('Date').title(null);
    const y = vl.y().fieldQ('Wow');
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
        vl.fieldN('Shares'),
        vl.fieldN('Impressions'),
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

  const getGraphSad = async (data) => {
    
    const x = vl.x().fieldT('Date').title(null);
    const y = vl.y().fieldQ('Sad');
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
        vl.fieldN('Shares'),
        vl.fieldN('Impressions'),
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

  const getGraphAngry = async (data) => {
    
    const x = vl.x().fieldT('Date').title(null);
    const y = vl.y().fieldQ('Angry');
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
        vl.fieldN('Shares'),
        vl.fieldN('Impressions'),
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
    // data
    const facebook = await getDataFromColumns('Facebook');
    const graphMegusta = await getGraphMegusta(facebook);
    const graphLove = await getGraphLove(facebook);
    const graphHaha = await getGraphHaha(facebook);
    const graphWow = await getGraphWow(facebook);
    const graphSad = await getGraphSad(facebook);
    const graphAngry = await getGraphAngry(facebook);
    
  	document.getElementById("grafico-megusta").appendChild(await graphMegusta.render());
    document.getElementById("grafico-love").appendChild(await graphLove.render());
    document.getElementById("grafico-Medivierte").appendChild(await graphHaha.render());
    document.getElementById("grafico-Wow").appendChild(await graphWow.render());
    document.getElementById("grafico-Sad").appendChild(await graphSad.render());
    document.getElementById("grafico-Angry").appendChild(await graphAngry.render());
  };

  run();

}(d3, vega, vegaLite, vl, vegaTooltip));
