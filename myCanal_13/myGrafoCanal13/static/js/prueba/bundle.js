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
  let inf = window.data

  //'https://gist.githubusercontent.com/Sebans31/9c6838ad91acf03537a75ec4ba54910e/raw/c402b5da25a0c588b804f2eceab7c43ef74e1ab3/PostPerformance.csv';
  const csvUrl = inf;
  
 
  console.log("Esta es la info")
  console.log(inf)

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


  // funcion para extraer columnas
  // const extractColumn = (arr, column) => arr.map(x=>x[column]);
  // const twoDimensionalArray = nodes.map((node) => [node.x, node.y]);
  // const picked = (({ a, c }) => ({ a, c }))(object);


  const getDataFromColumns = async (network) => {
  	const data = await getData();
  	const dataNetwork = data.filter(d => d['Network'] == network);
    console.log(data[0]);
    const picked = (({ Date, Likes }) => ({ Date, Likes }))(data[0]);
    console.log(picked);
  	const dataPicked = dataNetwork.map(d => (({Date, Likes, Engagements, Post}) => ({Date, Likes, Engagements, Post}))(d));
    console.log(dataPicked);
    return dataPicked;
    
  };

  const getGraph = async (data) => {
    
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


  const g2 = vl
    .markLine({ size : 1 })
    .encode(
      vl.x().fieldT('Date').timeUnit("date"),
      vl.y().fieldQ('Likes').aggregate('average'),
      vl.color().fieldN('Sentiment'),
      vl.tooltip().fieldT('Date').timeUnit('date')
    );

  // import { message } from './myMessage';



  vl.register(vega, vegaLite, {
    view: { renderer: 'canvas' },
    init: view => { view.tooltip(new vegaTooltip.Handler().call); }
  });

  const run = async () => {
    
    // data
    const twitter = await getDataFromColumns('Twitter');
    
    const facebook2 = await getDataFromColumns('Facebook');
    const facebook = await getDataFrom('Facebook');
    const instagram = await getDataFrom('Instagram');
    
    const graph = await getGraph(twitter);
    const graph_1 = await getGraph(instagram);

  	document.getElementById("grafico1").appendChild(await graph.render());
    document.getElementById("grafico2").appendChild(await graph_1.render());
    
  };


  run();

}(d3, vega, vegaLite, vl, vegaTooltip));
