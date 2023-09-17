const { value: relatorio } = Swal.fire({
    title: 'Gerador de Relatórios',
    input: 'select',
    inputOptions: {
        'Relatórios': {
            destinos_atacados: 'Relatório 1 - Destinos Atacados',
            origens_que_mais_atacaram: 'Relatório 2 - Origens que mais Atacaram',
            alert_report: 'Relatório 3 - Categorias de Ataque mais Frequentes',
            alert_report2: 'Relatório 4 - Categorias de cada Severidade',
        },
        'Relatórios Críticos': {
            port_21: 'Relatório Porta 21',
            port_22: 'Relatório Porta 22',
            port_445: 'Relatório Porta 445',
            port_3389: 'Relatório Porta 3389',
            port_5900: 'Relatório Porta 5900',

        },
        'Relatórios Parciais': {
            signatures_data: 'Dados de Assinatura',
            severity_total: 'Total de Severidade',
            suricata_categorization: 'Categorização do Suricata',
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
            url: "data/" + csv_name + ".csv", // use the value from the Swal fire
            success: function(data) {
            $('#alerts_table').html(arrayToTable(Papa.parse(data).data));
            geraGrafico();
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