function filterTable() {
    var search = document.getElementById('search').value.toLowerCase();
    var column = parseInt(document.getElementById('column').value);
    var table = document.getElementById(alerts_table_content);
    for (var i = 1; i < table.rows.length; i++) {
        var row = table.rows[i];
        var cell = row.cells[column].textContent.toLowerCase();
        if (cell.indexOf(search) > -1) {
            row.style.display = '';
        } else {
        row.style.display = 'none'
        }
    }
}

$(document).ready(function () {
    // Attach an event listener to the search input and column select
    $('#search').on('input change', function () {
        filterTable();
    });
    // Initial filter when the page loads
    filterTable();
});