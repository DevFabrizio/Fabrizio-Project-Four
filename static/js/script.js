// timeout function to display the reservation success message for 3 secs

setTimeout(function(){
    let successMsg = document.getElementById('reservation-success-msg');
    successMsg.remove();
},3000);

