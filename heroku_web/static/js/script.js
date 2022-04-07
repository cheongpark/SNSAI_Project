var animation = bodymovin.loadAnimation({
    container: document.getElementById('loading'),
    rederer: 'svg',
    loop: true,
    autoplay: true,
    path: './static/json/data.json'
})