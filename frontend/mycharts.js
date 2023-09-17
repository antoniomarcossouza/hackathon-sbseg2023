function geraGrafico(){
    // Obter a referência da tabela pelo id
    var table = document.getElementById("alerts_table_content");
    console.log(table)
    // Obter o número de linhas da tabela
    var rowCount = table.rows.length;
    // Criar arrays vazios para armazenar os dados
    var labels = []; // Os rótulos do eixo x
    var data = []; // Os valores do eixo y
    // Percorrer as linhas da tabela, começando pela segunda linha (ignorando o cabeçalho)
    for (var i = 1; i < 10; i++) {
        // Obter a referência da linha atual
        var row = table.rows[i];
        // Obter o texto da primeira célula da linha (o rótulo)
        var label = row.cells[0].innerText;
        // Obter o texto da segunda célula da linha (o valor)
        var value = row.cells[3].innerText;
        // Adicionar o rótulo e o valor aos arrays correspondentes
        labels.push(label);
        data.push(value);
    }
    console.log(labels)
    console.log(data)
    desenhaGrafico(labels, data);
}

function desenhaGrafico(labels, data){
    let myChart = document.getElementById('myChart').getContext('2d');

    let massPopChart = new Chart(myChart, {
        type: 'radar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Categories',
                data: data,
                backgroundColor:[
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(153, 102, 255, 0.6)',
                    'rgba(255, 159, 64, 0.6)',
                    'rgba(255, 99, 132, 0.6)',
                ]
            }],
        },
        options:{
            title:{
                display: true,
                text: 'Gráfico Teste',
                fontSize: 25,
                fontColor: '#000'
            },
            legend:{
                display: true,
                position: 'right',
                labels:{
                    fontColor: '#000'
                }
            }
        }
    });
}