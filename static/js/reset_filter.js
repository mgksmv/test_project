// аякс для сброса фильтров без перезагрузки страницы
$(document).ready(function () {
    $('#loading').hide();

    $('#reset-button').on('click', function () {
        var filterObjects = {};
        var column = $('#column-value').val();
        var condition = $('#condition-value').val();
        var search = $('#search-value').val();

        filterObjects.column = column;
        filterObjects.condition = condition;
        filterObjects.search_value = search;

        $.ajax({
            url: '/reset',
            data: filterObjects,
            dataType: 'json',
            beforeSend: function () {
                $('#loading').html('Загрузка...');
            },
            success: function (result) {
                $('#loading').hide();
                $('#filtered_data').html(result.table_data);
            }
        })
    });

})
