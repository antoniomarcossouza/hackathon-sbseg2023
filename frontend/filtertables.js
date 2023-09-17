function filterTable() {
    var search = $('#search').val().toLowerCase();
    var column = parseInt($('#column').val());
    var table = $('#alerts_table_content');

    table.find('tr').each(function (i, row) {
        var rowMatchesSearch = false;
        $(row).find('td').each(function (j, cell) {
            var cellText = $(cell).text().toLowerCase();
            if (cellText.indexOf(search) > -1) {
                rowMatchesSearch = true;
                return false; // Exit the inner loop once a match is found
            }
        });

        if (rowMatchesSearch) {
            $(row).show();
        } else {
            $(row).hide();
        }
    });
}
$(document).ready(function () {
    // Attach an event listener to the search input and column select
    $('#search').on('input change', function () {
        filterTable();
    });
    // Initial filter when the page loads
    filterTable();
});