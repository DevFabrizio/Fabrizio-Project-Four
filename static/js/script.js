// timeout function to display the reservation success message for 3 secs


document.addEventListener("DOMContentLoaded", function() {

    setTimeout(function(){
        let successMsg = document.getElementById('reservation-success-msg');
        if (successMsg) {
            successMsg.remove();
        }
    }, 3000);

});

