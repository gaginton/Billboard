
$(document).ready(function() {
    console.log('Register works');

    $('.user-input').on('click', function(e){
        var labels = $('label');

        for (let index = 0; index < labels.length; index++) {
            var element = labels[index];
            if (element.innerText==e.target.id) {
                element.classList.add('label-change');  
            }
            else{
                element.classList.remove('label-change');
            }
        }
    })
});