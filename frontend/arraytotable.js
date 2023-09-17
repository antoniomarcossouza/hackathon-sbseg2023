const { value: relatorio } = Swal.fire({
    title: 'Gerador de Relatórios',
    input: 'select',
    inputOptions: {
        'Relatórios Completos': {
            alert_report: 'Relatório 1',
            alert_report2: 'Relatório 2',
        },
        'Relatórios Parciais': {
            signatures_data: 'Dados de Assinatura',
            payload_scrapping: 'Scrapping do Payload',
        },
    },
    inputPlaceholder: 'Selecione um Relatório',
    inputValidator: (value) => {
        return new Promise((resolve) => {
            resolve()
        })
    }
    }).then((result) =>
    {
        // get the value from the result
        var csv_name = result.value;
        // use the value in your ajax request
        $(document).ready(function() {
        $.ajax({
            type: "GET",
            url: "Tables/" + csv_name + ".csv", // use the value from the Swal fire
            success: function(data) {
            $('#alerts_table').html(arrayToTable(Papa.parse(data).data));
            }
        });
    });
})


function arrayToTable(tableData) {
    var table = $('<table id="alerts_table_content" class = "table table-striped table-dark" style="max-width:1400px;"></table>');
    $(tableData).each(function(i, rowData) {
      var row = $('<tr></tr>');
      $(rowData).each(function(j, cellData) {
        row.append($('<td>'+cellData+'</td>'));
      });
      table.append(row);
    });
    return table;
}