let URLSearch = new URLSearchParams(window.location.search.replace(/^\?/ig,''));
let defaultEmbedGraphURL = 'https://graphxr.kineviz.com/p/60f0cb2f7218aa003c070b4b/Canal%2013'
let iframe = document.getElementById('injection-graphXR-iframe-id');
iframe.setAttribute('src', URLSearch.get('embedGraphURL') || URLSearch.get('url') || iframe.getAttribute('src') ||  defaultEmbedGraphURL);