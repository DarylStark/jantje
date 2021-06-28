function update_progress() {
    $('.progress_bar_fill').each(function (index, elem) {
        let perc = $(elem).data('percentage');
        $(elem).css('width', perc + '%');
    });
}

$(document).ready(function () {
    $('#avatar').click(function () {
        location.reload();
    });
    update_progress();
});