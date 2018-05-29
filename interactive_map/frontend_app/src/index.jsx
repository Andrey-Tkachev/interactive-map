import api from "./api";

const convert_coordinates = (str_coords) => {
    return str_coords.split(',').map(x => parseFloat(x)).reverse();
};

function init() {
    var myMap = new ymaps.Map("map", {
          center: [55.76, 37.64],
          zoom: 10
      }, {
          searchControlProvider: 'yandex#search'
    });


    api.Events.load().then((events) => {
        events.forEach(event => {
            console.log(event);
            myMap.geoObjects
            .add(new ymaps.Placemark(convert_coordinates(event.coordinates), {
                balloonContent: '<a href="' + event.news_url + '">' + event.news_title + '</a>',
                iconCaption: event.news_title.slice(0, Math.min(event.news_title.length, 20)).trim() + '...',
            }, {
                preset: 'islands#icon',
                iconColor: '#0095b6'
            }));
        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    ymaps.ready(init);
});
