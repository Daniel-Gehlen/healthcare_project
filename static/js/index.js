$(document).ready(function() {
    // Função para abrir o Datepicker quando o campo "Appointment date" for clicado
    $('#id_appointment_date').datepicker();

    // Função para carregar os horários disponíveis ao selecionar uma data
    $('#id_appointment_date').change(function() {
        var selectedDate = $(this).val();
        var url = $('form').data('url');  // Obter o URL da view Django
        $.ajax({
            type: 'GET',
            url: url,  // Use o URL correto para a sua view Django
            data: {'appointment_date': selectedDate},
            success: function(data) {
                $('#available-times').empty();
                $.each(data, function(index, value) {
                    $('#available-times').append('<label><input type="radio" name="time" value="' + value + '">' + value + '</label><br>');
                });
            }
        });
    });
});
