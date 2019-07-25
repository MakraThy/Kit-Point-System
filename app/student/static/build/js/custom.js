$(document).ready(function() {
      let $department = $('#department');
      let $batch = $('#batch');
      let $semester = $('#semester');
      setTimeout(function() { $('.alert').hide();}, 1500);
      $('#demo-form').on('submit', function(e) {
        let price = $('#price').val();
        if (!price.match(/^-?\d*[.,]?\d{0,2}$/)){
          let error = '<ul class="alert alert-danger">' +
              '<label>Price accepts number only!</label>' +
              '</ul>';
            $('#alert_message').append(error);
            e.preventDefault();
        }
      });
      $department.on('change', function() {
        let dep_id = $(this).val();
        let length = $(this).text();
        if (length ==='') return;
        $.getJSON('/student/get_batch/' + dep_id, function(res) {
          if (res['code'] === 200) {
            $batch.html('');
            let empty = '<option></optoin>';
            $batch.append(empty);
            Object.keys(res).forEach((v, i, arr) => {
              console.debug(res[v]);
              if (i !== arr.length - 1) {
                let option = '<option value=' + v + '>' + res[v].name + '</option>';
                $batch.append(option);
              }

            });
          } else {
            let error = '<ul class="alert alert-danger">' +
              '<label>Cannot get batches</label>' +
              '</ul>';
            $('#alert_message').append(error);
          }
        });
      });
      $batch.on('change', function() {
        let batch_id = $(this).val();
        let length = $(this).text();
        if (length==='') return;
        $.getJSON('/student/get_semester/' + batch_id, function(res) {
          if (res['code'] === 200){
            $semester.append('<option></option>');
            Object.keys(res).forEach((v, i, arr) => {
              console.debug(res[v]);
              if (i !== arr.length - 1){
                $semester.append('<option value='+ v + '>' + res[v].name + '</option>');
              }
            })
          }
        })
      })
    });
