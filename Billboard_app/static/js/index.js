var bill = {};



$( document ).ready(function() {
    $('#login').attr('href', 'login');
    $('#register').attr('href', 'register');

    $('#login').on('click', function(){
        console.log('Clicked login');
    });

    $('#register').on('click', function(){
        console.log('Clicked register');
    });

});