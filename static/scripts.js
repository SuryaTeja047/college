$(document).ready(function() {
    $.getJSON('/api/aspirants', function(aspirantsData) {
        var aspirantsContainer = $('#aspirants-container');

        aspirantsData.forEach(function(aspirant) {
            var card = $('<div>').addClass('aspirant-item');
            var contentContainer = $('<div>').addClass('content');
            var aspirantImage = $('<img>').attr({
                src: '/static/' + aspirant.imageUrl,  // Update this line
                alt: aspirant.name + "'s Image"
            });
            var aspirantName = $('<h1>').text(aspirant.name);

            contentContainer.append(aspirantName);
            card.append(aspirantImage).append(contentContainer);
            aspirantsContainer.append(card);
        });
    });
});
